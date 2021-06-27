#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/25 17:32
# software: PyCharm

import time
from HTMLTestRunner import HTMLTestRunner
import unittest
import os

# 测试用例存放路径
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
case_path = '%s/testcases/'%dir_path

# 获取所有测试用例
def get_allcase():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    return discover

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + 'report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'执行情况',verbosity=2)
    runner.run(get_allcase())
    fp.close