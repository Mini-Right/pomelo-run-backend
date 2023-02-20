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

ROUTER_NAME = '环境管理'


class RouterConfigEnum(str, Enum):
    Create = ROUTER_NAME + RunConfigEnum.Create
    Update = ROUTER_NAME + RunConfigEnum.Update
    Delete = ROUTER_NAME + RunConfigEnum.Delete
    ChangeStatus = ROUTER_NAME + RunConfigEnum.ChangeStatus
    Query = ROUTER_NAME + RunConfigEnum.Query
    QueryDetail = ROUTER_NAME + RunConfigEnum.QueryDetail


class PomeloManageEnvironmentConfigIDSchema(BaseModel):
    env_id: str = Field(default=..., title='环境ID')


class PomeloManageEnvironmentConfigCreateSchema(BaseModel):
    project_id: str = Field(default=..., title='项目ID')
    env_name: str = Field(default=..., title='环境名称')
    is_default: int = Field(default=0, title='是否默认项目环境 0否 1是')
    remark: str = Field(default=None, title='描述')


class PomeloManageEnvironmentConfigUpdateSchema(PomeloManageEnvironmentConfigCreateSchema, PomeloManageEnvironmentConfigIDSchema):
    ...


class PomeloManageEnvironmentConfigSetDefaultSchema(PomeloManageEnvironmentConfigIDSchema):
    project_id: str = Field(default=..., title='项目ID')


class PomeloManageEnvironmentConfigQueryListSchema(BaseModel):
    project_id: str = Field(default=None, title='项目ID')
