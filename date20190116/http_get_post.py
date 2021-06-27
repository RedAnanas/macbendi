#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/16 17:13
# software: PyCharm
import http.client

def http_get_method():
    con=http.client.HTTPConnection("admin",8080)
    con.request("GET","/WoniuSales1.4/")
    respones=con.getresponse()
    print(respones.status,respones.reason)
    content=respones.read()
    print(content.decode("utf8"))


def http_post_method():
    param={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    data="username=admin&password=admin&verifycode=0000"
    con = http.client.HTTPConnection("admin", 8080)
    con.request("POST", "http://admin:8080/WoniuSales1.4/user/login",data,param)
    resp=con.getresponse()
    print(resp.status,resp.reason)
if __name__ == '__main__':
    # http_get_method()
    http_post_method()