#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from appium import webdriver


class MessageDriver:
    """
    获取driver
    """
    def get_android_driver(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'OnePlus 7 Pro',
            'platformVersion': 9,
            'appPackage': 'com.android.mms',
            'appActivity': 'com.android.mms.ui.ConversationList',
            'noReset': True,
            # 'unicodeKeyboard': True,
            # 'resetKeyboard': True
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver
