#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController
from App.Library.Result import Result
from App.Models.DiagModel import DiagModel
from Core.Handler import Handler


class IndexController(BaseController):

    dg = None
    def __init__(self):
        self.dg = DiagModel()

    # 首页文章列表
    @get('/')
    def index(self):
        data = {}
        data['articleList'] = self.dg.articleList()
        return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()

    # 文章详情页
    @get('/article/{id}')
    def article(self, id):
        data = self.dg.article(id)
        if data == None:
            return Result().setCode(Result.CODE_ERROR).setMsg('无此文章').toJson()
        else:
            return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()

    # 服务套餐列表
    @get('/service')
    def service(self):
        data = {}
        data['serviceList'] = self.dg.service()
        return Result().setCode(Result.CODE_SUCCESS).setData(data).setMsg('操作成功').toJson()

