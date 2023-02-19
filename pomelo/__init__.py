#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/17 23:27
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :

import logging
import time

from fastapi import FastAPI, Request, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from pomelo.apps import api
from pomelo.databases.pomelo_system_api_record_table import PomeloSystemAPIRecordTable
from pomelo.middlewares import middlewares
from pomelo.middlewares.correlation_id import configure_logging_basic
from pomelo.plugins.crypt.token import get_token_user_id
from pomelo.plugins.curd import PomeloTableCURD
from root_path import root_path

logger = logging.getLogger(__name__)

pomelo = FastAPI(
    title='Pomelo Run',
    version='0.0.1',
    on_startup=[configure_logging_basic],
    docs_url=None,
    redoc_url=None,
)

pomelo.mount(path='/static', app=StaticFiles(directory=f"{root_path()}/pomelo/static"), name='static')

pomelo.include_router(router=api, prefix='/api', dependencies=[Depends(get_token_user_id)])


@pomelo.get("/api/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=pomelo.openapi_url,
        title="Pomelo Run",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url='/static/favicon.jpeg',
    )


middlewares(pomelo)


@pomelo.middleware('http')
async def process_timer(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    path = request.url.path
    status_code = response.status_code
    PomeloTableCURD().add_one(table_class=PomeloSystemAPIRecordTable(path=path, status_code=status_code))
    return response
