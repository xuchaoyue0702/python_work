#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/23

import zipfile
# 读取压缩包内文件
with zipfile.ZipFile('xxx.zip', 'r') as zipobj:
    print(zipobj.namelist())
    print(zipobj.getinfo())

# 将压缩包内单个文件解压出来
with zipfile.ZipFile('aaa.zip', 'r') as zipobj:
    zipobj.extract('xxx.txt', '解压到的位置')
    # 解压所有
    zipobj.extractall('位置', pwd=b'aaaaaa')

# 创建压缩包
file_list = ['test.py', '../page/dialer_page.py']
with zipfile.ZipFile('sss.zip', 'w') as zipobj:
    for file in file_list:
        zipobj.write(file)

# 向压缩包添加文件
with zipfile.ZipFile('sss.vip', 'a') as zipobj:
    zipobj.write('asd.txt')