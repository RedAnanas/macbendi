#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/4 20:41
# software: PyCharm

# 1.编写一个lambda函数，对x和y进行幂运算，并调用此函数。

# fun=lambda x,y:x**y
# print(fun(2,3))

# 2.实现一个函数，传入一个list后排序，并返回排序后的新list。

# def run (a):
#     for i in range(0, len(a) - 1):
#         for j in range(0, len(a) - 1 - i):
#             if a[j] > a[j + 1]:
#                 b = a[j]
#                 a[j] = a[j + 1]
#                 a[j + 1] = b
#     print(a)
#
# run([2,3,5,1,6])

# 3.实现一个函数count(str,substr),查找str中有多少个
#    substr,要求用到文档字符串（包含作者、功能、参数说
#    明、返回值几个信息）。
cou=0
def getss(s,su):
    """
    作者
    功能：查找str中有多少个substr

    :param s:
    :param su:
    :return:
    """
    global cou
    while True:
        if s.find(su)!=-1:
            news=s[s.find(su)+len(su):]
            cou+=1
            return getss(news,su)
        else:
            return

s=input("请输入一个字符串")
su=input("请输入要查找的字符串")
getss(s,su)
print(cou)
print(getss.__doc__)







