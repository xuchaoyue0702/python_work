#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/24

# 解压序列赋值给多个变量,任何的序列或者是可迭代对象可以通过一个简单的赋值语句解压并赋值给多个变量
from audioop import avg

p = (4, 5)
x, y = p
print(x, y)

data = [2, 145, 'xuchao', (2020, 4, 24)]
_, _, name, date = data
print(name, date)

s = 'asdfg'
a, b, c, d, e = s
print(a, b, c, d, e)

# 如果一个可迭代对象的元素个数超过变量个数时，会抛出valueError，如何从这个可迭代对象中解压出N个元素出来,使用*号
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


records = [
    ('foo', 1, 2),
    ('bar', 'xuchao'),
    ('foo', 3, 5)
]

def foo(x, y):
    print('foo', x, y)

def bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        foo(*args)
    elif tag == 'bar':
        bar(*args)
