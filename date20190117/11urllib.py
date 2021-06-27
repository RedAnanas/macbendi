#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/17 15:57
# software: PyCharm
from urllib import parse,request


def get_method1():
    return request.urlopen("http://admin/agileone/")

def post_method1():
    pass

if __name__ == '__main__':

    get_method1()