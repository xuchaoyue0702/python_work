#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/24

import threading
import time

semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
num = 0


def run(n):
    semaphore.acquire()   #加锁
    time.sleep(1)
    print("run the thread:%s\n" % n)
    semaphore.release()     #释放


for i in range(22):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()

while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('-----all threads done-----')