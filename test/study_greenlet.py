#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/5/12

"""
greenlet实现协程的步骤
    1.导入模块
    2.创建任务
    3.创建greenlet对象
    4.手动switch任务
"""
import time
from greenlet import greenlet


def work1():
    while True:
        print('1111111111111111')
        time.sleep(1)
        print('work1')
        g2.switch()


def work2():
    while True:
        print('2222222222222222')
        time.sleep(2)
        print('work2')
        g1.switch()


if __name__ == '__main__':
    g1 = greenlet(work1)
    g2 = greenlet(work2)

    g1.switch()