#! /usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time


class Calculator:

    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.0.2',
            'deviceName': 'Android_5.0',
            'appPackage': 'com.android.calculator2',
            'appActivity': '.Calculator'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)
        time.sleep(5)

    def number(self, number):
        self.driver.find_element_by_id('digit_%d' % number).click()

    def operator(self, op):
        result = self.driver.find_element_by_accessibility_id(op).get_attribute('name')
        print(result)
        # id对应android属性的resource_id
        # self.driver.find_element_by_id('op_%s' % op).click()
        # accessibility_id对应android属性的content_desc
        self.driver.find_element_by_accessibility_id(op).click()
        # name对应android属性的text。注意一下，appium高版本的find_element_by_name执行会有问题
        # 但是我们可以使用find_element_by_android_uiautomator方法，参数使用text("value")来代替
        # 这里面需要强调的是value两边的引号必须使用双引号
        # self.driver.find_element_by_android_uiautomator('text("%s")' % op).click()

    def execute(self):
        self.driver.find_element_by_id('eq').click()
        return int(self.driver.find_element_by_id('formula').text)

    def assert_result(self, actual, expect):
        # if actual == expect:
        #     return True
        # else:
        #     return False
        return actual == expect

    def close(self):
        self.driver.quit()

    def start_calculate(self):
        self.number(8)
        self.operator('plus')
        self.number(9)
        result = self.execute()
        if self.assert_result(result, 17):
            print('test success.')
        else:
            print('test fail.')
        self.close()


if __name__ == '__main__':
    Calculator().start_calculate()
