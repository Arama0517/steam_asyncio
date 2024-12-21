import logging

from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart, jsonify, request
from rich.logging import RichHandler
from steam_worker import SteamWorker

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
LOG = logging.getLogger('SimpleWebAPI')

app = Quart('SimpleWebAPI')

# 初始化 worker
worker = SteamWorker()


@app.route('/ISteamApps/GetProductInfo/', methods=['GET'])
async def GetProductInfo():
    appids = request.args.get('appids', '')
    pkgids = request.args.get('packageids', '')

    if not appids and not pkgids:
        return jsonify({})

    appids = map(int, appids.split(',')) if appids else []
    pkgids = map(int, pkgids.split(',')) if pkgids else []

    LOG.info('Requesting product info for apps: %s, packages: %s', appids, pkgids)
    result = await worker.get_product_info(appids, pkgids)
    LOG.info('Product info fetched: %s', result)
    return jsonify(result or {})


@app.route('/ISteamApps/GetProductChanges/', methods=['GET'])
async def GetProductChanges():
    chgnum = int(request.args.get('since_changenumber', 0))
    LOG.info('Requesting product changes since change number: %d', chgnum)
    result = await worker.get_product_changes(chgnum)
    LOG.info('Product changes fetched: %s', result)
    return jsonify(result)


@app.route('/ISteamApps/GetPlayerCount/', methods=['GET'])
async def GetPlayerCount():
    appid = int(request.args.get('appid', 0))
    LOG.info('Requesting player count for app ID: %d', appid)
    result = await worker.get_player_count(appid)
    LOG.info('Player count fetched: %s', result)
    return jsonify(result)


# 异步入口函数
async def main():
    LOG.info('Simple Web API recipe')
    LOG.info('-' * 30)
    LOG.info('Starting Steam worker...')

    # 异步初始化 Steam worker
    try:
        await worker.prompt_login()
        LOG.info('Successfully logged in to Steam.')
    except Exception as e:
        LOG.error('Error during Steam login: %s', e)
        return

    LOG.info('Starting HTTP server...')
    config = Config()
    config.bind = ['0.0.0.0:5000']

    # 使用 hypercorn 作为服务器
    try:
        LOG.info('Starting HTTP server on port 5000...')
        await serve(app, config)
    except KeyboardInterrupt:
        LOG.info('Exit requested by user.')
        await worker.close()
    except Exception as e:
        LOG.error('Error while running the server: %s', e)
        await worker.close()


# 运行异步主函数
if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
