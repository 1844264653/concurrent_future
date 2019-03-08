#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 23:18
# @Author  : 海心
# @Site    : 
# @File    : basic2.py
# @Software: PyCharm
# @descri  : 如果在电脑下，可以自行选择使用 ThreadPoolExecutor 或者 ProcessPoolExecutor。


from concurrent_futures.unitity import hello
from concurrent.futures import ProcessPoolExecutor


def main():
    ''' basic concirrent via "submit"
    '''
    executor = ProcessPoolExecutor()
    kitty = executor.submit(
        hello, 2, 'Kitty')
    doggy = executor.submit(
        hello, 1, 'Doggy')
    print(kitty.result())
    print(doggy.result())
    executor.shutdown()


if __name__ == '__main__':
    main()


# Doggy sleep for 1 seconds
# Kitty sleep for 2 seconds
# 	--> hello Doggy, good morning
# 	--> hello Kitty, good morning
# return value: Kitty==>>3
# return value: Doggy==>>2