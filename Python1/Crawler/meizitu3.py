#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/9 15:21  
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import os


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
    file_name = n
    fale_path=m
    path = "D:/%d/"%fale_path
    if not os.path.exists(path):
        os.makedirs(path)

    f = open(path+"%s.jpg" % file_name, 'wb')
    f.write(img_url.content)
    f.close()

for i in range(1,3):
    url="https://www.mzitu.com/page/%d/"%i
    resp=requests.get(url=url,headers = Hostreferer).text
    soup = BeautifulSoup(resp, "html.parser")

    all_names = soup.find_all('ul', id='pins')
    names = str([a for a in all_names])

    for i in range(3,257,11):
        for m in range(1,4493):

            url_all=(names.split('<')[i].split('>')[0])[8:-17]

            url = url_all

            resp = requests.get(url=url, headers=Hostreferer).text
            soup = BeautifulSoup(resp, "html.parser")
            max_pange = soup.find('div', class_='pagenavi')
            s = int((max_pange.text[10:12]))

            for n in range(1, s):

                url1 = url+"/%d" %n
                resp = requests.get(url=url, headers=Hostreferer).text
                soup = BeautifulSoup(resp, "html.parser")

                if n == 1:
                    titles = soup.find('h2', class_='main-title').text
                    img_down(titles)


                else:
                    title = soup.find('h2', class_='main-title')
                    titles = ((title.text).replace('（%d）' % n, ''))
                    img_down(titles)




