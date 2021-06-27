#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


base_url = 'http://jacky-vpc'


def get_method1():
    # 最基本的get方法使用
    return requests.get(base_url + '/agileone/?key=value&key1=value')


def get_method2():
    # 可以利用字典类型的数据传参数
    params = {'key': 'value', 'key1': 'value1'}
    return requests.get(base_url + '/agileone/', params)


def post_method():
    # 构造data变的简单了，直接使用字典类型数据即可。
    # 而且也不用考虑urlencode的编码转换问题，因为requests库帮我们代劳了。
    data = {'username': 'admin', 'password': 'admin', 'savelogin': True}
    # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # return requests.post(base_url + '/agileone/index.php/common/login', data, headers=headers)
    # 如果要传送的body数据是使用urlencode类型的编码传递，那么也不用构造headers了，
    # 因为requests默认使用这个类型传递body数据
    return requests.post(base_url + '/agileone/index.php/common/login', data)


def get_cookie_method1():
    resp = post_method()
    # 这是获得cookie的传统方法，获得的cookie是字符串类型，将来的使用和我们在http.client和urllib中的做法相同
    cookie = resp.headers['Set-Cookie']
    print(type(cookie))
    print(cookie)


def get_cookie_method2():
    resp = post_method()
    # 利用requests库的响应对象的cookies属性来获取cookie，要注意这样获得的cookie类型与传统方法不同
    cookies = resp.cookies
    print(type(cookies))
    print(cookies)

    data = {'headline': 'test', 'content': 'demo', 'scope': 1, 'expireddate': '2019-01-17'}
    # 利用cookies参数来传递上面这种方法获得的cookie对象，注意千万不要和传统方法获得的cookie混用
    return requests.post(base_url + '/agileone/index.php/notice/add', data, cookies=cookies)


def session_method():
    # 构建一个持久连接
    session = requests.session()
    # 利用持久连接的session机制，我们就不需要自己维护cookie了，因为requests库帮我们做了。
    login_data = {'username': 'admin', 'password': 'admin', 'savelogin': True}
    resp = session.post(base_url + '/agileone/index.php/common/login', login_data)
    notice_data = {'headline': 'new notice 0', 'content': '000', 'scope': 1, 'expireddate': '2019-01-17'}
    session.post(base_url + '/agileone/index.php/notice/add', notice_data)
    query_data = {'currentpage': 1}
    resp = session.post(base_url + '/agileone/index.php/notice/query', query_data)
    session.close()
    return resp


def convert_json1():
    resp = session_method()
    print('text: ', type(resp.text))
    # 注意requests给我们提供的json方法，它能够帮我们把json类型的字符串转换成python的基本数据类型，
    # 方便我们的处理。
    result = resp.json()
    print('result type: ', type(result))
    print('result: ', result)


def convert_json2():
    resp = session_method()
    # 利用python自带的json模块的loads方法（注意是复数）来将json字符串转换成python基本数据类型
    python_obj = json.loads(resp.text)
    print(type(python_obj[0]))
    print(python_obj[0])
    # 利用dumps方法（注意是复数）将python的基本数据类型转换成json格式的字符串
    json_str = json.dumps(python_obj[0])
    print(type(json_str))
    print(json_str)


def get_request_info():
    resp = post_method()
    # 注意下面三个方法是我们将来接口测试调试代码错误的利器，一定要掌握。
    print('真正发给服务器的url: ', resp.request.url)
    print('真正发给服务器的headers: ', resp.request.headers)
    print('真正发给服务器的body: ', resp.request.body)


def upload_file_method1():
    session = requests.session()
    login_data = {'username': 'admin', 'password': 'admin', 'savelogin': True}
    session.post(base_url + '/agileone/index.php/common/login', login_data)
    # 构造文件对象。它是一个字典类型数据，注意value的部分必须是一个元组对象。
    # 元组对象的第一个元素是要显示的文件名字，第二个元素是要上传的文件对象（可以通过open方法获得）
    # 第三个元素是要上传的文件的mime类型，第四个元素可以指定自定义的headers。注意第三、四元素可以省略。
    files = {'fileToUpload':
                 ('day1.txt', open('E:/Documents/work/PrepareLessons/API_TESTING/day1作业.txt', 'r'))}
    # 我们利用requests库post方法的files参数来上传文件，
    # 使用了这个参数requests就会使用multipart/form-data的方式提交数据
    resp = session.post(base_url + '/agileone/index.php/attach/upload/refertype/defect/referid/4',
                        files=files)
    session.close()
    return resp


def upload_file_method2():
    session = requests.session()
    login_data = {'username': 'admin', 'password': 'admin', 'savelogin': True}
    session.post(base_url + '/agileone/index.php/common/login', login_data)
    files = {'fileToUpload':
                 ('day1.txt', open('E:/Documents/work/PrepareLessons/API_TESTING/day1作业.txt', 'r'))}
    # 这是上传文件时同时上传其他数据的一种方法。
    resp = session.post(base_url + '/agileone/index.php/attach/upload/refertype/defect/referid/4',
                        login_data, files=files)
    session.close()
    return resp


def upload_file_method3():
    session = requests.session()
    login_data = {'username': 'admin', 'password': 'admin', 'savelogin': True}
    session.post(base_url + '/agileone/index.php/common/login', login_data)
    # 这是上传文件时同时提交数据的另外一种方法
    files = {'username': (None, 'admin'), 'password': (None, 'admin'), 'savelogin': (None, True),
            'fileToUpload':
                 ('day1.txt', open('E:/Documents/work/PrepareLessons/API_TESTING/day1作业.txt', 'r'))}
    resp = session.post(base_url + '/agileone/index.php/attach/upload/refertype/defect/referid/4',
                        files=files)
    session.close()
    return resp


def download_file_method():
    session = requests.session()
    login_data = {'username': 'admin', 'password': 'admin', 'savelogin': True}
    session.post(base_url + '/agileone/index.php/common/login', login_data)
    # 下面是下载文件的方法，对于下载的文件保存时注意文字编码
    resp = session.get(base_url + '/agileone/Attachment/AgileoneDemo/20190118093938.txt')
    with open('day1.txt', 'w', encoding='gbk') as f:
        f.write(resp.content.decode('gbk'))
    session.close()


def access_https_method():
    # 在访问https的网站时，代码可以利用verify参数来关闭证书验证的机制
    return requests.get('https://jacky-vpc/agileone/', verify=False)


def redirects_method():
    # 关于重定向如何显示历史记录的方法，这里注意allow_redirects参数默认值是False，代表不去追踪记录。
    resp = requests.get('http://jacky-vpc:8080/WoniuSales1.4', allow_redirects=True)
    for r in resp.history:
        print(r.status_code, r.reason)
        print('url: ', r.request.url)
    return resp


if __name__ == '__main__':
    resp = redirects_method()
    print(resp.status_code, resp.reason)
    # print(resp.content.decode())
    print('真正发给服务器的url: ', resp.request.url)
    # print('真正发给服务器的headers: ', resp.request.headers)
    # print('真正发给服务器的body: ', resp.request.body)
    # print(resp.json())
    # download_file_method()
