#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/3/1 18:47
# software: PyCharm

from selenium import webdriver
import time,xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Login:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://106.13.36.122:8080/WoniuBoss2.5/')

    def login_admin(self,name):
        self.driver.find_element_by_name('userName').clear()
        self.driver.find_element_by_name('userName').send_keys(name)
        self.same_login()


    def same_login(self):
        self.driver.find_element_by_name('userPass').clear()
        self.driver.find_element_by_name('userPass').send_keys('woniu123')
        self.driver.find_element_by_name('checkcode').clear()
        self.driver.find_element_by_name('checkcode').send_keys('0000')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button').click()
        time.sleep(2)

    def decode_method(self):  # 解密方法
        self.click_method(By.XPATH,'//*[@id="btn-decrypt"]')
        try:
            self.driver.switch_to.alert.send_keys('woniu123')
            self.driver.switch_to.alert.accept()
        except:
            self.input_method(By.NAME, 'secondPass', "woniu123")
            time.sleep(1)
            self.click_method(By.XPATH, '//div[3]/button')

    def click_method(self,method,element):  #点击
        self.driver.find_element(method,element).click()

    def input_method(self,method,element,value): #输入
        put = self.driver.find_element(method,element)
        put.clear()
        put.send_keys(value)

    def select_method(self,method,element,value):  #下拉框
        obj = self.driver.find_element(method,element)
        Select(obj).select_by_visible_text(value)

    def text(self,element): #获取页面文本信息
        text = self.driver.find_element_by_xpath(element).text
        return text

    def alert_method(self): #弹窗确定
        try:
            self.driver.switch_to.alert.accept()
        except:
            self.click_method(By.XPATH,'/html/body/div[18]/div/div/div[3]/button[2]')
            time.sleep(1)
            self.click_method(By.XPATH,'/html/body/div[18]/div/div/div[3]/button')

    def alert_text(self): #弹窗文本内容
        try:
            text = self.driver.switch_to.alert.text
        except:
            text = self.driver.find_element_by_xpath('/html/body/div[18]/div/div/div[2]/div').text
        return text

    def read_excel(self,file_path,index=0): #读取Excel表格
        data = xlrd.open_workbook(file_path)
        sheet = data.sheets()[index]
        return sheet

    def dispose_params(self,parameters):
        lines = parameters.strip().split('\n')
        params = {}
        for line in lines:
            key, value = line.strip().split('=')
            params[key] = value
        return params

    def close(self):
        self.driver.quit()


