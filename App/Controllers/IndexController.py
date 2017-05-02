#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController


class IndexController(BaseController):

    @get('/')
    def index(self):
        print ("index page")

    @get('/test/{id}')
    def test(self, id):
        print ('post test', id)
