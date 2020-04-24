#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/23

"""
os模块：和操作系统有关的操作，创建、复制、移动文件和文件夹；文件路径和名称处理
"""

# windows中采用反斜杠\作为文件夹直接的分隔符，反斜杠在Python中用于转义，所以变成了两个反斜杠\\
import os
import glob
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

# os.walk(指定的绝对路径或相对路径)
for dirpath, dirname, files in os.walk('.\\'):
    print(dirpath)
    print(dirname)
    print(files)

# 字符串匹配开头和结尾
print('xuchao'.startswith('xu'))
print('xuchao'.endswith('ao'))

# 查询文件信息
print(os.stat('study_os.py'))

# 利用glob模块 *表示匹配任意字符，?表示匹配单个字符，[qwe]表示匹配qwe任意字符，[],recursive表示递归下去找
print(glob.glob('*.py', recursive=True))

# 时间戳转换
import time
import datetime

print(time.ctime(123456789))
print(datetime.datetime.fromtimestamp(123456789))

# 创建文件夹，已存在时会报错
os.mkdir('新的文件夹')

# 检查文件夹是否存在
os.path.exists('新的文件夹')

# 创建多层文件夹
os.makedirs('第一层\\第二层\\第三层')

# 复制文件
import shutil
shutil.copy('源文件', '新的文件夹')
shutil.copy('源文件', '文件夹\\新文件名')
# 复制文件夹，新的文件夹不能是已存在的
shutil.copytree('文件夹', '新的文件夹')

# 移动文件和文件夹，如果是文件夹，要加\\
shutil.move('源文件', '文件夹\\新的文件名')
shutil.move('源文件', '文件夹\\')
shutil.move('文件夹', '新的文件夹\\')

# 重命名文件和文件夹
os.rename('文件', '新的文件名')
os.rename('文件夹', '新的文件夹名')

# 删除文件，给文件夹会报错
os.remove('文件名')

# 删除文件夹
shutil.rmtree('文件夹')