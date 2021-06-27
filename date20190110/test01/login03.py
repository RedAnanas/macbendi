#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 11:36
# software: PyCharm
from selenium import webdriver
import time
#上传文件

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
driver.find_element_by_link_text("批次管理").click()
logout=driver.find_element_by_link_text("查看清单图例").text
# print(logout)

if "查看清单" in logout:
    print("case3 成功")
else:
    print("case3 失败")

driver.quit()
