#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/9 19:35  
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import os

#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'}
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'}
for q in range(1,209):
    # 获取首页所有url
    url="https://www.mzitu.com/page/%d/"%q
    resp=requests.get(url=url,headers = Hostreferer).text
    soup = BeautifulSoup(resp, "html.parser")
    all_url = soup.find_all('ul', id='pins')
    url1 = str([a for a in all_url])
    for n in range(3,257,11):
        url2=(url1.split('<')[n].split('>')[0])[8:-17]
        # print(url2)

        # fale = 0
        # fale = fale + 1
        # print(fale)

        # 判断是否有文件夹，如果没有则创建
        path = "D:/mzt/" + str(n) + "/"
        if not os.path.exists(path):
            os.makedirs(path)



        #获取图片页面
        url3=url2+"/"
        resp=requests.get(url=url3,headers = Hostreferer).text
        soup = BeautifulSoup(resp, "html.parser")
        #获取页面最大页码数s
        max_pange=soup.find('div',class_='pagenavi')
        s=int((max_pange.text[10:12]))
        # 循环每个页面
        for i in range(1,s):
            url4=url2+'/%d'%i
            resp=requests.get(url=url4,headers = Hostreferer).text
            soup = BeautifulSoup(resp, "html.parser")


            if i==1:
                # 获取每一页的titles
                titles=soup.find('h2',class_='main-title').text
                img = soup.find('img', alt=titles)
                # 根据titles取得图片url
                img_url = requests.get(url=img['src'], headers=Picreferer)
                img_name = str(i)
                file_name=str(n)

                # 用url进行下载
                f = open("D:/mzt/"+file_name+"/"+img_name+".jpg", 'wb')
                f.write(img_url.content)
                f.close()
                # print("wo")
            else:
                title = soup.find('h2', class_='main-title')
                titles =((title.text).replace('（%d）'%i, ''))
                img = soup.find('img', alt=titles)
                img_url = requests.get(url=img['src'], headers=Picreferer)
                img_name = str(i)
                file_name = str(n)
                f = open("D:/mzt/" + file_name + "/" + img_name + ".jpg", 'wb')
                f.write(img_url.content)
                f.close()
                # print("ni")
