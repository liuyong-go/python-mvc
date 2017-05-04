#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Core.DB.Connection import Connection


class BaseModel(object):

    _db = None

    def __init__(self):
        self._db = Connection.getInstance()
