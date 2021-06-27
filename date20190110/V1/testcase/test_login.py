#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 20:36
# software: PyCharm
from date20190110.V1.common.browser_manager import BrowserManager
from date20190110.V1.common.login import Login
import time

url="http://admin:8080/WoniuSales1.4/"

bm=BrowserManager(url)
Login(bm).go_login("admin","admin","0000")
time.sleep(1)
logxx=bm.driver.find_element_by_link_text("注销").text
if "注销" in logxx:
    print("case1 登录成功")
else:
    print("case1 登录失败")
bm.driver.quit()


bm=BrowserManager(url)
Login(bm).go_login("admin","admin123","0000")
logxx=bm.driver.find_element_by_class_name("bootbox-body").text
if "登录失败" in logxx:
    print("case2 成功")
else:
    print("case2 失败")

bm.driver.quit()

