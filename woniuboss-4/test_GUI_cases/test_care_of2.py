#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/27 20:45
# software: PyCharm
import unittest,time,os
from common.login import public_Login
from common.Utility import Read_File

class care_of1(unittest.TestCase):
    def setUp(self):
        self.driver=public_Login()
        # 打开浏览器
        self.driver.open_url()
        # 管理员登陆
        self.driver.admin_login()
        # 解密
        self.driver.driver.find_element_by_id("btn-decrypt").click()
        self.driver.driver.find_element_by_xpath("//*[@id='secondPass-modal']/div/div/div[2]/input").send_keys("woniu123")
        self.driver.driver.find_element_by_xpath("//*[@id='secondPass-modal']/div/div/div[3]/button").click()
        # self.driver.driver.switch_to.alert.send_keys("woniu123")
        # self.driver.driver.switch_to.alert.accept()
        time.sleep(2)
        # 转到转交责任人模块
        self.driver.driver.find_element_by_link_text("转交责任人").click()
        time.sleep(2)
    def tearDown(self):
        # 注销并关闭浏览器
        self.driver.login_out()
    # 姓名查询
    def test_inquire1(self):
        errors = []
        try:
            self.driver.driver.find_element_by_xpath("//input[@placeholder='请输入姓名或电话或qq']").send_keys("伍彩霞")
            self.driver.driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/button").click()
            name=self.driver.driver.find_element_by_xpath("//*[@id='transmit-table']/tbody/tr/td[2]").text
            self.assertEqual(name,"伍彩霞")
            time.sleep(1)
        except Exception as e:
            errors.append('错误原因%s'%(str(e).split('\n')[0]))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass

    # 下拉框查询
    def test_inquire2(self):
        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = "%s/GUI_data/care_of.xlsx" % dir_path
        index = 0
        sheet = Read_File().read_excel(file_path, index)
        errors = []
        try:
            for i in range(1,sheet.nrows):
                row=sheet.row_values(i)
                number=row[0]
                counselor=row[1]
                area=row[2]
                condition=row[3]
                source=row[4]
                self.driver.driver.find_element_by_name("empName").send_keys(counselor)
                self.driver.driver.find_element_by_id("empNameSelect1").send_keys(area)
                self.driver.driver.find_element_by_id("regionSelect1").send_keys(condition)
                self.driver.driver.find_element_by_name("last_status").send_keys(source)
                self.driver.driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/button").click()
                name = self.driver.driver.find_element_by_xpath("//*[@id='transmit-table']/thead/tr/th[2]/div[1]").text
                self.assertEqual(name,"姓名")
                time.sleep(1)
        except Exception as e:
            errors.append('%s错误原因：%s'%((number),(str(e).split('\n')[0])))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass

    # 查看简历
    def test_inquire3(self):
        errors = []
        try:
            self.driver.driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/button").click()
            self.driver.driver.find_element_by_xpath("//*[@id='transmit-table']/tbody/tr[1]/td[13]/button").click()
            time.sleep(2)
            title=self.driver.driver.find_element_by_xpath("//*[@id='resumeDetails']/div/form/div/div[1]/h4").text
            self.driver.driver.find_element_by_xpath("//*[@id='resumeDetails']/div/form/div/div[1]/button/span[1]").click()
            self.assertEqual(title,"查看简历")
            time.sleep(1)
        except Exception as e:
            errors.append('错误原因%s'%(str(e).split('\n')[0]))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass
    # 提交功能
    def test_inquire4(self):
        errors = []
        try:
            self.driver.driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/button").click()
            self.driver.driver.find_element_by_xpath("//*[@id='transmit-table']/tbody/tr[9]/td[1]/input").click()
            time.sleep(2)
            self.driver.driver.find_element_by_id("empNameSelect2").send_keys("郑雪娇")
            self.driver.driver.find_element_by_id("Submit").click()
            time.sleep(2)
            self.driver.driver.find_element_by_xpath("//*[@class='modal-footer']/button[2]").click()
            time.sleep(2)
            hint=self.driver.driver.find_element_by_xpath("/html/body/div[9]/div/div/div[2]/div").text
            time.sleep(2)
            self.assertEqual(hint, "转交资源完成.")
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