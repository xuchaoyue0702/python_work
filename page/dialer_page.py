#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver


class DialerPage:
    """
    页面层：获取拨号页面所有元素
    """
    def __init__(self):
        self.driver = BaseDriver().get_android_driver()
        self.get_by_local = GetByLocal(self.driver)

    # 获取拨号按钮
    def get_dialer_button_element(self):
        dialer_button_element = self.get_by_local.get_element('dialer_button')
        return dialer_button_element

    # 获取号码文本框
    def get_dialer_text_element(self):
        dialer_text_element = self.get_by_local.get_element('dialer_text')
        return dialer_text_element

    # 获取1号键
    def get_dialer_one_element(self):
        dialer_one_element = self.get_by_local.get_element('dialer_one')
        return dialer_one_element

    # 获取快速拨号按钮
    def get_dialer_quick_element(self):
        dialer_quick_element = self.get_by_local.get_element('dialer_quick')
        return dialer_quick_element

    # 获取通讯录按钮
    def get_dialer_contact_element(self):
        dialer_contact_element = self.get_by_local.get_element('dialer_contact')
        return dialer_contact_element
