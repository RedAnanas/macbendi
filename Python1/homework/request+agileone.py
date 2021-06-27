#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import unittest
import HTMLTestRunner


# 1.我们要把requests库对我们的测试用例透明，目的是将来底层的http发送库可以随时替换为更好的库
# 2.把这样一个自有的类作为我们测试方法中发送http请求的类使用
# 3.我们再来实现测试用例。通过继承unittest的TestCase类来实现
# 4.在测试用例类中构造测试方法，每一个测试方法负责针对一个接口来测试
# 5.在针对一个接口设计测试方法时首先考虑http请求三要素，然后还有http请求的方法
# 6.一个参数数据怎么设计，再一个返回结果怎么验证
# 7.上述事情干完实际上就完成了一个测试方法
# 8.最后我们把所有写好的TestCase加载到TestSuite对象中，然后构建HTMLTestRunner对象
# 9.通过HTMLTestRunner对象的run方法来运行测试用例。
class Connection:

    def __init__(self, host, port=None):
        if port is None:
            self.base_url = 'http://' + host
        else:
            self.base_url = 'http://%s:%d' % (host, port)
        self.session = requests.session()

    def get(self, url, params=None):
        # 这个方法是我们自己定义的，如果你自己有任何想法，那么都可以按照自己的设想来尝试一下
        return self.session.get(self.base_url + url, params=params)

    def post(self, url, data, headers=None, files=None):
        return self.session.post(self.base_url + url, data, headers=headers, files=files)

    def close(self):
        self.session.close()


class AgileOne(unittest.TestCase):

    con = None

    @classmethod
    def setUpClass(cls):
        # 此处我们希望在所有测试方法执行前获得我们的http连接对象。当然大家也可以考虑在setUP情形下该怎做。
        cls.con = Connection('jacky-vpc')

    @classmethod
    def tearDownClass(cls):
        # 用完了资源要记着清理
        cls.con.close()

    def test_login(self):
        data = [{'username': 'admin', 'password': 'admin', 'savelogin': True},
                {'username': 'abc', 'password': 'admin', 'savelogin': True},
                {'username': 'admin', 'password': '123', 'savelogin': True},
                {'username': '', 'password': '', 'savelogin': True}]
        errors = []
        for d in data:
            try:
                resp = self.con.post('/agileone/index.php/common/login', d)
                self.assertEqual(200, resp.status_code)
                if d['username'] == 'admin' and d['password'] == 'admin':
                    self.assertEqual('successful', resp.text)
                elif d['username'] != 'admin':
                    self.assertEqual('', resp.text)
                else:
                    self.assertEqual('', resp.text)
            except Exception as e:
                errors.append('使用用户名：%s 密码：%s登录失败，错误原因：%s'
                              % (d['username'], d['password'], str(e).split('\n')[0]))
        raise AssertionError(*errors)

    def test_welcome_page(self):
        resp = self.con.get('/agileone/index.php')
        self.assertIn('蜗牛学院-敏捷项目', resp.content.decode('utf8'))

    # 实现一个普通方法，供自己的测试方法和其他测试方法使用
    def add_notice(self, data):
        return self.con.post('/agileone/index.php/notice/add', data)

    # 注意这个方法呢会报没有权限的错误，那么原因是什么，如何能够让它变的正确。
    # 结合我们上课所讲，大家自己把改正确了。这里修改是有多种思路的，大家可以一一尝试。
    def test_add_notice(self):
        notice_data = {'headline': 'new notice 0', 'content': '000',
                       'scope': 1, 'expireddate': '2019-01-21'}
        resp = self.add_notice(notice_data)
        self.assertEqual(200, resp.status_code)
        self.assertGreater(0, int(resp.text))

    def test_query_notice(self):
        notice_data = {'headline': 'new notice 1', 'content': '000',
                       'scope': 1, 'expireddate': '2019-01-21'}
        resp = self.add_notice(notice_data)
        # 关联方法
        notice_id = resp.text
        resp = self.con.post('/agileone/index.php/notice/query', {'currentpage': 1})
        first_el_notice_id = resp.json()[0]['noticeid']
        self.assertEqual(200, resp.status_code)
        self.assertEqual(notice_id, first_el_notice_id)


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AgileOne))
    # 这是一种变形用法，用上面或下面这两种中的一种即可
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AgileOne)
    # 注意文件保存时只有文本文件才需要设置encoding参数，如果保存的是类似图片这样的二进制数据，
    # 那么mode参数应该用'wb'，encoding参数就没必要设置了。
    with open('unittest_requests_test_report.html', 'w', encoding='utf8') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='AgileOne Test Report', verbosity=2)
        runner.run(suite)
