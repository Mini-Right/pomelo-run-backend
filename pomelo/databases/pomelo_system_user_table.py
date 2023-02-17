#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/25 02:20
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_system_user_table.py
# @Software    : PyCharm
# @Description : 
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR

from pomelo.databases import Base


class PomeloSystemUserTable(Base):
    __tablename__ = "pomelo_system_user"
    __table_args__ = ({'comment': '系统用户表'})
    username = Column(VARCHAR(50), nullable=False, unique=True, comment="账号")
    nickname = Column(VARCHAR(50), nullable=False, comment="姓名")
    password = Column(VARCHAR(255), nullable=False, comment="密码")
    gender = Column(VARCHAR(1), default=0, comment="性别")
    mobile = Column(VARCHAR(11), comment="手机号")
    email = Column(VARCHAR(255), comment="邮箱")
    signature = Column(LONGTEXT, comment="个性签名")
    avatar = Column(LONGTEXT, comment="头像")
    lark_suite_open_id = Column(VARCHAR(50), nullable=False, unique=True, comment="飞书账号openID")
    status = Column(VARCHAR(1), default=0, comment="用户状态 1启用 0禁用")
