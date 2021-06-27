#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/6 16:09
# software: PyCharm
import xlrd,xlwt,xlutils



all=xlrd.open_workbook("../File/atm.xlsx")
atm_info=all.sheets()[0]#获取第一个sheel页
rows=atm_info.nrows#获取行数
cols=atm_info.ncols#获取列数


