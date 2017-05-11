#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Const

if Const.ENV == 'localhost':

    configs = {
        'db' : {
            'host' : 'localhost',
            'port' : 3306,
            'user' : 'root',
            'passwd' : '123',
            'db' : 'cup_diag',
            'charset' : 'utf8'
        },
    }
else:
    configs = {
        'db' : {
            'host' : 'localhost',
            'port' : 3306,
            'user' : 'root',
            'passwd' : '123',
            'db' : 'life',
            'charset' : 'utf8'
        },
    }