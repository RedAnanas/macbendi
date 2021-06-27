#! /usr/bin/env python
# coding = utf-8
# editor":"wang

import requests
con = requests.session()
con.get('http://106.13.36.122:8080/WoniuBoss2.0/log/userLogin?userName=WNCD000&userPass=woniu123&checkcode=0000')

# data1 = {"pe.phase_exam_student_id":"1256","pe_orientation1":"",
#         "pe_class1":"","pe.phase":" 公共基础阶段","pe.score":"88","status":"1","pe.comment":"邓强试测试"}
# con.post('http://106.13.36.122:8080/WoniuBoss2.0/student/saveScore',data=data1)

# data2 = {"pageSize":"10","pageIndex":"1","stuClass":"WNCDC034","orientation":"","stuName":"王森"}
#
# resp = con.post('http://106.13.36.122:8080/WoniuBoss2.0/student/queryStuScore',data=data2)
# print(resp.status_code,resp.json())
#
#
# data3 = {'pageSize': '10', 'pageIndex': '1', 'stuClass': '',
#          'orientation': '', 'stuName': '敬大彦', 'phase': ''}
#
# resp = con.post('http://192.168.6.244:8080/WoniuBoss2.0/student/showPhaseExam',data=data3)
# print(resp.status_code,resp.json())



# data3 = {"stuIdArr[]":"1253","stuClass":"WNCDC033","orientation":"公共"}
#
# resp = con.post('http://106.13.36.122:8080/WoniuBoss2.0/student/allocate',data=data3)
# print(resp.status_code,resp.content.decode())


# data4 = {'pageSize': '10', 'pageIndex': '1', 'courseTime': '', 'courseTeacher': '全部'}
#
# resp = con.post('http://106.13.36.122:8080/WoniuBoss2.0/student/queryCourse',data=data4)
# print(resp.status_code,resp.content.decode())

# data5 = {"cur.id":"670","cur.classroom_id":"19","cur.course_id":"26","cur.start_time":"2019-02-22","cur.end_time":"2019-02-22","teacherName":"代虎军","cur.teacher_status":"正常","orientation":"测试","course_id":"26","class_no":"WNCDC025","classroom_id":"19"}
#
# resp = con.post('http://106.13.36.122:8080/WoniuBoss2.0/student/saveModifyCourse',data=data5)
# print(resp.status_code,resp.content.decode())


data6 = {'arr':'[{"work_id":"WNCD005","classroom_id":"全部","class_no":"全部",'
               '"orientation":"全部","course_id":"全部","teacher_status":"休息"},'
               '{"work_id":"WNCD056","classroom_id":"全部","class_no":"全部",'
               '"orientation":"全部","course_id":"全部","teacher_status":"休息"},'
               '{"work_id":"WNCD024","classroom_id":"全部","class_no":"全部",'
               '"orientation":"全部","course_id":"全部","teacher_status":"休息"},'
               '{"work_id":"WNCD028","classroom_id":"全部","class_no":"全部",'
               '"orientation":"全部","course_id":"全部","teacher_status":"休息"},'
               '{"work_id":"WNCD030","classroom_id":"全部","class_no":"全部",'
               '"orientation":"全部","course_id":"全部","teacher_status":"休息"},'
               '{"work_id":"WNCD051","classroom_id":"1","class_no":"WNCDC034",'
               '"orientation":"公共","course_id":"1","teacher_status":"正常"},'
               '{"work_id":"WNCD046","classroom_id":"全部","class_no":"全部",'
               '"orientation":"全部","course_id":"全部","teacher_status":"休息"},'
               '{"work_id":"WNCD060","classroom_id":"全部","class_no":"全部",'
               '"orientation":"全部","course_id":"全部","teacher_status":"休息"},'
               '{"work_id":"WNCD067","classroom_id":"全部","class_no":"全部",'
               '"orientation":"全部","course_id":"全部","teacher_status":"休息"}]',
         'startTime':'2019-02-01','endTime':'2019-03-30'}

resp = con.post('http://106.13.36.122:8080/WoniuBoss2.0/student/saveCourse',data=data6)
print(resp.status_code,resp.content.decode())

