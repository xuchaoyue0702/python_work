#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/23

# f = open('xuchao.txt', 'r', encoding='utf-8')
# text = f.readlines()
# print(text)
# f.close()
# 'r'表示读取，'w'表示写入，若没有这个文件则会新建一个，若有这个文件则会被清空
# 'a'表示写入，若没有这个文件则会新建一个，若有这个文件则会在原有内容后面添加
# 'w+'表示写入及读取文件

with open('test.txt', 'w', encoding='utf-8') as f:
    text = '第一行内容\n第二行内容\n'
    f.write(text)
    f.write('第三行内容')
    # print(text)

# 创建临时文件存储数据
from tempfile import TemporaryFile
# f = TemporaryFile('w+')
# f.write('哈哈哈')
# f.seek(0)
# print(f.readlines())
# f.close()

with TemporaryFile('w+') as f:
    f.write('hahah')
    f.seek(0)
    print(f.readlines())


