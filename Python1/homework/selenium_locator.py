#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(30)
# driver.get('http://jacky-vpc/agileone/')
# time.sleep(2)
# # 利用id定位，注意代码效率，最好用变量接收找到的对象，便于后续使用
# username = driver.find_element_by_id('username')
# username.clear()
# username.send_keys('admin')
# password = driver.find_element_by_id('password')
# password.clear()
# password.send_keys('admin')
# driver.find_element_by_id('login').click()
# time.sleep(1)
# 利用partial_link_text模糊匹配定位
# driver.find_element_by_partial_link_text('公告管理').click()
# time.sleep(1)
# 注意两种不同获取表格元素对象的xpath写法
# result = driver.find_element_by_xpath('//table[@id="dataTable"]/tbody/tr[1]/td[2]').text
# result = driver.find_element_by_xpath('//tbody[@id="dataPanel"]/tr[1]/td[2]').text
# total = int(driver.find_element_by_id('totalRecord').text)
# 这里按定位元素的选择策略应该用id定位，但是我们为了给大家演示xpath的用法，所以这里专门使用xpath定位
# total = int(driver.find_element_by_xpath('//span[@id="totalRecord"]').text)
# random_select_num = random.randint(1, 10000) % total + 1
# 注意下面三种同一元素的xpath定位写法，都是可以的
# driver.find_element_by_xpath('//tbody[@id="dataPanel"]/tr[%d]/td[5]/label[@onclick="goEdit(this,true)"]'
#                              % random_select_num).click()
# driver.find_element_by_xpath('//tbody[@id="dataPanel"]/tr[%d]/td[5]/label[text()="编辑"]'
#                              % random_select_num).click()
# driver.find_element_by_xpath('//tr[@id="dtrow_%d"]/td[5]/label[text()="编辑"]'
#                              % random_select_num).click()
# 对于js提示窗口alert、confirm、prompt的操作
# 点击确定按钮
# driver.switch_to.alert.accept()
# # 点击取消按钮
# driver.switch_to.alert.dismiss()
# # 获取窗口的文本内容
# driver.switch_to.alert.text
# # 向窗口输入文本信息
# driver.switch_to.alert.send_keys('想的美！')
driver.get('http://www.baidu.com')
time.sleep(2)
driver.find_element_by_id('kw').send_keys('蜗牛学院')
driver.find_element_by_id('su').click()
# time.sleep(1)
# driver.find_element_by_link_text('...西安|上海IT|Java|软件测试|Python开发培训学校|机构-蜗牛学院').click()
# current_window = driver.current_window_handle
# print(current_window)
# window_list = driver.window_handles
# for page in window_list:
#     print(page)
#     driver.switch_to.window(page)
#     time.sleep(2)
# driver.switch_to.window(current_window)
# webdriver.ActionChains(driver).click_and_hold(driver.find_element_by_link_text('设置')).perform()
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
WebDriverWait(driver, 60).\
    until(lambda driver:
          driver.
          find_element_by_link_text('...西安|上海IT|Java|软件测试|Python开发培训学校|机构-蜗牛学院'))
WebDriverWait(driver, 60).until(
    expected_conditions.presence_of_element_located
    ((By.LINK_TEXT, '...西安|上海IT|Java|软件测试|Python开发培训学校|机构-蜗牛学院')))
