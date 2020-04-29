#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/28

import time
from lxml import etree
import requests
import aiohttp
import asyncio

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
titles = []
sem = asyncio.Semaphore(10)  # 信号量，控制协程数

"""
提交请求获取页面，并解析html获取title
"""


# def get_title(url, number):
#     response = requests.get(url)  # 提交请求获取响应内容
#     html = response.content  # 获取网页内容(content获取的是bytes型数据，text获取的是unicode型数据)
#     title = etree.HTML(html).xpath('//*[@id="title"]/text()')  # xpath解析html
#     print('第%d个title:%s' % (number, title))
async def get_title(url):
    with(await sem):
        # async with是异步上下文管理器
        async with aiohttp.ClientSession() as session:
            async with session.request('GET', url) as resp:
                html = await resp.read()  # 可直接获取bytes
                title = etree.HTML(html).xpath('//*[@id="title"]/text()')
                print(''.join(title))

"""
调用方
"""
def main():
    loop = asyncio.get_event_loop()  # 获取事件循环
    tasks = [get_title(url) for url in urls]  # 把所有任务放到一个列表中
    loop.run_until_complete(asyncio.wait(tasks))  # 激活协程
    loop.close()


if __name__ == '__main__':
    # start1 = time.time()
    # i = 0
    # for url in urls:
    #     i = i+1
    #     start = time.time()
    #     get_title(url, i)
    #     print('第%d个title爬取耗时:%.5f秒' % (i, float(time.time() - start)))
    # print('爬取总耗时:%.5f秒' % float(time.time() - start1))
    start = time.time()
    main()
    print('总耗时：%.5f秒' % float(time.time() - start))