#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2021/6/27 上午2:25
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : root_path.py
# @Software    : PyCharm
# @Description : 获取跟路径

import os


def root_path():
    return os.path.dirname(os.path.abspath(__file__))
