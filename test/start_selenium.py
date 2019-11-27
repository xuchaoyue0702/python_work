#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('../tools/chromedriver.exe')
driver.get('http://www.baidu.com')
print(EC.title_contains('百度'))
search_element = driver.find_element_by_xpath('//*[@id="kw"]')
# locator = (By.ID, 'kw')
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
search_content = random.sample('1234567890abcdefg', 5)
search_element.send_keys(search_content)
time.sleep(5)
driver.quit()


class A:

    _singleton = None

    def __init__(self):
        print("__init__ ")
        super(A, self).__init__()
        return None

    def __new__(cls, *args, **kwargs):
        print('__new__')
        if not cls._singleton:
            cls._singleton = object.__new__(cls, *args, **kwargs)
        return cls._singleton

    def __call__(self):  # 可以定义任意参数
        print('__call__ ')


