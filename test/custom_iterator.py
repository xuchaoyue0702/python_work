#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: ccyy
# @Date: 2020/5/11


class MyList(object):
    """
    可迭代对象
    """
    def __init__(self):
        self.my_list = []

    def __iter__(self):
        mylist_iterator = MyListIterator(self.my_list)
        return mylist_iterator

    def addItem(self, mylist_item):
        self.my_list.append(mylist_item)


class MyListIterator(object):
    """
    迭代器
    """
    def __init__(self, items):
        self.items = items
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.items):
            data = self.items[self.current_index]
            self.current_index += 1
            return data
        else:
            raise StopIteration


if __name__ == '__main__':

    mylists = MyList()
    mylists.addItem('许超')
    mylists.addItem('杨超越')
    mylists.addItem('超超越越')
    mylists.addItem('超超越越哈')

    for item in mylists:
        print(item)