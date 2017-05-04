#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from App.Core.BaseModel import BaseModel
from collections import Iterable


class IndexModel(BaseModel):

    def __init__(self):
        super().__init__()

    def testSql(self):
        sql = "SELECT * FROM city WHERE id in(%d,%d) "
        data = (1, 2)
        print(self._db.fetch_all(sql, data))
        print(self._db.fetch(sql, data))

    def testInsert(self):
        data = {}
        data['userid'] = 1
        data['content'] = 'ceshi'
        data['contact'] = '12222'
        data['create_time'] = '2016-12-12 11:11:11'
        print(self._db.insert('feedback', data))

    def testUp(self):
        data = {}
        data['content'] = '修改测试'
        data['contact'] = '12222'
        data['create_time'] = '2016-12-12 11:11:11'
        where = "id='%s'"
        whereBind = ['39']
        self._db.update('feedback', data, where, whereBind)

    def testDel(self):
        where = "id='%s'"
        whereBind = ['40']
        self._db.delete('feedback', where, whereBind)
