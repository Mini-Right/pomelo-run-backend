#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/18 02:15
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_run_database_config_service.py
# @Software    : PyCharm
# @Description :
from pomelo.apps.manage.schemas.pomelo_manage_database_config_schemas import PomeloManageDatabaseConfigCreateSchema, PomeloManageDatabaseConfigUpdateSchema, PomeloManageDatabaseConfigIDSchema, PomeloManageDatabaseConfigQueryListSchema, PomeloManageDatabaseConfigStatusSchema
from pomelo.databases.pomelo_manage_database_config_table import PomeloManageDatabaseConfigTable
from pomelo.plugins.curd import PomeloTableCURD


class PomeloManageDatabaseConfigService(object):

    @staticmethod
    def create(data: PomeloManageDatabaseConfigCreateSchema, operation_user: str):
        if PomeloTableCURD().query_exists(params=[PomeloManageDatabaseConfigTable.database_name == data.database_name]):
            raise Exception('数据库名称重复 请修改')

        PomeloTableCURD().add_one(
            table_class=PomeloManageDatabaseConfigTable(
                database_name=data.database_name,
                database_host=data.database_host,
                database_user=data.database_user,
                database_port=data.database_port,
                database_password=data.database_password,
                database_schema=data.database_schema,
                last_connection_state=data.last_connection_state,
                last_connection_time=data.last_connection_time if data.last_connection_time else None,
                remark=data.remark,
                create_user=operation_user,
                operation_user=operation_user,
            )
        )

    @staticmethod
    def update(data: PomeloManageDatabaseConfigUpdateSchema, operation_user: str):
        if PomeloTableCURD().query_exists(params=[PomeloManageDatabaseConfigTable.database_name == data.database_name, PomeloManageDatabaseConfigTable.database_id != data.database_id]):
            raise Exception('数据库名称重复 请修改')

        PomeloTableCURD().update(
            table_class=PomeloManageDatabaseConfigTable,
            params=[PomeloManageDatabaseConfigTable.database_id == data.database_id],
            update=dict(
                database_name=data.database_name,
                database_host=data.database_host,
                database_user=data.database_user,
                database_port=data.database_port,
                database_password=data.database_password,
                database_schema=data.database_schema,
                last_connection_state=data.last_connection_state,
                last_connection_time=data.last_connection_time,
                remark=data.remark,
                operation_user=operation_user,
            )
        )

    @staticmethod
    def delete(data: PomeloManageDatabaseConfigIDSchema):
        PomeloTableCURD().delete(table_class=PomeloManageDatabaseConfigTable, params=[PomeloManageDatabaseConfigTable.database_id == data.database_id])

    @staticmethod
    def change_status(data: PomeloManageDatabaseConfigStatusSchema, operation_user: str):
        PomeloTableCURD().update(
            table_class=PomeloManageDatabaseConfigTable,
            params=[PomeloManageDatabaseConfigTable.database_id == data.database_id],
            update=dict(
                is_delete=data.status,
                operation_user=operation_user,
            )
        )

    @staticmethod
    def query(data: PomeloManageDatabaseConfigQueryListSchema):
        params = []
        if data.database_name:
            params.append(PomeloManageDatabaseConfigTable.database_name.like(f"%{data.database_name}%"))
        result = PomeloTableCURD().query_table_all(
            table_class=PomeloManageDatabaseConfigTable,
            params=params,
            order_bys=[PomeloManageDatabaseConfigTable.update_time.desc()],
            is_list=True,
        )
        return result

    @staticmethod
    def query_detail(database_id: str):
        return PomeloTableCURD().query_table_one(
            table_class=PomeloManageDatabaseConfigTable,
            params=[PomeloManageDatabaseConfigTable.database_id == database_id],
            is_dict=True,
        )

