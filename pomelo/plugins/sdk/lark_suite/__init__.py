#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/10 15:35
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
import requests

from pomelo.config import config
from pomelo.plugins.logger import logging

logger = logging.getLogger(__name__)


class LarkSuiteAuth(object):
    def __init__(self):
        self.domain = 'https://passport.feishu.cn'
        self.session = requests.Session()

    def oauth_token(self, code: str):
        url = self.domain + '/suite/passport/oauth/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': config.LARK_SUITE.APP_ID,
            'client_secret': config.LARK_SUITE.APP_SECRET,
            'redirect_uri': config.LARK_SUITE.REDIRECT_URI,
        }
        res = self.session.post(url=url, data=data)
        access_token = res.json().get('access_token')
        return access_token

    def oauth_userinfo(self, access_token: str):
        """获取用户信息"""
        url = self.domain + '/suite/passport/oauth/userinfo'
        headers = {'Authorization': f'Bearer {access_token}'}
        res = self.session.get(url=url, headers=headers)
        return res.json()
