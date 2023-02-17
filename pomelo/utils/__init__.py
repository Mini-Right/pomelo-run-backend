#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/1/29 12:33
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
def arr_size(arr: list, size: int = 10):
    """
    长数组切分短数组
    :param arr:     数组对象
    :param size:    短数组长度
    :return:
    """
    s = []
    for i in range(0, int(len(arr)) + 1, size):
        c = arr[i:i + size]
        s.append(c)
    new_list = [x for x in s if x]
    return new_list
