#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DecorateFunc import get, post
from  App.Core.BaseController import BaseController
from App.Library.Result import Result
from App.Models.UserModel import UserModel


class UserController(BaseController):


    User = None
    def __init__(self):
        self.User = UserModel()

    # 微信登录
    @post('/user/wechatLogin')
    def wechatLogin(self, **kw):
        return self.User.wechatLogin(kw).toJson()


