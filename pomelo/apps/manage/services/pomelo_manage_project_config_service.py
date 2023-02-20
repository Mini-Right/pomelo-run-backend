#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 21:34
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_project_config_service.py
# @Software    : PyCharm
# @Description :
from pomelo.apps.manage.schemas.pomelo_manage_project_config_schemas import PomeloManageProjectConfigCreateSchema, PomeloManageProjectConfigUpdateSchema, PomeloManageProjectConfigStatusSchema, PomeloManageProjectConfigQueryListSchema
from pomelo.databases.pomelo_manage_project_config_table import PomeloManageProjectConfigTable
from pomelo.plugins.curd import PomeloTableCURD


class PomeloManageProjectConfigService(object):

    @staticmethod
    def create(data: PomeloManageProjectConfigCreateSchema, operation_user: str):
        if PomeloTableCURD().query_exists(params=[PomeloManageProjectConfigTable.project_name == data.project_name]):
            raise Exception('项目名称重复 请修改')

        PomeloTableCURD().add_one(
            table_class=PomeloManageProjectConfigTable(
                project_name=data.project_name,
                owner_user=data.owner_user,
                remark=data.remark,
                create_user=operation_user,
                operation_user=operation_user,
            )
        )

    @staticmethod
    def update(data: PomeloManageProjectConfigUpdateSchema, operation_user: str):
        if PomeloTableCURD().query_exists(params=[PomeloManageProjectConfigTable.project_name == data.project_name, PomeloManageProjectConfigTable.project_id != data.project_id]):
            raise Exception('项目名称重复 请修改')

        PomeloTableCURD().update(
            table_class=PomeloManageProjectConfigTable,
            params=[PomeloManageProjectConfigTable.project_id == data.project_id],
            update=dict(
                project_name=data.project_name,
                owner_user=data.owner_user,
                remark=data.remark,
                operation_user=operation_user,
            )
        )

    @staticmethod
    def change_status(data: PomeloManageProjectConfigStatusSchema, operation_user: str):
        PomeloTableCURD().update(
            table_class=PomeloManageProjectConfigTable,
            params=[PomeloManageProjectConfigTable.project_id == data.project_id],
            update=dict(
                is_delete=data.status,
                operation_user=operation_user,
            )
        )

    @staticmethod
    def query(data: PomeloManageProjectConfigQueryListSchema):
        params = []
        if data.project_name:
            params.append(PomeloManageProjectConfigTable.project_name.like(f"%{data.project_name}%"))
        result = PomeloTableCURD().query_table_all(
            table_class=PomeloManageProjectConfigTable,
            params=params,
            order_bys=[PomeloManageProjectConfigTable.update_time.desc()],
            is_list=True,
        )
        return result

    @staticmethod
    def query_detail(project_id: str):
        return PomeloTableCURD().query_table_one(
            table_class=PomeloManageProjectConfigTable,
            params=[PomeloManageProjectConfigTable.project_id == project_id],
            is_dict=True,
        )
