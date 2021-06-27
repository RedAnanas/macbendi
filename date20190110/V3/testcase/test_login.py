#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 20:36
# software: PyCharm
from date20190110.V3.common.browser_manager import BrowserManager
from date20190110.V3.common.login import Login

with open("D:\Python\date20190110\V3\data\login.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        username, password,verifycode= line.strip().split(',')

        bm = BrowserManager()
        Login(bm).go_login(username,password,verifycode)
        if username=="admin" and password=="admin" and verifycode=="0000":
            logxx =bm.driver.find_element_by_link_text("注销").text
            if "注销" in logxx:
                print("case 成功")
            else:
                print("case 失败")
        else:
            logxx=bm.driver.find_element_by_class_name("bootbox-body").text
            if username=="admin"and("登录失败" in logxx):
                print("case 成功")
            elif verifycode=="1234"and("验证码失效" in logxx):
                print("case 成功")
            else:
                print("case 失败")
        bm.driver.quit()

