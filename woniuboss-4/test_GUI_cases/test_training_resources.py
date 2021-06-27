#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/27 21:34
# software: PyCharm
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from common.login import public_Login
import unittest
import HTMLTestRunner
#####
class Training_resources(unittest.TestCase):

    def setUp(self):
        self.public=public_Login()
        self.public.open_url() # 打开首页
        self.public.admin_login() # 使用管理员进行登录
        # 解密
        self.public.driver.find_element_by_xpath('//*[@id="btn-decrypt"]').click()
        try:
            self.public.driver.switch_to.alert.send_keys('woniu123')
            time.sleep(1)
            self.public.driver.switch_to.alert.accept()
            time.sleep(3)
        except:
            self.public.driver.find_element_by_xpath('//*[@id="secondPass-modal"]/div/div/div[2]/input').send_keys(
                'woniu123')
            self.public.driver.find_element_by_xpath('//*[@id="secondPass-modal"]/div/div/div[3]/button').click()
            time.sleep(1)

    def tearDown(self):
        self.public.driver.quit()

    # 添加资源
    def test_add_resources(self):
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/button[1]').click()
        ## 电话号码
        self.public.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[1]/div[1]/input').send_keys('15564278744')
        ## 姓名
        self.public.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[1]/div[2]/input').send_keys('科比')
        ## 最新状态
        self.public.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[2]/div[1]/select').send_keys('新入库')
        ## 渠道来源
        self.public.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[5]/div[1]/select').send_keys('中华英才网')
        self.public.driver.find_element_by_xpath('// *[ @ id = "addCusBtn"]').click()
        time.sleep(2)
        try:
            self.public.driver.switch_to.alert.accept() ## 点击弹窗确认按钮
            time.sleep(2)
        except:
            self.public.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[3]/button').click()  ## 点击确认按钮
            time.sleep(2)
        resp=self.public.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody')
        # print(resp.text)# 打印所有的人员信息
        self.assertIn('15564278744',resp.text)

    # 废弃资源
    def test_throw_resources(self):
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/input[3]').send_keys('科比')
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/button').click()
        time.sleep(2)
        left_click=self.public.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody/tr/td[1]/input')
        time.sleep(2)
        ActionChains(self.public.driver).click(left_click).perform()
        time.sleep(2)
        self.public.driver.find_element_by_xpath('//*[@id="abandon"]').click()
        time.sleep(1)
        try:
            self.public.driver.switch_to.alert.accept()
            time.sleep(3)
        except:
            self.public.driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
            time.sleep(3)
        resp = self.public.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody')
        # print(resp.text)
        self.assertNotIn('15564278744', resp.text)
        self.claim_resources()

    # 认领回废弃资源
    def claim_resources(self):
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[4]/a').click()
        time.sleep(2)
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/input').send_keys('科比')
        time.sleep(1)
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/button').click()
        time.sleep(2)
        left_click = self.public.driver.find_element_by_xpath('//*[@id="public-pool-table"]/thead/tr/th[1]/div[1]')
        time.sleep(2)
        # 鼠标左击
        ActionChains(self.public.driver).click(left_click).perform()
        time.sleep(1)
        self.public.driver.find_element_by_xpath('//*[@id="ownCusBtn"]').click()  ###
        time.sleep(2)
        try:
            self.public.driver.switch_to.alert.accept()
            time.sleep(3)
            self.public.driver.switch_to.alert.accept()
            time.sleep(3)
        except:
            self.public.driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
            time.sleep(2)
            self.public.driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
            time.sleep(2)

    # 查询资源
    def test_query_resources(self):
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/input[3]').send_keys('科比')
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/button').click()
        time.sleep(1)
        resp = self.public.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody')
        # print(resp.text)
        self.assertIn('科比',resp.text)

    # 跟踪资源
    def test_track_resources(self):
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/input[3]').send_keys('科比')
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/button').click()
        time.sleep(2)
        self.public.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody/tr/td[15]/button[1]').click()
        self.public.driver.find_element_by_xpath('//*[@id="trackingCusLi"]/a').click()
        time.sleep(2)
        ## 本次状态
        self.public.driver.find_element_by_xpath('//*[@id="newStatus"]').send_keys('已预约')
        ## 优先级别
        self.public.driver.find_element_by_xpath('//*[@id="newStatus"]').send_keys('低')
        ## 下次跟踪
        self.public.driver.find_element_by_xpath('//input[@id="next_time"]').send_keys(Keys.DELETE)
        self.public.driver.find_element_by_xpath('//input[@id="next_time"]').send_keys('2019-03-02')
        time.sleep(3)
        ## 跟踪内容
        self.public.driver.find_element_by_xpath('//*[@id="formFollow"]/div[5]/textarea').send_keys('有意向，再考虑考虑！')
        time.sleep(3)
        ## 保存
        self.public.driver.find_element_by_xpath('//*[@id="saveTrackingBtn"]').click()
        time.sleep(4)
        # 进行断言
        resp = self.public.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody/tr/td[12]')
        # print(resp.text)
        self.assertEqual('2019-03-02',resp.text)

    # 修改资源
    def test_alter_resources(self):
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/input[3]').send_keys('科比')
        self.public.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/button').click()
        time.sleep(2)
        self.public.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody/tr/td[15]/button[2]').click()
        self.public.driver.find_element_by_xpath('//*[@id="cusSchool"]').clear()
        self.public.driver.find_element_by_xpath('//*[@id="cusSchool"]').send_keys('东京大学')
        time.sleep(2)
        self.public.driver.find_element_by_xpath('//*[@id="alterCusBtn"]').click()
        ## 进行断言
        self.public.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody/tr[1]/td[15]/button[1]').click()
        time.sleep(3)
        resp=self.public.driver.find_element_by_xpath('//*[@id="resumeDivId"]/div[3]/p[2]')
        # print(resp.text)
        self.assertIn('东京大学',resp.text)

if __name__ == '__main__':
    # unittest.main() # ASCII码顺序运行
    suite = unittest.TestSuite()
    suite.addTests([Training_resources('test_add_resources'), Training_resources('test_query_resources'),
                    Training_resources('test_track_resources'), Training_resources('test_alter_resources'),
                    Training_resources('test_throw_resources')])
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    # # 生成报告
    # suite=unittest.TestSuite()
    # suite.addTests([Training_resources('test_add_resources'),Training_resources('test_query_resources'),
    #                 Training_resources('test_track_resources'),Training_resources('test_alter_resources'),
    #                 Training_resources('test_throw_resources')])
    # with open('report.html','wb') as f:
    #     runner=HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title="Test Report")
    #     runner.run(suite)