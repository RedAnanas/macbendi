#! /usr/bin/env python
# coding = utf-8
# editor:wang

import unittest,os
from HTMLTestRunner import HTMLTestRunner
#
# suite = unittest.defaultTestLoader.discover(start_dir='../testcases',pattern='test*.py')
# with open('../report/testdiscover.html','wb+') as f:
#     runner = HTMLTestRunner(stream=f,verbosity=2,title='test discover')
#     runner.run(suite)
#
# print(os.getcwd())
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = dir_path+'\\testcases'
# print(path)
suite = unittest.defaultTestLoader.discover(start_dir=path,pattern='test*.py')
with open('../report/test1.html','wb') as f:
    runner = HTMLTestRunner(stream=f,verbosity=2,title='test discover')
    runner.run(suite)