#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/20 00:08
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : environment_routers.py
# @Software    : PyCharm
# @Description :

from fastapi import APIRouter, Request

from pomelo.apps.manage.schemas.pomelo_manage_environment_config_schemas import PomeloManageEnvironmentConfigIDSchema, PomeloManageEnvironmentConfigCreateSchema, PomeloManageEnvironmentConfigUpdateSchema, PomeloManageEnvironmentConfigQueryListSchema, RouterConfigEnum, \
    PomeloManageEnvironmentConfigSetDefaultSchema
from pomelo.apps.manage.services.pomelo_manage_environment_config_service import PomeloManageEnvironmentConfigService
from pomelo.handler import success_response, fail_response
from pomelo.plugins.logger import logging

logger = logging.getLogger(__name__)

env = APIRouter()
router_name = '环境配置'


@env.post('/create', name=RouterConfigEnum.Create)
async def project_create(data: PomeloManageEnvironmentConfigCreateSchema, request: Request):
    try:
        PomeloManageEnvironmentConfigService.create(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.Create}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Create}失败: {str(e)}")


@env.post('/update', name=RouterConfigEnum.Update)
async def project_update(data: PomeloManageEnvironmentConfigUpdateSchema, request: Request):
    try:
        PomeloManageEnvironmentConfigService.update(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.Update}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Update}失败: {str(e)}")


@env.post('/set_default', name=RouterConfigEnum.ChangeStatus)
async def project_set_default(data: PomeloManageEnvironmentConfigSetDefaultSchema, request: Request):
    try:
        PomeloManageEnvironmentConfigService.set_default(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.ChangeStatus}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.ChangeStatus}失败: {str(e)}")


@env.post('/query', name=RouterConfigEnum.Query)
async def project_query(data: PomeloManageEnvironmentConfigQueryListSchema):
    try:
        config_list = PomeloManageEnvironmentConfigService.query(data=data)
        return success_response(data=config_list, msg=f"{RouterConfigEnum.Query}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Query}失败: {str(e)}")


@env.get('/query_detail/{env_id}', name=RouterConfigEnum.QueryDetail)
async def project_query_detail(env_id: str):
    try:
        print(env_id)
        config_detail = PomeloManageEnvironmentConfigService.query_detail(env_id=env_id)
        return success_response(data=config_detail, msg=f"{RouterConfigEnum.QueryDetail}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.QueryDetail}失败: {str(e)}")
