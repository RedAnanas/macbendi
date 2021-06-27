#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/20 11:14
# software: PyCharm
import xlrd
class Read_File:
    #定义一个读取excel文件的方法，返回表格对象
    def read_excel(self,file_path,index=0):
        data=xlrd.open_workbook(file_path)
        sheet=data.sheets()[index]
        return sheet
    # def dispose_params(self,parameters):
    #     lines=parameters.strip().split('\n')
    #     params={}
    #     for line in lines:
    #         key,value=line.strip().split('=')
    #         params[key] = value
    #     return params
    def dispose_params1(self,parameters):
        params = {}
        if parameters=='NONE':
            return params
        else:
            lines=parameters.strip().split('\n')
            for line in lines:
              key,value=line.strip().split('=')
              params[key] = value
            return params
    #变量rownumber是传入一个excel表中用例所在的行数，sheet是表的对象
    def read_excel_data(self,sheet,rownumber):
        list=sheet.row_values(rownumber-1)
        number=list[0]
        url=list[2]
        method=list[3]
        parameter=list[4]
        contenttype=list[5]

        #return url
        #print(url)
        return number,url,method,parameter,contenttype

    # def read_excel_data1(self,startnumber,endnumber):
    #     for i in range(startnumber-1,endnumber):





    # def get_params(self,sheet,number):
    #     for i in range(1,sheet.nrows):
    #         if i==number:
    #             list=sheet.row_values(i)
    #             parameters=list[4]
    #             return parameters

