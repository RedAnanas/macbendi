#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/12 11:50
# software: PyCharm
class Car:
    brand=""
    price=0
    def print_info(self):
        print("车的品牌为：%s\n车的价格为：%d万\n"%(self.brand,self.price))

if __name__ == '__main__':

    x=Car()
    x.brand="宝马"
    x.price=40
    print(x.brand,x.price)