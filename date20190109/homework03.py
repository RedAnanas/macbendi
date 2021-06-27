#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/9 21:11
from selenium import webdriver
import time
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
#查询
driver.find_element_by_link_text("销售出库").click()
driver.find_element_by_id("barcode").send_keys("22222222")

driver.find_element_by_xpath("//div[@class='container']/div[1]/div/div[1]/form/button").click()
driver.find_element_by_id("customerphone").send_keys("18682558655")
driver.find_element_by_xpath("//*[@id='vipsell']/div[1]/form/div[2]/button").click()
driver.find_element_by_id("submit").click()
driver.switch_to.alert.accept()

