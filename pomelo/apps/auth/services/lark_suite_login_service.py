#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/18 00:06
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : lark_suite_login_service.py
# @Software    : PyCharm
# @Description : 飞书用户登录
from pomelo.apps.auth.services import PomeloAuthService
from pomelo.databases.pomelo_system_user_table import PomeloSystemUserTable
from pomelo.plugins.crypt import Password
from pomelo.plugins.curd import PomeloTableCURD
from pomelo.plugins.sdk.lark_suite import LarkSuiteAuth


class PomeloLarkSuiteLoginService(PomeloAuthService):
    def login(self, code: str):
        auth = LarkSuiteAuth()
        access_token = auth.oauth_token(code=code)
        lark_suite_userinfo = auth.oauth_userinfo(access_token=access_token)
        lark_suite_mobile = lark_suite_userinfo.get('mobile').replace('+86', '')
        user_info: PomeloSystemUserTable = PomeloTableCURD().query_table_one(
            table_class=PomeloSystemUserTable,
            params=[PomeloSystemUserTable.mobile == lark_suite_mobile],
        )
        # 通过手机号判断用户是否在系统存在，如不存在 则创建并返回user_id 进行token生成
        user_id = user_info.id if user_info else self.create_user(lark_suite_userinfo=lark_suite_userinfo)
        token = self.set_user_token(user_id=user_id)
        return {'token': token}

    @staticmethod
    def create_user(lark_suite_userinfo: dict):
        lark_suite_mobile = lark_suite_userinfo.get('mobile').replace('+86', '')
        user_id = PomeloTableCURD().add_one(
            table_class=PomeloSystemUserTable(
                username=lark_suite_mobile,
                nickname=lark_suite_userinfo.get('name'),
                password=Password().get_password_hash('123456'),
                mobile=lark_suite_mobile,
                avatar=lark_suite_userinfo.get('avatar_url'),
                lark_suite_open_id=lark_suite_userinfo.get('open_id'),
                status='1',
            )
        )
        return user_id
