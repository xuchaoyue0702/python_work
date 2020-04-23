#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import functools


def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('calls %s' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s, %s' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log2('hahaha')
def now():
    print('2020-4-22')


if __name__ == '__main__':
    now()
    print(now.__name__)
