#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/25 10:29
# software: PyCharm
import HTMLTestRunner
import requests,unittest
from woniubossV01.common.Utility import Read_File
from woniubossV01.common.public_port import WoniuBoss


class student(unittest.TestCase):

    def setUp(cls):
        cls.con = WoniuBoss()
        cls.con.post_login_method6('WNCD051')
        cls.readfile = Read_File()

    def tearDown(cls):
        cls.con.close()



    # def test(self):
    #     sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
    #     str = ''
    #     error = []
    #     for i in range(6,10):
    #         list= sheet.row_values(i-1)
    #         hoperesult=list[7]
    #         print(hoperesult)
    #         number,method, url, parameter, headers = self.readfile.read_excel_data(sheet, i)
    #         parameter1 = self.readfile.dispose_params1(parameter)
    #         headers = {'content-type': 'application/x-www-form-urlencoded'}
    #         response = self.con.judge_method(method.lower(), url, parameter1, headers)
    #         self.assertEqual(response.text, hoperesult)
    #
    #         try:
    #
    #
    #             self.assertEqual(hoperesult,response.text)
    #         except Exception as e:
    #             str += '第%d条用例执行失败，失败信息是%s'%(number,e)
    #             error.append(str)
    #             print(str)
    #     if error!=[]:
    #         raise AssertionError
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

    def test_01(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx',index=2)
        number,url, method, parameter, headers=self.readfile.read_excel_data(sheet,5)
        # print(method,url,parameter,headers)
        parameter1= self.readfile.dispose_params1(parameter)
        headers= {'content-type':'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(),url,parameter1,headers)
        # print(response.text)
        self.assertEqual(response.text,'checkcodeError')

    def test_02(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 6)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.text)
        self.assertEqual(response.text, 'yes')

    def test_03(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 7)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.text)
        self.assertEqual(response.text, '二级密码输入错误')

    def test_04(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 8)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.json())
        # print(type(response.json()))
        self.assertEquals(response.json()['education'], '大专')

    def test_05(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 11)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.text)
        self.assertEqual(response.text, '')



    def test_06(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 12)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.text)
        self.assertEqual(response.text, '')


    def test_07(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 13)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.json())
        self.assertEqual(response.json()['totalRow'], 158)



    def test_08(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 14)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.text)
        self.assertEqual(response.text, '')


    def test_09(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 15)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.json())
        self.assertEqual(response.json()['totalRow'], 0)


    


    def test_11(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 17)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.text)
        self.assertEqual(response.text, 'success')



    def test_12(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 18)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.text)
        self.assertEqual(response.text, 'success')



    def test_13(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 19)
        # print(method, url, parameter, headers)
        # print(parameter)
        parameter1 = self.readfile.dispose_params1(parameter)
        # print(parameter1)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.text)
        self.assertEqual(response.text, 'success')


    def test_14(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 20)
        # print(method, url, parameter, headers)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        # print(response.json())
        self.assertEqual(response.json()['totalRow'], 158)

    def test_15(self):
        sheet = self.readfile.read_excel('../data/接口.xlsx', index=2)
        number,url, method, parameter, headers = self.readfile.read_excel_data(sheet, 21)
        parameter1 = self.readfile.dispose_params1(parameter)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.con.judge_method(method.lower(), url, parameter1, headers)
        self.assertEqual(response.json()['totalRow'], 4)














if __name__ == '__main__':

    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(student))
    with open('test_report.html', 'wb+') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='report', verbosity=2)
        runner.run(suite)



