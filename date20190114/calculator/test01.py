#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/14 11:19
# software: PyCharm
from appium import webdriver
import time

class Calculator:

    def __init__(self):
        desired_caps={
            "appPackage": "com.android.calculator2",
            "appActivity": "Calculator",
            "deviceName": "Android_5.0.2",
            "platformName": "Android"
        }
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(20)
        time.sleep(3)

    def number(self,number):
        self.driver.find_element_by_id("digit_%d"%number).click()

    def operator(self,oper):
        self.driver.find_element_by_id("op_%s"%oper).click()

    def execute(self,expect):
        self.driver.find_element_by_id("eq").click()
        result=int(self.driver.find_element_by_id("formula").text)
        return result==expect

    def start(self):
        self.number(6)
        self.operator("add")
        self.number(7)
        result=self.execute(13)
        if result:
            print("测试成功")
        else:
            print("测试失败")

if __name__ == '__main__':
    Calculator().start()