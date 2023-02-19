#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/17 23:56
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
from fastapi import APIRouter

from pomelo.apps.auth.routers import auth
from pomelo.apps.manage.routers import manage
from pomelo.apps.public.routers import public

api = APIRouter()

api.include_router(router=auth, prefix='/auth', tags=['鉴权'])
api.include_router(router=manage, prefix='/manage', tags=['配置管理'])
api.include_router(router=public, prefix='/public', tags=['公共管理'])
