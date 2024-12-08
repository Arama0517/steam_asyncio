import asyncio
import logging

from rich.logging import RichHandler

from steam.client import SteamClient

# logging.basicConfig(level=logging.DEBUG, handlers=[RichHandler()])
logging.root.setLevel(logging.DEBUG)
logging.root.addHandler(RichHandler(rich_tracebacks=True))


async def main():
    client = SteamClient()
    print(await client.login('agt8729', 'Apk66433'))
    print(client.logged_on, client.connected)
    resp = await client.send_um_and_wait(
        'PublishedFile.GetDetails#1',
        {'publishedfileids': [3273220145]},
    )
    print(resp)


if __name__ == '__main__':
    asyncio.run(main())
