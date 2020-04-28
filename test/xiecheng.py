#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/4/24

from gevent import monkey; monkey.patch_all()
import gevent
import requests


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://cn.bing.com/'),
        gevent.spawn(f, 'https://www.bilibili.com/'),
])
