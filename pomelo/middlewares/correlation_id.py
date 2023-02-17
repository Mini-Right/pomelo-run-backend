#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/24 07:12
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : request_var.py
# @Software    : PyCharm
# @Description :
import logging
from logging.config import dictConfig
from typing import Optional

from asgi_correlation_id import CorrelationIdFilter

logger = logging.getLogger(__name__)


def correlation_id_filter(uuid_length):
    class CorrelationIdFilterNew(CorrelationIdFilter):
        def __init__(self, name: str = '', uuid_length: Optional[int] = uuid_length):
            super().__init__(name=name, uuid_length=uuid_length)

    return CorrelationIdFilterNew


def configure_logging_dict() -> None:
    dictConfig(
        {
            'version': 1,
            'disable_existing_loggers': False,
            'filters': {
                'correlation_id': {'()': correlation_id_filter(uuid_length=32)},
            },
            'formatters': {
                'console': {
                    'class': 'logging.Formatter',
                    'datefmt': '%H:%M:%S',
                    'format': '%(levelname)s: \t  %(asctime)s %(name)s:%(lineno)d [%(correlation_id)s] %(message)s',
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'filters': ['correlation_id'],
                    'formatter': 'console',
                },
            },
            'loggers': {
                # project
                'app': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': True},
                # third-party packages
                'httpx': {'handlers': ['console'], 'level': 'INFO'},
                'databases': {'handlers': ['console'], 'level': 'WARNING'},
                'asgi_correlation_id': {'handlers': ['console'], 'level': 'WARNING'},
            },
        }
    )


def configure_logging_basic() -> None:
    cid_filter = CorrelationIdFilter(uuid_length=32)
    console_handler = logging.StreamHandler()
    console_handler.addFilter(cid_filter)
    logging.basicConfig(
        handlers=[console_handler],
        level=logging.DEBUG,
        format='%(levelname)s: \t  %(asctime)s %(name)s:%(lineno)d [%(correlation_id)s] %(message)s',
        filename=''
    )
