#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from handle.message_handle import MessageHandle


class MessageBusiness:
    def __init__(self):
        self.message_handle = MessageHandle()

    def click_new_mms(self):
        self.message_handle.click_new_mms()
