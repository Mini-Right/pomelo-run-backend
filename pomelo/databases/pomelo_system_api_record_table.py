#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/11 02:48
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_system_api_record_table.py
# @Software    : PyCharm
# @Description : 接口请求记录表
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from pomelo.databases import Base, gen_id


class PomeloSystemAPIRecordTable(Base):
    __tablename__ = "pomelo_system_api_record_table"
    __table_args__ = ({'comment': '接口请求记录表'})
    database_id = Column(VARCHAR(50), default=gen_id, primary_key=True, index=True)
    path = Column(VARCHAR(255), nullable=False, comment="路径")
    status_code = Column(INTEGER, comment='状态码')
