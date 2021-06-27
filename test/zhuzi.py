#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:ananas
# datetime:2019/6/19 20:14
# software: PyCharm
import datetime
import pyautogui
import time
import random

def time_timer(now_time):
    next_time = datetime.datetime.strptime("2019-6-21 0:00:00", "%Y-%m-%d %H:%M:%S")
    timer_start_time = (next_time - now_time).total_seconds()
    return timer_start_time

def pyautogui_dnf(now_time):
    #主体：打开养竹活动界面，领取竹子，退出界面
    print("开始执行,当前系统时间: %s" % now_time)
    #坐标1：点击竹子的小图标
    pyautogui.click(913, 831)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(5)
    # 坐标2：点击领取按钮
    pyautogui.click(910, 752)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    # 坐标3：点击关闭按钮关闭活动界面
    pyautogui.click(1282, 158)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    c = random.randint(600,1200)
    print("执行完毕，开始休眠，%s"%(datetime.timedelta(seconds=c)))
    time.sleep(c)

def tomrrow_Refresh(now_time):
    #点击公告下的确定按钮
    pyautogui.click(944, 713)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    print("已关闭公告，继续执行")
    time.sleep(5)
    #死循环继续执行领竹子的脚本
    while True:
        pyautogui_dnf(now_time)

def main_pyauto():
    while True:
        now_time = datetime.datetime.now()
        d = time_timer(now_time)
        if d > 0:
            print("距离公告弹窗时间还有%s秒" % (int(d)))
            pyautogui_dnf(now_time)
        else:
            print("关闭公告")
            tomrrow_Refresh(now_time)

if __name__ == "__main__":
    main_pyauto()