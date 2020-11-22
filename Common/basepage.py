#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/11/22 0022 16:07
# @Author  : liudinglong
# @File    : basepage.py
# @Description: 
# @Question: 
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self,driver,url):
        """

        @param driver:
        @param base_url:
        """
        self.dr = driver
        self.base_url =  url

    # 定义私有方法，类对象和子类可以访问
    def _open(self,url):
        self.dr.get(url)
        self.dr.maximize_window()

    # 定义open方法，调用_open方法
    def open(self):
        self._open(self.base_url)

    def find_emelemt(self,*loc):
        try:
            WebDriverWait(self.dr,10).until(EC.visibility_of_all_elements_located(loc))
            return self.dr.find_element(*loc)
        except:
            print("页面中没有%s元素"%(self.loc))

    # 定义script()方法，用于执行JS脚本，比方上上传文件啥的
    def script(self, src):
        self.dr.excute_script(src)

        # 定义页面跳转方法，比方说有的页面有frame嵌套

    def switch_frame(self, loc):
        return self.dr.switch_to_frame(loc)

        # 重新定义send_keys()方法，为了保证搜索按钮是否存在，还有有的输入框中默认有值，要清空

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            # getattr方法相当于实现了self.loc
            loc = getattr(self, "_%s" % loc)
            # 是否存在搜索按钮
            if click_first:
                self.find_emelemt(*loc).click()
            # 清空搜索框中的值，并输入需要搜索的值
            if clear_first:
                self.find_emelemt(*loc).clear()
                self.find_emelemt(*loc).send_keys(value)

        except:
            print("页面上未找到%s元素" % (self.loc))
