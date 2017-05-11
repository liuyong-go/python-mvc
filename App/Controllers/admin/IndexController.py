#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController


class IndexController(BaseController):
    middlewares = ['login']
    @get('/admin')
    def indextest(self):
        print ("admin index page")

    @post('/admin/test/{id}')
    def test(self, id):
        print ('post test', id)
