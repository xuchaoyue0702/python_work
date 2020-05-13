#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/5/11


class Fib(object):

    def __init__(self, num):
        self.num = num
        self.a = 1
        self.b = 1
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.num:
            data = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_index += 1
            return data
        else:
            raise StopIteration


if __name__ == '__main__':
    fib_iterator = Fib(5)
    for item in fib_iterator:
        print(item)
