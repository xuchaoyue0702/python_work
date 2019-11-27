#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def get_driver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'A1601',
        'platformVersion': 5,
        'appPackage': 'com.oppo.launcher',
        'appActivity': 'com.oppo.launcher.Launcher',
        'noReset': True,
        'newCommandTimeout': 200,
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


def dialer_number(driver, number):
    try:
        ele = driver.find_elements_by_xpath('//*[@class="android.widget.TextView"]')[2]
    except Exception:
        print('找不到元素')
    if ele and ele.text == '10086':
        driver.find_elements_by_xpath
    else:
        pass


if __name__ == '__main__':
    driver = get_driver()
    driver.implicitly_wait(5)
    driver.start_activity('com.android.contacts', 'com.android.contacts.DialtactsActivityAlias')
    # ele = driver.find_elements_by_xpath('//*[@class="android.widget.TextView"]')[2]
    # print(ele.text)
    # driver.find_element_by_id('com.android.contacts:id/one_indonesian').click()
    # driver.find_element_by_id('com.android.contacts:id/zero_indonesian').click()
    # driver.find_element_by_id('com.android.contacts:id/zero_indonesian').click()
    # driver.find_element_by_id('com.android.contacts:id/eight_indonesian').click()
    # driver.find_element_by_id('com.android.contacts:id/six_indonesian').click()
    # driver.find_element_by_id('com.android.contacts:id/show_dialpad_btn').click()
    driver.find_element_by_id('com.android.contacts:id/primary_action_view').click()
    # wait = WebDriverWait(driver, 60, poll_frequency=15)
    # wait.until(lambda x: x.find_element_by_id('com.android.incallui:id/endButton')).click()
    time.sleep(10)
    driver.find_element_by_id('com.android.incallui:id/endButton').click()
    driver.quit()
