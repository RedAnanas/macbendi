#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/25 10:41
# software: PyCharm
import HTMLTestRunner
import unittest

from woniubossV01.common.Utility import Read_File
from woniubossV01.common.public_port import WoniuBoss
import os

class login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.con = WoniuBoss()
        cls.readfile = Read_File()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
    # def test_login_01(self):
    #     sheet=self.readfile.read_excel("../data/interface1.xlsx",index=2)
    #     number,url,method,parameter,contenttype=self.readfile.read_excel_data(sheet,4)
    #     print(number,url,method.lower(),parameter,contenttype)
    #     parameter1=self.readfile.dispose_params1(parameter)
    #     headers={'content-type':'application/x-www-form-urlencoded'}
    #     resp=self.con.judge_method(method.lower(),url,parameter1,headers)
    #     print(resp.text)
    #     self.assertEqual('error',resp.text)
    #
    #
    # def test_login_02(self):
    #     try:
    #         sheet = self.readfile.read_excel("../data/interface1.xlsx", index=2)
    #         number, url, method, parameter, contenttype = self.readfile.read_excel_data(sheet, 5)
    #         parameter1 = self.readfile.dispose_params1(parameter)
    #         headers = {'content-type': 'application/x-www-form-urlencoded'}
    #         resp = self.con.judge_method(method.lower(), url, parameter1, headers)
    #         self.assertEqual('checkcodeErrori', resp.text)
    #     except Exception as e:
    #         print(e)
    # def test_login_03(self):
    #     sheet=self.readfile.read_excel("../data/interface1.xlsx",index=2)
    #     number,url,method,parameter,contenttype=self.readfile.read_excel_data(sheet,6)
    #     print(number,url,method.lower(),parameter,contenttype)
    #     parameter1=self.readfile.dispose_params1(parameter)
    #     headers={'content-type':'application/x-www-form-urlencoded'}
    #     resp=self.con.judge_method(method.lower(),url,parameter1,headers)
    #     print(resp.text)
    #     self.assertEqual('success',resp.text)
    #
    # def test_login_04(self):
    #     sheet=self.readfile.read_excel("../data/interface1.xlsx",index=2)
    #     number,url,method,parameter,contenttype=self.readfile.read_excel_data(sheet,7)
    #     print(number,url,method.lower(),parameter,contenttype)
    #     parameter1=self.readfile.dispose_params1(parameter)
    #     headers={'content-type':'application/x-www-form-urlencoded'}
    #     resp=self.con.judge_method(method.lower(),url,parameter1,headers)
    #     print(resp.text)
    #     self.assertEqual('successfully',resp.text)
    # def test_login_05(self):
    #     sheet=self.readfile.read_excel("../data/interface1.xlsx",index=2)
    #     number,url,method,parameter,contenttype=self.readfile.read_excel_data(sheet,8)
    #     print(number,url,method.lower(),parameter,contenttype)
    #     parameter1=self.readfile.dispose_params1(parameter)
    #     headers={'content-type':'application/x-www-form-urlencoded'}
    #     resp=self.con.judge_method(method.lower(),url,parameter1,headers)
    #     print(resp.text)
    #     self.assertEqual('successful',resp.text)
    def test_logoin_06(self):
            sheet = self.readfile.read_excel("../data/interface1.xlsx", index=2)
            error=[]
            #str=''
            for i in range(4,12):
                list1= sheet.row_values(i-1)
                hoperesult=list1[8]
                print(hoperesult)
                number, url, method, parameter, contenttype = self.readfile.read_excel_data(sheet, i)
                print(url)
                parameter1 = self.readfile.dispose_params1(parameter)
                headers = {'content-type': 'application/x-www-form-urlencoded'}
                resp = self.con.judge_method(method.lower(), url, parameter1, headers)
                try:
                    self.assertEqual(hoperesult, resp.text)
                except Exception as e:
                    #list.append(e)
                    #str += '第%d条测试用例执行失败，失败信息是%s'%(number,e)
                    str = '第%d条测试用例执行失败，失败信息是%s' % (number, e)
                    error.append(str)
            if error!=[]:
                raise AssertionError(error)
    def test_logoin_07(self):
            sheet = self.readfile.read_excel("../data/interface1.xlsx", index=2)
            error=[]
            #str=''
            for i in range(4,12):
                list1= sheet.row_values(i-1)
                hoperesult=list1[8]
                print(hoperesult)
                number, url, method, parameter, contenttype = self.readfile.read_excel_data(sheet, i)
                print(url)
                parameter1 = self.readfile.dispose_params1(parameter)
                headers = {'content-type': 'application/x-www-form-urlencoded'}
                resp = self.con.judge_method(method.lower(), url, parameter1, headers)
                try:
                    self.assertEqual(hoperesult, resp.text)
                except Exception as e:
                    #list.append(e)
                    #str += '第%d条测试用例执行失败，失败信息是%s'%(number,e)
                    str = '第%d条测试用例执行失败，失败信息是%s' % (number, e)
                    error.append(str+'\n')
            if error!=[]:
                raise AssertionError(error)

    # def test_login_03(self):
    #
    #
    #     sheet = self.readfile.read_excel("../data/interface1.xlsx", index=2)
    #     for i in range(4,6):
    #         number, url, method, parameter, contenttype=self.readfile.read_excel_data(sheet,i)
    #
    #         parameter1 = self.readfile.dispose_params1(parameter)
    #         headers = {'content-type': 'application/x-www-form-urlencoded'}
    #         resp = self.con.judge_method(method.lower(), url, parameter1, headers)
    #         if resp.text=='error':
    #             self.assertEqual('error',resp.text)
    #         else:
    #             self.assertEqual('',resp.text)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(login_test))
    with open('test_report.html', 'w',encoding='utf8') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='report', verbosity=2)
        runner.run(suite)









