#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/4 20:11
# software: PyCharm

# 用户在屏幕上循环输入，每输入一次，就以字符串的形式
# 添加到列表中，当用户输入'quit'时，结束输入，打印整
# 个列表。
# 要求：添加列表元素的功能必须封装到一个函数中，用全
# 局变量和局部变量各实现一次。
a=[]
def run ():
    while True:
        s=input("请输入一个字符串")
        if s!="quit":
            a.append(s)
        else:
            print(a)
            break

run()
