#! /usr/bin/env python
# -*- coding: utf-8 -*-


# 我们今天的开发思路
# 1. 首先定义一个经过自己封装的通信类，目的就是把我们底层所使用requests库透明
# 2. 再完成一个工具类。这里面计划实现读取excel文件的方法、解析参数的方法、断言方法
# 3. 最后实现我们的测试类。
# 4. 这里面首先对类进行初始化，读取测试数据，并且要定义测试成功用例数，失败用例数，测试时长三个变量。
# 5. 实现run方法，负责真正执行测试
# 6. 实现一个执行方法，记录测试开始时间-》调用run方法-》记录测试结束时间，计算测试时长，最好打印测试结果。
# 7. 通过main方法来去调用测试类的执行方法。

from training.seventh_phase.API_Testing.testframework.Common import Common
from training.seventh_phase.API_Testing.testframework.Utility import *
import time


# 定义一个测试流程控制类
class Control:

    def __init__(self):
        # 获取具体的excel表格对象，定义成功、失败、运行时间的计数器
        self.table = read_excel('./TestData.xlsx', 1)
        self.count_success = 0
        self.count_fail = 0
        self.run_time = 0

    def run(self):
        # 定义一个具体的测试流程，这里面含有数据驱动的思想，注意理解。
        common = Common()
        for i in range(1, self.table.nrows):
            row = self.table.row_values(i)
            url = row[2]
            data = get_params(row[4])
            method = row[3]
            resp = common.request(url, data, method)
            if resp is None:
                self.count_fail += 1
            else:
                if assert_result(row, resp.status_code, resp.text):
                    self.count_success += 1
                else:
                    self.count_fail += 1
        common.close()

    def start_test(self):
        print('************** 开始进行测试 ***************')
        begin = time.clock()
        self.run()
        self.run_time = time.clock() - begin
        print('总测试时间：%d秒，测试用例执行成功：%d个，失败%d个。'
              % (self.run_time, self.count_success, self.count_fail))
        print('************** 测试全部完成 ***************')


if __name__ == '__main__':
    Control().start_test()
