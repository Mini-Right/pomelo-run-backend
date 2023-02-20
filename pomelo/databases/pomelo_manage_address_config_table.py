#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 23:30
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_address_config_table.py
# @Software    : PyCharm
# @Description :
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, DATETIME

from pomelo.databases import Base, gen_id


class PomeloManageAddressConfigTable(Base):
    __tablename__ = "pomelo_manage_address_config"
    __table_args__ = ({'comment': '环境地址配置表'})
    address_id = Column(VARCHAR(50), default=gen_id, primary_key=True, index=True)
    env_id = Column(VARCHAR(50), nullable=False, comment="环境ID")
    project_id = Column(VARCHAR(50), nullable=False, comment="项目ID")
    address_name = Column(VARCHAR(50), nullable=False, comment="地址名称")
    address = Column(VARCHAR(255), nullable=False, comment="地址")
    is_default = Column(INTEGER, nullable=False, comment="是否默认环境地址 0否 1是")
