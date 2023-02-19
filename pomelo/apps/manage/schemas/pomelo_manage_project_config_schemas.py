#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 21:37
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_project_config_schemas.py
# @Software    : PyCharm
# @Description :
from enum import Enum

from pydantic import BaseModel, Field

from pomelo.config.config_schemas import RunConfigEnum

ROUTER_NAME = '项目管理'


class RouterConfigEnum(str, Enum):
    Create = ROUTER_NAME + RunConfigEnum.Create
    Update = ROUTER_NAME + RunConfigEnum.Update
    Delete = ROUTER_NAME + RunConfigEnum.Delete
    ChangeStatus = ROUTER_NAME + RunConfigEnum.ChangeStatus
    Query = ROUTER_NAME + RunConfigEnum.Query
    QueryDetail = ROUTER_NAME + RunConfigEnum.QueryDetail


class PomeloManageProjectConfigIDSchema(BaseModel):
    project_id: str = Field(default=..., title='项目ID')


class PomeloManageProjectConfigCreateSchema(BaseModel):
    project_name: str = Field(default=..., title='project_name')
    owner_user: str = Field(default=..., title='项目负责人ID')
    remark: str = Field(default=None, title='描述')


class PomeloManageProjectConfigUpdateSchema(PomeloManageProjectConfigCreateSchema, PomeloManageProjectConfigIDSchema):
    ...


class PomeloManageProjectConfigStatusSchema(PomeloManageProjectConfigIDSchema):
    status: int = Field(default=..., title='状态')


class PomeloManageProjectConfigQueryListSchema(BaseModel):
    project_name: str = Field(default=None, title='project_name')
