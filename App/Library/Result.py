#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from aiohttp import web


class Result(object):
    """
        返回json
    """
    # 成功
    CODE_SUCCESS = 1
    # 失败
    CODE_ERROR = 0
    # 没有权限
    CODE_NOAUTH = -402
    #未登录
    CODE_NO_LOGIN = -401
    # 禁止访问
    CODE_FORBIDDEN = 403

    _result_arr = {}

    def __init__(self):
        self._result_arr = {
            'code':'1', 'data':'', 'msg':''
        }

    # 设置code
    def setCode(self, code):
        self._result_arr['code'] = code
        return self

    # 设置data
    def setData(self, data):
        self._result_arr['data'] = data
        return self

    # 设置msg
    def setMsg(self, msg):
        self._result_arr['msg'] = msg
        return self

    def toJson(self):
        if self._result_arr['data'] == '':
            self._result_arr.pop('data')
        result_json = json.dumps(self._result_arr, ensure_ascii = False)
        return web.Response(body = result_json, content_type='application/json',charset='utf-8')


