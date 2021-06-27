#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/7 17:41  
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

base_url = 'https://movie.douban.com/top250?start=%d&filter='
for page in range(0, 25, 25):
    allurl = base_url %int(page)

    resp=requests.get(allurl)
    soup = BeautifulSoup(resp.text, 'lxml')

    all_names = soup.find_all('span', class_='title')
    names = [a.get_text() for a in all_names]

    all_names1 = soup.find_all('span', class_='other')
    names1 = [a1.get_text() for a1 in all_names1]

    all_grade = soup.find_all('span', class_='rating_num')
    grade = [a.get_text() for a in all_grade]

    all_director = soup.find_all('p', class_='')
    director = [a.get_text() for a in all_director]

    all_intro = soup.find_all('span', class_='inq')
    intro = [a.get_text() for a in all_intro]

    for names, names1,grade, director, intro in zip(all_names, all_names1, all_grade,all_director, all_intro):
        name = '影名：' + str(names.text) + '\n'
        author = '别名：' + str(names1.text) + '\n'
        grade = '评分：' + str(grade.text) + '\n'
        # str.replace(u'\xa0', u' ')
        score = '导演：' + str(director.text).replace(' ','') + '\n'
        # score = '导演：' + str(director.text) + '\n'
        sum = '简介：' + str(intro.text) + '\n'
        data = name + author + grade + score + sum
        # print(data)


        # 文件名
        filename = '豆瓣电影Top250.txt'
        # 保存文件操作
        with open(filename, 'a', encoding='utf-8') as f:
            # 保存数据
            f.writelines(data + '=======================' + '\n')
        print('保存成功')




    # print(names)
    # print(names1)
    # print(director)
    # print(intro)

    # all_author = soup.find_all('p', class_='pl')
    # author = [b.text for b in all_author]
    # # print(author)
    #
    # all_grade = soup.find_all('span',class_='rating_nums')
    # grade = [c.text for c in all_grade]
    # # print(grade)
    #
    # all_intro = soup.find_all('span',class_='inq')
    # intro = [d.text for d in all_intro]
    # # print(intro)
    #
    # for name, author, score, sum in zip(names, all_author, all_grade, all_intro):
    #     name = '书名：' + str(name) + '\n'
    #     author = '作者：' + str(author.text) + '\n'
    #     score = '评分：' + str(score.text) + '\n'
    #     sum = '简介：' + str(sum.text) + '\n'
    #     data = name + author + score + sum
    #     # print(data)
    #
    #     # 文件名
    #     filename = '豆瓣图书Top250.txt'
    #     # 保存文件操作
    #     with open(filename, 'a', encoding='utf-8') as f:
    #         # 保存数据
    #         f.writelines(data + '=======================' + '\n')
    #     print('保存成功')








