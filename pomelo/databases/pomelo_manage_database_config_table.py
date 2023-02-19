#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/25 02:20
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_database_config_table.py
# @Software    : PyCharm
# @Description : 
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, DATETIME

from pomelo.databases import Base, gen_id


class PomeloManageDatabaseConfigTable(Base):
    __tablename__ = "pomelo_manage_database_config"
    __table_args__ = ({'comment': '数据库配置表'})
    database_id = Column(VARCHAR(50), default=gen_id, primary_key=True, index=True)
    database_name = Column(VARCHAR(50), nullable=False, unique=True, comment="数据库名称")
    database_host = Column(VARCHAR(50), nullable=False, comment="数据库 host")
    database_user = Column(VARCHAR(50), nullable=False, comment="数据库 user")
    database_password = Column(VARCHAR(50), nullable=False, comment="数据库 password")
    database_port = Column(INTEGER, nullable=False, comment="数据库 port")
    database_schema = Column(VARCHAR(50), comment="数据库 schema")
    last_connection_state = Column(INTEGER, default=0, comment="上次链接状态 0未连接 1成功  2失败")
    last_connection_time = Column(DATETIME, comment="上次链接时间")
