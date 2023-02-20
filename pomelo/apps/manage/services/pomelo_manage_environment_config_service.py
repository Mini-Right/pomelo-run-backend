#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 23:37
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_environment_config_service.py
# @Software    : PyCharm
# @Description :
import uuid

from pomelo.apps.manage.schemas.pomelo_manage_environment_config_schemas import PomeloManageEnvironmentConfigCreateSchema, PomeloManageEnvironmentConfigUpdateSchema, PomeloManageEnvironmentConfigQueryListSchema, PomeloManageEnvironmentConfigSetDefaultSchema
from pomelo.databases.pomelo_manage_environment_config_table import PomeloManageEnvironmentConfigTable
from pomelo.databases.pomelo_manage_project_config_table import PomeloManageProjectConfigTable
from pomelo.plugins.curd import PomeloTableCURD


class PomeloManageEnvironmentConfigService(object):

    @staticmethod
    def create(data: PomeloManageEnvironmentConfigCreateSchema, operation_user: str):
        if PomeloTableCURD().query_exists(params=[PomeloManageEnvironmentConfigTable.project_id == data.project_id, PomeloManageEnvironmentConfigTable.env_name == data.env_name]):
            raise Exception('环境名称重复 请修改')

        env_id = uuid.uuid4().hex
        PomeloTableCURD().add_one(
            table_class=PomeloManageEnvironmentConfigTable(
                env_id=env_id,
                project_id=data.project_id,
                env_name=data.env_name,
                is_default=data.is_default,
                remark=data.remark,
                create_user=operation_user,
                operation_user=operation_user,
            )
        )
        if data.is_default:
            PomeloManageEnvironmentConfigService.set_default(
                data=PomeloManageEnvironmentConfigSetDefaultSchema(env_id=env_id, project_id=data.project_id),
                operation_user=operation_user
            )

    @staticmethod
    def update(data: PomeloManageEnvironmentConfigUpdateSchema, operation_user: str):
        if PomeloTableCURD().query_exists(params=[PomeloManageEnvironmentConfigTable.project_id == data.project_id, PomeloManageEnvironmentConfigTable.env_name == data.env_name, PomeloManageEnvironmentConfigTable.env_id != data.env_id]):
            raise Exception('项目名称重复 请修改')

        PomeloTableCURD().update(
            table_class=PomeloManageEnvironmentConfigTable,
            params=[PomeloManageEnvironmentConfigTable.env_id == data.env_id],
            update=dict(
                project_id=data.project_id,
                env_name=data.env_name,
                is_default=data.is_default,
                remark=data.remark,
                operation_user=operation_user,
            )
        )

        if data.is_default:
            PomeloManageEnvironmentConfigService.set_default(
                data=PomeloManageEnvironmentConfigSetDefaultSchema(env_id=data.env_id, project_id=data.project_id),
                operation_user=operation_user
            )

    @staticmethod
    def set_default(data: PomeloManageEnvironmentConfigSetDefaultSchema, operation_user: str):
        SQL = f"""update pomelo_manage_environment_config set is_default = concat(case when env_id = '{data.env_id}' then 1 else 0 end), operation_user = '{operation_user}' where project_id = '{data.project_id}';"""
        PomeloTableCURD().execute(sql=SQL)

    @staticmethod
    def query(data: PomeloManageEnvironmentConfigQueryListSchema):
        params = [PomeloManageEnvironmentConfigTable.project_id == PomeloManageProjectConfigTable.project_id]
        if data.project_id:
            params.append(PomeloManageEnvironmentConfigTable.project_id == data.project_id)

        result = PomeloTableCURD().query_table_fields_all(
            table_fields_list=[
                PomeloManageEnvironmentConfigTable.env_id,
                PomeloManageEnvironmentConfigTable.project_id,
                PomeloManageEnvironmentConfigTable.env_name,
                PomeloManageEnvironmentConfigTable.is_default,
                PomeloManageEnvironmentConfigTable.create_time,
                PomeloManageEnvironmentConfigTable.update_time,
                PomeloManageEnvironmentConfigTable.create_user,
                PomeloManageEnvironmentConfigTable.operation_user,
                PomeloManageEnvironmentConfigTable.remark,
                PomeloManageEnvironmentConfigTable.is_delete,
                PomeloManageProjectConfigTable.project_name,
            ],
            params=params,
            order_bys=[
                PomeloManageEnvironmentConfigTable.project_id,
                PomeloManageEnvironmentConfigTable.is_default.desc(),
                PomeloManageEnvironmentConfigTable.update_time.desc()],
            is_list=True,
        )
        return result

    @staticmethod
    def query_detail(env_id: str):
        return PomeloTableCURD().query_table_one(
            table_class=PomeloManageEnvironmentConfigTable,
            params=[PomeloManageEnvironmentConfigTable.env_id == env_id],
            is_dict=True,
        )
