#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/8 11:05
# software: PyCharm
import uiautomation
import os
import time
os.system("start /b calc.exe")
time.sleep(2)
calculator=uiautomation.WindowControl(searchDepth=1,Name="计算器")
calculator.SetActive(2)
calculator.ButtonControl(Name="5").Click()
calculator.ButtonControl(Name="5").Click()
calculator.ButtonControl(Name="加").Click()
calculator.ButtonControl(Name="7").Click()
calculator.ButtonControl(Name="5").Click()
calculator.ButtonControl(Name="等于").Click()
result=calculator.TextControl(AutomationId="158").Name
if result=="130":
    print("测试成功")
else:
    print("测试失败")
calculator.Close()
