#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/5 14:24
# software: PyCharm

#使用1个列表用于处理账户信息
import time
acc_info = [{'acc_name':'admin','acc_pass':'123','balance':2000},
            {'acc_name':'teacher','acc_pass':'123','balance':3000}]

def show_start_menu():
    choice = input('1.登录；2.注册；3.查看账户信息')
    if choice == '1' :
        acc_index = login()
        return acc_index
    elif choice == '2':
        regedit_acc()
        return show_start_menu()
    elif choice == '3':
        print(acc_info)
    else:
        return show_start_menu()

def regedit_acc():
    while True:
        acc_name = input('请输入账号名称')
        if not check_acc(acc_name):
            break
        else:
            print('账号已存在，请重新输入')

    #输入注册密码
    acc_pass = input('请输入密码')
    acc_balance = int(input('请输入初始金额'))

    acc_info.append({'acc_name':acc_name,'acc_pass':acc_pass,'balance':acc_balance})
    print('您的账号是%s;密码是%s；余额是%d' % (acc_name, acc_pass, acc_balance))

#2.1账号检查
def check_acc(acc):
    for i in acc_info :
        if i.get('acc_name') == acc :
            return True
    return False
#3.1密码验证
def confirm_pass(acc_name):
    while True:
        acc_pass = input('请输入密码')
        for i in acc_info:
            if i.get('acc_name') == acc_name:
                if i.get('acc_pass') == acc_pass:
                    print('输入正确，欢迎使用本机')
                    acc_index = acc_info.index(i)
                    return acc_index
        else:
            print('密码输入错误，请重新输入密码')

#3.登录；
def login():
    while True:
        acc_name = input('请输入您的账号')
        if  check_acc(acc_name):
            acc_index = confirm_pass(acc_name)
            return acc_index
        else:
            print('没有这个账号，请重新输入')


def show_main_menu(acc_index):
    while True:
        choice = input('1.查询余额；2.存款；3.取款；4.转账')
        if choice == '1':
            get_balance(acc_index)
        elif choice == '2':
            save_money(acc_index)
        elif choice == '3':
            draw_money(acc_index)
        elif choice == '4':
            tran_money(acc_index)
        else:
            pass

#5.查询余额；
def get_balance(acc_index):
    print('您的余额是%d'%(acc_info[acc_index].get('balance')))

#6.存款；
def save_money(acc_index):
    smoney = int(input('请输入你要存款的金额'))
    print('正在存款，请稍后...')
    time.sleep(3)
    balance = acc_info[acc_index].get('balance')
    balance += smoney
    acc_info[acc_index].update({'balance':balance})
    get_balance(acc_index)
    return
#7.取款
def draw_money(acc_index):
    while True:
        dmoney = int(input('请输入要取款的金额'))
        balance = acc_info[acc_index].get('balance')
        if balance >= dmoney:
            print('正在取款，请稍后...')
            time.sleep(3)
            balance -= dmoney
            acc_info[acc_index].update({'balance': balance})
            get_balance(acc_index)
            return
        else:
            print('余额不足，请重新输入')

#8.转账
def tran_money(acc_index):
    while True:
        other_acc = input('请输入对方账号')
        if not check_acc(other_acc):
            while True:
                tran_money = int(input('请输入转账金额：'))
                balance = acc_info[acc_index].get('balance')
                if balance >= tran_money:
                    balance -= tran_money
                    acc_info[acc_index].update({'balance': balance})
                    get_balance(acc_index)
                    # 获取对方的账号对应的余额
                    print('正在转账，请稍后...')
                    time.sleep(3)
                    for i in acc_info:
                        if i.get('acc_name') == other_acc:
                            other_index = acc_info.index(i)
                            other_balance = i.get('balance')
                            other_balance += tran_money
                            acc_info[other_index].update({'balance': other_balance})
                            print('转账完成')
                            return
                else:
                    print('转账金额不足，请重新输入')
        else:
            print('没有这个账号，请重新输入')
acc_index = show_start_menu()
show_main_menu(acc_index)
