import logging
from binascii import hexlify

import vdf

from steam.client import SteamClient
from steam.core.msg import MsgProto
from steam.enums.emsg import EMsg
from steam.utils.proto import proto_to_dict
from steam.webauth import WebAuth

LOG = logging.getLogger('Steam Worker')


class SteamWorker:
    def __init__(self):
        self.logged_on_once = False

        self.steam = client = SteamClient()

        @client.on('error')
        def handle_error(result):
            LOG.info('Logon result: %s', repr(result))

        @client.on('connected')
        def handle_connected():
            LOG.info('Connected to %s', client.current_server_addr)

        @client.on('channel_secured')
        async def send_login():
            await client.login(self.username, access_token=self.access_token)

        @client.on('logged_on')
        async def handle_after_logon():
            self.logged_on_once = True

            LOG.info('-' * 30)
            LOG.info('Logged on as: %s', await client.user.name)
            LOG.info('Community profile: %s', client.steam_id.community_url)
            LOG.info('Last logon: %s', await client.user.last_logon)
            LOG.info('Last logoff: %s', await client.user.last_logoff)
            LOG.info('-' * 30)

        @client.on('disconnected')
        async def handle_disconnect():
            LOG.info('Disconnected.')
            LOG.info('Reconnecting...')
            await client.reconnect(maxdelay=30)

        @client.on('reconnect')
        def handle_reconnect(delay):
            LOG.info('Reconnect in %ds...', delay)

    async def prompt_login(self):
        async with WebAuth() as webauth:
            await webauth.cli_login(input('Steam user: '))
            self.username = webauth.username
            self.access_token = webauth.refresh_token
            await self.steam.connect()

    async def close(self):
        if self.steam.logged_on:
            self.logged_on_once = False
            LOG.info('Logout')
            await self.steam.logout()
        if self.steam.connected:
            await self.steam.disconnect()

    async def get_product_info(self, appids=[], packageids=[]):
        resp = await self.steam.send_job_and_wait(
            MsgProto(EMsg.ClientPICSProductInfoRequest),
            {
                'apps': map(lambda x: {'appid': x}, appids),
                'packages': map(lambda x: {'packageid': x}, packageids),
            },
            timeout=10,
        )

        if not resp:
            return {}

        resp = proto_to_dict(resp)

        for app in resp.get('apps', []):
            app['appinfo'] = vdf.loads(app.pop('buffer')[:-1].decode('utf-8', 'replace'))['appinfo']
            app['sha'] = hexlify(app['sha']).decode('utf-8')
        for pkg in resp.get('packages', []):
            pkg['appinfo'] = vdf.binary_loads(pkg.pop('buffer')[4:])[str(pkg['packageid'])]
            pkg['sha'] = hexlify(pkg['sha']).decode('utf-8')

        return resp

    async def get_product_changes(self, since_change_number):
        resp = await self.steam.send_job_and_wait(
            MsgProto(EMsg.ClientPICSChangesSinceRequest),
            {
                'since_change_number': since_change_number,
                'send_app_info_changes': True,
                'send_package_info_changes': True,
            },
            timeout=10,
        )
        return proto_to_dict(resp) or {}

    async def get_player_count(self, appid):
        resp = await self.steam.send_job_and_wait(
            MsgProto(EMsg.ClientGetNumberOfCurrentPlayersDP),
            {'appid': appid},
            timeout=10,
        )
        return proto_to_dict(resp) or {}
