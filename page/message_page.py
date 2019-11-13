#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from base.message_driver import MessageDriver
from util.get_by_local import GetByLocal


class MessagePage:
    def __init__(self):
        self.driver = MessageDriver().get_android_driver()
        self.get_by_local = GetByLocal(self.driver)

    def get_new_mms_element(self):
        new_mms_element = self.get_by_local.get_element('message_button')
        return new_mms_element

