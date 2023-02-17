#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/25 02:05
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : config_schemas.py
# @Software    : PyCharm
# @Description :

from pydantic import BaseModel, Field


class DBItemSchema(BaseModel):
    host: str = Field(...)
    port: int = Field(...)
    user: str = Field(...)
    password: str = Field(...)
    database: str = Field(None)


class DBSchema(BaseModel):
    POMELO: DBItemSchema


class RedisItemSchema(BaseModel):
    host: str
    port: int
    password: str = Field(None)
    db: str


class RedisSchema(BaseModel):
    POMELO: RedisItemSchema


class LarkSuiteSchema(BaseModel):
    APP_ID: str
    APP_SECRET: str
    REDIRECT_URI: str


class ConfigSchema(BaseModel):
    JWT_SECRET: str
    REQUEST_TIMEOUT: int
    DB: DBSchema
    REDIS: RedisSchema
    LARK_SUITE: LarkSuiteSchema
