#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from App.Core.BaseModel import BaseModel


class DiagModel(BaseModel):

    def __init__(self):
        super().__init__()

    # 首页获取文章列表
    def articleList(self):
        sql = "select id,title from article where id>%s"
        data = (1)
        return self._db.fetch_all(sql, data)

    # 文章详情
    def article(self, id):
        sql = "select * from article where id=%s"
        data = (id)
        return self._db.fetch(sql, data)

    #服务套餐列表
    def service(self):
        sql = "select * from service order by id desc"
        return self._db.fetch_all(sql)


