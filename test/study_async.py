#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/28

import aiohttp
import time
import asyncio

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://httpbin.org/get') as resp:
#             print(resp.status)
#             print(await resp.text())
#
# main()


url = 'http://docs.aiohttp.org/en/stable/client_quickstart.html'


async def getPage(session, url):
    async with session.get(url, timeout=5) as resp:
        print(await resp.text())


async def main():
    async with aiohttp.ClientSession() as session:
        await getPage(session, url)


start = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(url))

end = time.time()

print(end - start)
