#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/13 14:47
# software: PyCharm
from selenium import webdriver
import json
import time
class self:
    driwer=webdriver.Chrome()
    driwer.get("http://admin/agileone/index.php")
    driwer.find_element_by_id("username").send_keys("admin")
    driwer.find_element_by_id("password").send_keys("admin")
    driwer.find_element_by_id("login").click()
    time.sleep(1)
    dictCookies=driwer.get_cookies()
    jsonCookies=json.dumps(dictCookies)
    with open("cookies.json","w") as f:
        f.write(jsonCookies)




