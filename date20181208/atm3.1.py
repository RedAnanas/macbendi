#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/8 13:23
# software: PyCharm

from date20181208.atmfun import check_acc,check_pass,add_user,inquire,amend_balance

# 1.显示开始菜单
def show_star():
    print("===================================================")
    print("=============欢迎使用蜗牛ATM系统====================")
    print("=====请输入你的选项 1：登录   2：注册   3：退出======")
    print("===================================================")
    choice=input("请选择：")
    if choice=="1":

        enter()
    elif choice=="2":
        register()
    elif choice=="3":
        exit("退出")
    else:
        print("输入错误，请重新输入")
        return show_star()

#2.注册
def register():
    while True:
        acc_name = input("请输入用户名：")
        user=check_acc(acc_name)
        if not user:
            break
        else:
            print("用户名存在，请重新输入")

    acc_pass = input("请输入密码：")
    balance = int(input("请输入存款金额："))
    add_user(acc_name, acc_pass, balance)
    show_star()

# 3.登录
def enter():
    while True:
        acc_name = input("请输入用户名：")
        user = check_acc(acc_name)

        if user:
            acc_pass = input("请输入密码：")
            if check_pass(acc_name,acc_pass):
                print("登录成功")
                show_main(acc_name)
                break
            else:
                print("密码错误，请重新输入")
        else:
            print("用户名不存在，请重新输入")

# 4.显示主菜单
def show_main(acc_name):
    print("===================================================")
    print("=======1:查询余额 2:存款 3:取款 4:转账 5.返回=========")
    print("===================================================")
    choice = input("请选择：")
    if choice == "1":
        balances=inquire(acc_name)
        balances=balances[0]
        print(balances)
        show_main(acc_name)
    elif choice == "2":
        money = int(input("请输入存款金额："))
        balances = inquire(acc_name)
        balances = balances[0]
        balances+=money
        add=amend_balance(balances, acc_name)
        if add:
            print("存款成功")
        else:
            print("存款失败")
        show_main(acc_name)
    elif choice == "3":
        while True:
            money = int(input("请输入取款金额："))
            balances = inquire(acc_name)
            balances = balances[0]
            if money <= balances:
                balances -= money
                add = amend_balance(balances, acc_name)
                if add:
                    print("取款成功")
                    show_main(acc_name)
                    break
                else:
                    print("取款失败")
                show_main(acc_name)
            else:
                print("余额不足，请重新输入")
    elif choice == "4":
        acc_yname = input("请输入需要转账的用户名：")
        if check_acc(acc_name):
            while True:
                money = int(input("请输入转账金额："))
                balances = inquire(acc_name)
                balances = balances[0]

                balance = inquire(acc_yname)
                balance = balance[0]
                if money <= balances:
                    balances -= money
                    amend_balance(balances, acc_name)
                    balance+=money
                    amend_balance(balance, acc_yname)
                    print("转账成功")
                    show_main(acc_name)
                    break
                else:
                    print("余额不足，请重新输入")
        else:
            print("用户名不存在，请重新输入")
    elif choice == "5":
        show_star()
    else:
        print("输入错误")

show_star()