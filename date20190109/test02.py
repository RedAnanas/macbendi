#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/9 15:12
# software: PyCharm
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://admin:8080/WoniuSales1.4/")
driver.find_element_by_xpath("//input[@id='username']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='password']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='verifycode']").send_keys("0000")
# driver.find_element_by_xpath("//button[@class='form-control.btn-primary'and@type='button']").click()

