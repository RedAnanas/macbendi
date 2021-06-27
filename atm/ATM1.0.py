#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/4 9:33
# software: PyCharm
import time
welcome = '欢迎使用蜗牛ATM1.0系统'
print(welcome.center(len(welcome)+30,'='))
accounts = []   #创建空列表，用于存放账号信息
passwords = []  #创建空列表，用于存放密码信息
balances = [] #创建空列表，用于存放余额信息
while True:
    # 用户注册及登录
    while True:
        choice = input('===============1.登录；2.注册；3.退出===============')
        if choice == '1':  #登录业务
            accErr = 0
            passErr = 0
            isCheck = False
            while True :
                if accErr < 3 :
                    getAcc = input('请输入账号')
                    isCheckAcc = False
                    if getAcc != '':
                        for i in accounts:
                            if i == getAcc:
                                isCheckAcc = True
                                aIndex = accounts.index(i)  # 获取匹配项的位置
                                break
                    else:
                        accErr += 1
                        print('账号不能为空，请重新输入')

                    if isCheckAcc:
                        break
                    else:
                        while True:
                            accErr += 1
                            c = input("账号不匹配，请输入选择：1.重新输入账号；2.退出系统")
                            if c == '1':
                                break
                            elif c == '2':
                                exit('bye')
                            else:
                                print('输入错误，请重新输入')
                else:
                    exit('账号错误次数过多，退出系统。。。')
            while True:
                if passErr < 3 :
                    getPass = input('请输入密码')
                    isCheckPass = False
                    if getPass != '':
                       if passwords[aIndex] == getPass :
                           isCheck = True
                           break
                    else:
                        passErr += 1
                        print('密码不能为空，请重新输入')

                    if isCheckPass:
                        break
                    else:
                        while True:
                            passErr += 1
                            c = input("密码不匹配，请输入选择：1.重新输入密码；2.退出系统")
                            if c == '1':
                                break
                            elif c == '2':
                                exit('bye')
                            else:
                                print('输入错误，请重新输入')
                else:
                    exit('密码错误次数过多，退出系统。。。')

            if isCheck :
                print("账号密码输入正确，欢迎进入系统")
                break
        elif choice == '2':  #注册业务
            #账号不能为空，账号长度不能超过20位
           while True:
               isRepeatAcc = False  #创建标记，初始表示账号没有重复
               acc = input("请输入账号")
               if acc != '':  #账号不为空
                   if len(acc) <= 20 :  #账号长度不能超过20位
                       for i in accounts :  #遍历现有的账户列表
                           if i == acc :
                               isRepeatAcc = True  #账号有重复
                               break

                       if isRepeatAcc:
                           print("有重复账号，请重新输入")
                       else:
                           accounts.append(acc)
                           break
                   else:
                       print("账号长度不能超过20位，请重新输入")
               else:
                   print("输入的账号不能为空，请重新输入")

            #密码不能为空，密码必须都是数字
           while True:
                pa = input('请输入密码')
                if pa != '' :
                    if pa.isdigit() :
                        passwords.append(pa)
                        balances.append(5000)
                        print('账号密码创建成功，您的账号是%s,密码是%s余额是%d'%(acc,pa,5000))
                        break
                    else:
                        print("输入的密码应该都是数字，请重新输入")
                else:
                    print("密码不能为空，请重新输入")


        elif choice == '3':  #退出系统
            exit('bye')
        else:
            print("选择错误，请重新输入！")

    # 完成业务功能
    while True:
        mainChoice = input("==1.查询余额；2.存款；3.取款；4.转账；5.返回上一级；6.退出==")
        if mainChoice == '1':
            print('您当前的余额是%d'%(balances[aIndex]))
        elif mainChoice == '2': #存款业务
            savMoney = int(input('请输入您要存款的金额'))
            print('正在存款中，请稍后。。。')
            time.sleep(3)
            balances[aIndex] += savMoney
            print('存款完成，您现在的余额是%d'%(balances[aIndex]))
        elif mainChoice == '3':  #取款业务
            while True:
                drawMoney = input('请输入您要取款的金额')
                if drawMoney.isdigit():
                    drawMoney = int(drawMoney)
                    if balances[aIndex] >= drawMoney :
                        print('正在取款中，请稍后。。。')
                        time.sleep(3)
                        balances[aIndex] -= drawMoney
                        print('取款完成，您现在的余额是%d' % (balances[aIndex]))
                        break
                    else:
                        ch = input('账户余额不足1.重新输入；2.返回上一级；3.退出系统')
                        if ch == '1' :
                            continue
                        elif ch == '2' :
                            break
                        else:
                            exit('bye')

                else:
                    print('金额应该是数字，请重新输入')

        elif mainChoice == '4':  #转账业务
            while True:
                otherAcc = input('请输入对方账号：')
                isOtherAcc = False
                for i in accounts:
                    if otherAcc == i:
                        isOtherAcc = True
                        break
                if isOtherAcc:  #找到对方账户
                    while True:
                        moveMoney = int(input('请输入转账金额'))
                        if balances[aIndex] >= moveMoney:
                            print("正在转账，请稍后...")
                            time.sleep(3)
                            balances[aIndex] -= moveMoney
                            oIndex = accounts.index(otherAcc)  #获得对方账户的下标
                            balances[oIndex] += moveMoney
                            print('转账完成，您的余额为%d'%(balances[aIndex]))
                            break
                        else:
                            isF = False
                            while True:

                                s = input('转账余额不足。1.重新输入金额；2.返回上一级；3.退出')
                                if s == '1':
                                    break
                                elif s == '2':
                                    isF = True
                                    break
                                elif s == '3':
                                    exit('bye')
                                else:
                                    print('输入错误，请重新输入')
                            if isF:
                                break  # 可以返回上一级

                else:
                    f = False
                    while True:
                        r = input('没有这个账号1.重新输入；2.返回上一级；3.退出系统')
                        if r == '1':
                            break
                        elif r == '2':
                            f = True
                            break
                        elif r == '3':
                            exit('bye')
                        else:
                            print('输入错误，请重新输入')

                    if f :
                        break
        elif mainChoice == '5':  #返回上一级菜单
            break
        elif mainChoice == '6':  #退出系统
            exit('bye')
        else:
            print("选择错误，请重新输入！")
