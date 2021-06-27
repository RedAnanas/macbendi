#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/8 14:32
# software: PyCharm
import uiautomation,os,time

os.system("start /b notepad.exe")
notepad=uiautomation.WindowControl(searchDepth=1,ClassName="Notepad")
#窗口最前
notepad.SetTopmost(True)
#窗口放屏幕中心
notepad.MoveCursor()
#最大化
#notepad.Maximize()
#定位鼠标焦点
edit=notepad.EditControl(ClassName="Edit",AutomationId="15")
#SetValue光标在开始位置，重复执行覆盖
edit.SetValue("我爱吃西瓜，")
edit.SetValue("我爱吃菠萝。")
notepad.SetActive(1)
#SendKeys光标在尾部，重复执行追加
edit.SendKeys("我还爱吃橙子，")
edit.SendKeys("我更爱吃柚子，")
#组合键
#uiautomation.Win32API.SendKeys("{ctrl}s")
#获取菜单项
notepad.MenuItemControl(Name="文件(F)").Click()
for i in range(3):
    # uiautomation.Win32API.KeyDown(uiautomation.Keys.VK_DOWN)
    uiautomation.Win32API.SendKey(uiautomation.Keys.VK_DOWN)
    time.sleep(1)

uiautomation.Win32API.SendKey(uiautomation.Keys.VK_ENTER)
notepad.EditControl(AutomationId="1001").SendKeys("D:\\test.txt")
notepad.ButtonControl(Name="保存(S)").SendKey(uiautomation.Keys.VK_ENTER)
try:
    notepad.ButtonControl(Name="是(Y)").SendKey(uiautomation.Keys.VK_ENTER)
except:
    pass
notepad.Close().Key

