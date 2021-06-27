#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/25 15:40
# software: PyCharm

from woniuboss1.common.Utility import Read_File
from woniuboss1.common.public_port import WoniuBoss
import unittest

class decode(unittest.TestCase):
    def setUp(self):
        self.WoniuBoss=WoniuBoss()
        self.WoniuBoss.post_login_method()
        self.WoniuBoss.decode_method()
    def tearDown(self):
        self.WoniuBoss.close()

    def test_training_resources_revision(self):
        file_path = "../data/培训资源-接口文档2.1.xlsx"
        index = 1
        sheet=Read_File().read_excel(file_path,index)
        errors = []
        try:
            for i in range(1,sheet.nrows):
                row=sheet.row_values(i)
                num=str(row[0])
                url=row[2]
                method=row[3].lower()
                # parameter=Read_File().dispose_params1(row[4])
                status_code = int(row[6])
                expection = row[8]
                # print(num,url,method,status_code,expection)

                returned_value=self.WoniuBoss.judge_method(method=method,url=url,data=None,headers=None)
                self.assertEqual(returned_value.status_code,status_code)
                # print(returned_value.text)
                self.assertEqual(returned_value.text,expection)
        except Exception as e:
            errors.append('%s错误原因：%s'%((num),(str(e).split('\n')[0])))
            if errors!=None:
                raise AssertionError(errors)
            else:
                pass

if __name__ == '__main__':
    unittest.main()