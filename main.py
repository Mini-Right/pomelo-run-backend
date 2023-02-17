#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/2/18 00:22
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : main.py
# @Software    : PyCharm
# @Description :
import uvicorn
from pomelo import pomelo


if __name__ == "__main__":
    uvicorn.run(
        'pomelo.__init__:pomelo',
        host="0.0.0.0",
        port=5004,
        workers=1
    )
