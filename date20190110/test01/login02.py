#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 11:36
# software: PyCharm
from selenium import webdriver
import time
# 密码错误

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
password.send_keys("111111")

driver.find_element_by_id("verifycode").send_keys("0000")

driver.find_element_by_xpath("//form[@class='form-inline']/div[6]/button").click()
time.sleep(2)
logout=driver.find_element_by_class_name("bootbox-body").text


if "登录失败，请重新登录." in logout:
    print("case2 成功")
else:
    print("case2 失败")

driver.quit()
