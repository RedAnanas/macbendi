#! /usr/bin/env python
# coding = utf-8
# editor:wang

import unittest,time,HTMLTestRunner
# from woniuboss.common.Utility import Read_File
# from woniuboss.common.public_port import WoniuBoss
from woniubossV01.common.Utility import Read_File
from woniubossV01.common.public_port import WoniuBoss


class Student_02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.con = WoniuBoss()
        cls.file = Read_File()
        cls.table = cls.file.read_excel('../data/student_data_01.xlsx', 2)
        cls.errors = []
        cls.countsuccess = 0
        cls.countfail = 0
        cls.runtime = 0


    def tearDown(self):
        self.con.judge_method(method='get',url='http://106.13.36.122:8080/WoniuBoss2.0/log/logOut',data=None,headers=None)


    @classmethod
    def tearDownClass(cls):
        cls.con.close()

    def mylogin(self,uname,isdecode):
        if isdecode == '是':
            self.con.post_login_method6(uname)
            self.con.judge_method(method='get', url='http://106.13.36.122:8080/WoniuBoss2.0/second?vp=woniu123',
                                  data=None, headers=None)

        else:
            self.con.post_login_method6(uname)


    def get_para(self,i,moduname):
        row = self.table.row_values(i)
        info = self.file.dispose_params1(row[1])
        name = str(info.keys())[12:-3]
        title = info[name]
        code = row[0]
        if name == moduname:
            info = self.file.dispose_params1(row[1])
            name = str(info.keys())[12:-3]
            isdecode = row[2]
            uname = row[3]
            url = row[4]
            method = row[5].lower()
            data = self.file.dispose_params1(row[6])
            header = self.file.dispose_params1(row[7])
            exp_status = int(row[8])
            assert_method = row[9]
            value = row[10]
            expect = row[11]
            # return row,code,name,title,isdecode,uname,url,method,data,header,exp_status,assert_method,value,expect
        else:
            name = None
            isdecode=None
            uname=None
            url=None
            method=None
            data=None
            header=None
            exp_status=None
            assert_method=None
            value=None
            expect=None
        return row,code,name,title,isdecode,uname,url,method,data,header,exp_status,assert_method,value,expect

    def loginout(self):
        self.con.judge_method(method='get',url='http://106.13.36.122:8080/WoniuBoss2.5/log/logOut',data=None,headers=None)



    def student(self,moduname):
        self.countfail = 0
        self.errors = []
        flag = False
        for i in range(1,91):
            try:
                row,code,name,title, isdecode, uname, url, method, data, header, exp_status, \
                assert_method, value, expect = self.get_para(i,moduname)
                if expect != None:
                    desc = '%s - %s'%(code,title)
                    print('************** %s test start **************'%desc)
                    self.mylogin(uname,isdecode)
                    resp = self.con.judge_method(url=url,method=method,data=data,headers=header)
                    self.loginout()
                    if resp == None:
                        self.countfail+=1
                        print('result: %s test fail' % desc)
                    else:
                        if assert_method == 'json':
                            if isdecode == '是':
                                result = resp.json()['list']
                                if len(result):
                                    actual = result[0][value]
                                else:
                                    actual = 'fail'
                            else:
                                actual = '*****'
                        else:
                            actual = resp.content.decode()
                        flag,err_msg = self.assert_eq(i,resp,row,actual)
                        if flag and self.errors == []:
                            self.countsuccess += 1
                            print('result: %s test success' % desc)
                        else:
                            self.countfail += 1
                            print('result: %s test fail' % desc)
                            self.errors.append('学员管理模块编号%s标题%s的用例执行失败，原因：断言：%s'
                                               % (code, title, err_msg))
            except Exception as e:
                pass
                # self.errors.append('学员管理模块编号%s标题%s的用例执行失败，原因：断言：%s 其他：%s'
                #                    % (code, title,err_msg,str(e)))
                # raise AssertionError(*self.errors)
        if self.errors != []:
            # print('失败原因：%s'%self.errors)
            print(self.errors)
            raise AssertionError(*self.errors)

    def assert_eq(self,i,resp,row,actual):
        errors = []
        desc = '%s - %s'%(row[0],row[1])
        self.assertEqual(resp.status_code, int(row[8]))
        try:
            self.assertEqual(resp.status_code,int(row[8]))
            self.assertEqual(actual,row[11])
        except Exception as e:
            errors.append(str(e))

        return errors == [],errors
        # print(err_info)

    # 阶段测评查询学生信息
    def test_stu_01(self):
        print('test start'.center(80,'*'))
        begin = time.clock()
        # self.student(1,41)
        moduname = '查询信息1'
        self.student(moduname)
        self.runtime = time.clock()-begin
        print('test time: %d '%self.runtime)
        print('success: %d'%self.countsuccess)
        print('fail: %d'%self.countfail)
        print('test over'.center(80, '*'))


    # 查询单个学生信息
    def test_stu_02(self):
        print('test start'.center(80,'*'))
        begin = time.clock()
        moduname = '查询信息2'
        self.student(moduname)
        #此处17-18执行不成功，邓强账号所有查看功能未实现
        self.runtime = time.clock()-begin
        print('test time: %d '%self.runtime)
        print('success: %d'%self.countsuccess)
        print('fail: %d'%self.countfail)
        print('test over'.center(80, '*'))


    # 测评
    def test_stu_03(self):
        print('test start'.center(80,'*'))
        begin = time.clock()
        moduname = '测评'
        self.student(moduname)
        #此处21-22执行不成功，测评接口没有权限限制
        self.runtime = time.clock()-begin
        print('test time: %d '%self.runtime)
        print('success: %d'%self.countsuccess)
        print('fail: %d'%self.countfail)
        print('test over'.center(80, '*'))
        # if self.countfail !=  0:
        #     raise AssertionError

    # 测评记录
    def test_stu_04(self):
        print('test start'.center(80,'*'))
        begin = time.clock()
        moduname = '测评记录'
        self.student(moduname)
        #此处全部通过
        self.runtime = time.clock()-begin
        print('test time: %d '%self.runtime)
        print('success: %d'%self.countsuccess)
        print('fail: %d'%self.countfail)
        print('test over'.center(80, '*'))
        # if self.countfail !=  0:
        #     raise AssertionError

    # 分班
    def test_stu_05(self):
        print('test start'.center(80,'*'))
        begin = time.clock()
        moduname = '分班'
        self.student(moduname)
        #此处39未通过，此接口总经理无权点击
        self.runtime = time.clock()-begin
        print('test time: %d '%self.runtime)
        print('success: %d'%self.countsuccess)
        print('fail: %d'%self.countfail)
        print('test over'.center(80, '*'))
        # if self.countfail !=  0:
        #     raise AssertionError

        #少课程安排界面切换

    # 对教师安排课程
    def test_stu_06(self):
        print('test start'.center(80,'*'))
        begin = time.clock()
        moduname = '课程安排'
        self.student(moduname)
        self.runtime = time.clock()-begin
        print('test time: %d '%self.runtime)
        print('success: %d'%self.countsuccess)
        print('fail: %d'%self.countfail)
        print('test over'.center(80, '*'))


    def test_stu_07(self):
        print('test start'.center(80,'*'))
        begin = time.clock()
        moduname = '修改课程'
        self.student(moduname)
        self.runtime = time.clock()-begin
        print('test time: %d '%self.runtime)
        print('success: %d'%self.countsuccess)
        print('fail: %d'%self.countfail)
        print('test over'.center(80, '*'))



    # 新增排课
    def test_stu_08(self):
        print('test start'.center(80,'*'))
        begin = time.clock()
        moduname = '新增排课'
        self.student(moduname)
        self.runtime = time.clock()-begin
        print('test time: %d '%self.runtime)
        print('success: %d'%self.countsuccess)
        print('fail: %d'%self.countfail)
        print('test over'.center(80, '*'))
        # if self.countfail !=  0:
        #     raise AssertionError





if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Student_02)
    with open('../report/student_report.html','wb+') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='student mode test report',verbosity=2)
        runner.run(suite)

