#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.read_init import ReadIni


class GetByLocal:
    """
    根据配置文件的元素定位信息获取元素
    """
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_init = ReadIni()
        # id?com.android.dialer:id/floating_action_button
        if 'dialer' in key:
            local = read_init.get_value(key)
            if local:
                by, local_by = local.split('?')
                if by == 'id':
                    print(self.driver.find_element_by_id(local_by))
                    return self.driver.find_element_by_id(local_by)
                elif by =='className':
                    return self.driver.find_element_by_class_name(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            else:
                # 或者记录到日志
                return None
        else:
            local = read_init.get_value(key, section='message_element')
            if local:
                by, local_by = local.split('?')
                if by == 'id':
                    # print(self.driver.find_element_by_id(local_by))
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            else:
                # 或者记录到日志
                return None
