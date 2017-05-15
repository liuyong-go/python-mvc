#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
判断登录
"""
from Core.Handler import Handler
from App.Library.Result import Result
from App.Models.UserModel import UserModel


def checkLogin(request):
    hand =  Handler()
    params = hand.parseGet(request)
    token = params.get('loginToken')
    if token == None:
        return Result().setCode(Result.CODE_ERROR).setMsg('缺少参数').toJson()
    um = UserModel()
    return um.setLogin(token)
