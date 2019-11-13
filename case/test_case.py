#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import unittest
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

class CaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dialer_business = DialerBusiness()

    def setUp(self) -> None: ...

    def test_1(self) -> bool:
        self.dialer_business.click_dialer_button_pass()

    @unittest.skip('CaseTest')
    def test_2(self):
        print('this is 2')

    def tearDown(self): ...

    @classmethod
    def tearDownClass(cls): ...


if __name__ == '__main__':
    # unittest.main()
    # 生成一个罐子放入case
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_1'))
    unittest.TextTestRunner().run(suite)



