#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from App.Core.BaseModel import BaseModel
import hashlib, random
from App.Library.Result import Result
import  asyncio


class UserModel(BaseModel):
    """
    用户信息
    """
    userid = 0
    def __init__(self):
        super().__init__()

    # 微信登录或注册
    def wechatLogin(self, data):
        openid = data['openid']
        uinfo = self.getUserInfoByField('wx_openid',openid)
        print(uinfo)
        rsdata = {}
        rsdata['is_reg'] = 0
        if uinfo == None: #需要注册
            m1 = hashlib.md5()
            m1.update(openid.encode("utf8"))
            rsdata['is_reg'] = 1
            userinfo = {}
            userinfo['wx_openid'] = openid
            userinfo['unionid'] = data['unionid']
            userinfo['token'] = m1.hexdigest()+ str(random.random()*10000).split('.')[0]
            userinfo['nick_name'] = data['nickname']
            userinfo['head_image'] = data['head_image']
            userid = self._db.insert('user', userinfo)
            rsdata['userid'] = userid
            rsdata['token'] = userinfo['token']
            if int(userid) >0:
                return Result().setCode(Result.CODE_SUCCESS).setData(rsdata).setMsg('操作成功')
            else:
                return Result().setCode(Result.CODE_ERROR).setMsg('注册失败')
        rsdata['userid'] = uinfo['id']
        rsdata['token'] = uinfo['token']
        return Result().setCode(Result.CODE_SUCCESS).setData(rsdata).setMsg('操作成功')

    # 根据用户ID获取用户信息
    def getUserInfo(self, id):
        pass

    # 根据字段获取用户信息
    def getUserInfoByField(self, field, value):
        sql = "select * from user where "+field+"='%s'"
        data = (value)
        return self._db.fetch(sql, data)


    # 获取当前登录用户id
    def getLoginUid(self):
        return UserIdModel.getInstance().userid

    # 根据token获取登录用户设置session
    def setLogin(self, token):
        uinfo = self.getUserInfoByField('token', token)
        if uinfo == None:
            return Result().setCode(Result.CODE_ERROR).setMsg('不存在此用户').toJson()
        UserIdModel.getInstance().userid = uinfo['id']
        return None

    # 测试
    @asyncio.coroutine
    def sumTest(self):
        sum = 0
        for x in list(range(10000000)):
            sum = sum + x
        sum2 = yield from  self.moreSum()
        return sum + sum2

    @asyncio.coroutine
    def moreSum(self):
        sum = 0
        for x in list(range(10000000)):
            sum = sum + x
        return sum

class UserIdModel(BaseModel):

    _userid = None
    __distance = None

    @staticmethod
    def getInstance():
        if UserIdModel.__distance is None:
            UserIdModel.__distance = UserIdModel()
        return UserIdModel.__distance

    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value


