#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/4 15:34
# software: PyCharm

#实现一个函数，支持传入任意多个整数进行加法运算，并返回结果。

# def sum(*n):
#     s=0
#     for i in n:
#         s+=i
#     return s
#
#
# print(sum(12,1,3))

#实现一个简易计算器，根据用户输入执行相应的加、减、乘、
#除运算，例如用户输入'9 / 3',得出结果。每种运算请用单独的
#函数处理。

def jia (a,c):
    s=0
    s=a+c
    return s
def jian (a,c):
    s=0
    s=a-c
    return s
def cheng (a,c):
    s=0
    s=a*c
    return s
def chu (a,c):
    s=0
    s=a/c
    return s

a=int(input("请输入第一个数字"))
b=input("请输入运算符")
c=int(input("请输入第二个数字"))
if b=="+":
    print(jia(a,c))
elif b=="-":
    print(jian(a,c))
elif b=="*":
    print(cheng(a,c))
elif b=="/":
    print(chu(a,c))
else:
    print("输入错误")


