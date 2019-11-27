#!/usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver


class BaseDriver:
    """
    获取driver
    """
    def get_android_driver(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'OnePlus 7 Pro',
            'platformVersion': 10,
            'appPackage': 'com.android.dialer',
            'appActivity': 'com.oneplus.contacts.activities.OPDialtactsActivity',
            'noReset': True,
            # 'unicodeKeyboard': True,
            # 'resetKeyboard': True
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver
