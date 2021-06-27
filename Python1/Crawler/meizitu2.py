#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/9 12:50  
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup


#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'
               }
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'
}
# 获取首页所有url
url="https://www.mzitu.com/page/1/"
resp=requests.get(url=url,headers = Hostreferer).text
soup = BeautifulSoup(resp, "html.parser")
all_url = soup.find_all('ul', id='pins')
url = str([a for a in all_url])
for i in range(3,257,11):
    urls=(url.split('<')[i].split('>')[0])[8:-17]
    print(urls)

