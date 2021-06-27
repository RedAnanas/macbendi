#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:ananas
# datetime:2019/7/2 22:47
# software: PyCharm
import time
import pyautogui

def one():
    time.sleep(5)
    pyautogui.click(x=401,y=810)
    print("111")
    pyautogui.click(clicks=2)

    print("成功")

if __name__ == '__main__':
    one()