#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/13 21:12
# software: PyCharm

try:
    f = open("test.txt", "w")
    f.write("qqqqqqqq")
    f.close()
except PermissionError:
    print("没有写入权限")