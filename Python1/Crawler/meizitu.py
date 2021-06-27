#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/8 19:03  
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

def img_down(titles):
    img = soup.find('img', alt=titles)
    img_url = requests.get(url=img['src'], headers=Picreferer)
    file_name = i

    f = open("D:/mzitu3/%s.jpg" % file_name, 'wb')
    f.write(img_url.content)
    f.close()
url="https://www.mzitu.com/99413/"

resp=requests.get(url=url,headers = Hostreferer).text
soup = BeautifulSoup(resp, "html.parser")
max_pange=soup.find('div',class_='pagenavi')
s=int((max_pange.text[10:12]))


for i in range(1,s):

    url="https://www.mzitu.com/99413/%d"%i
    resp=requests.get(url=url,headers = Hostreferer).text
    soup = BeautifulSoup(resp, "html.parser")

    if i==1:
        titles=soup.find('h2',class_='main-title').text
        img_down(titles)

    else:
        title = soup.find('h2', class_='main-title')
        titles =((title.text).replace('（%d）'%i, ''))
        img_down(titles)


