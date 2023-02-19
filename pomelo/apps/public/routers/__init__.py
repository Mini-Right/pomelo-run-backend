#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/5/9 21:20
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
from fastapi import APIRouter

from pomelo.apps.public.services import DatabaseConnectionMySQLSchema
from pomelo.apps.public.services.database_connection import DatabaseConnectionService
from pomelo.apps.public.services.user_cache import get_user_info, user_info_list
from pomelo.handler import success_response, fail_response
from pomelo.plugins.logger import logging

logger = logging.getLogger(__name__)
public = APIRouter()


@public.get('/user_info/{user_id}', name='获取用户信息')
async def public_user_info(user_id: str):
    try:
        user_info = get_user_info(user_id=user_id)
        return success_response(data=user_info, msg=f"获取用户信息成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"获取用户信息失败: {str(e)}")


@public.get('/user_info/list', name='获取用户信息列表')
async def public_user_info_list():
    try:
        user_info = user_info_list()
        return success_response(data=user_info, msg=f"获取用户信息成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"获取用户信息失败: {str(e)}")




@public.post('/database_connection/mysql', name='数据库连接')
async def public_database_connection_mysql(data: DatabaseConnectionMySQLSchema):
    try:
        version = DatabaseConnectionService.mysql(data=data)
        return success_response(msg=f"数据库连接成功 数据库版本: {version}")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"数据库连接失败: {str(e)}")
