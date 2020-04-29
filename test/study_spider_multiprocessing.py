#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/28

import multiprocessing
from multiprocessing import Pool
import time
import requests
from lxml import etree

urls = [
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16488',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16583',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16380',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16911',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16581',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16674',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16112',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/17343',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16659',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16449',
]


def get_title(url, number):
    response = requests.get(url)  # 提交请求获取响应内容
    html = response.content  # 获取网页内容(content获取的是bytes型数据，text获取的是unicode型数据)
    title = etree.HTML(html).xpath('//*[@id="title"]/text()')  # xpath解析html
    print('第%d个title:%s' % (number, title))


def main():
    print('当前环境CPU核数：%d' % multiprocessing.cpu_count())
    p = Pool(4)
    i = 0
    for url in urls:
        i += 1
        p.apply_async(get_title, args=(url, i))
    p.close()
    p.join()


if __name__ == '__main__':
    start = time.time()
    main()
    print(start)