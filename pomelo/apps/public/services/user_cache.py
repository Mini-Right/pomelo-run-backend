#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 01:46
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : user_cache.py
# @Software    : PyCharm
# @Description :

from pomelo.databases.pomelo_system_user_table import PomeloSystemUserTable
from pomelo.plugins.curd import PomeloTableCURD
from pomelo.plugins.session import RedisSession


def user_cache():
    user_list = PomeloTableCURD().query_table_fields_all(
        table_fields_list=[
            PomeloSystemUserTable.user_id,
            PomeloSystemUserTable.username,
            PomeloSystemUserTable.nickname,
            PomeloSystemUserTable.avatar
        ],
        is_list=True
    )
    for user in user_list:
        RedisSession.pomelo.hmset(f"userInfo:{user.get('user_id')}", user)


def get_user_info(user_id: str):
    return RedisSession.pomelo.hgetall(f"userInfo:{user_id}")


def user_info_list():
    user_list = PomeloTableCURD().query_table_fields_all(
        table_fields_list=[
            PomeloSystemUserTable.user_id,
            PomeloSystemUserTable.username,
            PomeloSystemUserTable.nickname,
            PomeloSystemUserTable.avatar
        ],
        is_list=True
    )
    return user_list
