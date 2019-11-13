#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.message_page import MessagePage


class MessageHandle:
    def __init__(self):
        self.message_page = MessagePage()

    def click_new_mms(self):
        self.message_page.get_new_mms_element().click()
