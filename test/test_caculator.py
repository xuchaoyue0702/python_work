#!/usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
import pytest

# desired_caps = {
#         'platformName': 'Android',
#         'deviceName': 'OnePlus 7 Pro',
#         'platformVersion': 9,
#         'appPackage': 'com.android.settings',
#         'appActivity': 'com.android.settings.Settings',
#         'noReset': True,
#         'unicodeKeyboard': True,
#         'resetKeyboard': True
#     }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def func(x):
    return x+1


def test_func():
    assert func(3) == 5

