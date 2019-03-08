#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 22:56
# @Author  : 海心
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
# @descri  : 并发-开篇


"""
python 3.2 的时候推出了一个新的高级并发模块，叫做 concurrent.futures 这个模块在保持了进程以及线程统一的界面。

concurrent.futures的灵感来自于java的util.concurrent，在python中，concurrent.futures提供两个Executor，

一个是ThreadPoolExecutor(线程)一个是ProcessPoolExecutor（进程）两个类拥有统一的界面。submit，map 以及shutdown。

!!!两个类都支持context management，也就是说可以使用 with 的语法来做。

这个模块的设计目标就是通过提供高级的接口来简化常用的线程跟进程管理。

从进程(线程)池的创建管理，提交线程任务，管理列队回收结果，处理超时回调函数等等。

看到很多人仍然是使用threading模块做线程，multiprocessing来做进程，而实际代码所用到的需求concurrent.futures是足够满足的。

虽然一些复杂的东西还是需要用到底层threading/multiprocessing模块才能处理，但是很多时候代码并不需要使用过于复杂的东西。

也许是因为concurrent.futures比较新，很多人没有喜欢这个模块的信心？

又有可能这个模块介绍的不多，所以不为人知。从出现的时间来说，concurrent.futures自从2011年2月就出现在python3.2的正式发行版中了，

使用难度来说，比threading 或 multiprocessing 简单的多。

首先说下背景。因为我是在手机写的例子，我用的 python 在手机中不支持多进程，

所以例子都是以 ThreadPoolExecutor 来完成。
如果在电脑下，可以自行选择使用 ThreadPoolExecutor 或者 ProcessPoolExecutor。
两个类的界面以及用法是 100% 相同的。两个的最大区别（除了线程跟进程的区别以外）就是在初始化的时候默认参数 max_workers 的不同。
使用进程，缺省默认情况下，进程数控是 CPU 核的数量。而线程则是 CPU 核的数量乘以5。
常见的用法是在进程池下再做线程池（反过来的比较少见）达到多进程多线程的设计。
以我笔记本为例，全部使用缺省默认参数下，开进程池然后每个进程池下面开线程池。
我是8核的 CPU，就是开8个进程。每个进程开线程池（5 x 8 = 40 个线程)，一共就是320个线程分散在8个核上 （40 x 8）
为例简单，所有 concurrent.futures 的代码都会共用一个叫做 hello 的函数。
这个函数很简单。可以接受3个参数，
第一个是决定延迟的时间（time.sleep),
第二个参数接受一个名字。
第三个如果参数是 True，
则会在 hello 内 raise 一个 exception。
（后面演示 exception 逻辑的时候使用）hello 写在 basic1.py 中。
basic1.py 里面还有个 time_me 的装饰器，可以忽略。
那个只是拿来计算一下函数运行时间而已。


Executor中定义了submit()方法，这个方法的作用是提交一个可执行的回调task，并返回一个future实例。future对象代表的就是给定的调用。

"""