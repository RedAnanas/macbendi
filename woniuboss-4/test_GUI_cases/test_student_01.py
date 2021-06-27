#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/28 9:19
# software: PyCharm
import HTMLTestRunner
import unittest, requests,time
from common.login import public_Login
from selenium.webdriver.support.select import Select
from common.Utility import Read_File


class student(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.public_login = public_Login()
        cls.public_login.open_url()
        cls.public_login.diff_account("WNCD051")
        time.sleep(2)
        cls.public_login.driver.find_element_by_id('btn-decrypt').click()
        try:

            alert = cls.public_login.driver.switch_to_alert()
            alert.send_keys("woniu123")
            alert.accept()
        except:
            cls.public_login.driver.find_element_by_xpath("//input[@name='secondPass']").send_keys('woniu123')
            cls.public_login.driver.find_element_by_xpath("//button[@class='btn btn-info']").click()

    # def tearDownClass(cls):
    #
    #     cls.public_login.driver.login_out()

       #基本信息
    def test_01(self):
        errors = []
        try:
            self.public_login.driver.find_element_by_xpath('//a[@href="student"]').click()
            time.sleep(2)
            self.public_login.driver.find_element_by_xpath('//select[@name="stuClass"]/option[1]').click()
            self.public_login.driver.find_element_by_xpath('//select[@name="orientation"]/option[1]').click()
            self.public_login.driver.find_element_by_xpath('//input[@name="stuName"]').send_keys("陈怡")

            self.public_login.driver.find_element_by_xpath('//input[@name="stuNo"]').send_keys("WNCD201805012")
            self.public_login.driver.find_element_by_xpath('// *[ @ id = "stuInfo"] / div[2] / button').click()
            content = self.public_login.driver.find_element_by_xpath('// *[ @ id = "stuInfo_table"] / tbody / tr[1] / td[1]').text
            self.assertEqual(content,'陈怡')
        except Exception as e:
            errors.append('错误原因%s' % (str(e).split('\n')[0]))
            if errors != None:
                raise AssertionError(errors)
            else:
                pass




        #今日考勤
    def test_02(self):

            self.public_login.driver.find_element_by_xpath('//a[@href="student"]').click()
            time.sleep(2)
            self.public_login.driver.find_element_by_link_text("今日考勤").click()
            try:
                self.public_login.driver.find_element_by_name("btSelectAll").click()
                self.public_login.driver.find_element_by_xpath('// *[ @ id = "atten"] / div[1] / button').click()
                content = self.public_login.driver.switch_to_alert().text
                # print(content)
                self.public_login.driver.switch_to_alert().accept()
                self.assertEqual(content, '考勤完毕.')
            except:
                self.public_login.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div[2]/div[1]/button[2]').click()
                self.public_login.driver.find_element_by_xpath('/ html / body / div[18] / div / div / div[3] / button[2]').click()
                #self.public_login.driver.find_element_by_xpath('/html/body/div[18]/div/div/div[3]/button"]').click()
                self.public_login.driver.switch_to_alert().accept()
                content = self.public_login.driver.switch_to_alert().text
                #content = self.public_login.driver.find_element_by_xpath('/html/body/div[18]/div/div/div[2]/div').text
                print(content)
                # content = self.public_login.driver.switch_to_alert().text
                # # print(content)
                # self.public_login.driver.switch_to_alert().accept()
                self.assertEqual(content, '考勤完毕.')








        #今日晨考
    def test_03(self):
        errors = []
        try:
            self.public_login.driver.find_element_by_xpath('//a[@href="student"]').click()
            time.sleep(2)
            self.public_login.driver.find_element_by_xpath('//a[@href="#mornExam"]').click()
            self.public_login.driver.find_element_by_xpath(
                '// *[ @ id = "mornExam-table"] / tbody / tr[1] / td[8] / button').click()

            self.public_login.driver.find_element_by_xpath(
                '/ html / body / div[11] / div / div / div[2] / form / div / div[2] / input'). \
                send_keys('90')
            self.public_login.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/form/div/div[3]/textarea') \
                .send_keys('高级语言的翻译方式？')
            self.public_login.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button').click()
        except Exception as e:
            errors.append('错误原因%s' % (str(e).split('\n')[0]))
            if errors != None:
                raise AssertionError(errors)
            else:
                pass







        #学员请假
    def test_04(self):
        errors = []
        try:
            self.public_login.driver.find_element_by_xpath('//a[@href="student"]').click()
            time.sleep(2)

            self.public_login.driver.find_element_by_xpath(
                '// *[ @ id = "content"] / div[2] / div / ul / li[4] / a').click()
            self.public_login.driver.find_element_by_xpath('//select[@name="leave_status"]/option[1]').click()
            time.sleep(2)
            self.public_login.driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div'
                                                           '/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[12]/button[2]').click()  # 定位修改
            conbox = self.public_login.driver.find_element_by_xpath(
                '/html/body/div[13]/div/div/div[2]/form/div[3]/div/select')
            Select(conbox).select_by_visible_text('许敏')
            self.public_login.driver.find_element_by_xpath('/html/body/div[13]/div/div/div[3]/button').click()
        except Exception as e:
            errors.append('错误原因%s'%(str(e).split('\n')[0]))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass

        #晨考记录
    def test_05(self):
        errors = []
        try:
            self.public_login.driver.find_element_by_xpath('//a[@href="student"]').click()
            time.sleep(2)
            self.public_login.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul/li[5]/a').click()
            self.public_login.driver.find_element_by_xpath('//*[@id="morningexam"]/div[1]/select[1]/option[1]').click()
            time.sleep(2)
            self.public_login.driver.find_element_by_xpath('//*[@id="morningexam"]/div[1]/select[2]/option[1]').click()
            self.public_login.driver.find_element_by_xpath('//input[@name="stu_name"]').send_keys("陈怡")
            self.public_login.driver.find_element_by_xpath(
                '/html/body/div[6]/div[3]/div/div/div[8]/div[2]/button').click()
        except Exception as e:
            errors.append('错误原因%s'%(str(e).split('\n')[0]))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass





if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(student))
    # with open('test_report.html', 'wb+') as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='report', verbosity=2)
    #     runner.run(suite)
