#!/usr/bin/env python
# -*- coding:utf-8 -*-

from random import randint
from threading import Thread
from time import time, sleep


# def download(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
#     t1.start()
#     t2 = Thread(target=download, args=('Peking Hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.3f秒' % (end - start))
#
#
# if __name__ == '__main__':
#     main()


# class DownLoadTask(Thread):
#
#     def __init__(self, filename):
#         super().__init__()
#         self.filename = filename
#
#     def run(self):
#         print('开始下载%s...' % self.filename)
#         time_to_download = randint(5, 10)
#         sleep(time_to_download)
#         print('%s下载完成! 耗费了%d秒' % (self.filename, time_to_download))
#
#
# def main():
#     start = time()
#     t1 = DownLoadTask('头发从茂密到秃顶')
#     t2 = DownLoadTask('我学不下去了')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共花费%d秒' % (end-start))


# if __name__ == '__main__':
#     main()


# from time import sleep
# from threading import Thread, Lock
#
#
# class Account(object):
#
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()
#
#     def deposit(self, money):
#         # 先获取锁才能执行后面的代码
#         self._lock.acquire()
#         try:
#             # # 计算存款后的余额
#             # new_balance = self._balance + money
#             # # 模拟受理存款业务需要0.01秒的时间
#             # sleep(0.01)
#             # # 修改账户余额
#             # self._balance = new_balance
#             self._balance += money
#         finally:
#             self._lock.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
#
# class AddMoneyThread(Thread):
#
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def run(self):
#         self._account.deposit(self._money)
#
#
# def main():
#     account = Account()
#     threads = []
#     # 创建100个存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     # 等所有存款的线程都执行完毕
#     for t in threads:
#         t.join()
#     print('账户余额为: ￥%d元' % account.balance)
#
#
# if __name__ == '__main__':
#     main()


from threading import Thread, Lock


class Account:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def add_money(self, money):
        self.lock.acquire()
        try:
            self.balance += money
        finally:
            self.lock.release()


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self.account = account
        self.money = money

    def run(self):
        self.account.add_money(self.money)


def main():
    account = Account()
    thread = []

    for _ in range(100):
        t = AddMoneyThread(account, 1)
        thread.append(t)
        t.start()
    for i in thread:
        i.join()
    print(account.balance)


if __name__ == '__main__':
    main()























