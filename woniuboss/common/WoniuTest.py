#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/20 14:54
# software: PyCharm
from woniuboss1.common.Utility import Read_File
import unittest
from woniuboss1.common.login import public_Login
class WoniuBossTest(unittest.TestCase):
        # 获取读文件类的对象，并且把文件对象赋值给一个变量，通过次变量来访问读文件类当中的方法
    #测试过程中先执行这个方法，因所有的测试用例都来源于excel表中，所以不管测试那个模块首先要获取excel表的对象
    def setUp(self):
        self.readfile=Read_File()
        self.sheet=self.readfile.read_excel(file_path='')
    # def test_login(self):
    #     start_rows=0
    #     end_rows=0
    #     #从指定行循环读取数据，
    #     for i in range(start_rows-1,end_rows):
    #         #获取到的指定行的数据，并且是以列表形式的数据来显示
    #         list_data=self.sheet.row_values(i)
    #         parameters=list_data[]
    #         login_test_data=self.readfile.dispose_params(parameters)
    #         #下面是获取字典中用户名，密码，验证码key值所对应的value值
    #         username=login_test_data['username']
    #         password=login_test_data['password']
    #         verifycode=login_test_data['verifycode']
    #         try:
    #             login=Login("wf")
    #             login.dologin(username,password,verifycode)
    #             login.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button').click()
    #             con=login.wd.find_element_by_link_text('密码修改').text
    #             self.assertEqual('密码修改',con)
    #         except Exception as e:
    #             raise print("用户名:%s,密码:%s,验证码:%s输入错误"%(username,password,verifycode),e)
    #         login.wd.close()
    def test_login(self):
        start_rows=0
        end_rows=0
        #从指定行循环读取数据，
        for i in range(start_rows-1,end_rows):
            #获取到的指定行的数据，并且是以列表形式的数据来显示
            list_data=self.sheet.row_values(i)
            parameters=list_data[]
            login_test_data=self.readfile.dispose_params(parameters)
            #下面是获取字典中用户名，密码，验证码key值所对应的value值
            username=login_test_data['username']
            password=login_test_data['password']
            verifycode=login_test_data['verifycode']
            try:
                # login=Login("wf")
                login=public_Login()
                login.open_url()
                login.dologin(username,password,verifycode)
                login.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button').click()
                con=login.driver.find_element_by_link_text('密码修改').text
                self.assertEqual('密码修改',con)
            except Exception as e:
                raise print("用户名:%s,密码:%s,验证码:%s输入错误"%(username,password,verifycode),e)
            login.driver.close()

               







