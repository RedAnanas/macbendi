#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/17 16:45
# software: PyCharm
import requests

def get_test():
    resp=requests.get("http://admin/agileone/")
    return resp


if __name__ == '__main__':
    resp=get_test()
    print(resp.status_code,resp.reason)
    print(resp.content.decode())