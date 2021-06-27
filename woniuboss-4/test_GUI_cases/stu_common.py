#! /usr/bin/env python
# coding = utf-8
# editor:wang
#! /usr/bin/env python
# coding = utf-8
# editor:wang

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Common:

    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://106.13.36.122:8080/WoniuBoss2.5/")
        self.driver.minimize_window()
        self.driver.implicitly_wait(2)

    def mylogin(self,uname='WNCD000',isdecode='是'):
        if isdecode == '是':
            self.input_text(how=By.NAME, what='userName', content=uname)
            self.input_text(how=By.NAME, what='userPass', content='woniu123')
            self.input_text(how=By.NAME, what='checkcode', content='0000')
            self.doclick(how=By.XPATH,
                         what='/html/body/div[1]/div/div/div[2]/button')
            time.sleep(2)
            self.doclick(how=By.XPATH, what='//*[@id="btn-decrypt"]')
            try:
                self.switch_alert('woniu123')
            except:
                self.input_text(how=By.XPATH,what='//*[@id="secondPass-modal"]/div/div/div[2]/input',content='woniu123')
                self.doclick(how=By.XPATH,what='//*[@id="secondPass-modal"]/div/div/div[3]/button')
            return self.driver
        else:
            self.input_text(how=By.NAME, what='userName', content=uname)
            self.input_text(how=By.NAME, what='userPass', content='woniu123')
            self.input_text(how=By.NAME, what='checkcode', content='0000')
            self.doclick(how=By.XPATH,
                         what='/html/body/div[1]/div/div/div[2]/button')
            time.sleep(2)
            return self.driver




    def loginout_close(self):
        self.driver.close()


    def input_text(self,how,what,content):
        time.sleep(2)
        element = self.driver.find_element(how,what)
        element.clear()
        element.send_keys(content)
        return self.driver

    def doclick(self,how,what):
        time.sleep(2)
        self.driver.find_element(how,what).click()
        return self.driver

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def get_src(self,how,what):
        src = self.driver.find_element(how,what).get_attribute('src')
        return src


    def find_driver(self,how,what):
        time.sleep(2)
        self.driver.find_element(how, what)



    def select_box(self,how,what,select_txt):
        time.sleep(2)
        Select(self.driver.find_element(how,what)).select_by_visible_text(select_txt)
        return self.driver


    def get_allselect(self,how,what):
        time.sleep(2)
        content = self.driver.find_element(how, what).text
        return content

    def get_text(self,how,what):
        time.sleep(2)
        content = self.driver.find_element(how, what).text
        return content

    def switch_alert(self,content):
        alert = self.driver.switch_to.alert
        alert.send_keys(content)
        alert.accept()
        return self.driver
