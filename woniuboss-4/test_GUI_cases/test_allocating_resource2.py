#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/3/1 9:36
# software: PyCharm

import unittest,time
from common.login import public_Login
class care_of(unittest.TestCase):
    def setUp(self):
        self.driver=public_Login()
        # 打开浏览器
        self.driver.open_url()
        # 咨询主管登陆
        self.driver.question_manager()
        # 解密
        self.driver.driver.find_element_by_id("btn-decrypt").click()
        self.driver.driver.find_element_by_xpath("//*[@id='secondPass-modal']/div/div/div[2]/input").send_keys("woniu123")
        self.driver.driver.find_element_by_xpath("//*[@id='secondPass-modal']/div/div/div[3]/button").click()
        time.sleep(2)
        # 转到分配资源模块
        self.driver.driver.find_element_by_link_text("分配资源").click()
        time.sleep(2)
    def tearDown(self):
        # 注销并关闭浏览器
        self.driver.login_out()
    # 按比例分配
    def test_operation1(self):
        errors = []
        try:
            self.driver.driver.find_element_by_xpath("//*[@id='content']/div[2]/div[4]/button[2]").click()
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[1]/td[3]/input").clear()
            time.sleep(2)
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[1]/td[3]/input").send_keys("1%")
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[2]/td[3]/input").clear()
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[2]/td[3]/input").send_keys("1%")
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[3]/td[3]/input").clear()
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[3]/td[3]/input").send_keys("1%")
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[4]/td[3]/input").clear()
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[4]/td[3]/input").send_keys("1%")
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[5]/td[3]/input").clear()
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[5]/td[3]/input").send_keys("1%")
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[6]/td[3]/input").clear()
            self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[6]/td[3]/input").send_keys("1%")
            # self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[7]/td[3]/input").clear()
            # self.driver.driver.find_element_by_xpath("//*[@id='proportion_num']/tr[7]/td[3]/input").send_keys("3%")
            time.sleep(2)
            self.driver.driver.find_element_by_id("proportion_submit").click()
            self.driver.driver.find_element_by_xpath("/html/body/div[10]/div/div/div[3]/button[2]").click()
            # self.driver.driver.find_element_by_xpath("/html/body/div[9]/div/div/div[3]/button").click()

            time.sleep(2)
            hint = self.driver.driver.find_element_by_class_name("bootbox-body").text
            time.sleep(2)
            self.assertEqual(hint, "分配完成.")
            self.driver.driver.find_element_by_xpath("/html/body/div[9]/div/div/div[3]/button").click()
            time.sleep(2)
        except Exception as e:
            errors.append('错误原因%s'%(str(e).split('\n')[0]))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass
    # 单独分配
    def test_operation2(self):
        errors = []
        try:
            self.driver.driver.find_element_by_xpath("//*[@id='allot-table']/tbody/tr[1]/td[1]/input").click()
            time.sleep(1)
            self.driver.driver.find_element_by_id("empNameSelect").send_keys("刘雪梅")
            time.sleep(1)
            self.driver.driver.find_element_by_id("Submit").click()
            self.driver.driver.find_element_by_xpath("/html/body/div[9]/div/div/div[3]/button[2]").click()

            time.sleep(2)
            hint = self.driver.driver.find_element_by_class_name("bootbox-body").text
            time.sleep(2)
            self.assertEqual(hint, "分配完成.")
            self.driver.driver.find_element_by_xpath("/html/body/div[9]/div/div/div[3]/button").click()
            time.sleep(2)
        except Exception as e:
            errors.append('错误原因%s'%(str(e).split('\n')[0]))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass
if __name__ == '__main__':
    unittest.TestSuite()