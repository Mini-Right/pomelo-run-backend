#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/25 02:05
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description : 
import toml

from pomelo.config.config_schemas import (ConfigSchema, DBItemSchema, RedisItemSchema)
from root_path import root_path

__all__ = ['config', 'DBItemSchema', 'RedisItemSchema']

config_path = f"{root_path()}/pomelo/config/config.toml"


def pomelo_config():
    _config = toml.load(config_path)
    return ConfigSchema(**_config)


config: ConfigSchema = pomelo_config()
