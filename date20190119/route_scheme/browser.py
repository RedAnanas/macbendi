#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 19:55
# software: PyCharm
from selenium import webdriver

class BrowserManager:

    def __init__(self,url):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(url=url)
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)

    def close(self):
        self.driver.quit()


