#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/9 20:20
# software: PyCharm
from selenium import webdriver
import time
import uiautomation

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://admin:8080/WoniuSales1.4/")
driver.implicitly_wait(30)
time.sleep(1)

username=driver.find_element_by_id("username")
username.clear()
username.send_keys("admin")

password=driver.find_element_by_id("password")
password.clear()
password.send_keys("admin")

driver.find_element_by_id("verifycode").send_keys("0000")

driver.find_element_by_xpath("//form[@class='form-inline']/div[6]/button").click()

time.sleep(1)

driver.find_element_by_link_text("批次管理").click()
time.sleep(1)


driver.find_element_by_id("batchfile").send_keys("D:\\Python\\date20190109\\GB20190109.xls")

# driver.find_element_by_id("batchfile").click()
# time.sleep(2)
# uiautomation.EditControl(AutomationId="1148").SendKeys("D:\\Python\\date20190109\\GB20190109.xls")
# uiautomation.Win32API.SendKey(uiautomation.Keys.VK_ENTER)
time.sleep(1)
driver.find_element_by_xpath("//div[@class='row']/form[2]/div/input[1]").click()



