#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController
from aiohttp import web
from App.Library.Result import Result
from App.Models.DiagModel import DiagModel


class IndexController(BaseController):

    @get('/')
    def index(self):
        dg = DiagModel()
        data = {}
        data['articleList'] = dg.articleList()
        return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()

    @get('/test/{id}')
    def test(self, id):
        data = {'name':'liuyong', 'age':'1'}
        return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()
        #return web.Response(body='<h1>前台测试</h1>' + id, content_type='text/html')
