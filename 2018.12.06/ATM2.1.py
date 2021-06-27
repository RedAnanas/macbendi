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

        enter()

    elif choice=="2":
        register()

    elif choice=="3":
        exit("退出")
    else:
        print("输入错误")
        return show_star()

#2.1验证用户名是否存在，存在返回真，不存在返回假
def u(users):
    file=open("../File/atm.txt")
    user=file.readlines()
    if len(user)!=0:
        for i in user:
            if i[:i.find(",")] == users:
                file.close()
                return True
        else:
            file.close()
            return False
    else:
        file.close()
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
    balances=input("请输入存款金额")
    file = open("../File/atm.txt","a+")
    s="\n"+users+","+passwds+","+balances
    file.writelines(s)
    file.close()
    print("用户名为%s,密码为%s，余额为%s"%(users,passwds,balances))
    show_star()
#3.1验证密码是否正确
def confirm_passwd (users):
    while True:
        passwds = input("请输入密码")
        file = open("../File/atm.txt")
        user = file.readlines()
        for i in user:
            user_index=i.split(",")#将字符串分割成列表
            if user_index[0]==users:
                if user_index[1]==passwds:
                    print("密码正确，欢迎登陆")
                    show_main(user_index)
                    return user_index
                else:
                    print("密码错误，请重新输入")

# 3.登录
def enter():
    while True:
        users = input("请输入用户名")
        if u(users):
            confirm_passwd(users)
            # show_main(user_index)

        else:
            print("用户名不存在，请重新输入")

# 4.显示主菜单
def show_main(user_index):
    while True:
        print("===================================================")
        print("=======1:查询余额 2:存款 3:取款 4:转账 5.返回=========")
        print("===================================================")
        choice = input("请选择：")
        if choice == "1":
            cat_money(user_index)
            print("您的余额为%s" % (user_index[2]))

        elif choice == "2":
            deposit_money(user_index)

        elif choice == "3":
            pass
            # draw_money(user_index)
            # show_main(user_index)
        elif choice == "4":
            pass
            # move_money(user_index)
            # show_main(user_index)
        elif choice == "5":
            pass
        else:
            print("输入错误")

#5.查询余额
def cat_money(user_index):
    file = open("../File/atm.txt")
    user = file.readlines()
    for i in user:
        users = i.split(",")  # 将字符串分割成列表
        if users[0] == user_index:
            file.close()
            return user_index[2]

#从文件中读取所有的内容，改变其中选定的余额，返回该条记录
def read_info(user_index,balance):
    file = open("../File/atm.txt")
    user = file.readlines()
    for i in user:
        user = i.split(",")  # 将字符串分割成列表
        if user[0] == user_index:
            new_user_index=user[0] + "," + user[1] + "," + balance + "\n"
    file.close()
    return new_user_index

#将被修改的内容重新写入到文件中
def write_info(user_index,new_user_index):
    f=open("../File/atm.txt","r")
    user_info=f.readlines()
    f.close()
    file = open("../File/atm.txt","w")
    user = file.readlines()
    for i in user:
        userss = i.split(",")  # 将字符串分割成列表
        if userss[0] == user_index:
            file.writelines(new_user_index)
        else:
            file.writelines(i)
        file.close()

#更新文件中的余额
def update_balance(user_index,balance):
    new_acc_info = read_info(user_index, balance)
    write_info(user_index, new_acc_info)

#增加账户余额
def add_balance(user_index,balance,money):
    balance += money
    balance = str(balance)
    update_balance(user_index, balance)


# 6.存款
def deposit_money(user_index):
    money=int(input("请输入存款金额："))
    balance = int(cat_money(user_index))
    add_balance(user_index, balance, money)

    cat_money(user_index)
    return
# # 7.取款
# def draw_money(user_index):
#     while True:
#         money = int(input("请输入取款金额："))
#         if money <= user[user_index][2]:
#             user[user_index][2] -= money
#             cat_money(user_index)
#             break
#
#         else:
#             print("账户余额不足，请重新输入")
# # 8.转账
# def move_money(user_index):
#     while True:
#         youuser = input("请输入需要转账的用户名")
#         if u(youuser):
#             money = int(input("请输入转账金额："))
#             if money <= user[user_index][2]:
#                 user[user_index][2] -= money
#                 #获取对方账户余额
#                 for i in user:
#                     if i[0]==youuser:
#                         i[2]+=money
#                         cat_money(user_index)
#                         return
#
#             else:
#                 print("账户余额不足，请重新输入")
#         else:
#             print("用户名不存在，请重新输入")

show_star()

