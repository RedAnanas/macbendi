#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/9 9:37
# software: PyCharm
from selenium import webdriver
import time

# web=webdriver.Chrome()
def test_logn1():
    web=webdriver.Firefox()
    web.get("http://admin:8080/WoniuSales1.4/")
    # web.maximize_window()
    # time.sleep(2)
    # web.set_window_size(1200,800)
    # time.sleep(2)
    web.implicitly_wait(20)
    web.set_page_load_timeout(20)
    web.find_element_by_id("username").send_keys("admin")
    web.find_element_by_id("password").send_keys("admin")
    web.find_element_by_id("verifycode").send_keys("0000")
    web.find_element_by_class_name("form-control.btn-primary").click()
    # web.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
    # time.sleep(2)
    s=web.find_element_by_link_text("注销").text
    web.find_element_by_link_text("注销").click()
    web.quit()
    return s
    # time.sleep(2)

def test_logn2():
    web=webdriver.Firefox()
    web.get("http://admin:8080/WoniuSales1.4/")
    # web.maximize_window()
    # time.sleep(2)
    # web.set_window_size(1200,800)
    # time.sleep(2)
    web.implicitly_wait(20)
    web.set_page_load_timeout(20)
    web.find_element_by_id("username").send_keys("admin")
    web.find_element_by_id("password").send_keys("admin11")
    web.find_element_by_id("verifycode").send_keys("0000")
    web.find_element_by_class_name("form-control.btn-primary").click()
    # web.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
    # time.sleep(2)
    s=web.find_element_by_class_name("bootbox-body").text
    web.quit()
    return s
    # time.sleep(2)

