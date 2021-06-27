#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/21 11:28
# software: PyCharm


import requests
session = requests.session()

a=session.get("http://106.13.36.122:8080/WoniuBoss2.0/log/userLogin?userName=WNCD000&userPass=woniu123&checkcode=0000")
# print(a.text)

data={'vp':'woniu123'}
# s=session.post("http://106.13.36.122:8080/WoniuBoss2.0/second?vp=woniu123")
s=session.post("http://106.13.36.122:8080/WoniuBoss2.0/second?",data=data)
# print(s.text)

# data={'pageSize':'10',
#       'pageIndex':'1',
#       'status':'all',
#       'cusInfo':'郝保成',
#       'lastStatus':'',
#       'empName':'',
#       'source':'',
#       's_time':'',
#       'e_time':'',
#       'poolType':''
#       }
# s=session.post("http://106.13.36.122:8080/WoniuBoss2.0/resource/queryCusByCusInfo",data=data)
# print(s.json())

# data="cus.customer_id=592802&cus.name=郝保成&cus.sex=男&cus.last_status=新入库&cus.tel=17781071581&cus.email=&cus.qq=1231315881&cus.school=西北大学&cus.education=本科&cus.major=&cus.intent=&cus.workage=应届毕业生&cus.salary=&cus.age=24&cus.source=智联招聘&cus.applposition=&cus.eduexp=&cus.experience=&cus.last_tracking_remark=lijia"
#
# s=session.get("http://106.13.36.122:8080/WoniuBoss2.0/resource/modifyCusInfo?"+data)
# print(s.text)

# data={
# 'fee':'16800元',
# 'remark':'随便啦111asasdajsdhkjsahd',
# 'status':'未联系上',
# 'id':'592803',
# 'nextTime':'2019-02-27',
# 'priority':'中',
# }
#
# s=session.post("http://106.13.36.122:8080/WoniuBoss2.0/resource/saveTrackingRecord",data=data)
# print(s.text,s.status_code,s.content.decode())

# data={'arr[]':'592805,WNCD000'
# }
#
# s=session.post("http://106.13.36.122:8080/WoniuBoss2.0/resource/abandonResource",data=data)
# print(s.text,s.status_code,s.content.decode())

url="http://106.13.36.122:8080/WoniuBoss2.0/resource/modifyCusInfo?cus.customer_id=592797&cus.name=何来&cus.sex=男&cus.last_status=新认领&cus.tel=17681671581&cus.email=&cus.qq=&cus.school=&cus.education=本科&cus.major=&cus.intent=&cus.workage=应届毕业生&cus.salary=&cus.age=&cus.source=智联招聘&cus.applposition=&cus.eduexp=&cus.experience=&cus.last_tracking_remark="

s=session.get(url=url)
print(s.text,s.status_code,s.content.decode())

# data={'pageSize': '10',
#       'pageIndex': '1',
#       'status': 'all',
#       'cusInfo': '汪子尧',
#       'lastStatus': '',
#       'empName': '',
#       'source': '',
#       's_time': '',
#       'e_time': '',
#       'poolType': ''}
#
# s=session.post("http://106.13.36.122:8080/WoniuBoss2.5/resource/queryCusByCusInfo",data=data)
# print(s.text,s.status_code,s.content.decode(),type(s))
