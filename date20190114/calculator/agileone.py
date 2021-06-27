#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/14 20:44
# software: PyCharm
from appium import webdriver
import time

class Agileone:
    def __init__(self):
        desired_caps={
            "platformVersion": "8.0.0",
            "appActivity": ".BrowserActivity",
            "appPackage": "com.android.browser",
            "deviceName": "854430ab",
            "platformName": "Android"
            # "unicodeKeyboard": "True",
            # "noReset": "False"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(20)
        self.driver.get("http://www.hao123.com")
if __name__ == '__main__':
    Agileone()
