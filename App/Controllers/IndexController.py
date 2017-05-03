#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController
from aiohttp import web


class IndexController(BaseController):

    @get('/')
    def index(self):
        return web.Response(body=b'<h1>shouye</h1>', content_type='text/html')

    @get('/test/{id}')
    def test(self, id):
        return web.Response(body=b'<h1>qiantaiceshi</h1>', content_type='text/html')
