#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from App.Core.BaseModel import BaseModel
import time

class DiagModel(BaseModel):

    def __init__(self):
        super().__init__()

    # 首页获取文章列表
    def articleList(self):
        sql = "select id,title from diag_article where id>%s"
        data = (1)
        return self._db.fetch_all(sql, data)

    # 文章详情
    def article(self, id):
        sql = "select * from diag_article where id=%s"
        data = (id)
        return self._db.fetch(sql, data)

    #服务套餐列表
    def service(self):
        j = 0
        for i in range(1000000000):
            j += i

        sql = "select * from diag_service order by id desc"
        return self._db.fetch_all(sql)


