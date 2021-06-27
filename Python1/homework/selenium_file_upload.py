#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import uiautomation


driver = webdriver.Firefox(firefox_binary='D:/Mozilla Firefox/firefox.exe',
                           executable_path='./driver/geckodriver.exe')
driver.get('http://jacky-vpc/agileone')
driver.set_page_load_timeout(30)
driver.implicitly_wait(30)
time.sleep(2)
username = driver.find_element_by_id('username')
username.clear()
username.send_keys('admin')
password = driver.find_element_by_id('password')
password.clear()
password.send_keys('admin')
driver.find_element_by_id('login').click()
driver.find_element_by_partial_link_text('缺陷跟踪').click()
driver.find_element_by_xpath('//tbody[@id="dataPanel"]/tr[1]/td[1]/label').click()
time.sleep(2)
driver.find_element_by_id('showAttach').click()
# driver.find_element_by_id('fileToUpload').send_keys('E:\\Documents\\baidu.side')

time.sleep(5)
# driver.find_element_by_id('fileToUpload').click()
# uiautomation.EditControl(AutomationId='1148').SendKeys('E:\\Documents\\baidu.side')
# uiautomation.ButtonControl(Name='打开(O)').Click()
# driver.find_element_by_id('buttonUpload').click()

