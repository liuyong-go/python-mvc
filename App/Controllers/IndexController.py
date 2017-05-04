#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController
from aiohttp import web
from App.Models.IndexModel import IndexModel


class IndexController(BaseController):

    @get('/')
    def index(self):
        ix = IndexModel()
        ix.testDel()
        return web.Response(body='<h1>shouye</h1>', content_type='text/html')

    @get('/test/{id}')
    def test(self, id):
        return web.Response(body='<h1>前台测试</h1>' + id, content_type='text/html')
