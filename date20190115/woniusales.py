#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/15 20:31
# software: PyCharm
import time
from date20190115.homework01 import TestWoniusales
from HTMLTestRunner import HTMLTestRunner
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    testCases01 =unittest.TestLoader().loadTestsFromTestCase(TestWoniusales)
    suite.addTests(testCases01)

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + 'report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'执行情况')
    runner.run(suite)
    fp.close()





















    # def __init__(self):
    #     self.driver=webdriver.Firefox()
    #     self.driver.get("http://admin:8080/WoniuSales1.4/")
    #     self.driver.implicitly_wait(20)
    #     self.driver.set_page_load_timeout(20)
    #
    # def input_text(self,id,value):
    #     inputText=self.driver.find_element_by_id(id)
    #     inputText.clear()
    #     inputText.send_keys(value)
    #
    # def close(self):
    #     self.driver.quit()
    #
    #
    # def username(self, name):
    #     self.input_text("username", name)
    #
    # def password(self, password):
    #     self.input_text("password", password)
    #
    # def verification(self, verifycode):
    #     self.input_text("verifycode", verifycode)
    #
    # def login(self):
    #     self.driver.find_element_by_xpath("//form[@class='form-inline']/div[6]/button").click()
    #
    # def result(self):
    #     return self.driver.find_element_by_link_text("注销").text
    #
    # def result1(self):
    #     return self.driver.find_element_by_class_name("bootbox-body").text







