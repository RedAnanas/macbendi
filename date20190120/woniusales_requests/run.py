#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/20 19:51
# software: PyCharm

import time
from HTMLTestRunner import HTMLTestRunner
from date20190120.woniusales_requests.Test_case import Test_case
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    testCases01 =unittest.TestLoader().loadTestsFromTestCase(Test_case)
    suite.addTests(testCases01)

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + 'report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'执行情况')
    runner.run(suite)
    fp.close()




