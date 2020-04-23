#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/23

"""
os模块：和操作系统有关的操作，创建、复制、移动文件和文件夹；文件路径和名称处理
"""

# windows中采用反斜杠\作为文件夹直接的分隔符，反斜杠在Python中用于转义，所以变成了两个反斜杠\\
import os
print(os.getcwd())

# 处理路径连接
print(os.path.join('Test', 'xxx'))

# 列出当前文件夹下所有的文件和文件夹,os.listdir(指定的绝对路径或相对路径)
print(os.listdir('D:\\app'))

# 判断是否是文件夹
print(os.path.isdir('D:\\app'))

# os.scandir()返回一个迭代器
for file in os.scandir('D:\\app'):
    print(file.name, file.path, file.is_dir())

