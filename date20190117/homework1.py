#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/17 20:01
# software: PyCharm

import requests

def logn():
    session = requests.session()
    date={'username':'admin','password':'admin','verifycode':'0000'}
    resp=session.post("http://admin:8080/WoniuSales1.4/user/login",date)
    # print(resp.text)
    session.close()


def cookies():
    session=requests.session()
    date = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
    r=session.post("http://admin:8080/WoniuSales1.4/user/login",date).cookies
    print(r)

def Userquery():
    session = requests.session()
    date = {"customerphone":"17868871347","page":"1"}
    resp = session.post("http://admin:8080/WoniuSales1.4/customer/search", date)
    print(resp.text)
    print(resp.status_code)
    print(type(resp.status_code))
    session.close()

def add_vip():
    session = requests.session()
    date = {"customername":"张三","customerphone":"17868871347","childsex":"男",
            "childdate":"2019-01-20","creditkids":"111","creditcloth":"222"}
    resp = session.post("http://admin:8080/WoniuSales1.4/customer/add", date)
    # print(resp.text)#already-added(添加失败),add-successful(添加成功)
    # print(resp.status_code)
    # print(type(resp.status_code))
    session.close()


def stock_search():
    session = requests.session()
    date = {"goodsserial":"M3Q1498B","goodsname":"","barcode":"","goodstype":"",
            "earlystoretime":"","laststoretime":"","page":"1"}
    resp = session.post("http://admin:8080/WoniuSales1.4/query/stored", date)

    print(resp.text)

    session.close()

def get_cookie_method1():
    resp = logn()
    cookie = resp.headers['Set-Cookie']
    return print(cookie)

if __name__ == '__main__':
    # logn()
    # Userquery()
    # add_vip()
    # stock_search()
    cookies()
    # get_cookie_method1