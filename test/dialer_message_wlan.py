#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
需求：卡1卡2分别做副卡拨打电话20通并统计呼通率
"""
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def get_driver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'OnePlus 7 Pro',
        'platformVersion': 10,
        'appPackage': 'com.android.dialer',
        'appActivity': 'com.oneplus.contacts.activities.OPDialtactsActivity',
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'newCommandTimeout': 200
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


# 拨打电话
def dialer_number(driver, number):
    # driver.find_element_by_accessibility_id('电话').click()
    driver.find_element_by_accessibility_id('拨号键盘').click()
    driver.find_element_by_id('com.android.dialer:id/digits').send_keys(number)
    TouchAction(driver).tap(element=None, x=713, y=2712).perform()
    time.sleep(30)
    driver.find_element_by_id('com.android.dialer:id/floating_end_call_action_button').click()


# 发送短信
def send_mms(driver, number, message):
    driver.start_activity('com.android.mms', 'com.android.mms.ui.ConversationList')
    driver.find_element_by_id('com.android.mms:id/start_new_conversation_button').click()
    driver.find_element_by_id('com.android.mms:id/recipient_text_view').send_keys(number)
    driver.press_keycode(66)
    driver.find_element_by_id('com.android.mms:id/compose_message_text').send_keys(message)
    driver.find_element_by_id('com.android.mms:id/send_message_button').click()


# 开关WiFi
def open_or_close_wlan(driver, password):
    # driver.start_activity('com.android.settings', 'com.android.settings.Settings')
    driver.find_element_by_xpath('//*[contains(@text,"WLAN 和互联网")]').click()
    wlan_switch_element = driver.find_element_by_id('com.android.settings:id/switchWidget')
    wlan_switch_status = True if wlan_switch_element.get_attribute('checked') == 'true' else False
    if wlan_switch_status:
        driver.find_element_by_xpath('//*[@text="WLAN"]').click()
    else:
        wlan_switch_element.click()
        driver.find_element_by_xpath('//*[@text="WLAN"]').click()
    driver.find_element_by_xpath('//*[contains(@text,"NETGEAR10-8")]').click()
    driver.find_element_by_id('com.android.settings:id/password').send_keys(password)
    driver.find_element_by_id('android:id/button1').click()


def set_sim(driver):
    driver.start_activity('com.android.settings', 'com.android.settings.Settings')
    driver.find_element_by_xpath('//*[contains(@text,"WLAN 和互联网")]').click()


if __name__ == '__main__':
    driver = get_driver()
    driver.implicitly_wait(5)
    dialer_number(driver, 10001)
    time.sleep(5)
    set_sim(driver)
    driver.quit()


