#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:ananas
# datetime:2019/5/14 19:59
# software: PyCharm

class cat:
    def __init__(self,newname):
        self.name=newname
    def eat(self):
        print("%s爱吃鱼"%self.name)
if __name__ == '__main__':
    a=cat("tom")
    a.eat()