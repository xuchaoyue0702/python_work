#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import time
import hashlib
from serial import Serial
import serial.tools.list_ports


def findPort():
    ports = serial.tools.list_ports.comports()
    for each in ports:
        if 'Android' in each:
            com_android = each.split(' - ')[0]
            return com_android


def sendAT(port, bsn):
    try:
        serial = Serial(port=port, baudrate=9600, timeout=1)
        at_bsn = 'AT*****={}'.format(bsn)  # 具体命令就不给出了，各位看官根据需要看。
        sha256 = hashlib.sha256()  # 用到了哈希函数。
        sha256.update(bsn.encode('utf-8'))
        hash = 'AT******={}'.format(sha256.hexdigest())

        serial.write(at_bsn.encode('utf-8') + b'\r\n')  # 向端口发送指令必须二进制格式；末尾添加\r\n表示发送。
        serial.write(b'AT******\r\n')
        serial.write(b'AT******\r\n')
        serial.write(hash.encode('utf-8') + b'\r\n')
        print('SUCCESS!')
    except Exception as e:
        print(e)
    finally:
        serial.close()  # 最后不要忘记把占用的端口关掉。


if __name__ == '__main__':
    port = findPort()
    if 'COM' in port:
        _bsn = input('Please input your BSN number: ')
        sendAT(port=port, bsn=_bsn)
    else:
        print("Can't find the port!")
        time.sleep(2)  # CMD终端运行时，打印语句一闪而过，需要设置等待。
