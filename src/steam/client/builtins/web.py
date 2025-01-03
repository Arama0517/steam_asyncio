"""
Web related features
"""

from aiohttp import ClientSession

from steam import webapi
from steam.core.crypto import generate_session_key, symmetric_encrypt
from steam.core.msg import MsgProto
from steam.enums.emsg import EMsg
from steam.utils.web import AioHttpClientSessionWithUA, generate_session_id


class Web:
    _web_session = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.on(self.EVENT_DISCONNECTED, self.__handle_disconnect)

    async def __handle_disconnect(self):
        self._web_session = None

    # TODO: DEPRECATED. This function not work anymore.
    # This function must be rewritten to use  WebAuth
    async def get_web_session_cookies(self):
        """Get web authentication cookies via WebAPI's ``AuthenticateUser``

        .. note::
            The cookies are valid only while :class:`.SteamClient` instance is logged on.

        :return: dict with authentication cookies
        :rtype: :class:`dict`, :class:`None`
        """
        if not self.logged_on:
            return None

        resp = await self.send_job_and_wait(
            MsgProto(EMsg.ClientRequestWebAPIAuthenticateUserNonce), timeout=7
        )

        if resp is None:
            return None

        skey, ekey = generate_session_key()

        data = {
            'steamid': self.steam_id,
            'sessionkey': ekey,
            'encrypted_loginkey': symmetric_encrypt(
                resp.webapi_authenticate_user_nonce.encode('ascii'), skey
            ),
        }

        try:
            resp = await webapi.post('ISteamUserAuth', 'AuthenticateUser', 1, params=data)
        except Exception as exp:
            self._LOG.debug('get_web_session_cookies error: %s' % str(exp))
            return None

        return {
            'steamLogin': resp['authenticateuser']['token'],
            'steamLoginSecure': resp['authenticateuser']['tokensecure'],
        }

    async def get_web_session(self, language='english') -> ClientSession | None:
        """Get a :class:`aiohtttp.ClientSession` that is ready for use

        See :meth:`get_web_session_cookies`

        .. note::
            Auth cookies will only be send to ``(help|store).steampowered.com`` and ``steamcommunity.com`` domains

        .. note::
            The session is valid only while :class:`.SteamClient` instance is logged on.

        :param language: localization language for steam pages
        :type language: :class:`str`
        :return: authenticated Session ready for use
        """
        cookies = await self.get_web_session_cookies()
        if cookies is None:
            return None

        # self._web_session = session = make_requests_session()
        session = AioHttpClientSessionWithUA()
        session_id = generate_session_id()

        for domain in [
            'store.steampowered.com',
            'help.steampowered.com',
            'steamcommunity.com',
        ]:
            result = {
                'domain': domain,
            }
            for name, val in cookies.items():
                result[name] = val

            # session.cookies.set('Steam_Language', language, domain=domain)
            # session.cookies.set('birthtime', '-3333', domain=domain)
            # session.cookies.set('sessionid', session_id, domain=domain)
            # session.cookie_jar.update_cookies(
            #     {
            #         'Steam_Language': language,
            #         'birthtime': '-3333',
            #         'sessionid': session_id,
            #     },
            #     URL(f'https://{domain}'),
            # )
            result['Steam_Language'] = language
            result['birthtime'] = '-3333'
            result['sessionid'] = session_id
            session.cookie_jar.update_cookies(result)
        return session
