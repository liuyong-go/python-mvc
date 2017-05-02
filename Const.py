#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


class ConstDic(object):
    '''
    定义常量类
    '''
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise "不可以重复定义常量"
        else:
            self.__dict__[key] = value

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.key
        else:
            return None


sys.modules[__name__] = ConstDic()
