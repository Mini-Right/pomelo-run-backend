#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 04:18
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : database_connection.py
# @Software    : PyCharm
# @Description :
from pomelo.apps.public.services import DatabaseConnectionMySQLSchema
from pomelo.plugins.curd import PomeloTableCURD
from pomelo.config import DBItemSchema
from pomelo.plugins.session import init_mysql_session


class DatabaseConnectionService(object):

    @staticmethod
    def mysql(data: DatabaseConnectionMySQLSchema):
        tmp_session = init_mysql_session(database_config=DBItemSchema(
            host=data.database_host,
            port=data.database_port,
            user=data.database_user,
            password=data.database_password,
            database=data.database_schema,
        ))
        try:
            database_info = PomeloTableCURD(session=tmp_session).query_sql_one(sql="select @@version as version;", is_dict=True)
            return database_info.get('version')
        except Exception as e:
            raise Exception(e.orig)
