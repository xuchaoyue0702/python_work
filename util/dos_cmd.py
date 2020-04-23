#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os


class DosCmd:
    """
    执行cmd命令
    """
    def get_device_name(self):
        # 获取设备信息
        device_list = []
        result = os.popen('adb devices').readlines()[1:-1]
        # print(result)
        if len(result) >= 1:
            for device in result:
                device_info = device.split('\t')
                if 'device' in device:
                    device_list.append(device_info[0])
            return device_list
        else:
            print('no device')


if __name__ == '__main__':
    print(DosCmd().get_device_name())
