#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser


class ReadIni:
    """
    读取配置文件，返回元素的定位信息
    """
    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = '../config/Elements.ini'
        self.data = self.read_ini()

    def read_ini(self):
        read_init = configparser.ConfigParser()
        read_init.read(self.file_path, encoding='utf-8')
        return read_init

    def get_value(self, key, section=None):
        """
        通过key获取对应的value
        :return:
        """
        if section == None:
            section = 'dialer_element'
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value('dialer_button', 'dialer_element'))
