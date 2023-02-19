#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 21:50
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : project_routers.py
# @Software    : PyCharm
# @Description :

from fastapi import APIRouter, Request

from pomelo.apps.manage.schemas.pomelo_manage_project_config_schemas import PomeloManageProjectConfigCreateSchema, PomeloManageProjectConfigUpdateSchema, PomeloManageProjectConfigStatusSchema, PomeloManageProjectConfigQueryListSchema, RouterConfigEnum
from pomelo.apps.manage.services.pomelo_manage_project_config_service import PomeloManageProjectConfigService
from pomelo.handler import success_response, fail_response
from pomelo.plugins.logger import logging

logger = logging.getLogger(__name__)

project = APIRouter()
router_name = '项目配置'


@project.post('/create', name=RouterConfigEnum.Create)
async def project_create(data: PomeloManageProjectConfigCreateSchema, request: Request):
    try:
        PomeloManageProjectConfigService.create(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.Create}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Create}失败: {str(e)}")


@project.post('/update', name=RouterConfigEnum.Update)
async def project_update(data: PomeloManageProjectConfigUpdateSchema, request: Request):
    try:
        PomeloManageProjectConfigService.update(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.Update}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Update}失败: {str(e)}")


@project.post('/change_status', name=RouterConfigEnum.ChangeStatus)
async def project_change_status(data: PomeloManageProjectConfigStatusSchema, request: Request):
    try:
        PomeloManageProjectConfigService.change_status(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.ChangeStatus}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.ChangeStatus}失败: {str(e)}")


@project.post('/query', name=RouterConfigEnum.Query)
async def project_query(data: PomeloManageProjectConfigQueryListSchema):
    try:
        config_list = PomeloManageProjectConfigService.query(data=data)
        return success_response(data=config_list, msg=f"{RouterConfigEnum.Query}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Query}失败: {str(e)}")


@project.get('/query_detail/{project_id}', name=RouterConfigEnum.QueryDetail)
async def project_query_detail(project_id: str):
    try:
        config_detail = PomeloManageProjectConfigService.query_detail(project_id=project_id)
        return success_response(data=config_detail, msg=f"{RouterConfigEnum.QueryDetail}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.QueryDetail}失败: {str(e)}")
