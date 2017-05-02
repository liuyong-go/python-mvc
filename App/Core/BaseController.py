#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect


class BaseController(object):

    def __init__(self):
        pass

# 获取类方法
    @staticmethod
    def getFuncs(obj):
        theAttrs = inspect.getmembers(obj)
        theRetAttrs = []
        for attr in theAttrs:
            if inspect.isroutine(attr[1]) \
             and attr[0].startswith('_') is False and hasattr(BaseController(), attr[0]) == False:
                theRetAttrs.append(attr[0])
        return theRetAttrs
