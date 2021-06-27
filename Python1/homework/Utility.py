#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd


def read_excel(file, index=0):
    # 定义一个读取excel文件的的方法，返回获取到的表格sheet对象
    data = xlrd.open_workbook(file)
    sheet = data.sheets()[index]
    return sheet


def get_params(parameters):
    # 定义一个解析字符串参数到python字典对象的方法
    lines = parameters.strip().split('\n')
    params = {}
    for line in lines:
        key, value = line.strip().split('=')
        params[key] = value
    return params


def assert_result(row, actual_code, actual_content):
    # 定义一个断言方法，返回值是布尔值。
    description = '%s - %s' % (row[0], row[1])
    print('************** %s 测试开始 **************' % description)
    is_pass = int(row[5]) == actual_code and row[6] == actual_content
    if is_pass:
        print('测试成功。')
    else:
        print('测试失败。')
        print('响应代码：期望 %d, 但实际获得的值是 %d' % (int(row[5]), actual_code))
        print('响应正文：期望 %s, 但实际获得的值是 %s' % (row[6], actual_content))
    print('************** %s 测试结束 **************' % description)
    return is_pass
