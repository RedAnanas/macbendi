#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/28 17:22
# software: PyCharm
import HTMLTestRunner
import unittest
import time

from common.Utility import Read_File
from common.login import public_Login
from selenium.webdriver.support.select import Select

class TestResource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       cls.publiclogin=public_Login()
       cls.publiclogin.open_url()
       cls.publiclogin.diff_account('WNCD000')

       time.sleep(2)
       cls.publiclogin.driver.find_element_by_xpath("//button[@id='btn-decrypt']").click()
       try:
           alert=cls.publiclogin.driver.switch_to.alert
           alert.send_keys('woniu123')
           time.sleep(2)
           alert.accept()
       except:
           cls.publiclogin.driver.find_element_by_xpath("//input[@name='secondPass']").send_keys('woniu123')
           cls.publiclogin.driver.find_element_by_xpath("//button[@class='btn btn-info']").click()

    def test_public_resource5(self):
        sheet=Read_File().read_excel('../GUI_data/automation.xlsx',index=2)
        list=sheet.row_values(8)
        print(list)
        number=list[0]
        location=list[2]
        parameter=list[3]
        #exception=list[4]
        locat=location.split("\n") #分割定位元素
        print(locat[0])
        print(locat[1])
        #exce=exception.split("\n")
        #excep=exce[1]+" "+exce[2]
        print(locat)
        param=Read_File().dispose_params1(parameter)#分割参数
        self.publiclogin.driver.find_element_by_xpath("//a[@href='public']").click()
        time.sleep(3)
        # #self.publiclogin.driver.find_element_by_xpath("//select[@name='empName']/option[2]").click()
        Select(self.publiclogin.driver.find_element_by_xpath("//select[@name='empName']")).select_by_visible_text(param['name'])
        Select(self.publiclogin.driver.find_element_by_xpath("//select[@name='last_status']")).select_by_visible_text(param['status'])
        Select(self.publiclogin.driver.find_element_by_xpath("//select[@name='source']")).select_by_visible_text(param['source'])
        time.sleep(2)
        try:
            name=self.publiclogin.driver.find_element_by_xpath("//tbody/tr[@data-index='0']/td[3]").text
            #实现选中第一个资源和点击认领按钮
            for i in range(0,2):
                self.publiclogin.driver.find_element_by_xpath(locat[i]).click()
            try:
                time.sleep(2)
                alert=self.publiclogin.driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                alert.accept()
                time.sleep(2)
            except:
                self.publiclogin.driver.find_element_by_xpath("//button[@data-bb-handler='confirm']").click()
                time.sleep(1)
                self.publiclogin.driver.find_element_by_xpath("//button[@data-bb-handler='ok']").click()
                time.sleep(1)
            #获取认领之后的第一个资源
            try:
                name1=self.publiclogin.driver.find_element_by_xpath("//tbody/tr[@data-index='0']/td[3]").text
                self.assertNotEqual(name,name1)
            except Exception as e:
                #print(e)
                str='认领失败，失败信息是%s'%(e)
                raise AssertionError(str)
                #self.publiclogin.driver.find_element_by_xpath(locat[1]).click()
        except Exception as e:
            str="测试失败，无相关资源信息，错误是%s"%(e)
            print(str)
    def test_public_resource2(self):
        sheet = Read_File().read_excel('../GUI_data/automation.xlsx',index=2)
        error=[]
        for i in range(1,8):
            list = sheet.row_values(i)
            list1=sheet.row_values(9)
            location1=list1[2]
            locat1=location1.split("\n")
            number = list[0]
            location = list[2]
            parameter = list[3]
            exception = list[4]
            locat = location.split("\n")  # 分割定位元素
            exce = exception.split("\n")
            param = Read_File().dispose_params1(parameter)  # 分割参数
            self.publiclogin.driver.find_element_by_xpath(locat1[0]).click()
            time.sleep(3)
            for i in range(0,3):
                if i==0:
                    Select(self.publiclogin.driver.find_element_by_xpath(locat[i])).select_by_visible_text(param['name'])
                elif i==1:
                    Select(self.publiclogin.driver.find_element_by_xpath(locat[i])).select_by_visible_text(param['status'])
                elif i==2:
                    Select(self.publiclogin.driver.find_element_by_xpath(locat[i])).select_by_visible_text(param['source'])
            time.sleep(2)
            # if self.publiclogin.driver.find_element_by_xpath("//tbody/tr[@class='no-records-found']").text == '无符合条件的记录':
            #     print('没有相关的资源，测试失败')
            try:
                name=self.publiclogin.driver.find_element_by_xpath("//input[@name='btSelectItem'][1]").text
                content = self.publiclogin.driver.find_element_by_xpath(locat1[1]).text
                try:
                    self.assertIn(exce[0],content)
                    self.assertIn(exce[1],content)
                    self.assertIn(exce[2],content)
                except Exception as e:
                    str="第%d条用例执行失败，失败信息是%s"%(number,e)
                    error.append(str)
            except Exception as e:
                str = "第%d条用例执行失败，没有资源，失败信息是%s" % (number, e)
                error.append(str)
        if error!=[]:
            raise AssertionError(error)
    @classmethod
    def tearDownClass(cls):
        pass
        # cls.publiclogin=public_Login()
        # cls.publiclogin.login_out()

if __name__ == '__main__':
    #unittest.main()
    if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestResource))
        with open('woniuboss2.5.html', 'w', encoding='utf8') as f:
            runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='report', verbosity=2)
            runner.run(suite)
