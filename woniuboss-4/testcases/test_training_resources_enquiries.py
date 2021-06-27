#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/23 14:21
# software: PyCharm
from common.Utility import Read_File
from common.public_port import WoniuBoss
import unittest
import os

class decode(unittest.TestCase):
    def setUp(self):
        self.WoniuBoss=WoniuBoss()
        self.WoniuBoss.post_login_method()
        self.WoniuBoss.decode_method()

    def tearDown(self):
        self.WoniuBoss.close()

    def test_training_resources_enquiries(self):
        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = "%s/data/Training_resource_test_cases.xlsx" % dir_path
        index = 0
        sheet=Read_File().read_excel(file_path,index)
        errors = []
        try:
            for i in range(1,sheet.nrows):
                row=sheet.row_values(i)
                num = str(row[0])
                url=row[2]
                method=row[3].lower()
                parameter=Read_File().dispose_params1(row[4])
                status_code=int(row[6])
                expection=int(row[8])
                # print(url,status_code,expection)
                returned_value=self.WoniuBoss.judge_method(method=method,url=url,data=parameter,headers=None)
                # print(returned_value.status_code,returned_value.json()["totalPage"])
                self.assertEqual(returned_value.status_code,status_code)
                self.assertEqual(returned_value.json()["totalPage"],expection)
                # print(returned_value.json()["totalPage"])
        except Exception as e:
            errors.append('%s错误原因：%s'%((num),(str(e).split('\n')[0])))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass
if __name__ == '__main__':
    unittest.main()