#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/17 23:58
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : system_login_schemas.py
# @Software    : PyCharm
# @Description :
from pydantic import BaseModel, Field


class SystemLoginSchema(BaseModel):
    username: str = Field(default=..., title="用户名")
    password: str = Field(default=..., title="密码")
