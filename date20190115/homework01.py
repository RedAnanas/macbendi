#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/15 20:21
# software: PyCharm
import unittest
import time
from selenium import webdriver

class TestWoniusales(unittest.TestCase):
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://admin:8080/WoniuSales1.4/')
        cls.driver.implicitly_wait(20)
        cls.driver.set_page_load_timeout(20)
        time.sleep(1)

    def tearDown(cls):
        cls.driver.quit()

    def test_logn1(self):
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_id("verifycode").send_keys("0000")
        self.driver.find_element_by_class_name("form-control.btn-primary").click()
        result=self.driver.find_element_by_link_text("注销").text
        self.assertEquals(result,"注销")


    def test_logn2(self):
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin123")
        self.driver.find_element_by_id("verifycode").send_keys("0000")
        self.driver.find_element_by_class_name("form-control.btn-primary").click()
        result = self.driver.find_element_by_class_name("bootbox-body").text
        self.assertEquals(result, "登录失败，请重新登录.")






