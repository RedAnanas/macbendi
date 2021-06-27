#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/10 19:42
# software: PyCharm

class Login:

    def __init__(self,browser_manager):
        self.bm=browser_manager

    def input_username(self,name):
        self.bm.input_text("username",name)

    def input_password(self,password):
        self.bm.input_text("password",password)

    def input_verification(self,verifycode):
        self.bm.input_text("verifycode",verifycode)

    def cilck_login(self):
        self.bm.driver.find_element_by_xpath("//form[@class='form-inline']/div[6]/button").click()

    def go_login(self,name,password,verifycode):
        self.input_username(name)
        self.input_password(password)
        self.input_verification(verifycode)
        self.cilck_login()

    def login(self):
        self.go_login("admin","admin","0000")
        return self.bm


