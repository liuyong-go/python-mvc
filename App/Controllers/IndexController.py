#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController
from aiohttp import web
from App.Models.IndexModel import IndexModel
from App.Library.Result import Result


class IndexController(BaseController):

    @get('/')
    def index(self):
        ix = IndexModel()
        ix.testSql()
        return web.Response(body='<h1>shouye</h1>', content_type='text/html')

    @get('/test/{id}')
    def test(self, id):
        data = {'name':'liuyong', 'age':'1'}
        return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()
        #return web.Response(body='<h1>前台测试</h1>' + id, content_type='text/html')
