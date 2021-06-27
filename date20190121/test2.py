#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/21 21:35
# software: PyCharm


import unittest
import requests
import time
from HTMLTestRunner import HTMLTestRunner

class Test_case(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def login(self):

        self.session = requests.session()
        self.date = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
        return self.session.post("http://admin:8080/WoniuSales1.4/user/login", self.date).cookies



    def test_add_member1(self):
        self.session = requests.session()
        self.date1 = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
        lonin=self.session.post("http://admin:8080/WoniuSales1.4/user/login", self.date1)

        date2 = {"customername": "张三", "customerphone": "13571281657", "childsex": "男",
                "childdate": "2019-01-20", "creditkids": "111", "creditcloth": "222"}
        resp = self.session.post("http://admin:8080/WoniuSales1.4/customer/add",
                                 data=date2,cookies=lonin.cookies)
        result=resp.text  # already-added(添加失败),add-successful(添加成功)
        self.assertEqual(result, "already-added")
        print(type(resp.text))
        self.session.close()

    def test_add_member2(self):
        self.session = requests.session()
        self.date1 = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
        lonin = self.session.post("http://admin:8080/WoniuSales1.4/user/login", self.date1)

        date2 = {"customername": "张三", "customerphone": "13571281657", "childsex": "男",
                "childdate": "2019-01-20", "creditkids": "111", "creditcloth": "222"}
        resp = self.session.post("http://admin:8080/WoniuSales1.4/customer/add",
                                 data=date2, cookies=lonin.cookies)
        result = resp.text  # already-added(添加失败),add-successful(添加成功)
        self.assertEqual(result, "already-added")
        print(resp.text)
        self.session.close()

    def test_add_member3(self):
        self.session = requests.session()
        self.date1 = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
        lonin = self.session.post("http://admin:8080/WoniuSales1.4/user/login", self.date1)

        date2 = {"customername": "李四", "customerphone": "13571281657", "childsex": "男",
                "childdate": "2019-01-20", "creditkids": "111", "creditcloth": "222"}
        resp = self.session.post("http://admin:8080/WoniuSales1.4/customer/add",
                                 data=date2, cookies=lonin.cookies)
        result = resp.text  # already-added(添加失败),add-successful(添加成功)
        self.assertEqual(result, "already-added")
        print(resp.text)
        self.session.close()




