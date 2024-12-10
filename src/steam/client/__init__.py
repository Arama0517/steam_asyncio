"""
Implementation of Steam client based on ``gevent``

.. warning::
    ``steam.client`` no longer patches stdlib to make it gevent cooperative.
    This provides flexibility if you want to use :class:`.SteamClient` with async or other modules.
    If you want to monkey patch anyway use :meth:`steam.monkey.patch_minimal()`

.. note::
    Additional features are located in separate submodules. All functionality from :mod:`.builtins` is inherited by default.

.. note::
    Optional features are available as :mod:`.mixins`. This allows the client to remain light yet flexible.

"""

import logging
from random import random
from time import time

from steam.client.builtins import BuiltinBase
from steam.core.cm import CMClient
from steam.core.msg import MsgProto, get_um
from steam.enums import EOSType, EResult
from steam.enums.emsg import EMsg
from steam.steamid import SteamID
from steam.utils import ip4_to_int
from steam.utils.proto import proto_fill_from_dict


class SteamClient(CMClient, BuiltinBase):
    EVENT_LOGGED_ON = 'logged_on'
    """After successful login"""

    _LOG = logging.getLogger('SteamClient')
    _reconnect_backoff_c = 0
    current_jobid = 0
    username = None  #: username when logged on
    login_key = None
    chat_mode = 2  #: chat mode (0=old chat, 2=new chat)

    def __init__(self, protocol=CMClient.PROTOCOL_WEBSOCKET):
        CMClient.__init__(self, protocol=protocol)

        # register listners
        self.on(self.EVENT_DISCONNECTED, self._handle_disconnect)
        self.on(self.EVENT_RECONNECT, self._handle_disconnect)

        #: indicates logged on status. Listen to ``logged_on`` when change to ``True``
        self.logged_on = False

        BuiltinBase.__init__(self)

    def __repr__(self):
        return '<{}({}) {}>'.format(
            self.__class__.__name__,
            repr(self.current_server_addr),
            'online' if self.connected else 'offline',
        )

    # async def connect(self, *args, **kwargs):
    #     """Attempt to establish connection, see :meth:`.CMClient.connect`"""
    #     return CMClient.connect(self, *args, **kwargs)

    async def disconnect(self):
        """Close connection, see :meth:`.CMClient.disconnect`"""
        self.logged_on = False
        await CMClient.disconnect(self)

    async def _parse_message(self, message):
        result = await CMClient._parse_message(self, message)

        if result is None:
            return

        emsg, msg = result

        # emit job events
        if msg.proto:
            jobid = msg.header.jobid_target
        else:
            jobid = msg.header.targetJobID

        if jobid not in (-1, 18446744073709551615):
            jobid = 'job_%d' % jobid
            if msg.body is None and self.count_listeners(jobid):
                msg.parse()
            await self.emit(jobid, msg)

        # emit UMs
        if emsg in (
            EMsg.ServiceMethod,
            EMsg.ServiceMethodResponse,
            EMsg.ServiceMethodSendToClient,
        ):
            if msg.body is None and self.count_listeners(msg.header.target_job_name):
                msg.parse()
            await self.emit(msg.header.target_job_name, msg)

    async def _handle_cm_list(self, msg):
        if self.cm_servers.last_updated + 3600 * 24 > time() and self.cm_servers.cell_id != 0:
            return
        await CMClient._handle_cm_list(self, msg)  # clear and merge

    async def _handle_disconnect(self, *_):
        self.logged_on = False
        self.current_jobid = 0

    async def _handle_logon(self, msg):
        await CMClient._handle_logon(self, msg)

        result = EResult(msg.body.eresult)

        if result == EResult.OK:
            self._reconnect_backoff_c = 0
            self.logged_on = True
            await self.emit(self.EVENT_LOGGED_ON)
            return

        # CM kills the connection on error anyway
        await self.disconnect()

    async def reconnect(self, maxdelay=30, retry=0):
        """Implements explonential backoff delay before attempting to connect.
        It is otherwise identical to calling :meth:`.CMClient.connect`.
        The delay is reset upon a successful login.

        :param maxdelay: maximum delay in seconds before connect (0-120s)
        :type maxdelay: :class:`int`
        :param retry: see :meth:`.CMClient.connect`
        :type retry: :class:`int`
        :return: successful connection
        :rtype: :class:`bool`
        """
        delay_seconds = 2**self._reconnect_backoff_c - 1

        if delay_seconds < maxdelay:
            self._reconnect_backoff_c = min(7, self._reconnect_backoff_c + 1)

        delay_seconds = int(delay_seconds * 0.5 + delay_seconds * 0.5 * random())

        return await self.connect(delay=delay_seconds, retry=retry)

    async def wait_msg(self, event, timeout=None, raises=None):
        """Wait for a message, similiar to :meth:`.wait_event`

        :param event: event id
        :type  event: :class:`.EMsg` or :class:`str`
        :param timeout: seconds to wait before timeout
        :type  timeout: :class:`int`
        :param raises: On timeout when ``False`` returns :class:`None`, else raise :class:`gevent.Timeout`
        :type  raises: :class:`bool`
        :return: returns a message or :class:`None`
        :rtype: :class:`None`, or `proto message`
        :raises: :class:`gevent.Timeout`
        """
        resp = await self.wait_event(event, timeout, raises)

        if resp is not None:
            return resp[0]

    async def send(self, message, body_params=None):
        """Send a message to CM

        :param message: a message instance
        :type message: :class:`.Msg`, :class:`.MsgProto`
        :param body_params: a dict with params to the body (only :class:`.MsgProto`)
        :type body_params: dict
        """
        if not self.connected:
            self._LOG.debug('Trying to send message when not connected. (discarded)')
        else:
            if body_params and isinstance(message, MsgProto):
                proto_fill_from_dict(message.body, body_params)

            await CMClient.send(self, message)

    async def send_job(self, message, body_params=None):
        """Send a message as a job

        .. note::
            Not all messages are jobs, you'll have to find out which are which

        :param message: a message instance
        :type message: :class:`.Msg`, :class:`.MsgProto`
        :param body_params: a dict with params to the body (only :class:`.MsgProto`)
        :type body_params: dict
        :return: ``jobid`` event identifier
        :rtype: :class:`str`

        To catch the response just listen for the ``jobid`` event.

        .. code:: python

            jobid = steamclient.send_job(my_message)

            resp = steamclient.wait_event(jobid, timeout=15)
            if resp:
                (message,) = resp

        """
        jobid = self.current_jobid = ((self.current_jobid + 1) % 10000) or 1
        self.remove_all_listeners('job_%d' % jobid)

        if message.proto:
            message.header.jobid_source = jobid
        else:
            message.header.sourceJobID = jobid

        await self.send(message, body_params)

        return 'job_%d' % jobid

    async def send_job_and_wait(self, message, body_params=None, timeout=None, raises=False):
        """Send a message as a job and wait for the response.

        .. note::
            Not all messages are jobs, you'll have to find out which are which

        :param message: a message instance
        :type  message: :class:`.Msg`, :class:`.MsgProto`
        :param body_params: a dict with params to the body (only :class:`.MsgProto`)
        :type  body_params: dict
        :param timeout: (optional) seconds to wait
        :type  timeout: :class:`int`
        :param raises: (optional) On timeout if ``False`` return ``None``, else raise :class:`gevent.Timeout`
        :type  raises: :class:`bool`
        :return: response proto message
        :rtype: :class:`.Msg`, :class:`.MsgProto`
        :raises: :class:`gevent.Timeout`
        """
        job_id = await self.send_job(message, body_params)
        response = await self.wait_event(job_id, timeout, raises=raises)
        if response is None:
            return None
        return response[0].body

    async def send_message_and_wait(
        self, message, response_emsg, body_params=None, timeout=None, raises=False
    ):
        """Send a message to CM and wait for a defined answer.

        :param message: a message instance
        :type  message: :class:`.Msg`, :class:`.MsgProto`
        :param response_emsg: emsg to wait for
        :type  response_emsg: :class:`.EMsg`,:class:`int`
        :param body_params: a dict with params to the body (only :class:`.MsgProto`)
        :type  body_params: dict
        :param timeout: (optional) seconds to wait
        :type  timeout: :class:`int`
        :param raises: (optional) On timeout if ``False`` return ``None``, else raise :class:`gevent.Timeout`
        :type  raises: :class:`bool`
        :return: response proto message
        :rtype: :class:`.Msg`, :class:`.MsgProto`
        :raises: :class:`gevent.Timeout`
        """
        await self.send(message, body_params)
        response = await self.wait_event(response_emsg, timeout, raises=raises)
        if response is None:
            return None
        return response[0].body

    async def send_um(self, method_name, params=None):
        """Send service method request

        :param method_name: method name (e.g. ``Player.GetGameBadgeLevels#1``)
        :type  method_name: :class:`str`
        :param params: message parameters
        :type  params: :class:`dict`
        :return: ``job_id`` identifier
        :rtype: :class:`str`

        Listen for ``jobid`` on this object to catch the response.
        """
        proto = get_um(method_name)

        if proto is None:
            raise ValueError('Failed to find method named: %s' % method_name)

        message = MsgProto(EMsg.ServiceMethodCallFromClient)
        message.header.target_job_name = method_name
        message.body = proto()

        if params:
            proto_fill_from_dict(message.body, params)

        return await self.send_job(message)

    async def send_um_and_wait(self, method_name, params=None, timeout=10, raises=False):
        """Send service method request and wait for response

        :param method_name: method name (e.g. ``Player.GetGameBadgeLevels#1``)
        :type  method_name: :class:`str`
        :param params: message parameters
        :type  params: :class:`dict`
        :param timeout: (optional) seconds to wait
        :type  timeout: :class:`int`
        :param raises: (optional) On timeout if :class:`False` return :class:`None`, else raise :class:`gevent.Timeout`
        :type  raises: :class:`bool`
        :return: response message
        :rtype: proto message instance
        :raises: :class:`gevent.Timeout`
        """
        job_id = await self.send_um(method_name, params)
        return await self.wait_msg(job_id, timeout, raises=raises)

    async def _pre_login(self):
        if self.logged_on:
            self._LOG.debug('Trying to login while logged on???')
            raise RuntimeError('Already logged on')

        if not self.connected and not self._connecting:
            if not await self.connect():
                return EResult.Fail

        if not self.channel_secured:
            resp = await self.wait_event(self.EVENT_CHANNEL_SECURED, timeout=10)

            # some CMs will not send hello
            if resp is None:
                if self.connected:
                    await self.wait_event(self.EVENT_DISCONNECTED)
                return EResult.TryAnotherCM

        return EResult.OK

    async def login(self, username, password='', access_token='', login_id=None) -> EResult:
        """Login as a specific user.

        :param username: optionally provide username
        :type  username: :class:`str`
        :param password: optionally provide password
        :type  password: :class:`str`
        :param access_token: optionally, provide access token
        :type  access_token: :class:`str`
        :return: logon result, see `CMsgClientLogonResponse.eresult`
        :rtype: :class:`.EResult`

        .. note::
            Failure to login will result in the server dropping the connection, ``error`` event is fired

        If you have 2FA/SteamGuard, login first with :class:`WebAuth` then pass
        the WebAuth `refresh_token` as Client `access_token`.
        You can save the `username` and `refresh_token` somewhere for automatic
        login at a later time.

        Example:

        .. code:: python
            In [1]: import steam.client, steam.webauth
            In [2]: webauth = steam.webauth.WebAuth()
            In [3]: _ = webauth.cli_login('username')
            Enter password for 'username':
            Enter your Steam Guard code (or simply press Enter if approved via app):
            In [4]: client = steam.client.SteamClient()
            In [5]: client.login(webauth.username, access_token=webauth.refresh_token)
            Out[5]: <EResult.OK: 1>
        """
        self._LOG.debug('Attempting steam client login from webauth')
        if not password and not access_token:
            raise RuntimeError('Must provide either password or access token')

        eresult = await self._pre_login()
        if eresult != EResult.OK:
            return eresult

        self.username = username

        message = MsgProto(EMsg.ClientLogon)
        message.header.steamid = SteamID(type='Individual', universe='Public')
        message.body.protocol_version = 65580
        message.body.client_os_type = EOSType.Windows10
        message.body.client_language = 'english'
        message.body.should_remember_password = True
        message.body.supports_rate_limit_response = True
        message.body.chat_mode = self.chat_mode

        if login_id is None:
            message.body.obfuscated_private_ip.v4 = (
                ip4_to_int(self.connection.local_address) ^ 0xBAADF00D
            )
        else:
            message.body.obfuscated_private_ip.v4 = login_id

        message.body.account_name = username

        if access_token:
            message.body.access_token = access_token
        else:
            message.body.password = password

        await self.send(message)

        resp = await self.wait_msg(EMsg.ClientLogOnResponse, timeout=30)

        if resp and resp.body.eresult == EResult.OK:
            await self.sleep(0.5)

        return EResult(resp.body.eresult) if resp else EResult.Fail

    async def anonymous_login(self):
        """Login as anonymous user

        :return: logon result, see `CMsgClientLogonResponse.eresult <https://github.com/ValvePython/steam/blob/513c68ca081dc9409df932ad86c66100164380a6/protobufs/steammessages_clientserver.proto#L95-L118>`_
        :rtype: :class:`.EResult`
        """
        self._LOG.debug('Attempting Anonymous login')

        eresult = await self._pre_login()

        if eresult != EResult.OK:
            self._LOG.debug('Failed to login as anonymous user')
            return eresult

        self.username = None
        self.login_key = None

        message = MsgProto(EMsg.ClientLogon)
        message.header.steamid = SteamID(type='AnonUser', universe='Public')
        message.body.client_package_version = 1561159470
        message.body.protocol_version = 65580
        await self.send(message)

        resp = await self.wait_msg(EMsg.ClientLogOnResponse, timeout=30)
        return EResult(resp.body.eresult) if resp else EResult.Fail

    async def logout(self):
        """
        Logout from steam. Doesn't nothing if not logged on.

        .. note::
            The server will drop the connection immediatelly upon logout.
        """
        if self.logged_on:
            self.logged_on = False
            await self.send(MsgProto(EMsg.ClientLogOff))
            try:
                await self.wait_event(self.EVENT_DISCONNECTED, timeout=5, raises=True)
            except Exception:
                await self.disconnect()
            await self.idle()

    async def run_forever(self):
        """
        Transfer control the gevent event loop

        This is useful when the application is setup and ment to run for a long time
        """
        while True:
            await self.sleep(300)
