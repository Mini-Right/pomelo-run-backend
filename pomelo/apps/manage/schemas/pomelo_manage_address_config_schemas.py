#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 23:38
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_environment_config_schemas.py
# @Software    : PyCharm
# @Description :
from enum import Enum

from pydantic import BaseModel, Field

from pomelo.config.config_schemas import RunConfigEnum

ROUTER_NAME = '地址管理'


class RouterConfigEnum(str, Enum):
    Create = ROUTER_NAME + RunConfigEnum.Create
    Update = ROUTER_NAME + RunConfigEnum.Update
    Delete = ROUTER_NAME + RunConfigEnum.Delete
    ChangeStatus = ROUTER_NAME + RunConfigEnum.ChangeStatus
    Query = ROUTER_NAME + RunConfigEnum.Query
    QueryDetail = ROUTER_NAME + RunConfigEnum.QueryDetail


class PomeloManageAddressConfigIDSchema(BaseModel):
    address_id: str = Field(default=..., title='环境ID')


class PomeloManageAddressConfigCreateSchema(BaseModel):
    project_id: str = Field(default=..., title='项目ID')
    env_id: str = Field(default=..., title='环境ID')
    address_name: str = Field(default=..., title='地址名称')
    address: str = Field(default=..., title='地址')
    is_default: int = Field(default=0, title='是否默认项目环境 0否 1是')
    remark: str = Field(default=None, title='描述')


class PomeloManageAddressConfigUpdateSchema(PomeloManageAddressConfigCreateSchema, PomeloManageAddressConfigIDSchema):
    ...


class PomeloManageAddressConfigSetDefaultSchema(PomeloManageAddressConfigIDSchema):
    project_id: str = Field(default=..., title='项目ID')
    env_id: str = Field(default=..., title='环境ID')


class PomeloManageAddressConfigQueryListSchema(BaseModel):
    project_id: str = Field(default=None, title='项目ID')
    env_id: str = Field(default=None, title='环境ID')
