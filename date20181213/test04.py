#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/13 20:27
# software: PyCharm

# 3.假设一个小球从20米高落下，然后在弹起，让后再落下，每
# # 次跳起的高度为上一次的一半，那么，20次后小球运行了多少
# # 米！

class ball:

    def count(self,time):
        a=20
        b=20
        s=0
        counts=0
        while counts<time-1:
            counts+=1
            a=b
            b=a/2
            s+= (2*b)
        return s+20
if __name__ == '__main__':

    print(ball().count(20))
