#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/5/9 21:20
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
from fastapi import APIRouter
from pomelo.apps.manage.routers.database_routers import database
from pomelo.apps.manage.routers.project_routers import project

manage = APIRouter()

manage.include_router(router=database, prefix='/database')
manage.include_router(router=project, prefix='/project')