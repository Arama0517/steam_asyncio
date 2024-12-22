import json
import logging
from pathlib import Path

from steam.client import SteamClient
from steam.enums import EResult
from steam.webauth import WebAuth

# setup logging
logging.basicConfig(format='%(asctime)s | %(message)s', level=logging.INFO)
LOG = logging.getLogger()

# file to save/load credentials
CREDENTIALS = Path.cwd() / 'credentials.json'


async def main():
    if CREDENTIALS.exists():
        with CREDENTIALS.open('r', encoding='utf-8') as f:
            credentials = json.load(f)
    else:
        async with WebAuth() as webauth:
            await webauth.cli_login(input('Steam user: '))
            credentials = {
                'username': webauth.username,
                'refresh_token': webauth.refresh_token,
            }
            with CREDENTIALS.open('w', encoding='utf-8') as f:
                json.dump(credentials, f, indent=4)

    client = SteamClient()

    @client.on('error')
    def handle_error(result):
        LOG.info('Logon result: %s', repr(result))

    @client.on('channel_secured')
    async def send_login():
        await client.login(credentials['username'], access_token=credentials['refresh_token'])

    @client.on('connected')
    def handle_connected():
        LOG.info('Connected to %s', client.current_server_addr)

    @client.on('reconnect')
    def handle_reconnect(delay):
        LOG.info('Reconnect in %ds...', delay)

    @client.on('disconnected')
    async def handle_disconnect():
        LOG.info('Disconnected.')
        LOG.info('Reconnecting...')
        await client.reconnect(maxdelay=30)

    @client.on('logged_on')
    async def handle_after_logon():
        LOG.info('-' * 30)
        LOG.info('Logged on as: %s', await client.user.name)
        LOG.info('Community profile: %s', client.steam_id.community_url)
        LOG.info('Last logon: %s', await client.user.last_logon)
        LOG.info('Last logoff: %s', await client.user.last_logoff)
        LOG.info('-' * 30)
        LOG.info('Press ^C to exit')

    # main bit
    LOG.info('Persistent logon recipe')
    LOG.info('-' * 30)

    result = await client.connect()

    if result != EResult.OK:
        LOG.info('Failed to login: %s' % repr(result))
        raise SystemExit

    try:
        await client.run_forever()
    except KeyboardInterrupt:
        if client.connected:
            LOG.info('Logout')
            await client.logout()
