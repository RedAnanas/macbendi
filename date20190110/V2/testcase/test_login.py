#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 20:36
# software: PyCharm
from date20190110.V2.common.browser_manager import BrowserManager
from date20190110.V2.common.login import Login

data=[{"username":"admin","password":"admin","verifycode":"0000"},
    {"username":"admin","password":"11111","verifycode":"0000"},
    {"username":"admin","password":"admin","verifycode":"1234"}
]
for line in data:
    bm = BrowserManager()
    Login(bm).go_login(line["username"],line["password"],line["verifycode"])
    if line["username"]=="admin" and line["password"]=="admin" and line["verifycode"]=="0000":
        logxx =bm.driver.find_element_by_link_text("注销").text
        if "注销" in logxx:
            print("case 成功")
        else:
            print("case 失败")
    else:
        logxx=bm.driver.find_element_by_class_name("bootbox-body").text
        if line["username"]=="admin"and("登录失败" in logxx):
            print("case 成功")
        elif line["verifycode"]=="1234"and("验证码失效" in logxx):
            print("case 成功")
        else:
            print("case 失败")
    bm.driver.quit()

