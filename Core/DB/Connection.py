#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql.cursors


class Connection(object):
    """
        数据库连接及基本操作类
    """
    __dbinstance = None
    __distance = None
    __connect = None

    def __init__(self):
        if self.__dbinstance is None:
            # 连接数据库
            self.__connect = pymysql.Connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123',
                db='life',
                charset='utf8'
            )
            self.__dbinstance = self.__connect.cursor()

# 单例模式获取数据库连接
    @staticmethod
    def getInstance():
        if Connection.__distance is None:
            Connection.__distance = Connection()
        return Connection.__distance

# 获取列表记录
    def fetch_all(self, sql, bind):
        self.__dbinstance.execute(sql % bind)
        rs = []
        for row in self.__dbinstance.fetchall():
            rs.append(row)
        return rs

# 获取单记录
    def fetch(self, sql, bind):
        self.__dbinstance.execute(sql % bind)
        rs = []
        for row in self.__dbinstance.fetchone():
            rs.append(row)
        return rs

# 插入数据
    def insert(self, table, data):
        sql = "insert into " + table + "("
        column = ""
        cvalue = ""
        cdata = []
        for k, value in data.items():
            column += k + ', '
            cvalue += "'%s', "
            cdata.append(value)
        column = column.rstrip(', ')
        cvalue = cvalue.rstrip(', ')
        sql += column + ") values (" + cvalue + ")"
        newdata = tuple(cdata)
        self.__dbinstance.execute(sql % newdata)
        insertid = self.__connect.insert_id()
        self.__connect.commit()
        return insertid

# 更新记录
    def update(self, table, data, where, whereBind):
        sql = "update " + table + " set "
        upstr = ""
        binddata = []
        for k, value in data.items():
            upstr += k + "= '%s', "
            binddata.append(value)

        upstr = upstr.rstrip(", ")
        binddata.extend(whereBind)
        sql += upstr + " where " + where
        newdata = tuple(binddata)
        self.__dbinstance.execute(sql % newdata)
        self.__connect.commit()

# 删除记录
    def delete(self, table, where, whereBind):
        sql = "delete from " + table + " where " + where
        newdata = tuple(whereBind)
        self.__dbinstance.execute(sql % newdata)
        self.__connect.commit()















