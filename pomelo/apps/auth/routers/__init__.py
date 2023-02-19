#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/5/9 21:20
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
from fastapi import APIRouter, Request

from pomelo.apps.auth.schemas.system_login_schemas import SystemLoginSchema
from pomelo.apps.auth.services import PomeloAuthService
from pomelo.apps.auth.services.lark_suite_login_service import PomeloLarkSuiteLoginService
from pomelo.apps.auth.services.system_login_service import PomeloSystemLoginService
from pomelo.handler import login_fail_response, success_response
from pomelo.plugins.logger import logging

logger = logging.getLogger(__name__)
auth = APIRouter()


@auth.post('/login', name='登录')
async def auth_login(data: SystemLoginSchema):
    try:
        result = PomeloSystemLoginService().login(data)
        return success_response(data=result, msg="登陆成功")
    except Exception as e:
        logger.exception(e)
        return login_fail_response(msg=f"登陆失败: {str(e)}")


@auth.get('/lark_suite_login', name='飞书登录')
async def auth_lark_suite_login(code: str):
    try:
        result = PomeloLarkSuiteLoginService().login(code=code)
        return success_response(data=result, msg="登陆成功")
    except Exception as e:
        logger.exception(e)
        return login_fail_response(msg=f"登陆失败: {str(e)}")


@auth.get('/logout', name='登出')
async def user_logout(request: Request):
    try:
        PomeloAuthService.logout(request.state.user_id)
    except Exception as e:
        logger.exception(e)
        return login_fail_response(msg=f"登出失败: {str(e)}")
