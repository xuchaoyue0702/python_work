#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/28

from multiprocessing import Pool
import time
import aiohttp
import asyncio
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

htmls = []
titles = []
sem = asyncio.Semaphore(10)


async def get_html(url):
    with(await sem):
        async with aiohttp.ClientSession() as session:
            async with session.request('GET', url) as resp:
                html = await resp.read()
                htmls.append(html)
                print('异步获取%s下的页面' % url)


"""
协程调用方，请求网页
"""
def main_get_html():
    loop = asyncio.get_event_loop()  # 获取事件循环
    tasks = [get_html(url) for url in urls]  # 所有任务放入列表
    loop.run_until_complete(asyncio.wait(tasks))  # 激活协程
    loop.close()


"""
使用多进程解构html
"""
def multi_parse_html(html, cnt):
        title = etree.HTML(html).xpath('//*[@id="title"]/text()')
        titles.append(''.join(title))
        print('第%d个html完成解析－title:%s' % (cnt,''.join(title)))


"""
多进程调用总函数
"""
def main_parse_html():
    p = Pool(4)
    i = 0
    for html in htmls:
        i += 1
        p.apply_async(multi_parse_html, args=(html, i))
    p.close()
    p.join()


if __name__ == '__main__':
    start = time.time()
    main_get_html()
    main_parse_html()
    print('总耗时：%.5f秒' % float(time.time()-start))