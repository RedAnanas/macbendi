#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/9 18:52
# software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
#键盘事件
from selenium.webdriver.common.keys import Keys

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

# driver.find_element_by_xpath("//form[@class='form-inline']/div[6]/button").click()
driver.find_element_by_xpath("//button[@class='form-control btn-primary']").click()

time.sleep(1)
#查询
driver.find_element_by_link_text("会员管理").click()
driver.find_element_by_xpath("//input[@id='customerphone']").send_keys("18682558655")
driver.find_element_by_xpath("//form[@class='form-inline']/div[2]/button[3]").click()
time.sleep(2)
#新增
driver.find_element_by_xpath("//input[@id='customerphone']").clear()
driver.find_element_by_xpath("//input[@id='customerphone']").send_keys("12213413234")
driver.find_element_by_id("customername").clear()
driver.find_element_by_id("customername").send_keys("李明明")
# driver.find_element_by_id("form-control")

combox = Select(driver.find_element_by_id("childsex"))
combox.select_by_visible_text("女")

driver.execute_script("document.getElementById('childdate').readOnly=false;")
driver.find_element_by_id("childdate").clear()
driver.find_element_by_id("childdate").send_keys("1995-09-13")
driver.find_element_by_id("childdate").send_keys(Keys.ENTER)

driver.find_element_by_xpath("//form[@class='form-inline']/div[2]/button[1]").click()

driver.find_element_by_link_text("注销").click()
time.sleep(2)
driver.quit()


