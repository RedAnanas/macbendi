#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 21:01
# software: PyCharm
import os,glob

path=os.path.join(os.getcwd(),"testcase")
file_list=glob.glob("%s/*.py"%path)
for file in file_list:
    os.system("Python %s 1>>log2.txt 2>&1"%file)