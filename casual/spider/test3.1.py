#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/13 15:09
# software: PyCharm
import json
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://admin/agileone/index.php")
driver.delete_all_cookies()
# time.sleep(1)
with open("D:\Python\casual\spider\cookies.json","r",encoding="utf-8")as f:
    listCookies=json.loads(f.read())
for cookie in listCookies:
    driver.add_cookie({'domain': 'admin',
                       'httpOnly': False,
                       'name': 'PHPSESSID',
                       'path': '/',
                       'secure': False,
                       'value': 'd65b1a7fd62ffecfd5c5bc11d1962988'})
driver.get("http://admin/agileone/index.php")
