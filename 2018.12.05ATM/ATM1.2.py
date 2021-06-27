#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/5 11:02
# software: PyCharm

# 1.显示开始菜单
def show_star():
    print("===================================================")
    print("=============欢迎使用蜗牛ATM系统====================")
    print("=====请输入你的选项 1：登录   2：注册   3：退出======")
    print("===================================================")
    choice=input("请选择：")
    if choice=="1":
        user_index=enter()
        return user_index
    elif choice=="2":
        register()
        return show_star()
    elif choice=="3":
        exit("退出")
    else:
        print("输入错误")
        return show_star()

#2.1验证用户名是否存在，存在返回真，不存在返回假
def u(users):
    for i in user:
        if i[0]==users:
            return True
    return False

#2.注册
def register():
    while True:
        users = input("请输入用户名：")
        if not u(users):
            break
        else:
            print("用户名存在，请重新输入")

    passwds=input("请输入密码：")
    balances=int(input("请输入存款金额"))
    user.append([users,passwds,balances])
    print("用户名为%s,密码为%s，余额为%d"%(users,passwds,balances))
    show_star()
#3.1验证密码是否正确
def confirm_passwd (users):
    while True:
        passwds = input("请输入密码")
        for i in user:
            if i[0]==users:
                if passwds == i[1]:
                    print("密码正确，欢迎登陆")
                    user_index=user.index(i)
                    return user_index
                else:
                    print("密码错误，请重新输入")

# 3.登录
def enter():
    while True:
        users = input("请输入用户名")
        if u(users):
            user_index=confirm_passwd(users)
            show_main(user_index)
            return user_index
        else:
            print("用户名不存在，请重新输入")

# 4.显示主菜单
def show_main(user_index):
    print("===================================================")
    print("=======1:查询余额 2:存款 3:取款 4:转账 5.返回=========")
    print("===================================================")
    choice = input("请选择：")
    if choice == "1":
        cat_money(user_index)
        show_main(user_index)
    elif choice == "2":
        deposit_money(user_index)
        show_main(user_index)
    elif choice == "3":
        draw_money(user_index)
        show_main(user_index)
    elif choice == "4":
        move_money(user_index)
        show_main(user_index)
    elif choice == "5":
        show_star()
    else:
        print("输入错误")

# 5.查询余额
def cat_money(user_index):
    print("您的余额为%d"%(user[user_index][2]))

# 6.存款
def deposit_money(user_index):
    money=int(input("请输入存款金额："))
    user[user_index][2]+=money
    cat_money(user_index)

# 7.取款
def draw_money(user_index):
    while True:
        money = int(input("请输入取款金额："))
        if money <= user[user_index][2]:
            user[user_index][2] -= money
            cat_money(user_index)
            break

        else:
            print("账户余额不足，请重新输入")
# 8.转账
def move_money(user_index):
    while True:
        youuser = input("请输入需要转账的用户名")
        if u(youuser):
            money = int(input("请输入转账金额："))
            if money <= user[user_index][2]:
                user[user_index][2] -= money
                #获取对方账户余额
                for i in user:
                    if i[0]==youuser:
                        i[2]+=money
                        cat_money(user_index)
                        return

            else:
                print("账户余额不足，请重新输入")
        else:
            print("用户名不存在，请重新输入")
user=[["111","111",2000],["222","222",2000]]

show_star()

