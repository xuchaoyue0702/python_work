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


@pytest.fixture()
def init_test():
    print('测试之前')


class TestCase:
    def test_1(self, init_test):
        print('111')
        assert True

    def test_2(self):
        print('222')
        assert True

    @staticmethod
    def test_3():
        print('hhh')


if __name__ == '__main__':
    TestCase.test_3()





