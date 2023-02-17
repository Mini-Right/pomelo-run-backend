#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/25 05:43
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : token.py
# @Software    : PyCharm
# @Description :
import uuid
from typing import Any, Optional, Union

from fastapi import HTTPException, Request
from jose import jwt

from pomelo.config import config
from pomelo.plugins.errors import PomeloTokenError
from pomelo.plugins.logger import logging
from pomelo.plugins.session import RedisSession

logger = logging.getLogger(__name__)
ALGORITHM = "HS256"


def create_access_token(subject: Union[str, Any]) -> str:
    """
    # 生成token
    :param subject: 保存到token的值
    :return:
    """
    to_encode = {"sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def check_jwt_token(token: Optional[str]) -> Union[str, Any]:
    """
    解析验证 headers中为token的值
    """
    try:
        payload = jwt.decode(token, config.JWT_SECRET, algorithms=[ALGORITHM])
        if RedisSession.pomelo.exists(f"user:{payload['sub']}:token") == 1:
            RedisSession.pomelo.expire(
                f"user:{payload['sub']}:token", config.REQUEST_TIMEOUT
            )
        else:
            raise PomeloTokenError("token失效 请重新登陆")
        return payload
    except (jwt.JWTError, jwt.ExpiredSignatureError, AttributeError):
        # 抛出自定义异常， 然后捕获统一响应
        raise PomeloTokenError("token失效 请重新登陆")


def get_token_user_id(request: Request):
    try:
        raw_token = request.headers.get("Authorization")
        # 不对登录接口进行解析token获取user_id
        if '/api/auth/login' in request.url.path or '/api/auth/lark_suite_login' in request.url.path:
            return
        _token = raw_token.replace("Bearer ", "")
        token = check_jwt_token(_token)
        request.state.user_id = token.get("sub")
        request.state.track_uuid = uuid.uuid4().hex
    except PomeloTokenError as e:
        logger.warning(f"解析token获取user_id失败: {e}")
        raise HTTPException(status_code=401)
