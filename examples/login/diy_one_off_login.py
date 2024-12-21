import asyncio
from getpass import getpass

import steam.webauth as wa
from steam.client import SteamClient


async def main():
    print('One-off login recipe')
    print('-' * 20)

    LOGON_DETAILS = {
        'username': input('Steam user: '),
        'password': getpass('Password: '),
    }

    webauth = wa.WebAuth()

    try:
        await webauth.login(**LOGON_DETAILS)
    except wa.TwoFactorCodeRequired:
        await webauth.login(code=input('Enter SteamGuard Code: '))
    except wa.EmailCodeRequired:
        await webauth.login(code=input('Enter Email Code: '))

    client = SteamClient()

    @client.on('error')
    def error(result):
        print('Logon result:', repr(result))

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
