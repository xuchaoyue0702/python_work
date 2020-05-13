#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/5/11


def generator_add():
    sum_add = 0
    while True:
        num = yield sum_add
        sum_add = sum_add + num
        print(sum_add)


gener_add = generator_add()
next(gener_add)
gener_add.send(10)
gener_add.send(20)
gener_add.send(30)