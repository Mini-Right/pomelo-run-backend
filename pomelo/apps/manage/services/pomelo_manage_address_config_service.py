#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/19 23:37
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pomelo_manage_address_config_service.py
# @Software    : PyCharm
# @Description :
import uuid

from pomelo.apps.manage.schemas.pomelo_manage_address_config_schemas import PomeloManageAddressConfigCreateSchema, PomeloManageAddressConfigUpdateSchema, PomeloManageAddressConfigQueryListSchema, PomeloManageAddressConfigSetDefaultSchema
from pomelo.databases.pomelo_manage_address_config_table import PomeloManageAddressConfigTable
from pomelo.databases.pomelo_manage_environment_config_table import PomeloManageEnvironmentConfigTable
from pomelo.databases.pomelo_manage_project_config_table import PomeloManageProjectConfigTable
from pomelo.plugins.curd import PomeloTableCURD


class PomeloManageAddressConfigService(object):

    @staticmethod
    def create(data: PomeloManageAddressConfigCreateSchema, operation_user: str):
        if PomeloTableCURD().query_exists(
                params=[
                    PomeloManageAddressConfigTable.project_id == data.project_id,
                    PomeloManageAddressConfigTable.env_id == data.env_id,
                    PomeloManageAddressConfigTable.address_name == data.address_name,
                ]
        ):
            raise Exception('项目名称重复 请修改')

        address_id = uuid.uuid4().hex
        PomeloTableCURD().add_one(
            table_class=PomeloManageAddressConfigTable(
                address_id=address_id,
                env_id=data.env_id,
                project_id=data.project_id,
                address_name=data.address_name,
                address=data.address,
                is_default=data.is_default,
                remark=data.remark,
                create_user=operation_user,
                operation_user=operation_user,
            )
        )
        if data.is_default:
            PomeloManageAddressConfigService.set_default(
                data=PomeloManageAddressConfigSetDefaultSchema(address_id=address_id, env_id=data.env_id, project_id=data.project_id),
                operation_user=operation_user
            )

    @staticmethod
    def update(data: PomeloManageAddressConfigUpdateSchema, operation_user: str):
        if PomeloTableCURD().query_exists(
                params=[
                    PomeloManageAddressConfigTable.project_id == data.project_id,
                    PomeloManageAddressConfigTable.env_id == data.env_id,
                    PomeloManageAddressConfigTable.address_name == data.address_name,
                    PomeloManageAddressConfigTable.address_id != data.address_id,
                ]
        ):
            raise Exception('项目名称重复 请修改')

        PomeloTableCURD().update(
            table_class=PomeloManageAddressConfigTable,
            params=[PomeloManageAddressConfigTable.address_id == data.address_id],
            update=dict(
                env_id=data.env_id,
                project_id=data.project_id,
                address_name=data.address_name,
                address=data.address,
                is_default=data.is_default,
                remark=data.remark,
                operation_user=operation_user,
            )
        )
        if data.is_default:
            PomeloManageAddressConfigService.set_default(
                data=PomeloManageAddressConfigSetDefaultSchema(address_id=data.address_id, env_id=data.env_id, project_id=data.project_id),
                operation_user=operation_user
            )

    @staticmethod
    def set_default(data: PomeloManageAddressConfigSetDefaultSchema, operation_user: str):
        SQL = f"""update pomelo_manage_address_config set is_default = concat(case when address_id = '{data.address_id}' then 1 else 0 end), operation_user = '{operation_user}' where project_id = '{data.project_id}' and env_id = '{data.env_id}';"""
        PomeloTableCURD().execute(sql=SQL)

    @staticmethod
    def query(data: PomeloManageAddressConfigQueryListSchema):
        params = [
            PomeloManageAddressConfigTable.project_id == PomeloManageProjectConfigTable.project_id,
            PomeloManageAddressConfigTable.env_id == PomeloManageEnvironmentConfigTable.env_id,
        ]
        if data.project_id:
            params.append(PomeloManageAddressConfigTable.project_id == data.project_id)
        if data.env_id:
            params.append(PomeloManageAddressConfigTable.env_id == data.env_id)

        result = PomeloTableCURD().query_table_fields_all(
            table_fields_list=[
                PomeloManageAddressConfigTable.address_id,
                PomeloManageAddressConfigTable.env_id,
                PomeloManageAddressConfigTable.project_id,
                PomeloManageAddressConfigTable.address_name,
                PomeloManageAddressConfigTable.address,
                PomeloManageAddressConfigTable.is_default,
                PomeloManageAddressConfigTable.create_time,
                PomeloManageAddressConfigTable.update_time,
                PomeloManageAddressConfigTable.create_user,
                PomeloManageAddressConfigTable.operation_user,
                PomeloManageAddressConfigTable.remark,
                PomeloManageAddressConfigTable.is_delete,
                PomeloManageProjectConfigTable.project_name,
                PomeloManageEnvironmentConfigTable.env_name,
            ],
            params=params,
            order_bys=[
                PomeloManageAddressConfigTable.project_id,
                PomeloManageEnvironmentConfigTable.env_id,
                PomeloManageAddressConfigTable.is_default.desc(),
                PomeloManageAddressConfigTable.update_time.desc()],
            is_list=True,
        )
        return result

    @staticmethod
    def query_detail(address_id: str):
        return PomeloTableCURD().query_table_one(
            table_class=PomeloManageAddressConfigTable,
            params=[PomeloManageAddressConfigTable.address_id == address_id],
            is_dict=True,
        )
