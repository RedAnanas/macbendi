#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/28 21:01
# software: PyCharm
from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get('http://www.baidu.com/')
wd.maximize_window()
time.sleep(1)
wd.find_element_by_id("kw").click()
wd.find_element_by_id("kw").clear()
wd.find_element_by_id("kw").send_keys("刘德华")
wd.find_element_by_id("su").click()
time.sleep(3)
wd.find_element_by_link_text("刘德华_百度百科").click()
time.sleep(5)
wd.quit()
