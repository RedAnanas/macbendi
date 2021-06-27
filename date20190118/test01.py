#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/18 11:37
# software: PyCharm

import requests

def upload_file():
    session=requests.session()
    login_date={"username":"admin","password":"admin","verifycode":"0000"}
    session.post("http://admin:8080/WoniuSales1.4/user/login",login_date)
    files={"batchfile":("textmin.xls",open("D:/Python/date20190118/textmin.xls","rb"))}
    bach_data={"batchname":"2019011802"}
    resp = session.post("http://admin:8080/WoniuSales1.4/goods/upload",bach_data,files=files)
    session.close()
    return resp.text
if __name__ == '__main__':
    print(upload_file())