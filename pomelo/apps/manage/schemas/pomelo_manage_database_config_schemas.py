#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/18 02:17
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_run_database_config_schemas.py
# @Software    : PyCharm
# @Description :
from enum import Enum
from typing import List

from pydantic import BaseModel, Field

from pomelo.config.config_schemas import RunConfigEnum

ROUTER_NAME = '数据库配置'


class RouterConfigEnum(str, Enum):
    Create = ROUTER_NAME + RunConfigEnum.Create
    Update = ROUTER_NAME + RunConfigEnum.Update
    ChangeStatus = ROUTER_NAME + RunConfigEnum.ChangeStatus
    Delete = ROUTER_NAME + RunConfigEnum.Delete
    Query = ROUTER_NAME + RunConfigEnum.Query
    QueryDetail = ROUTER_NAME + RunConfigEnum.QueryDetail


class PomeloManageDatabaseConfigIDSchema(BaseModel):
    database_id: str = Field(default=..., title='数据库 ID')


class PomeloManageDatabaseConfigCreateSchema(BaseModel):
    database_name: str = Field(default=..., title='数据库名称')
    database_host: str = Field(default=..., title='数据库 host')
    database_user: str = Field(default=..., title='数据库 user')
    database_port: int = Field(default=..., title='数据库 port')
    database_password: str = Field(default=..., title='数据库 password')
    database_schema: str = Field(default=None, title='数据库 schema')
    last_connection_state: int = Field(default=0, title='上次链接状态 0未连接 1成功  2失败')
    last_connection_time: str = Field(default=None, title='上次链接时间')
    remark: str = Field(default=None, title='描述')


class PomeloManageDatabaseConfigUpdateSchema(PomeloManageDatabaseConfigCreateSchema, PomeloManageDatabaseConfigIDSchema):
    ...


class PomeloManageDatabaseConfigQueryListSchema(BaseModel):
    database_name: str = Field(default=None, title='数据库名称')


class PomeloManageDatabaseConfigItemSchema(BaseModel):
    database_id: str
    database_name: str
    database_host: str
    database_user: str
    database_port: int
    database_password: str
    create_time: str
    update_time: str
    create_user: str
    operation_user: str
    remark: str
    is_delete: int


class ResponseBaseSchema(BaseModel):
    code: int
    msg: str


class PomeloManageDatabaseConfigQueryListResponseSchema(ResponseBaseSchema):
    data: List[PomeloManageDatabaseConfigItemSchema]


class PomeloManageDatabaseConfigStatusSchema(PomeloManageDatabaseConfigIDSchema):
    status: int = Field(default=..., title='状态')


class PomeloDatabaseTestConnection(BaseModel):
    database_host: str = Field(default=..., title='数据库 host')
    database_user: str = Field(default=..., title='数据库 user')
    database_port: int = Field(default=..., title='数据库 port')
    database_password: str = Field(default=..., title='数据库 password')
    database_schema: str = Field(default=None, title='数据库 schema')