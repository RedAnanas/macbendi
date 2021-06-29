#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/3 15:02
# software: PyCharm
#输入一个数，判断是否为质数

while True:
    a=input("请输入一个整数")
    if a.isdigit():#判断是否为数字

        if int(a)%2==0 and int(a)!=2:
            print("不是质数")
        else:
            print("是质数")

    else:
        print("输入错误，请重新输入")
        continue