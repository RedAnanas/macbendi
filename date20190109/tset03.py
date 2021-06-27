#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/9 16:24
# software: PyCharm
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").click()
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("周杰伦")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.find_element_by_link_text("周杰伦_百度百科").click()
time.sleep(7)
driver.find_element_by_link_text("范特西").click()
