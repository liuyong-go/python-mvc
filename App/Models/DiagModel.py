#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from App.Core.BaseModel import BaseModel
from collections import Iterable


class DiagModel(BaseModel):

    def __init__(self):
        super().__init__()

    def articleList(self):
        sql = "select id,title from article where id>%s"
        data = (1)
        return self._db.fetch_all(sql, data)

