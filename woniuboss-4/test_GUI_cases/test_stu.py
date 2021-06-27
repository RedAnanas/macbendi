#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/3/1 16:38
# software: PyCharm

import unittest,time,os
from test_GUI_cases.login import Login
from selenium.webdriver.common.by import By

class Gui(unittest.TestCase):

    def setUp(self):
        self.log = Login()
        self.log.login_admin('wncd000')
        time.sleep(2)
        self.log.decode_method()
        time.sleep(1)
        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = dir_path + '\\GUI_data\\stu_data.xlsx'
        index=0
        self.sheet = self.log.read_excel(file_path,index)
        # print(self.sheet)

    def tearDown(self):
        self.log.close()

    def test_01_stu(self):  #基本信息

        self.log.click_method(By.XPATH,'//*[@id="nav2"]/a[5]') #学员管理
        time.sleep(1)
        self.log.select_method(By.NAME,'stuClass','WNCDC034') #选择班级
        self.log.select_method(By.XPATH,'//*[@id="stuInfo"]/div[1]/select[2]','公共') #选择方向
        time.sleep(1)
        self.log.input_method(By.XPATH,'//*[@id="stuInfo"]/div[2]/input[1]','王森') #输入姓名
        self.log.click_method(By.XPATH,'//*[@id="stuInfo"]/div[2]/button') #点击搜索
        errors = []
        try:
            result = self.log.text('//*[@id="stuInfo_table"]/tbody/tr/td[1]')
            print(result)
            self.assertEqual('王森',result)
        except Exception as e:
            errors.append(e)
        if errors != []:
            raise AssertionError(*errors)

    def test_02_stu(self): #班级管理
        errors=[]
        try:
            self.log.click_method(By.XPATH, '//*[@id="nav2"]/a[5]') #学员管理
            time.sleep(1)
            self.log.click_method(By.XPATH,'//*[@id="content"]/div[2]/div/ul/li[8]/a') #点击班级管理
            time.sleep(1)
            self.log.click_method(By.XPATH,'//*[@id="cmDiv"]/div[1]/button[1]') #点击查询
            time.sleep(1)
            self.log.click_method(By.XPATH, '//*[@id="class-table"]/tbody/tr[1]/td[1]')  # 单选框
            self.log.select_method(By.XPATH,'//*[@id="cmDiv"]/div[1]/select[1]','WNCDC027') #选择分班班级
            self.log.select_method(By.XPATH,'//*[@id="cmDiv"]/div[1]/select[2]','开发')  #选择方向
            self.log.click_method(By.XPATH,'//*[@id="cmDiv"]/div[1]/button[2]') #点击确认
            time.sleep(1)
            self.log.alert_method()  #弹窗确定
            resp = self.log.alert_text()
            # print(resp)
            self.assertIn('处理',resp)
            # self.log.alert_method()
        except Exception as e:
            errors.append(e)
        if errors !=[]:
            raise AssertionError(*errors)

    def test_03_stu(self): #课程安排
        errors=[]
        try:
            for line in range(1,3):
                row = self.sheet.row_values(line)
                data_dict = self.log.dispose_params(row[2])
                teacher1 = data_dict['李懿']
                teacher2 = data_dict['尹瑞']
                teacher3 = data_dict['王欢欢']
                teacher4 = data_dict['周海峰']
                teacher5 = data_dict['许敏']
                teacher6 = data_dict['邓乃文']
                teacher7 = data_dict['曾云莲']
                teacher8 = data_dict['徐小兵']
                teacher9 = data_dict['代虎军']
                teacher = [teacher1, teacher2, teacher3, teacher4, teacher5,
                           teacher6, teacher7, teacher8, teacher9]

                self.log.click_method(By.XPATH, '//*[@id="nav2"]/a[5]') #学员管理
                time.sleep(1)
                self.log.click_method(By.XPATH,'//*[@id="content"]/div[2]/div/ul/li[9]/a') #课程安排
                time.sleep(1)
                self.log.click_method(By.XPATH,'//*[@id="course"]/div[1]/button')  #新增排课
                time.sleep(1)
                self.log.input_method(By.NAME, 'cur.start_time', '2019-01-01')
                self.log.input_method(By.NAME, 'cur.end_time', '2019-03-01')
                for j in range(9): #共9名老师
                    value = teacher[j].strip().split(',') #每名老师的状态，教室，方向
                    # print(value[0],type(value[0]))
                    for i in range(5): #将每位老师的状态，教室，班号，方向，课程，填入表格
                        self.log.select_method(By.XPATH,'//*[@id="addCourse-table"]/tr[%d]/td[%d]/select'%(j+1,i+3),value[i])
                self.log.click_method(By.XPATH,'//*[@id="course-add"]/div/div/div[3]/button[2]') #保存并关闭
        except Exception as e:
            errors.append(e)
        if errors != []:
            raise AssertionError(*errors)



if __name__ == '__main__':
    unittest.main()