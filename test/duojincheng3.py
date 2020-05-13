#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/24

import multiprocessing
from multiprocessing import Process, Pool
import time


def copy_txt():
    print("开始拷贝------", multiprocessing.current_process())
    time.sleep(2)


if __name__ == '__main__':
    pool = Pool(5)
    for i in range(100):
        pool.apply_async(copy_txt)
    pool.close()
    pool.join()