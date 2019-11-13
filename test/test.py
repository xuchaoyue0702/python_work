#!/usr/bin/env python
# -*- coding:utf-8 -*-


from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
            'platformName': 'Android',
            'deviceName': 'OnePlus 7 Pro',
            'platformVersion': 9,
            'appPackage': 'com.android.dialer',
            'appActivity': 'com.oneplus.contacts.activities.OPDialtactsActivity',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# for number in range(1, 101):
#         if number/10 < 1:
#                 driver.find_element_by_id('com.oneplus.calculator:id/digit_%d' % number).click()
#                 driver.find_element_by_id('com.oneplus.calculator:id/op_add').click()
#         elif number/10 >= 1 and number/100 < 1:
#                 driver.find_element_by_id('com.oneplus.calculator:id/digit_%d' % (number//10)).click()
#                 driver.find_element_by_id('com.oneplus.calculator:id/digit_%d' % (number%10)).click()
#                 driver.find_element_by_id('com.oneplus.calculator:id/op_add').click()
#         else:
#                 driver.find_element_by_id('com.oneplus.calculator:id/digit_%d' % (number//100)).click()
#                 driver.find_element_by_id('com.oneplus.calculator:id/digit_%d' % (number//10%10)).click()
#                 driver.find_element_by_id('com.oneplus.calculator:id/digit_%d' % (number%10)).click()
#
# driver.find_element_by_id('com.oneplus.calculator:id/eq').click()

# texts = driver.find_elements_by_class_name('android.widget.TextView')
# for text in texts:
#         print(text.text)

# 通过xpath获取所有包含“设”字的控件
# texts = driver.find_elements_by_xpath('//*[contains(@text,"设")]')
# for text in texts:
#         print(text.text)

# wait = WebDriverWait(driver, 5)
# back_button = wait.until(lambda x: x.find_element_by_xpath('//*[contains(@text,"设")]'))
# back_button.click()

# driver.implicitly_wait(10)
# texts = driver.find_elements_by_xpath('//*[contains(@text,"设")]')
# for text in texts:
#         print(text.text)

# qq = driver.find_element_by_accessibility_id('QQ')
# print(qq.get_attribute('text'))
# print(qq.get_attribute('className'))
# print(qq.get_attribute('resourceId'))

# driver.swipe(100, 2300, 100, 200, duration=5000)
# time.sleep(5)
# start_el = driver.find_element_by_xpath('//*[@text="电池"]')
# end_el = driver.find_element_by_xpath('//*[@text="显示"]')
# driver.drag_and_drop(start_el, end_el)
# time.sleep(5)

# el = driver.find_element_by_xpath("//*[@text='显示']")
# TouchAction(driver)\
#         .long_press(el, duration=2000)\
#         .perform()

# driver.set_network_connection(1)

# driver.find_element_by_id('com.android.dialer:id/floating_action_button').click()
driver.find_element_by_id('com.android.dialer:id/one').click()


driver.quit()
