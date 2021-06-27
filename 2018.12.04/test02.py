#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/4 17:58
# software: PyCharm

# 编写一个函数，在函数内部对参数进行操作后打印值，
# 同时在函数外也打印该参数的值。要求如下：
# 1.如果传入的是数字，则在函数内加1。
# 2.如果传入的是字符串，则在字符串后加‘1’。
# 3.如果传入的是列表，则在后加一个元素1。

def a (n):
    if type(n)==int:
        s=n+1
        return s
    elif type(n)==str:
        s=n+"2"
        return s
    elif type(n)==list:
        n.append(3)
        return n
print(a([2,3,5,6]))

