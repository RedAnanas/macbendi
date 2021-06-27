#! /usr/bin/env python
# coding = utf-8
# editor:wang

import unittest,time,os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support.select import Select
from test_GUI_cases.stu_common import Common


class Student_GUI_02(unittest.TestCase):

    def setUp(self):
        self.error = []
        self.countfail = 0
        self.bm = Common()

    def tearDown(self):
        self.bm.loginout_close()

    # 阶段测评查询
    def test_query_01(self,uname='WNCD000'):
        self.error = []
        try:
            # 默认为管理员登录，若非管理员可传参数进去
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='阶段测评')
            data = {"班级":"WNCDC034","方向":"公共","姓名":"陈浩"}
            # 下拉框选择
            if data['班级'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="examination"]/div[1]/select[1]', select_txt=data['班级'])
            if data['方向'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="examination"]/div[1]/select[2]', select_txt=data['方向'])
            if data['姓名'] != '':
                self.bm.input_text(how=By.XPATH, what='//*[@id="examination"]/div[1]/input',content =data['姓名'])
            # 点击查询按钮
            self.bm.doclick(how=By.XPATH,what='//*[@id="examination"]/div[1]/button')
            actual = self.bm.get_text(how=By.XPATH,what='//*[@id="exam-table"]/tbody/tr')
            # 断言查询结果姓名为输入的姓名
            self.assertIn(data['姓名'],actual)
        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_query_01 执行成功')
        else:
            print('test_query_01 执行失败')
            raise AssertionError(*self.error)

    # 阶段测评-测评
    def test_dotest_02(self,uname='WNCD000'):
        self.error = []
        try:
            # 默认为管理员登录，若非管理员可传参数进去
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='阶段测评')
            data = {"班级":"WNCDC034","方向":"公共","姓名":"陈浩"}
            info = {"阶段":"公共基础阶段","成绩":"90","评语":"测试1"}
            # 下拉框选择
            if data['姓名'] != '':
                self.bm.input_text(how=By.XPATH, what='//*[@id="examination"]/div[1]/input', content=data['姓名'])
            # 点击查询按钮
            self.bm.doclick(how=By.XPATH,what='//*[@id="examination"]/div[1]/button')
            # 点击测评并输入测评内容
            self.bm.doclick(how=By.XPATH, what='//*[@id="exam-table"]/tbody/tr/td[6]/button[1]')
            if info['阶段'] != '':
                self.bm.select_box(how=By.NAME, what='pe.phase', select_txt=info['阶段'])
            if info['成绩'] != '':
                self.bm.input_text(how=By.NAME, what='pe.score', content=info['成绩'])
            if info['评语'] != '':
                self.bm.input_text(how=By.NAME, what='pe.comment', content=info['评语'])
            # 点击确定
            self.bm.doclick(how=By.ID, what='saveStageBtn')
            # 点击测评记录查询测评是否正常保存
            self.bm.doclick(how=By.LINK_TEXT, what='测评记录')
            self.bm.input_text(how=By.XPATH, what='//*[@id="stagetest"]/div[1]/input', content=data['姓名'])
            self.bm.doclick(how=By.XPATH, what='//*[@id="stagetest"]/div[1]/button')
            actual = self.bm.get_text(how=By.XPATH, what='//*[@id="pe-result"]/tbody/tr')
            self.assertIn(data['姓名'],actual)
        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_dotest_02 执行成功')
        else:
            print('test_dotest_02 执行失败')
            raise AssertionError(*self.error)

    # 转就业
    def test_employ_03(self,uname='WNCD000'):
        self.error = []
        try:
            # 默认为管理员登录，若非管理员可传参数进去
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='阶段测评')
            data = {"班级":"WNCDC034","方向":"公共","姓名":"万宝霖"}
            info = {"阶段":"项目实战阶段","成绩":"","评语":""}
            # 下拉框选择
            if data['姓名'] != '':
                self.bm.input_text(how=By.XPATH, what='//*[@id="examination"]/div[1]/input', content=data['姓名'])
            # 点击查询按钮
            self.bm.doclick(how=By.XPATH,what='//*[@id="examination"]/div[1]/button')
            # 点击测评
            self.bm.doclick(how=By.XPATH, what='//*[@id="exam-table"]/tbody/tr/td[6]/button[1]')
            # 选择为项目实战阶段并转就业选择是
            if info['阶段'] == '项目实战阶段':
                self.bm.select_box(how=By.NAME, what='pe.phase', select_txt=info['阶段'])
                self.bm.doclick(how=By.XPATH,what='//*[@id="toEmployment"]/input[1]')
            if info['成绩'] != '':
                self.bm.input_text(how=By.NAME, what='pe.score', content=info['成绩'])
            if info['评语'] != '':
                self.bm.input_text(how=By.NAME, what='pe.comment', content=info['评语'])
            # 点击确定
            self.bm.doclick(how=By.ID, what='saveStageBtn')
            # 查找转就业学生已不在此
            self.bm.input_text(how=By.XPATH, what='//*[@id="examination"]/div[1]/input', content=data['姓名'])
            self.bm.doclick(how=By.XPATH, what='//*[@id="examination"]/div[1]/button')
            actual = self.bm.get_text(how=By.XPATH, what='//*[@id="exam-table"]/tbody/tr/td')
            self.assertEqual('无符合条件的记录',actual)
        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_employ_03 执行成功')
        else:
            print('test_employ_03 执行失败')
            raise AssertionError(*self.error)

    # 降级
    def test_get_down_04(self,uname='WNCD000'):
        self.error = []
        try:
            # 默认为管理员登录，若非管理员可传参数进去
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='阶段测评')
            data = {"姓名":"刘吉斌"}
            info = {"方向":"公共","班级":"WNCDC034"}
            # 下拉框选择
            if data['姓名'] != '':
                self.bm.input_text(how=By.XPATH, what='//*[@id="examination"]/div[1]/input', content=data['姓名'])
            # 点击查询按钮
            self.bm.doclick(how=By.XPATH,what='//*[@id="examination"]/div[1]/button')
            # 点击降级
            self.bm.doclick(how=By.XPATH, what='//*[@id="exam-table"]/tbody/tr/td[6]/button[2]')
            if info['方向'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="repeat-form"]/div/div[2]/div[2]/select', select_txt=info['方向'])
            if info['班级'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="repeat-form"]/div/div[2]/div[3]/select', select_txt=info['班级'])
            # 点击确定
            self.bm.doclick(how=By.ID, what='saveRepeatBtn')
            # 查看降级班级是否成功
            self.bm.input_text(how=By.XPATH, what='//*[@id="examination"]/div[1]/input', content=data['姓名'])
            self.bm.doclick(how=By.XPATH, what='//*[@id="examination"]/div[1]/button')
            actual = self.bm.get_text(how=By.XPATH, what='//*[@id="exam-table"]/tbody/tr')
            self.assertIn(data['姓名'],actual)
            self.assertIn(info['班级'],actual)

        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_get_down_04 执行成功')
        else:
            print('test_get_down_04 执行失败')
            raise AssertionError(*self.error)


    # 测评记录查询
    def test_query_measure_05(self,uname='WNCD000'):
        self.error = []
        try:
            # 默认为管理员登录，若非管理员可传参数进去
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='测评记录')
            data = {"班级":"全部","方向":"全部","阶段":"全部","姓名":""}
            # 下拉框选择
            if data['班级'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="stagetest"]/div[1]/select[1]', select_txt=data['班级'])
            if data['方向'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="stagetest"]/div[1]/select[2]', select_txt=data['方向'])
            if data['阶段'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="stagetest"]/div[1]/select[3]', select_txt=data['阶段'])
            if data['姓名'] != '':
                self.bm.input_text(how=By.XPATH, what='//*[@id="stagetest"]/div[1]/input',content =data['姓名'])
            # 点击确定按钮
            self.bm.doclick(how=By.XPATH,what='//*[@id="stagetest"]/div[1]/button')
            actual = self.bm.get_text(how=By.XPATH,what='//*[@id="stagetest"]/div[2]/div[2]/div[4]/div[1]/span[1]')
            # 可以查询到记录断言为左下角提示信息
            self.assertIn('记录',actual)
        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_query_measure_05 执行成功')
        else:
            print('test_query_measure_05 执行失败')
            raise AssertionError(*self.error)

    # 课程安排查询
    def test_schedule_06(self,uname='WNCD000'):
        self.error = []
        try:
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='课程安排')
            data = {"讲师": "邓乃文"}
            if data['讲师'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="course"]/div[1]/select', select_txt=data['讲师'])
            actual = self.bm.get_text(how=By.XPATH, what='//*[@id="course"]/div[2]/div[2]/div[4]/div[1]/span[1]')
            self.assertIn('记录', actual)
        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_schedule_06 执行成功')
        else:
            print('test_schedule_06 执行失败')
            raise AssertionError(*self.error)

    # 修改课程
    def test_change_schedule_07(self,uname='WNCD000'):
        self.error = []
        try:
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='课程安排')
            data = {"讲师": "邓乃文"}
            info = {'开始时间':'2019-03-02',"结束时间":"2019-03-30","状态":"正常","方向":"公共","课程模块":"基础阶段第一周-HTML5+CSS3","班号":"WNCDC034","班级":"教室一"}
            # 选择讲师
            if data['讲师'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="course"]/div[1]/select',select_txt=data['讲师'])
            # 点击修改按钮
            self.bm.doclick(how=By.XPATH,what='//*[@id="course_table"]/tbody/tr[1]/td[10]/button')
            # 输入修改内容
            if info['开始时间'] != '':
                start_time = self.bm.driver.find_element(By.XPATH, '//*[@id="modifyCourseForm"]/div/div/div[1]/input')
                start_time.send_keys(Keys.DELETE)
                start_time.send_keys(info['开始时间'])
            if info['结束时间'] != '':
                start_time = self.bm.driver.find_element(By.XPATH, '//*[@id="modifyCourseForm"]/div/div/div[2]/input')
                start_time.send_keys(Keys.DELETE)
                start_time.send_keys(info['结束时间'])
            if info['状态'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="modifyCourseForm"]/div/div/div[4]/select', select_txt=info['状态'])
            if info['方向'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="modifyCourseForm"]/div/div/div[5]/select', select_txt=info['方向'])
            if info['课程模块'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="modifyCourseForm"]/div/div/div[6]/select', select_txt=info['课程模块'])
            if info['班号'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="modifyCourseForm"]/div/div/div[7]/select', select_txt=info['班号'])
            if info['班级'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="modifyCourseForm"]/div/div/div[8]/select', select_txt=info['班级'])
            # 点击保存
            self.bm.doclick(how=By.XPATH,what='//*[@id="modifyCourse"]/div/div/div[2]/button')
            actual = self.bm.get_text(how=By.XPATH, what='//*[@id="course_table"]/tbody/tr[1]')
            self.assertIn(info['结束时间'], actual)
        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_change_schedule_07 执行成功')
        else:
            print('test_change_schedule_07 执行失败')
            raise AssertionError(*self.error)


    # 新增排课
    def test_new_schedule_08(self,uname='WNCD000'):
        self.error = []
        try:
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='课程安排')
            # 点击新增排课
            self.bm.doclick(how=By.XPATH, what='//*[@id="course"]/div[1]/button')
            info = {'开始时间':'2019-03-30',"结束时间":"2019-04-13",
                    "李懿":"休息","尹瑞":"休息","王欢欢":"休息","周海峰":"休息","许敏":"休息",
                    "邓乃文":"正常","曾云莲":"休息","徐小兵":"休息","代虎军":"休息",
                    "教室":"教室一","班号":"WNCDC034","方向":"公共","课程安排":"基础阶段第一周-HTML5+CSS3",}
            # 输入排课内容
            if info['开始时间'] != '':
                start_time = self.bm.driver.find_element(By.XPATH, '//*[@id="addcourse"]/div/div[1]/input')
                start_time.send_keys(Keys.DELETE)
                start_time.send_keys(info['开始时间'])
            if info['结束时间'] != '':
                start_time = self.bm.driver.find_element(By.XPATH, '//*[@id="addcourse"]/div/div[2]/input')
                start_time.send_keys(Keys.DELETE)
                start_time.send_keys(info['结束时间'])
                # 此处仅给邓乃文老师做新增排课因此其他老师选择为休息
            if info['李懿'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[1]/td[3]/select', select_txt=info['李懿'])
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[2]/td[3]/select', select_txt=info['李懿'])
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[3]/td[3]/select', select_txt=info['李懿'])
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[4]/td[3]/select', select_txt=info['李懿'])
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[5]/td[3]/select', select_txt=info['李懿'])
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[7]/td[3]/select', select_txt=info['李懿'])
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[8]/td[3]/select', select_txt=info['李懿'])
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[9]/td[3]/select', select_txt=info['李懿'])
            if info['邓乃文'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[6]/td[3]/select', select_txt=info['邓乃文'])
            if info['教室'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[6]/td[4]/select', select_txt=info['教室'])
            if info['班号'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[6]/td[5]/select', select_txt=info['班号'])
            if info['方向'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[6]/td[6]/select', select_txt=info['方向'])
            if info['课程安排'] != '':
                self.bm.select_box(how=By.XPATH, what='//*[@id="addCourse-table"]/tr[6]/td[7]/select', select_txt=info['课程安排'])
            # # 点击保存并关闭
            # self.bm.doclick(how=By.XPATH,what='//*[@id="course-add"]/div/div/div[3]/button[2]')
            # actual = self.bm.get_text(how=By.XPATH, what='//*[@id="course_table"]/tbody/tr[9]/td[8]')
            # self.assertEqual(info['开始时间'], actual)
            # 点击继续排课
            self.bm.doclick(how=By.XPATH,what='//*[@id="course-add"]/div/div/div[3]/button[1]')
            actual = self.bm.get_text(how=By.ID, what='saveCourseInfo')
            self.assertEqual('保存成功.',actual)

        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_new_schedule_08 执行成功')
        else:
            print('test_new_schedule_08 执行失败')
            raise AssertionError(*self.error)


#     上传假条
    def test_upload_09(self, uname='WNCD000'):
        self.error = []
        try:
            self.bm.mylogin(uname)
            self.bm.doclick(how=By.LINK_TEXT, what='学员管理')
            self.bm.doclick(how=By.LINK_TEXT, what='学员请假')
            # 点击假条
            self.bm.select_box(how=By.XPATH,what='//*[@id="leave"]/div[1]/select',select_txt='请假中')
            self.bm.doclick(how=By.XPATH,what='//*[@id="leave-table"]/tbody/tr/td[13]/button[1]')
            # 点击选择文件
            # self.bm.doclick(how=By.ID,what='selectStuLeave')
            # 获取当前地址
            dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            path = dir_path+'\\GUI_data\\leave_note.jpg'
            # 上传文件
            self.bm.input_text(how=By.ID,what='selectStuLeave',content=path)
            # 点击保存
            self.bm.doclick(how=By.XPATH,what='//*[@id="leavePermit-modal"]/div/div/div[3]/button')
            # 点击假条
            self.bm.doclick(how=By.XPATH,what='//*[@id="leave-table"]/tbody/tr[1]/td[13]/button[1]')
            # 获取src以作断言
            src = self.bm.get_src(how=By.XPATH, what='//*[@id="leavePermit-form"]/div[1]/img')
            self.assertIn('upload', src)
        except Exception as e:
            self.error.append(str(e))
        if self.error == []:
            print('test_upload_09 执行成功')
        else:
            print('test_upload_09 执行失败')
            raise AssertionError(*self.error)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Student_GUI_02('test_new_schedule_08'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)