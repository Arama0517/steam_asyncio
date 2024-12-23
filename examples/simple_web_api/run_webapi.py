import logging

from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart, jsonify, request
from rich.logging import RichHandler
from steam_worker import SteamWorker

logging.root.setLevel(logging.INFO)
logging.root.handlers = [RichHandler()]
LOG = logging.getLogger('SimpleWebAPI')

app = Quart('SimpleWebAPI')

worker = SteamWorker()


@app.route('/ISteamApps/GetProductInfo/', methods=['GET'])
async def GetProductInfo():
    appids = request.args.get('appids', '')
    pkgids = request.args.get('packageids', '')

    if not appids and not pkgids:
        return jsonify({})

    appids = map(int, appids.split(',')) if appids else []
    pkgids = map(int, pkgids.split(',')) if pkgids else []

    result = await worker.get_product_info(appids, pkgids)
    return jsonify(result or {})


@app.route('/ISteamApps/GetProductChanges/', methods=['GET'])
async def GetProductChanges():
    chgnum = int(request.args.get('since_changenumber', 0))
    result = await worker.get_product_changes(chgnum)
    return jsonify(result)


@app.route('/ISteamApps/GetPlayerCount/', methods=['GET'])
async def GetPlayerCount():
    appid = int(request.args.get('appid', 0))
    result = await worker.get_player_count(appid)
    return jsonify(result)


async def main():
    LOG.info('Simple Web API recipe')
    LOG.info('-' * 30)
    LOG.info('Starting Steam worker...')

    try:
        await worker.prompt_login()
        LOG.info('Successfully logged in to Steam.')
    except Exception as e:
        LOG.error('Error during Steam login: %s', e)
        return

    LOG.info('Starting HTTP server...')
    config = Config()
    config.bind = ['127.0.0.1:5000']
    config.accesslog = LOG

    try:
        LOG.info('Starting HTTP server on port 5000...')
        await serve(app, config)
    finally:
        await worker.close()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
