#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import unittest
import pytest
from business.dialer_business import DialerBusiness
from business.message_business import MessageBusiness


# def get_driver():
#     desired_caps = {
#         'platformName': 'Android',
#         'deviceName': 'OnePlus 7 Pro',
#         'platformVersion': 9,
#         'appPackage': 'com.android.dialer',
#         'appActivity': 'com.oneplus.contacts.activities.OPDialtactsActivity',
#         'noReset': True,
#         'unicodeKeyboard': True,
#         'resetKeyboard': True
#     }
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#     return driver
#
#
# driver = get_driver()
# dialer_business = DialerBusiness(driver)
# # dialer_business.click_dialer_button_pass()
# driver.set_network_connection(4)
# driver.quit()
# dialer_business = DialerBusiness()
# dialer_business.click_dialer_button_pass()
# dialer_business.send_keys_dialer_text_pass()
#
# message_business = MessageBusiness()
# message_business.click_new_mms()
#
# DialerBusiness().click_dialer_button_pass()
class TestCase:

    def setup_class(self):
        print('测试前')
        self.dialer_business = DialerBusiness()
        # cls.driver = cls.dialer_business.dialer_handle.dialer_page.driver

    def test_1(self):
        print('测试开始')
        self.dialer_business.click_dialer_button_pass()


if __name__ == '__main__':
    TestCase().test_1()



