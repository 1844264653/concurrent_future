#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 23:20
# @Author  : 海心
# @Site    : 
# @File    : unitity.py
# @Software: PyCharm
# @descri

import time
from random import random


def hello(delay, name, raise_exception=False):
    ''' simple hellow function'''
    time.sleep(random() / 10)
    print(f'{name} sleep for {delay} seconds')
    time.sleep(delay)
    if raise_exception:
        raise ValueError(f'{name} not happy')
    print(f'\t--> hello {name}, good morning')
    return f'return value: {name}==>>{delay+1}'
