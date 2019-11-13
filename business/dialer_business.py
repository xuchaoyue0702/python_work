#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handle.dialer_handle import DialerHandle


class DialerBusiness:
    """
    业务层
    """
    def __init__(self):
        self.dialer_handle = DialerHandle()

    # 点击拨号按钮
    def click_dialer_button_pass(self):
        if self.dialer_handle.click_dialer_button():
            return True
        else:
            return False

    # 输入号码
    def send_keys_dialer_text_pass(self):
        self.dialer_handle.send_dialer_text(123456)

    # 点击1号键
    def click_dialer_one_pass(self):
        self.dialer_handle.click_dialer_one_button()

    # 点击快速拨号
    def click_dialer_quick(self):
        self.dialer_handle.click_dialer_quick()

    # 点击通讯录
    def click_dialer_contact(self):
        self.dialer_handle.click_dialer_contact()
