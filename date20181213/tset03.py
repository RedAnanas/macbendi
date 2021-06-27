#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/13 20:08
# software: PyCharm

# 1.有一对兔子从出生后3月起一个月生一对小兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数

class rabbit:

    def count(self,month):
        a=0
        b=1
        counts=0
        while counts<month:
            counts+=1
            a,b=b,a+b
        return b
if __name__ == '__main__':
    print(rabbit().count(9))
