#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/5/9 21:20
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
from pydantic import BaseModel, Field


class DatabaseConnectionMySQLSchema(BaseModel):
    database_host: str = Field(default=...)
    database_port: int = Field(default=...)
    database_user: str = Field(default=...)
    database_password: str = Field(default=...)
    database_schema: str = Field(default=None)
