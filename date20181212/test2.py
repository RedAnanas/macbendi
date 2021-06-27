#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/12 14:23
# software: PyCharm

# 定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高分数的课程。get_course()
# 4 返回该学生的平均成绩get_avg()

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade


