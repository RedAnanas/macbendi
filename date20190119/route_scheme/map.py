#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/19 13:45
# software: PyCharm
from date20190119.route_scheme.browser import *
import requests

class map:
    def __init__(self):
        self.ak="MKzM9GLcWkcIOzBvTIkG7ujMLazfzNEe"

    def get_Position_Info(self,address):
        self.session = requests.session()
        self.site=(self.session.get("http://api.map.baidu.com/geocoder/v2/"
                            "?address=%s&"
                            "output=json&"
                            "ak=%s&"% (address, self.ak))).json()
        self.lat=str(self.site["result"]["location"]["lat"])
        self.lng=str(self.site["result"]["location"]["lng"])
        return self.lat,self.lng
    def trip_mode(self,trip_mode):
        if trip_mode=="公交":
            return "transit"
        elif trip_mode=="驾车":
            return "driving"
        elif trip_mode=="步行":
            return "walking"
        else:
            print("输入错误，请重新输入")

    def path(self,start_lat,start_lng,start,end_lat,end_lng,end,trip_mode):

        url=("http://api.map.baidu.com/direction?"
             "origin=latlng:%s,%s|name:%s&"
             "destination=latlng:%s,%s|name:%s&"
             "mode=%s"
             "&region=西安"
             "&output=html&"
             "src=webapp.baidu.openAPIdemo"
             %(start_lat,start_lng,start,end_lat,end_lng,end,trip_mode))
        BrowserManager(url)