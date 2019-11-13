#!/usr/bin/env python
# -*- coding:utf-8 -*-

from page.dialer_page import DialerPage


class DialerHandle:
    """
    操作层：操作拨号界面
    """
    def __init__(self):
        self.dialer_page = DialerPage()

    # 点击拨号按钮
    def click_dialer_button(self):
        self.dialer_page.get_dialer_button_element().click()

    # 号码文本框输入号码
    def send_dialer_text(self, number):
        self.dialer_page.get_dialer_text_element().send_keys(number)

    # 点击1号键
    def click_dialer_one_button(self):
        self.dialer_page.get_dialer_one_element().click()

    # 点击快速拨号
    def click_dialer_quick(self):
        self.dialer_page.get_dialer_quick_element().click()

    # 点击通讯录
    def click_dialer_contact(self):
        self.dialer_page.get_dialer_contact_element().click()

