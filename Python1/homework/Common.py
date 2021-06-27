#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests


# 定义一个自有的通信类，透明化底层的requests库
class Common:

    def __init__(self):
        self.session = requests.session()
        # 因为我们测试的是会员管理方面的请求，所以呢必须先登录。目的是获取cookie。
        data = {'username': 'admin', 'password': 'Milor123', 'verifycode': '0000'}
        self.session.post('http://jacky-vpc:8080/WoniuSales1.4/user/login', data)

    def get(self, url):
        # 定义一个get方法
        return self.session.get(url)

    def post(self, url, data):
        # 定义一个post方法
        return self.session.post(url, data)

    def request(self, url, data=None, method='get'):
        # 自动依据传入的方法字符串来判断我们要使用的具体请求方法
        method = method.lower()
        if method == 'get':
            resp = self.get(url)
        elif method == 'post':
            resp = self.post(url, data)
        else:
            resp = None
        return resp

    def close(self):
        self.session.close()
