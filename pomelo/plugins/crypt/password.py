#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/25 05:39
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : password.py
# @Software    : PyCharm
# @Description :
from passlib.context import CryptContext


class Password(object):
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)
