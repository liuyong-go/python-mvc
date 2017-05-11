#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.parse

class Handler(object):

    def __init__(self):
      pass

    # 解析get参数
    def parseGet(self, request):
        qs = request.query_string
        kw = dict()
        if qs:
            for k, v in urllib.parse.parse_qs(qs, True).items():
                kw[k] = v[0]
        return kw


