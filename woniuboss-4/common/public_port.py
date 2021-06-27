#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/2/21 10:11
# software: PyCharm
import requests
class WoniuBoss:
   def __init__(self):
        #self.baseurl = "http://106.13.36.122"
        self.session = requests.session()

   # def query(self):
   #      response=self.post_login_method()
   #      print(response.status_code)
   #      print(response.text)
   #      res=self.session.post(self.baseurl + ":8080/WoniuSales1.4/query")
   #      print(res.text)
   #      querydata={"page":"1"}
   #      res=self.session.post(self.baseurl + ":8080/WoniuSales1.4/query/zerostored", querydata)
   #      print(res.text)
   #      print(res.json())
   #      print(res.json()[0])

   def post_login_method(self):
        #login_data={"userName":"WNCD000","userPass":"woniu123","checkcode":"0000"}
        response=self.session.get('http://106.13.36.122:8080/WoniuBoss2.0/log/userLogin?userName=WNCD000&userPass=woniu123&checkcode=0000')
        # vp={'vp':'woniu123'}
        # response=self.session.post('http://106.13.36.122:8080/WoniuBoss2.0/second?vp=woniu123',vp)
        #
        return response
   def post_login_method1(self):
        #login_data={"userName":"WNCD001","userPass":"woniu123","checkcode":"0000"}
        response = self.session.get(
            'http://106.13.36.122:8080/WoniuBoss2.0/log/userLogin?userName=WNCD000&userPass=woniu123&checkcode=0000')
        return response
   def post_login_method2(self):
        #login_data={"userName":"WNCD002","userPass":"woniu123","checkcode":"0000"}
        response = self.session.get(
            'http://106.13.36.122:8080/WoniuBoss2.0/log/userLogin?userName=WNCD000&userPass=woniu123&checkcode=0000')
        return response
   def post_login_method3(self):
        #login_data={"userName":"WNCD011","userPass":"woniu123","checkcode":"0000"}
        response = self.session.get(
            'http://106.13.36.122:8080/WoniuBoss2.0/log/userLogin?userName=WNCD000&userPass=woniu123&checkcode=0000')
        return response
   def post_login_method4(self):
        #login_data={"userName":"WNCD023","userPass":"woniu123","checkcode":"0000"}
        response = self.session.get(
            'http://106.13.36.122:8080/WoniuBoss2.0/log/userLogin?userName=WNCD000&userPass=woniu123&checkcode=0000')
        return response
   def decode_method(self):
       vp={'vp':'woniu123'}
       response=self.session.post('http://106.13.36.122:8080/WoniuBoss2.0/second?vp=woniu123',vp)
       return response
   def post(self,url,data=None,headers=None,files=None):
       return self.session.post(url,data=data,headers=headers,files=files)
   def get(self,url,params=None):
       return self.session.get(url,params=params)
    # print(response.status_code)
    # print(response.text)
    # res=session.post(baseurl + ":8080/WoniuSales1.4/query")
    # print(res.text)
    # querydata={"page":"1"}
    # res=session.post(baseurl + ":8080/WoniuSales1.4/query/zerostored", querydata)
    # print(res.text)
    # print(res.json())
    # print(res.json()[0])
   def post_login_method6(self,username):
       response = self.session.get(
           'http://106.13.36.122:8080/WoniuBoss2.5/log/userLogin?userName=%s&userPass=woniu123&checkcode=0000'%(username))
       return response

   # def upload_file(self):
   #     response=self.post_login_method()
   #     # print(response.status_code)
   #     # print(response.cookies)
   #     resp=self.session.get(self.baseurl+":8080/WoniuSales1.4/goods")
   #     # print(resp.content.decode())
   #     # print(resp.text)
   #     res=self.session.post(self.baseurl+":8080/WoniuSales1.4/store/querybatch")
   #     handers={"Content-Type":"application/vnd.ms-excel"}
   #     file={"batchname":(None,'GB20190119(2)'),"batchfile":("sss.xls",open("C:/Users/Administrator/Desktop/sss.xls",'rb'),None,handers)}
   #     res=self.session.post(self.baseurl+":8080/WoniuSales1.4/goods/upload",files=file)
   #     return res
   #     # print(res.request.url)
   #     # print(res.request.headers)
   #     # print(res.request.body)
   # #此方法是通过Excel表获取到相应的接口所需要的数据时候，可以调用此方法来获得返回值
   def judge_method(self,method,url,data,headers):
       if method=="get":
           resp=self.get(url=url)
       elif method=="post":
           resp=self.post(url=url,data=data,headers=headers)
       else:
           resp=None
       return resp
   def close(self):
       self.session.close()
if __name__ == '__main__':
    #WoniuBoss().post_login_method()
    resp=WoniuBoss().post_login_method6("WNCD000")
    print(resp.text)