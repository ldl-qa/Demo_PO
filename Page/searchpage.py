#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/11/22 0022 18:38
# @Author  : liudinglong
# @File    : SearchPage.py
# @Description: 
# @Question: 
'''

from selenium.webdriver.common.by import By
from Common.basepage import  BasePage

class SearchPage(BasePage):
    # 定位元素
    search_loc = (By.ID,"kw") #搜索框
    btn_loc = (By.ID,"su")    #搜索按钮

    # 重写父类的open()方法
    def open(self):
        self._open(self.base_url)

    def search_content(self,content):
        # 调用父类的find_emelemt，然后将本类的参数传入
        content1 =  self.find_emelemt(*self.search_loc)
        content1.send_keys(content)

    def btn_click(self):
        btn1 = self.find_emelemt(*self.btn_loc)
        btn1.click()