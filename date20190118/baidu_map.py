#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/18 21:46
# software: PyCharm

import requests
import json
from selenium import webdriver
import time
def map():
    session=requests.session()
    ak="MKzM9GLcWkcIOzBvTIkG7ujMLazfzNEe"
    ip="1.83.1.133"
    return (session.get("http://api.map.baidu.com/location/"
                        "ip?ip=%s&"
                        "ak=%s&coor=bd09ll"%(ip,ak)))
def map1_1():
    session=requests.session()
    ak = "MKzM9GLcWkcIOzBvTIkG7ujMLazfzNEe"
    address="西安市第五国际A座"
    value=(session.get("http://api.map.baidu.com/geocoder/v2/?"
                       "address=%s&"
                       "output=json&"
                       "ak=%s"%(address,ak)))
    site=value.json()

    return site


def map1():

    url=("http://api.map.baidu.com/marker?"
            "location=34.323390409878147,108.95454125787927&"
            "title=我的位置&"
            "content=西安市第五国际A座&"
            "output=html&"
            "src=webapp.baidu.openAPIdemo ")
    # url = ("http://api.map.baidu.com/direction/v2/transit?"
    #        "origin=34.323390409878144,108.95454125787927&"
    #        "destination=34.277799897830626,108.95309827919623&"
    #        "ak=%s")
    driver=webdriver.Chrome()
    driver.get(url=url)
    time.sleep(20)


if __name__ == '__main__':
    # print(map().json())
    print(map1())
    # print(type(map1_1()))
    # print (str(type(map1_1()["result"]["location"]["lat"])))
    # print(map1_1()["result"]["location"]["lng"])
