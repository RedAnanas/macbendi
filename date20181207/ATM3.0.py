#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/7 11:14
# software: PyCharm

#from date20181207.fun import*
import pymysql
import pymysql.connections
def getConn(hostname='localhost',username='root',password='root',database='atm'):
        conn = pymysql.connect(hostname, username, password, database)
        return conn

def inquire(acc_name):#传入用户名返回元祖
    sql = 'select balance from acc_info where acc_name="%s"' % (acc_name) #查
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    return result

def all_list():#查询所有的表
    sql = 'select acc_name from acc_info'
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    return result

def get_balance(acc_name):
    sql = 'select balance from acc_info where acc_name="%s"'%(acc_name)
    balance = inquire(sql)
    print('您的账户余额是:%d'%(balance))

def add_user(acc_name, acc_pass, balance):#增加函数
    sql = 'insert into acc_info values("%s","%s",%d)' % (acc_name, acc_pass, balance)  # 增
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def amend_balance(blances,acc_name):#修改函数

    sql = 'update acc_info set balance=%d where acc_name="%s"' % (blances, acc_name)
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)

    conn.commit()
    conn.close()
    return True

def amend_balance(acc_name):#删除函数

    sql = 'delete from acc_info where acc_name="%s"' % acc_name #删
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

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

#2.1验证用户名是否存在，存在返回真，不存在返回假
def u(acc_name):
    all=all_list()
    for i in all:
        for j in i:
            if j==acc_name:
                return True
    else:
        return False
#2.注册
def register():
    while True:
        acc_name = input("请输入用户名：")
        if not u(acc_name):
            break
        else:
            print("用户名存在，请重新输入")

    acc_pass = input("请输入密码：")
    balance = int(input("请输入存款金额："))
    add_user(acc_name, acc_pass, balance)
    show_star()

#3.1验证密码是否正确
def confirm_passwd (acc_name):
    while True:
        acc_pass = input("请输入密码：")
        all = all_list()
        for i in all:
            for j in i:
                if j == acc_name:
                    return True
                else:
                    print("密码错误，请重新输入")
        else:
            return False
# 3.登录
def enter():
    while True:
        acc_name = input("请输入用户名：")
        if u(acc_name):
            if confirm_passwd(acc_name):
                print("登录成功")
                show_main(acc_name)
                break
        else:
            print("用户名不存在，请重新输入")

# 4.显示主菜单
def show_main(acc_name):
    print("===================================================")
    print("=======1:查询余额 2:存款 3:取款 4:转账 5.返回=========")
    print("===================================================")
    choice = input("请选择：")
    if choice == "1":
        blances=inquire(acc_name)
        blances=blances[0]
        print(blances)

        show_main(acc_name)
    elif choice == "2":
        money=int(input("请输入存款金额："))
        blances = inquire(acc_name)
        blances= blances[0]
        blances += money
        flat=amend_balance(blances,acc_name)
        if flat:
            print("存款成功")
        else:
            print("存款失败")

        show_main(acc_name)
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        show_star()
    else:
        print("输入错误")

show_star()
