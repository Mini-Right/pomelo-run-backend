#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/25 02:04
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description : 
from redis.client import Redis

from pomelo.config import config
from pomelo.plugins.session.mysql_session import init_session as init_mysql_session
from pomelo.plugins.session.redis_session import init_session as init_redis_session

__all__ = ['MySQLSession', 'RedisSession']


class MySQLSession(object):
    pomelo = init_mysql_session(config.DB.POMELO)


class RedisSession(object):
    pomelo: Redis = init_redis_session(config.REDIS.POMELO)
