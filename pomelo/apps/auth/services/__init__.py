#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/5/9 21:20
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
from pomelo.config import config
from pomelo.plugins.crypt import create_access_token
from pomelo.plugins.session import RedisSession


class PomeloAuthService(object):

    @staticmethod
    def logout(user_id: str):
        RedisSession.pomelo.delete(f"user:{user_id}:token")
        return True

    @staticmethod
    def set_user_token(user_id: str):
        """创建用户token"""
        token = create_access_token(user_id)
        RedisSession.pomelo.set(name=f"user:{user_id}:token", value=token, ex=config.REQUEST_TIMEOUT)
        return token
