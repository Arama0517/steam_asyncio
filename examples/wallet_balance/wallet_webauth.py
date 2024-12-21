import asyncio
import re
from getpass import getpass

from steam.webauth import WebAuth


async def main():
    username = input('Username: ')
    password = getpass('Password: ')

    webauth = WebAuth()

    await webauth.cli_login(username, password)

    if webauth.logged_on:
        resp = await webauth.get('https://store.steampowered.com/account/store_transactions/')
        resp.raise_for_status()
        balance = re.search(r'store_transactions/">(?P<balance>.*?)</a>', await resp.text()).group(
            'balance'
        )
        print('Current balance: %s' % balance)


if __name__ == '__main__':
    asyncio.run(main())
