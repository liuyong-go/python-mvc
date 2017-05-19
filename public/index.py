#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging, sys
sys.path.append("..")
logging.basicConfig(level=logging.INFO)
import asyncio, os
from App.Middleware.Middleware import checkLogin

from aiohttp import web
from Core.Router import add_routes
import Const

Const.BasePath = os.path.dirname(os.path.abspath('.')) + '/'
Const.AppPath = Const.BasePath + 'App/'
Const.ENV = 'localhost'

def index(request):
    return web.Response(body=b'<h1>Awesom222e</h1>', content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    #app.router.add_route('GET', '/', index)
    add_routes(app)
    handler = app.make_handler()
    srv = await loop.create_server(handler, '127.0.0.1', 10000)
    logging.info('server started at http://127.0.0.1:10000...')
    return handler


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
