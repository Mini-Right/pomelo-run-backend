#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/11 02:48
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_api_record_table.py
# @Software    : PyCharm
# @Description : 接口请求记录表
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER

from pomelo.databases import Base


class PomeloAPIRecordTable(Base):
    __tablename__ = "pomelo_api_record_table"
    __table_args__ = ({'comment': '接口请求记录表'})
    path = Column(String(255), nullable=False, comment="路径")
    status_code = Column(INTEGER, comment='状态码')
