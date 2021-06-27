#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/7 17:41  
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

base_url = 'https://book.douban.com/top250?start='
# urllist = []
# 从0到225，间隔25的数组
for page in range(0, 250, 25):
    allurl = base_url + str(page)
    # urllist.append(allurl)

    resp=requests.get(allurl)
    soup = BeautifulSoup(resp.text, 'lxml')

    all_names = soup.find_all('div', class_='pl2')
    names = [a.find('a')['title'] for a in all_names]
    # print(names)

    all_author = soup.find_all('p', class_='pl')
    author = [b.text for b in all_author]
    # print(author)

    all_grade = soup.find_all('span',class_='rating_nums')
    grade = [c.text for c in all_grade]
    # print(grade)

    all_intro = soup.find_all('span',class_='inq')
    intro = [d.text for d in all_intro]
    # print(intro)

    for name, author, score, sum in zip(names, all_author, all_grade, all_intro):
        name = '书名：' + str(name) + '\n'
        author = '作者：' + str(author.text) + '\n'
        score = '评分：' + str(score.text) + '\n'
        sum = '简介：' + str(sum.text) + '\n'
        data = name + author + score + sum
        # print(data)

        # 文件名
        filename = '豆瓣Top250.txt'
        # 保存文件操作
        with open(filename, 'a', encoding='utf-8') as f:
            # 保存数据
            f.writelines(data + '=======================' + '\n')
        print('保存成功')








