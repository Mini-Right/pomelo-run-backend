#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/18 02:45
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : database_routers.py
# @Software    : PyCharm
# @Description :
from fastapi import APIRouter, Request

from pomelo.apps.manage.schemas.pomelo_manage_database_config_schemas import PomeloManageDatabaseConfigCreateSchema, PomeloManageDatabaseConfigUpdateSchema, PomeloManageDatabaseConfigStatusSchema, PomeloManageDatabaseConfigQueryListSchema, RouterConfigEnum
from pomelo.apps.manage.services.pomelo_manage_database_config_service import PomeloManageDatabaseConfigService
from pomelo.handler import success_response, fail_response
from pomelo.plugins.logger import logging

logger = logging.getLogger(__name__)
database = APIRouter()
router_name = '数据库配置'


@database.post('/create', name=RouterConfigEnum.Create)
async def database_create(data: PomeloManageDatabaseConfigCreateSchema, request: Request):
    try:
        PomeloManageDatabaseConfigService.create(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.Create}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Create}失败: {str(e)}")


@database.post('/update', name=RouterConfigEnum.Update)
async def database_update(data: PomeloManageDatabaseConfigUpdateSchema, request: Request):
    try:
        PomeloManageDatabaseConfigService.update(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.Update}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Update}失败: {str(e)}")


@database.post('/change_status', name=RouterConfigEnum.ChangeStatus)
async def database_change_status(data: PomeloManageDatabaseConfigStatusSchema, request: Request):
    try:
        PomeloManageDatabaseConfigService.change_status(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.ChangeStatus}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.ChangeStatus}失败: {str(e)}")


@database.post('/query', name=RouterConfigEnum.Query)
async def database_query(data: PomeloManageDatabaseConfigQueryListSchema):
    try:
        config_list = PomeloManageDatabaseConfigService.query(data=data)
        return success_response(data=config_list, msg=f"{RouterConfigEnum.Query}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Query}失败: {str(e)}")


@database.get('/query_detail/{database_id}', name=RouterConfigEnum.QueryDetail)
async def database_query_detail(database_id: str):
    try:
        config_detail = PomeloManageDatabaseConfigService.query_detail(database_id=database_id)
        return success_response(data=config_detail, msg=f"{RouterConfigEnum.QueryDetail}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.QueryDetail}失败: {str(e)}")
