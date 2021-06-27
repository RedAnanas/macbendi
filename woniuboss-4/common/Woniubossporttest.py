#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/21 10:43
# software: PyCharm
import unittest
import HTMLTestRunner
from common.Utility import Read_File
from common.public_port import WoniuBoss


class WoniuPortTest(unittest.TestCase):
    con = None
    @classmethod
    def setUpClass(cls):
        cls.con =WoniuBoss()
        #cls.baseurl = cls.con.baseurl
        cls.readfile=Read_File()
    @classmethod
    def tearDownClass(cls):
        #         cls.con.close()
        #     #测试登录的接口，
        #     def test_l_login(self):
        #         sheet=self.readfile.read_excel()
        #         #定义登录接口的测试用例的在excel中的起始行和终点行
        #         # start_rows=0
        #         # end_rows=0
        #         # for i in range(start_rows-1,end_rows):
        #         #     list=sheet.row_values(i)
        #         #     data=list[]
        #         #     url=list[]
        #         #     method=list[]
        #     if method=='get'

        url=self.readfile.read_excel_data(sheet,2)
        self.readfile.read_excel_data()
        print(url)




