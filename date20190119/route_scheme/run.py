#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/19 19:06
# software: PyCharm
from date20190119.route_scheme.map import *
class Run():
    def go_run(self):
        self.start=input("请输入起点：")
        self.end=input("请输入终点：")
        self.trip_mode=input("请输入出行方式(公交，驾车，步行)：")
        self.trip_mode1=map().trip_mode(self.trip_mode)

        start_point=map().get_Position_Info(self.start)
        end_point=map().get_Position_Info(self.end)

        map().path(start_point[0],start_point[1],self.start,
                   end_point[0],end_point[1],self.end,self.trip_mode1)

if __name__ == '__main__':
    Run().go_run()