#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/3/12 11:00
# software: PyCharm

from appium import webdriver
import time,os

class app:
    # def __init__(self):
    #     pass

    def start_test(self):
        desired_caps={
                      "platformVersion": "8.0.0",
                      "appPackage": "com.mobivans.onestrokecharge",
                      "deviceName": "854430ab",
                      "platformName": "Android",
                      "appActivity": "com.stub.stub01.Stub01"
                    }
        url="http://127.0.0.1:4723/wd/hub"
        driver=webdriver.Remote(url,desired_caps)
        driver.implicitly_wait(60)
        time.sleep(5)
        # driver.find_element_by_android_uiautomator("text('记一笔')").click()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.View").click()
        time.sleep(2)
        driver.quit()

if __name__ == '__main__':
    app().start_test()