#! /usr/bin/env python
# coding = utf-8
# editor:wang

import unittest,os
from HTMLTestRunner import HTMLTestRunner


# dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = dir_path+'\\testcases'
# suite = unittest.defaultTestLoader.discover(start_dir=path,pattern='test*.py')
# with open('../report/test1.html','w+',encoding='utf8') as f:
#     runner = HTMLTestRunner(stream=f,verbosity=2,title='test discover')
#     runner.run(suite)

dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = dir_path + '\\test_GUI_cases'
suite = unittest.defaultTestLoader.discover(start_dir=path, pattern='test*.py')
with open('../report/GUI_report.html', 'wb+') as f:
    runner = HTMLTestRunner(stream=f, verbosity=2, title='test discover')
    runner.run(suite)