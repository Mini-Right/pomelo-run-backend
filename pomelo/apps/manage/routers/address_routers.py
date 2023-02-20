#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/20 00:08
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : environment_routers.py
# @Software    : PyCharm
# @Description :

from fastapi import APIRouter, Request

from pomelo.apps.manage.schemas.pomelo_manage_address_config_schemas import RouterConfigEnum, PomeloManageAddressConfigCreateSchema, PomeloManageAddressConfigUpdateSchema, PomeloManageAddressConfigSetDefaultSchema, PomeloManageAddressConfigQueryListSchema
from pomelo.apps.manage.services.pomelo_manage_address_config_service import PomeloManageAddressConfigService
from pomelo.handler import success_response, fail_response
from pomelo.plugins.logger import logging

logger = logging.getLogger(__name__)

address = APIRouter()
router_name = '环境配置'


@address.post('/create', name=RouterConfigEnum.Create)
async def project_create(data: PomeloManageAddressConfigCreateSchema, request: Request):
    try:
        PomeloManageAddressConfigService.create(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.Create}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Create}失败: {str(e)}")


@address.post('/update', name=RouterConfigEnum.Update)
async def project_update(data: PomeloManageAddressConfigUpdateSchema, request: Request):
    try:
        PomeloManageAddressConfigService.update(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.Update}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Update}失败: {str(e)}")


@address.post('/set_default', name=RouterConfigEnum.ChangeStatus)
async def project_set_default(data: PomeloManageAddressConfigSetDefaultSchema, request: Request):
    try:
        PomeloManageAddressConfigService.set_default(data=data, operation_user=request.state.user_id)
        return success_response(msg=f"{RouterConfigEnum.ChangeStatus}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.ChangeStatus}失败: {str(e)}")


@address.post('/query', name=RouterConfigEnum.Query)
async def project_query(data: PomeloManageAddressConfigQueryListSchema):
    try:
        config_list = PomeloManageAddressConfigService.query(data=data)
        return success_response(data=config_list, msg=f"{RouterConfigEnum.Query}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.Query}失败: {str(e)}")


@address.get('/query_detail/{address_id}', name=RouterConfigEnum.QueryDetail)
async def project_query_detail(address_id: str):
    try:
        config_detail = PomeloManageAddressConfigService.query_detail(address_id=address_id)
        return success_response(data=config_detail, msg=f"{RouterConfigEnum.QueryDetail}成功")
    except Exception as e:
        logger.exception(e)
        return fail_response(msg=f"{RouterConfigEnum.QueryDetail}失败: {str(e)}")
