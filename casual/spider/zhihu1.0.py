#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/13 16:14
# software: PyCharm
from selenium import webdriver
import json
import time
class self:
    driwer=webdriver.Chrome()
    driwer.get("https://www.zhihu.com/signup?next=%2F")
    driwer.find_element_by_xpath("//div[@class='SignContainer-switch']/span").click()
    driwer.find_element_by_name("username").click()
    driwer.find_element_by_name("username").send_keys("17868871347")
    driwer.find_element_by_name("password").click()
    driwer.find_element_by_name("password").send_keys("hbc19950821")
    driwer.find_element_by_xpath(
        "//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/button").click()
    # time.sleep(1)
    # dictCookies=driwer.get_cookies()
    # jsonCookies=json.dumps(dictCookies)
    # with open("cookies.json","w") as f:
    #     f.write(jsonCookies)