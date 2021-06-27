#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/7 14:30
# software: PyCharm
# 用于与用户交互
from atm.ATM2.manager import *
import time
def show_start_menu():
    while 1:
        choice = input('1.登录；2.注册；')
        if choice == '1':
            acc_name = login()
            return acc_name
        elif choice == '2':
            regedit_acc()
        else:
            return show_start_menu()

#账号注册
def regedit_acc():
    while True:
        acc_name = input('请输入账号名称')
        if check_acc(acc_name):
            print('账号已存在，请重新输入')
        else:
            print('账号输入正确')
            break

    acc_pass = input('请输入密码')
    balance = int(input('请输入余额'))
    sql = 'insert into acc_info values("%s","%s",%d)'%(acc_name,acc_pass,balance)
    flag = update_acc(sql)
    if flag:
        print('添加账号成功')
    else:
        print('添加账号失败')

def login():
   while 1:
       acc_name = input('请输入登录账号')
       flag = check_acc(acc_name)
       if flag:
           print('账号输入正确')
           break
       else:
           print('账号不存在，请重新输入')

   while 1:
       acc_pass = input('请输入密码')
       flag = check_pass(acc_name, acc_pass)
       if flag:
           print('密码输入正确.欢迎使用ATM')
           return acc_name
       else:
           print('密码错误，请重新输入')

def get_balance(acc_name):
    sql = 'select balance from acc_info where acc_name="%s"'%(acc_name)
    balance = get_balan(sql)
    print('您的账户余额是:%d'%(balance))

def save_money(acc_name):
    save_money = int(input('请输入您要存款的金额：'))
    balance = get_balan(acc_name)
    balance = balance[0]
    balance += save_money

    flag = update_acc(balance, acc_name)
    if flag:
        print('正在存款，请稍后...')
        time.sleep(3)
        print('存款成功')
    else:
        print('存款失败')

def draw_money(acc_name):
    draw_money = int(input('请输入您要取款的金额：'))
    balance = get_balan(acc_name)
    if balance[0] >= draw_money:
        balance = balance[0]
        balance -= draw_money

        flag = update_acc(balance, acc_name)
        if flag:
            print('正在取款，请稍后...')
            time.sleep(3)
            print('取款成功')
        else:
            print('取款失败')

def tran_money():
    while 1:
        other_acc_name = input('请输入对方的账号：')
        flag = check_acc(other_acc_name)
        if flag:
            print('对方账号输入正确')
            break
        else:
            print('对方账号输入错误，请重新输入')

    while 1:
        tran_money = int(input('请输入您要转账的金额：'))
        balance = get_balan(acc_name)
        if balance[0] >= tran_money:
            balance = balance[0]
            balance -= tran_money
            flag1 = update_acc(balance, acc_name)
            other_balance = get_balan(other_acc_name)
            other_balance = other_balance[0]
            other_balance += tran_money
            flag2 = update_acc(other_balance,other_acc_name)
            if flag1 and flag2:
                print('正在转账，请稍后...')
                time.sleep(3)
                print('转账成功')
                break
            else:
                print("转账失败")
        else:
            print('余额不足，请重新输入转账金额')


def show_main_nenu(acc_name):
    while True:
            choice = input('1.查询余额；2.存款；3.取款；4.转账')
            if choice == '1':
                get_balance(acc_name)
            elif choice == '2':
                save_money(acc_name)
            elif choice == '3':
                draw_money(acc_name)
            elif choice == '4':
                tran_money()
            else:
                pass

if __name__ == '__main__':
    acc_name = show_start_menu()
    show_main_nenu(acc_name)
