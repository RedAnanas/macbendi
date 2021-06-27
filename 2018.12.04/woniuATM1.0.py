#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/3 19:20
# software: PyCharm
username=[]
password=[]
print("==================================================================")
print("=====================欢迎使用蜗牛ATM系统===========================")
print("=============请输入你的选项 1：登录   2：注册   3：退出==============")
print("==================================================================")
while True:
    int1=input("请选择:")
    if int1=="1":
        user=input("请输入您的账号：")
        passwd=input("请输入您的密码：")
        if username.index(user)!=-1:
            if passwd==password[username.index(user)]:
                print("登录成功")
            else:
                print("账号或密码错误，请重新输入")
        else:
            print("账号不存在，请重新输入")

    elif int1=="2":
        while True:
            isuser=False #表示账号没有重复
            user = input("请输入账号：")
            if user!="":
                for i in username:
                    if i==user:
                        ispasswd=True
                        break
                if isuser:
                    print("账号重复，请重新输入")
                else:
                    username.append(user)
                    break
            else:
                print("账号不能为空，请重新输入")
        while True:
            passwd = input("请输入密码")
            if passwd != "":
                password.append(password)
                break
            else:
                print("密码不能为空，请重新输入")

    elif int1=="3":
        exit("退出")
    else:
        print("输入错误，请重新输入")

