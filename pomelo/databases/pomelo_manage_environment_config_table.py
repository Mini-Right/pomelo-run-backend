#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 23:30
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_environment_config_table.py
# @Software    : PyCharm
# @Description :
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER

from pomelo.databases import Base, gen_id


class PomeloManageEnvironmentConfigTable(Base):
    __tablename__ = "pomelo_manage_environment_config"
    __table_args__ = ({'comment': '环境配置表'})
    env_id = Column(VARCHAR(50), default=gen_id, primary_key=True, index=True)
    project_id = Column(VARCHAR(50), nullable=False, comment="项目ID")
    env_name = Column(VARCHAR(50), nullable=False, comment="环境名称")
    is_default = Column(INTEGER, nullable=False, comment="是否默认项目环境 0否 1是")
