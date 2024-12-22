import asyncio

from steam.client import SteamClient
from steam.enums import EResult
from steam.webauth import WebAuth


async def main():
    print('One-off login recipe')
    print('-' * 20)

    async with WebAuth() as webauth:
        await webauth.cli_login(input('Steam user: '))
        client = SteamClient()
        result = await client.login(webauth.username, access_token=webauth.refresh_token)

    if result != EResult.OK:
        print('Failed to login: %s' % repr(result))
        raise SystemExit

    print('-' * 20)
    print('Logged on as:', await client.user.name)
    print('Community profile:', client.steam_id.community_url)
    print('Last logon:', await client.user.last_logon)
    print('Last logoff:', await client.user.last_logoff)

    await client.logout()


if __name__ == '__main__':
    asyncio.run(main())
