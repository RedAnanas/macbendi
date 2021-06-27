#! /usr/bin/env python
# coding = utf-8
# editor:wang

import requests
session = requests.session()
resp = session.get('http://106.13.36.122:8080/WoniuBoss2.5/log/userLogin?userName=WNCD000&userPass=woniu123&checkcode=0000')

resp = session.get('http://106.13.36.122:8080/WoniuBoss2.5/student/saveMornExam?me.morn_exam_student_id=1254&me.type=随堂问答&me.score=90&me.question=讲一下你对测试的理解\n分析-设计-实现-执行')
print(resp.text)