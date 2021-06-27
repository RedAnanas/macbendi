#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/13 15:08
# software: PyCharm

# 2.编写三个类：person、teacher、student，teacher和
# student需继承于person，student需重写person中的
# make_money方法。
# 3.在上面的例子中另外再创建一个类class_room,
# class_room中有成员teacher和student对象，还有teach
# 方法。（组合）

class person:
    name=""
    age=0
    sex=""
    #定义构造方法
    def __init__(self,n):
        self.name=n
        # self.age=a
        # self.sex=s
    #定义方法
    def make_money(self):
        print("%s挣钱"%(self.name))
class teacher(person):
    def __init__(self,n):
        person.__init__(self,n)


    def make_money(self):
        print("%s上课挣钱" % (self.name))

class student(person):
    snom=0
    clas=""

    def __init__(self, n):
        person.__init__(self, n,)


    def make_money(self):
        print("%s学生打工挣钱" % (self.name))

class class_room:
    def __init__(self,tname,sname):
        self.t=teacher(tname)
        self.s=student(sname)

    def teach(self):
        print("%s正在教%s学习"%(self.t.name,self.s.name))


if __name__ == '__main__':
    g=teacher("王")
    g.make_money()

    f=student("王")
    f.make_money()

    h=class_room("王","张")
    h.teach()


