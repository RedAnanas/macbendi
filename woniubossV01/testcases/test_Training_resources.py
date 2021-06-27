#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/23 14:49
# software: PyCharm
import os
import unittest

from woniubossV01.common.public_port import WoniuBoss # 调用接口公共方法
from woniubossV01.common.Utility import * # 调用读取execl方法

class Trainning_resourses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 初始化WoniuBoss()
        cls.start = WoniuBoss()
        # 调用登录的方法
        cls.start.post_login_method()
        # 调用解密的方法
        cls.start.decode_method()
        # 读取execl数据
        # file_path = 'F:\PycharmProjects\Script\woniuboss\data\培训资源-接口文档.xlsx'
        file_path = os.path.abspath('../data/TestData1.xlsx')
        index = 1
        cls.sheet = Read_File().read_excel(file_path, index)
        # print(cls.sheet)

    # 测试培训资源查询  OK
    def test_Trainning_resourses_query(self):
        errors01 = []
        for i in range(1, 4):## sheet.nrows
            row = self.sheet.row_values(i)  ## 每一行的值
            url = row[2]
            method = row[3].lower()  ## lower转换成小写
            # print(row[0]) ## 第一列的值
            # 字符串转换成字典。
            if row[4] == '':
                data = None
            else:
                data = Read_File().dispose_params1(row[4])
            try:
                # 判断是get还是post方法,同时完成HTTP请求
                resp = self.start.judge_method(method, url, data, headers=None)
                # print(resp.status_code, resp.text)
                self.assertEqual(200, resp.status_code)
                # 对响应进行断言
                # print(type(resp.json()['totalRow']))
                # print(data['cusInfo'])
                if data['cusInfo']=='郝保成':## 用例1
                    self.assertEqual(2,resp.json()['totalRow'])  # 期望值正确：1
                elif data['cusInfo']=='吴帆':## 用例2
                    self.assertEqual(0,resp.json()['totalRow'])
                else:## 用例3
                    self.assertEqual(18,resp.json()['totalRow']) ##OK
            except Exception as e:
                # 记录所有异常
                errors01.append(str(e).split('\n')[0])
                # print(errors01)
        if errors01 != []:
            raise AssertionError(errors01)
        else:
            pass

    # 正确参数-新增   OK
    def test_Trainning_resourses_add(self):
        row = self.sheet.row_values(4)  ## 每一行的值
        url = row[2]
        method = row[3].lower()  ## lower转换成小写
        # 字符串转换成字典。
        if row[4] == '':
            data = None
        else:
            data = Read_File().dispose_params1(row[4])
        # print(url, method,data)
        # 判断是get还是post方法,同时完成HTTP请求
        resp = self.start.judge_method(method, url, data, headers=None)
        # print(resp.status_code, resp.text)
        self.assertEqual(200, resp.status_code)
        # 对响应进行断言
        self.assertEqual('该资源现属于测试账号名下,已更新该资源的信息.',resp.text)

    # 废弃功能  OK
    def test_Trainning_resourses_throw(self):
        row = self.sheet.row_values(5)  ## 每一行的值
        url = row[2]
        method = row[3].lower()  ## lower转换成小写
        # 字符串转换成字典。
        if row[4] == '':
            data = None
        else:
            data = Read_File().dispose_params1(row[4])
        # print(url, method,data)
        # 判断是get还是post方法,同时完成HTTP请求
        resp = self.start.judge_method(method, url, data, headers=None)
        # print(resp.status_code, resp.text)
        self.assertEqual(200, resp.status_code)
        # 对响应进行断言
        self.assertEqual('废弃资源完成.',resp.text)

    # 正确参数-修改   OK
    def test_Trainning_resourses_change(self):
        row = self.sheet.row_values(6)  ## 每一行的值
        url = row[2]
        method = row[3].lower()  ## lower转换成小写
        # 字符串转换成字典。
        if row[4] == '':
            data = None
        else:
            data = Read_File().dispose_params1(row[4])
        # print(url, method,data)
        # 判断是get还是post方法,同时完成HTTP请求
        resp = self.start.judge_method(method, url, data, headers=None)
        # print(resp.status_code, resp.text)
        self.assertEqual(200, resp.status_code)
        # 对响应进行断言
        self.assertEqual('修改成功.',resp.text)
    #
    #   公共资源池-最后废弃人-查询
    def test_Trainning_resourses_public(self):
        errors02 = []
        for i in range(7, 9):## sheet.nrows
            row = self.sheet.row_values(i)  ## 每一行的值
            url = row[2]
            method = row[3].lower()  ## lower转换成小写
            # print(row[0]) ## 第一列的值
            # 字符串转换成字典。
            if row[4] == '':
                data = None
            else:
                data = Read_File().dispose_params1(row[4])
            # print(data)
            try:
                # 判断是get还是post方法,同时完成HTTP请求
                resp = self.start.judge_method(method, url, data, headers=None)
                # print(resp.status_code, resp.text)
                self.assertEqual(200, resp.status_code)
                # 对响应进行断言
                if data['cusInfo']=='':
                    self.assertEqual(resp.json()['totalRow'],1)
                elif data['cusInfo']=='何来':
                    self.assertEqual(resp.json()['totalRow'], 0)
            except Exception as e:
                errors02.append(str(e))
        if errors02 != []:
            raise AssertionError(errors02)
        else:
            pass
    # 转交责任人-咨询师-查询    OK
    def test_Trainning_resourses_givePeople(self):
        row = self.sheet.row_values(9)  ## 每一行的值
        url = row[2]
        method = row[3].lower()  ## lower转换成小写
        # 字符串转换成字典。
        if row[4] == '':
            data = None
        else:
            data = Read_File().dispose_params1(row[4])
        # print(url, method,data)
        # 判断是get还是post方法,同时完成HTTP请求
        resp = self.start.judge_method(method, url, data, headers=None)
        # print(resp.status_code, resp.text)
        self.assertEqual(200, resp.status_code)
        # 对响应进行断言
        self.assertEqual(resp.json()['totalRow'],19)

if __name__=='__main__':
    unittest.main()