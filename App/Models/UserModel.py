#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from App.Core.BaseModel import BaseModel
import hashlib, random
from App.Library.Result import Result


class UserModel(BaseModel):
    """
    用户信息
    """

    def __init__(self):
        super().__init__()

    # 微信登录或注册
    def wechatLogin(self, data):
        openid = data['openid']
        uinfo = self.getUserInfoByField('wx_openid',openid)
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
        sql = "select * from user where "+field+"=%s"
        data = (value)
        return self._db.fetch(sql, data)


    # 获取当前登录用户id
    def getLoginUid(self):
        pass

    # 根据token获取登录用户设置session
    def setLogin(self, token):

        pass

