#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/5/12

from gevent import monkey
monkey.patch_all()

import gevent
import time


def work1():
    for i in range(5):
        print('work1', i, gevent.getcurrent())
        # 默认情况下time.sleep()不能被识别为耗时操作，在不修改程序的源代码的情况下，为程序增加新的功能
        # 导入monkey模块 from gevent import monkey
        # 破解 monkey.patch_all() 然后就可以识别time.sleep()为耗时操作
        gevent.sleep(2)


def work2():
    for i in range(10):
        print('work2', i, gevent.getcurrent())
        # gevent.sleep(3)
        time.sleep(3)


if __name__ == '__main__':
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    g1.join()
    g2.join()
    # 批量join协程,接收一个列表
    # gevent.joinall([])
