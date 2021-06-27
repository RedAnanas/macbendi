#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/5 9:40
# software: PyCharm

#使用函数进行重构

'''
1.显示开始菜单；
2.注册；
2.1账号检查
3.登录；
2.1账号检查
4.显示主菜单
5.查询余额；
6.存款；
7.取款；
8.转账
'''

#2.1账号检查
def check_acc(acc):
    for i in accounts :
        if i == acc :
            return False
    return True

#1.显示开始菜单；
def show_start_menu():
    choice = input('1.登录；2.注册；')
    if choice == '1' :
        acc_index = login()
        print(acc_index)
        return acc_index
    elif choice == '2':
        regedit_acc()
        return show_start_menu()
    else:
        return show_start_menu()



#2.注册；
def regedit_acc():
    while True:
        acc_name = input('请输入账号名称')
        if check_acc(acc_name):
            break
        else:
            print('账号已存在，请重新输入')

    #输入注册密码
    acc_pass = input('请输入密码')
    acc_balance = int(input('请输入初始金额'))

    accounts.append(acc_name)
    passwords.append(acc_pass)
    balances.append(acc_balance)
    print('您的账号是%s;密码是%s；余额是%d' % (acc_name, acc_pass, acc_balance))
    #show_start_menu()

#3.1密码验证
def confirm_pass(acc_name):
    acc_pass = input('请输入密码')
    acc_index = accounts.index(acc_name)
    if passwords[acc_index] == acc_pass:
        print('输入正确，欢迎使用本机')

        return acc_index  #返回该账户的下标
    else:
        print('密码输入错误，请重新输入密码')
#3.登录；
def login():
    while True:
        acc_name = input('请输入您的账号')
        if not check_acc(acc_name):
            acc_index = confirm_pass(acc_name)
        else:
            print('没有这个账号，请重新输入')

        return acc_index

#4.显示主菜单
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
    print('您的余额是%d'%(balances[acc_index]))

#6.存款；
def save_money(acc_index):
    smoney = int(input('请输入你要存款的金额'))
    balances[acc_index] += smoney
    get_balance(acc_index)
    return
#7.取款
def draw_money(acc_index):
    while True:
        dmoney = int(input('请输入要取款的金额'))
        if balances[acc_index] >= dmoney:
            balances[acc_index] -= dmoney
            get_balance(acc_index)
            return
        else:
            print('余额不足，请重新输入')

#8.转账
def tran_money(acc_index):
    while True:
        other_acc = input('请输入对方账号')
        if not check_acc(other_acc):
            tran_money = int(input('请输入转账金额：'))
            if balances[acc_index] >= tran_money :
                balances[acc_index] -= tran_money
                get_balance(acc_index)
                #获取对方的账号对应的余额
                other_index = accounts.index(other_acc)
                balances[other_index] += tran_money
                return
        else:
            print('没有这个账号，请重新输入')

accounts = ['admin','yang']   #创建空列表，用于存放账号信息
passwords = ['123','123']  #创建空列表，用于存放密码信息
balances = [1000,3000] #创建空列表，用于存放余额信息
acc_index = show_start_menu()
print(acc_index)
show_main_menu(acc_index)