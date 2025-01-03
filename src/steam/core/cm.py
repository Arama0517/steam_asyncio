import asyncio
import binascii
import logging
import struct
from collections import defaultdict
from gzip import GzipFile
from io import BytesIO
from itertools import count, cycle
from random import shuffle
from time import time
from typing import Optional

from steam.core import crypto
from steam.core.connection import Connection, WebsocketConnection
from steam.core.eventemitter import EventEmitter
from steam.core.msg import Msg, MsgProto
from steam.enums import EResult, EUniverse
from steam.enums.emsg import EMsg
from steam.exceptions import SteamError
from steam.steamid import SteamID
from steam.utils import ip4_from_int
from steam.utils.proto import clear_proto_bit, is_proto


class CMClient(EventEmitter):
    """
    CMClient provides a secure message channel to Steam CM servers
    Can be used as mixing or on it's own.

    Incoming messages are parsed and emitted as events using
    their :class:`steam.enums.emsg.EMsg` as event identifier
    """

    EVENT_CONNECTED = 'connected'
    """Connection establed to CM server
    """
    EVENT_DISCONNECTED = 'disconnected'
    """Connection closed
    """
    EVENT_RECONNECT = 'reconnect'
    """Delayed connect

    :param delay: delay in seconds
    :type delay: int
    """
    EVENT_CHANNEL_SECURED = 'channel_secured'
    """After successful completion of encryption handshake
    """
    EVENT_ERROR = 'error'
    """When login is denied

    :param eresult: reason
    :type eresult: :class:`.EResult`
    """
    EVENT_EMSG = 0
    """All incoming messages are emitted with their :class:`.EMsg` number.
    """

    # PROTOCOL_TCP = 0  #: TCP protocol enum
    # # PROTOCOL_UDP = 1  #: UDP protocol enum
    # PROTOCOL_WEBSOCKET = 2  #: WEBSOCKET protocol enum

    verbose_debug = False  #: print message connects in debug

    auto_discovery = True  #: enables automatic CM discovery
    cm_servers = None  #: a instance of :class:`.CMServerList`
    current_server_addr = None  #: (ip, port) tuple
    _seen_logon = False
    _connecting = False
    connection: Connection = None
    connected = False  #: :class:`True` if connected to CM
    channel_secured = False  #: :class:`True` once secure channel handshake is complete

    channel_key = None  #: channel encryption key
    channel_hmac = None  #: HMAC secret

    steam_id = SteamID()  #: :class:`.SteamID` of the current user
    session_id = None  #: session id when logged in
    cell_id = 0  #: cell id provided by CM

    _recv_loop = None
    _heartbeat_loop = None
    _LOG = logging.getLogger('CMClient')

    def __init__(self, connection: Optional[Connection] = None):
        super().__init__()
        self.cm_servers = CMServerList()

        # if protocol == CMClient.PROTOCOL_WEBSOCKET:
        #     self.connection = WebsocketConnection()
        # elif protocol == CMClient.PROTOCOL_TCP:
        #     self.connection = TCPConnection()
        # else:
        #     raise ValueError('Only Websocket and TCP are supported')
        self.connection = connection or WebsocketConnection()

        self.on(EMsg.ChannelEncryptRequest, self.__handle_encrypt_request)
        self.on(EMsg.Multi, self.__handle_multi)
        self.on(EMsg.ClientLogOnResponse, self._handle_logon)
        self.on(EMsg.ClientCMList, self._handle_cm_list)

    async def emit(self, event, *args):
        if event is not None:
            self._LOG.debug('Emit event: %s' % repr(event))
        await super().emit(event, *args)

    async def connect(self, retry=0, delay=0):
        """Initiate connection to CM. Blocks until connected unless ``retry`` is specified.

        :param retry: number of retries before returning. Unlimited when set to ``None``
        :type retry: :class:`int`
        :param delay: delay in seconds before connection attempt
        :type delay: :class:`int`
        :return: successful connection
        :rtype: :class:`bool`
        """
        if self.connected:
            self._LOG.debug('Connect called, but we are connected?')
            return
        if self._connecting:
            self._LOG.debug('Connect called, but we are already connecting.')
            return
        self._connecting = True

        if delay:
            self._LOG.debug('Delayed connect: %d seconds' % delay)
            await self.emit(self.EVENT_RECONNECT, delay)
            await self.sleep(delay)

        self._LOG.debug('Connect initiated.')

        i = count(0)

        while len(self.cm_servers) == 0:
            if not self.auto_discovery or (retry and next(i) >= retry):
                if not self.auto_discovery:
                    self._LOG.error('CM server list is empty. Auto discovery is off.')
                self._connecting = False
                return False

            # if isinstance(self.connection, WebsocketConnection):
            #     await self.cm_servers.bootstrap_from_webapi(cm_type='websockets')
            # elif isinstance(self.connection, TCPConnection):
            #     await self.cm_servers.bootstrap_from_webapi(cm_type='netfilter')
            await self.cm_servers.bootstrap_from_webapi(cm_type=self.connection.cm_type)
        for i, server_addr in enumerate(cycle(self.cm_servers), start=next(i) - 1):
            if retry and i >= retry:
                self._connecting = False
                return False

            start = time()

            if await self.connection.connect(server_addr):
                break
            self._LOG.debug('Failed to connect. Retrying...')

            diff = time() - start

            if diff < 5:
                await self.sleep(5 - diff)

        self.current_server_addr = server_addr
        self.connected = True
        await self.emit(self.EVENT_CONNECTED)

        # WebsocketConnection secures itself
        if isinstance(self.connection, WebsocketConnection):
            self.channel_secured = True
            await self.emit(self.EVENT_CHANNEL_SECURED)

        self._recv_loop = asyncio.create_task(self._recv_messages())
        self._connecting = False
        return True

    async def disconnect(self):
        """Close connection"""

        if not self.connected:
            return
        self.connected = False

        await self.connection.disconnect()

        if self._heartbeat_loop:
            self._heartbeat_loop.cancel()
        self._recv_loop.cancel()

        self._reset_attributes()

        await self.emit(self.EVENT_DISCONNECTED)

    def _reset_attributes(self):
        for name in [
            'connected',
            'channel_secured',
            'channel_key',
            'channel_hmac',
            'steam_id',
            'session_id',
            '_seen_logon',
            '_recv_loop',
            '_heartbeat_loop',
        ]:
            self.__dict__.pop(name, None)

    async def send(self, message: Msg | MsgProto):
        """
        Send a message

        :param message: a message instance
        :type message: :class:`steam.core.msg.Msg`, :class:`steam.core.msg.MsgProto`
        """
        if not isinstance(message, (Msg, MsgProto)):
            raise ValueError('Expected Msg or MsgProto, got %s' % message)

        if self.steam_id:
            message.steamID = self.steam_id
        if self.session_id:
            message.sessionID = self.session_id

        if self.verbose_debug:
            self._LOG.debug(f'Outgoing: {repr(message)}\n{str(message)}')
        else:
            self._LOG.debug('Outgoing: %s', repr(message))

        data = message.serialize()

        if self.channel_key:
            if self.channel_hmac:
                data = crypto.symmetric_encrypt_hmac(data, self.channel_key, self.channel_hmac)
            else:
                data = crypto.symmetric_encrypt(data, self.channel_key)

        await self.connection.put_message(data)

    async def _recv_messages(self):
        async for message in self.connection:
            if not self.connected:
                break

            if self.channel_key:
                if self.channel_hmac:
                    try:
                        message = crypto.symmetric_decrypt_hmac(
                            message, self.channel_key, self.channel_hmac
                        )
                    except RuntimeError as e:
                        self._LOG.exception(e)
                        break
                else:
                    message = crypto.symmetric_decrypt(message, self.channel_key)

            # gevent.spawn(self._parse_message, message)
            asyncio.create_task(self._parse_message(message))
            await self.idle()

        if not self._seen_logon and self.channel_secured:
            if await self.wait_event('disconnected', timeout=5) is not None:
                return

        await self.disconnect()

    async def _parse_message(self, message):
        (emsg_id,) = struct.unpack_from('<I', message)
        emsg = EMsg(clear_proto_bit(emsg_id))

        if not self.connected and emsg != EMsg.ClientLogOnResponse:
            self._LOG.debug(
                f'Dropped unexpected message: {repr(emsg)} (is_proto: {is_proto(emsg_id)})'
            )
            return

        if emsg in (
            EMsg.ChannelEncryptRequest,
            EMsg.ChannelEncryptResponse,
            EMsg.ChannelEncryptResult,
        ):
            msg = Msg(emsg, message, parse=False)
        else:
            try:
                if is_proto(emsg_id):
                    msg = MsgProto(emsg, message, parse=False)
                else:
                    msg = Msg(emsg, message, extended=True, parse=False)
            except Exception as e:
                self._LOG.fatal(
                    'Failed to deserialize message: %s (is_proto: %s)',
                    repr(emsg),
                    is_proto(emsg_id),
                )
                self._LOG.exception(e)
                return

        if self.count_listeners(emsg) or self.verbose_debug:
            msg.parse()

        if self.verbose_debug:
            self._LOG.debug(f'Incoming: {repr(msg)}\n{str(msg)}')
        else:
            self._LOG.debug('Incoming: %s', repr(msg))

        await self.emit(emsg, msg)
        return emsg, msg

    async def __handle_encrypt_request(self, req):
        self._LOG.debug('Securing channel')

        try:
            if req.body.protocolVersion != 1:
                raise RuntimeError('Unsupported protocol version')
            if req.body.universe != EUniverse.Public:
                raise RuntimeError('Unsupported universe')
        except RuntimeError as e:
            self._LOG.exception(e)
            await self.disconnect()
            return

        resp = Msg(EMsg.ChannelEncryptResponse)

        challenge = req.body.challenge
        key, resp.body.key = crypto.generate_session_key(challenge)
        resp.body.crc = binascii.crc32(resp.body.key) & 0xFFFFFFFF

        await self.send(resp)

        result = await self.wait_event(EMsg.ChannelEncryptResult, timeout=5)

        if result is None:
            self.cm_servers.mark_bad(self.current_server_addr)
            await self.disconnect()
            return

        eresult = result[0].body.eresult

        if eresult != EResult.OK:
            self._LOG.error('Failed to secure channel: %s' % eresult)
            await self.disconnect()
            return

        self.channel_key = key

        if challenge:
            self._LOG.debug('Channel secured')
            self.channel_hmac = key[:16]
        else:
            self._LOG.debug('Channel secured (legacy mode)')

        self.channel_secured = True
        await self.emit(self.EVENT_CHANNEL_SECURED)

    async def __handle_multi(self, msg):
        self._LOG.debug('Multi: Unpacking')

        if msg.body.size_unzipped:
            self._LOG.debug(
                'Multi: Decompressing payload (%d -> %s)'
                % (
                    len(msg.body.message_body),
                    msg.body.size_unzipped,
                )
            )

            with GzipFile(fileobj=BytesIO(msg.body.message_body)) as f:
                data = f.read()

            if len(data) != msg.body.size_unzipped:
                self._LOG.fatal('Unzipped size mismatch')
                await self.disconnect()
                return
        else:
            data = msg.body.message_body

        while len(data) > 0:
            (size,) = struct.unpack_from('<I', data)
            await self._parse_message(data[4 : 4 + size])
            data = data[4 + size :]

    async def __heartbeat(self, interval: int):
        message = MsgProto(EMsg.ClientHeartBeat)

        while True:
            await self.sleep(interval)
            await self.send(message)

    async def _handle_logon(self, msg):
        result = msg.body.eresult

        if result in (EResult.TryAnotherCM, EResult.ServiceUnavailable):
            self.cm_servers.mark_bad(self.current_server_addr)
            await self.disconnect()
        elif result == EResult.OK:
            self._seen_logon = True

            self._LOG.debug('Logon completed')

            self.steam_id = SteamID(msg.header.steamid)
            self.session_id = msg.header.client_sessionid
            self.cell_id = msg.body.cell_id

            if self._heartbeat_loop:
                self._heartbeat_loop.cancel()

            self._LOG.debug('Heartbeat started.')

            interval = msg.body.heartbeat_seconds
            self._heartbeat_loop = asyncio.create_task(self.__heartbeat(interval))
        else:
            await self.emit(self.EVENT_ERROR, EResult(result))
            await self.disconnect()

    async def _handle_cm_list(self, msg):
        self._LOG.debug('Updating CM list')

        new_servers = list(zip(map(ip4_from_int, msg.body.cm_addresses), msg.body.cm_ports))
        self.cm_servers.clear()
        self.cm_servers.merge_list(new_servers)
        self.cm_servers.cell_id = self.cell_id

    @staticmethod
    async def sleep(seconds):
        """Yeild and sleep N seconds. Allows other greenlets to run"""
        await asyncio.sleep(seconds)

    async def idle(self):
        """Yeild in the current greenlet and let other greenlets run"""
        await self.sleep(0)


class CMServerList:
    """
    Managing object for CM servers

    Comes with built in list of CM server to bootstrap a connection

    To get a server address from the list simply iterate over it

    .. code:: python

        servers = CMServerList()
        for server_addr in servers:
            pass

    The good servers are returned first, then bad ones. After failing to connect
    call :meth:`mark_bad` with the server addr. When connection succeeds break
    out of the loop.
    """

    Good = 1
    Bad = 2
    last_updated = 0  #: timestamp of when the list was last updated
    cell_id = 0  #: cell id of the server list
    bad_timestamp = 300  #: how long bad mark lasts in seconds

    def __init__(self):
        self._LOG = logging.getLogger('CMServerList')
        self.list = defaultdict(dict)

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return '<%s: %d servers>' % (self.__class__.__name__, len(self))

    def clear(self):
        """Clears the server list"""
        if len(self.list):
            self._LOG.debug('List cleared.')
        self.list.clear()

    # async def bootstrap_from_dns(self):
    #     """
    #     Fetches CM server list from WebAPI and replaces the current one
    #     """
    #     self._LOG.debug('Attempting bootstrap via DNS')
    #
    #     resolver = Resolver()
    #     try:
    #         # answer = socket.getaddrinfo(
    #         #     'cm0.steampowered.com', 27017, socket.AF_INET, proto=socket.IPPROTO_TCP
    #         # )
    #         answer = await resolver.resolve('cm0.steampowered.com', A)
    #     except Exception as exp:
    #         self._LOG.error('DNS boostrap failed: %s' % str(exp))
    #         return False
    #
    #     servers = list(map(lambda addr: (addr.to_text(), 27017), answer))
    #
    #     if servers:
    #         self.clear()
    #         self.merge_list(servers)
    #         return True
    #     else:
    #         self._LOG.error('DNS boostrap: cm0.steampowered.com resolved no A records')
    #         return False

    async def bootstrap_from_webapi(self, cm_type: str, cell_id: int = 0):
        """
        Fetches CM server list from WebAPI and replaces the current one

        :param cell_id: cell id (0 = global)
        :param cm_type: CM type filter
        :return: booststrap success
        """
        self._LOG.debug('Attempting bootstrap via WebAPI for %s' % cm_type)

        from steam import webapi

        resp = await webapi.get(
            'ISteamDirectory',
            'GetCMListForConnect',
            1,
            params={'cellid': cell_id, 'cmtype': cm_type},
        )
        result = EResult(resp['response']['success'])

        if result != EResult.OK:
            self._LOG.error('GetCMList failed with %s' % repr(result))
            raise SteamError('GetCMList failed.', result)

        serverlist = resp['response']['serverlist']
        self._LOG.debug('Received %d servers from WebAPI' % len(serverlist))

        def str_to_tuple(serverinfo):
            ip, port = serverinfo['endpoint'].split(':')
            return str(ip), int(port)

        self.clear()
        self.cell_id = cell_id
        self.merge_list(list(map(str_to_tuple, serverlist)))

    def __iter__(self):
        def cm_server_iter():
            if not self.list:
                self._LOG.error('Server list is empty.')
                return

            good_servers = list(
                filter(lambda x: x[1]['quality'] == CMServerList.Good, self.list.items())
            )

            if len(good_servers) == 0:
                self._LOG.debug('No good servers left. Reseting...')
                self.reset_all()
                return

            shuffle(good_servers)

            for server_addr, meta in good_servers:
                yield server_addr

        return cm_server_iter()

    def reset_all(self):
        """Reset status for all servers in the list"""

        self._LOG.debug('Marking all CMs as Good.')

        for key in self.list:
            self.mark_good(key)

    def mark_good(self, server_addr):
        """Mark server address as good

        :param server_addr: (ip, port) tuple
        :type server_addr: :class:`tuple`
        """
        self.list[server_addr].update({
            'quality': CMServerList.Good,
            'timestamp': time(),
        })

    def mark_bad(self, server_addr):
        """Mark server address as bad, when unable to connect for example

        :param server_addr: (ip, port) tuple
        :type server_addr: :class:`tuple`
        """
        self._LOG.debug('Marking %s as Bad.' % repr(server_addr))
        self.list[server_addr].update({
            'quality': CMServerList.Bad,
            'timestamp': time(),
        })

    def merge_list(self, new_list):
        """Add new CM servers to the list

        :param new_list: a list of ``(ip, port)`` tuples
        :type new_list: :class:`list`
        """
        total = len(self.list)

        for ip, port in new_list:
            if (ip, port) not in self.list:
                self.mark_good((ip, port))

        if len(self.list) > total:
            self._LOG.debug('Added %d new CM addresses.' % (len(self.list) - total))

        self.last_updated = int(time())
