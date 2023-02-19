#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/17 23:57
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : system_login_service.py
# @Software    : PyCharm
# @Description : 系统用户登录
from pomelo.apps.auth.schemas.system_login_schemas import SystemLoginSchema
from pomelo.apps.auth.services import PomeloAuthService
from pomelo.databases.pomelo_system_user_table import PomeloSystemUserTable
from pomelo.plugins.crypt import Password
from pomelo.plugins.curd import PomeloTableCURD
from pomelo.plugins.errors import PomeloUserError


class PomeloSystemLoginService(PomeloAuthService):

    def login(self, data: SystemLoginSchema):
        user_info: PomeloSystemUserTable = PomeloTableCURD().query_table_one(
            table_class=PomeloSystemUserTable,
            params=[PomeloSystemUserTable.username == data.username],
        )
        if not user_info:
            raise PomeloUserError('用户不存在')
        if not Password().verify_password(plain_password=data.password, hashed_password=user_info.password):
            raise PomeloUserError('用户名或密码错误')
        token = self.set_user_token(user_id=user_info.user_id)
        return {'token': token}


