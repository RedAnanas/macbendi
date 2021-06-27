#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/21 15:09
# software: PyCharm
import unittest
import requests
import time
from HTMLTestRunner import HTMLTestRunner

class Connection:

    def __init__(self):
        self.session=requests.session()

    def get(self,url,params=None):
        return self.session.get(url,params)

    def post(self,url,data,headers=None,files=None):
        return self.session.post(url=url,data=data,headers=headers,files=files)
    def close(self):
        self.close()

class Woniusales(unittest.TestCase):
    # con=None
    #
    # @classmethod
    # def setUp(cls):
    #     cls.con = Connection()
    # @classmethod
    # def tearDown(cls):
    #     cls.con.close()
    #     pass

    def login(self):
            self.session = requests.session()
            date = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
            return self.session.post("http://admin:8080/WoniuSales1.4/user/login", date)

    def test_add_member1(self):
        self.session = requests.session()
        lonin=self.login()

        date2 = {"customername": "张三", "customerphone": "13571281657", "childsex": "男",
                "childdate": "2019-01-20", "creditkids": "111", "creditcloth": "222"}
        resp = self.session.post("http://admin:8080/WoniuSales1.4/customer/add",
                                 data=date2,cookies=lonin.cookies)
        result=resp.text  # already-added(添加失败),add-successful(添加成功)
        self.assertEquals(result, "already-added")
        print(type(resp.text))
        self.session.close()

    def test_add_member2(self):
        self.session = requests.session()
        lonin = self.login()

        date2 = {"customername": "张三", "customerphone": "13571281657", "childsex": "男",
                "childdate": "2019-01-20", "creditkids": "111", "creditcloth": "222"}
        resp = self.session.post("http://admin:8080/WoniuSales1.4/customer/add",
                                 data=date2, cookies=lonin.cookies)
        result = resp.text  # already-added(添加失败),add-successful(添加成功)
        self.assertEquals(result, "already-added")
        print(resp.text)
        self.session.close()

    def test_add_member3(self):
        self.session = requests.session()
        lonin = self.login()
        date2 = {"customername": "李四", "customerphone": "13571281657", "childsex": "男",
                "childdate": "2019-01-20", "creditkids": "111", "creditcloth": "222"}
        resp = self.session.post("http://admin:8080/WoniuSales1.4/customer/add",
                                 data=date2, cookies=lonin.cookies)
        result = resp.text  # already-added(添加失败),add-successful(添加成功)
        self.assertEquals(result, "already-added")
        print(resp.text)
        self.session.close()



# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     testCases01 = unittest.TestLoader().loadTestsFromTestCase(Woniusales)
#     suite.addTests(testCases01)
#
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     filename = now + 'report.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'执行情况')
#     runner.run(suite)
#     fp.close()

