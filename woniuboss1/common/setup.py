#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/19 15:44
# software: PyCharm
import os
from selenium import webdriver
class setup:
    def __init__(self,hostname):
        self.hostname=hostname
        webdrive=webdriver.Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe",
                               executable_path="C:\python3.6\Scripts\geckodriver.exe")
        webdrive.get("http://%s:8080"%(self.hostname))
        self.wbdriver=webdrive