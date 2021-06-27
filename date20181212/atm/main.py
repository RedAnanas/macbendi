#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/12 17:52
# software: PyCharm

# 1.显示开始菜单
def show_star():
    print("===================================================")
    print("=============欢迎使用蜗牛ATM系统====================")
    print("=====请输入你的选项 1：登录   2：注册   3：退出======")
    print("===================================================")
    choice=input("请选择：")
    if choice=="1":
        pass
    elif choice=="2":
        pass
    elif choice=="3":
        exit("退出")
    else:
        print("输入错误，请重新输入")
        return show_star()