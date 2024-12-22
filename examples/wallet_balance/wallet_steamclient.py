import asyncio

from steam.client import EMsg, SteamClient
from steam.enums import ECurrencyCode
from steam.webauth import WebAuth


async def main():
    client = SteamClient()

    @client.on(EMsg.ClientWalletInfoUpdate)
    def print_balance(msg):
        bucks, cents = divmod(msg.body.balance64, 100)
        print(
            'Current balance is {:d}.{:02d} {:s}'.format(
                bucks, cents, ECurrencyCode(msg.body.currency).name
            )
        )

    async with WebAuth() as webauth:
        await webauth.cli_login(input('Steam user: '))
        await client.login(webauth.username, access_token=webauth.refresh_token)
        await client.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
