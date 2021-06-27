#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/13 14:39
# software: PyCharm

#将加减乘除计算器的例子进行封装成类，并结合之前对比。

class calculator:

    a = 0
    b = 0
    c = ""

    def sum(self):
        if self.c == "+":
            s = self.a + self.b
            return s
        elif self.c == "-":
            s = self.a - self.b
            return s
        elif self.c == "*":
            s = self.a * self.b
            return s
        elif self.c == "/":
            s = self.a / self.b
            return s
        else:
            print("输入错误，请重新输入")

while 1:
    try:
        n = int(input("请输入第一个数字"))
        m = int(input("请输入第二个数字"))
        x = input("请输入运算符")

        q = calculator()
        q.a = n
        q.b = m
        q.c = x
        print(q.sum())
    except ValueError:
        print("输入错误，请重新输入")
    except ZeroDivisionError:
        print("输入错误，请重新输入")




