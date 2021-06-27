#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/19 16:08
# software: PyCharm
from selenium import  webdriver
from woniuboss1.common.setup import setup
import time
import requests
class public_Login:

    def __init__(self):
        self.driver=webdriver.Firefox()
        self.session=requests.session()
    #此方法是实现打开url地址
    def open_url(self):
        self.driver.get("http://wf:8080/WoniuBoss2.0/")
        self.driver.implicitly_wait(2)

    def other_same_login(self):
        self.driver.find_element_by_name('userPass').clear()
        self.driver.find_element_by_name('userPass').send_keys('woniu123')
        time.sleep(3)
        self.driver.find_element_by_name('checkcode').clear()
        self.driver.find_element_by_name('checkcode').send_keys('0000')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button').click()
    #使用管理员账号登录系统
    def admin_login(self):
        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys('WNCD000')
        self.other_same_login()
    #使用总经理账号登录系统
    def main_manager(self):
        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys('WNCD001')
        self.other_same_login()
    #使用副总经理登录系统
    def second_manager(self):
        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys('WNCD001')
        self.other_same_login()
    #使用咨询主管登录系统
    def question_manager(self):
        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys('WNCD001')
        self.other_same_login()
    #使用咨询师登录系统
    def teach_manager(self):
        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys('WNCD001')
        self.other_same_login()

    # def __init__(self,hostnam):
    #     self.hostname=hostnam
    #     self.su=setup(hostname=self.hostname)
    #     self.wd=self.su.wbdriver
    # def dologin(self,username,password):
    #     wd=self.wd
    #     wd.find_element_by_name('userName').clear()
    #     wd.find_element_by_name('userName').send_keys(username)
    #     wd.find_element_by_name('userPass').clear()
    #     wd.find_element_by_name('userPass').send_keys(password)
    #     wd.find_elements_by_name('checkcode').clear()
    #     wd.find_element_by_name('checkcode').send_keys(verifycode)
    def dologin(self,username,password,verifycode):

        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys(username)
        self.driver.find_element_by_name('userPass').clear()
        self.driver.find_element_by_name('userPass').send_keys(password)
        self.driver.find_elements_by_name('checkcode').clear()
        self.driver.find_element_by_name('checkcode').send_keys(verifycode)
    #点击登出按钮，登出系统同时关闭浏览器窗口
    def login_out(self):
        self.driver.find_element_by_link_text("注销").click()
        self.driver.close()
    # def get_method(self,url):
    #     resp=self.session.get(url=url)
    #     return resp
    # def post_method(self):











