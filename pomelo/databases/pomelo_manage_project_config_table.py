#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 15:56
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_project_config_table.py
# @Software    : PyCharm
# @Description :
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR

from pomelo.databases import Base, gen_id


class PomeloManageProjectConfigTable(Base):
    __tablename__ = "pomelo_manage_project_config"
    __table_args__ = ({'comment': '项目配置表'})
    project_id = Column(VARCHAR(50), default=gen_id, primary_key=True, index=True)
    project_name = Column(VARCHAR(50), nullable=False, unique=True, comment="项目名称")
    owner_user = Column(VARCHAR(50), nullable=False, unique=True, comment="项目负责人ID")
