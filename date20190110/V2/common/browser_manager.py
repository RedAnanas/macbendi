#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 19:55
# software: PyCharm
from selenium import webdriver
import time

class BrowserManager:

    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://admin:8080/WoniuSales1.4/")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)

    def input_text(self,id,value):
        inputText=self.driver.find_element_by_id(id)
        inputText.clear()
        inputText.send_keys(value)

    def close(self):
        self.driver.quit()


