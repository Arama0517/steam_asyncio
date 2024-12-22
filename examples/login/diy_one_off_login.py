import asyncio
from getpass import getpass

from steam.client import SteamClient
from steam.webauth import WebAuth


async def main():
    print('One-off login recipe')
    print('-' * 20)

    LOGON_DETAILS = {
        'username': input('Steam user: '),
        'password': getpass('Password: '),
    }

    client = SteamClient()

    @client.on('error')
    def error(result):
        print('Logon result:', repr(result))

    async with WebAuth() as webauth:
        await webauth.cli_login(**LOGON_DETAILS)

        try:
            await client.login(webauth.username, access_token=webauth.refresh_token)
        except Exception:
            raise SystemExit

    print('-' * 20)
    print('Logged on as:', await client.user.name)
    print('Community profile:', client.steam_id.community_url)
    print('Last logon:', await client.user.last_logon)
    print('Last logoff:', await client.user.last_logoff)

    await client.logout()


if __name__ == '__main__':
    asyncio.run(main())
