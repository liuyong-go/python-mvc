#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController
from App.Library.Result import Result
from App.Models.DiagModel import DiagModel


class IndexController(BaseController):

    dg = None
    def __init__(self):
        self.dg = DiagModel()

    @get('/')
    def index(self):
        data = {}
        data['articleList'] = self.dg.articleList()
        return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()

    @get('/article/{id}')
    def article(self, id):
        data = self.dg.article(id)
        if data == None:
            return Result().setCode(Result.CODE_ERROR).setMsg('无此文章').toJson()
        else:
            return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()
        #return web.Response(body='<h1>前台测试</h1>' + id, content_type='text/html')
