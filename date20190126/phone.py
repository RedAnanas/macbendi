#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/26 17:02
# software: PyCharm
import requests
session=requests.session()
date_list=[{"moblienum":"17868871347"},
            {"moblienum":""},
            {"moblienum":"None"},
            {"moblienum":"1786887134711"}]
for i in date_list:
    resp=session.post("http://api.avatardata.cn/MobilePlace/LookUp",i)
    print(resp.text)
    if resp.status_code==200:
        print("ceshi")
        reat=resp.json()
        if i["moblienum"]=="17868871347"and reat["error_code"]==0 and reat["reason"]=="Succes":
            print("测试成功")
        elif i["moblienum"]!="17868871347"and reat["error_code"]==1:
            print("测试成功")
        else:
            print("测试失败")






