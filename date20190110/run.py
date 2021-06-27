#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 13:50
# software: PyCharm
import os

path=os.path.abspath("")
filelist=os.listdir(r"%s\test01"%path)
for file in filelist:
    if (not file.startswith("__init__"))and file.endswith("py"):
        print(file)
        os.system("Python %s\\test01\\%s 1 >>log.txt 2>&1"%(path,file))