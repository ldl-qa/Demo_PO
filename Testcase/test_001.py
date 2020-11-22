#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/11/22 0022 18:40
# @Author  : liudinglong
# @File    : test_001.py
# @Description: 
# @Question: 
'''

from unittest import TestCase
import unittest
from selenium import webdriver
from time import sleep
from Page.searchpage import SearchPage
class CaseRun(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com"
        sleep(3)
        self.content = "selenium"
    # 测试步骤
    def test_search(self):
        bing_page = SearchPage(self.driver,self.url)
        bing_page.open()
        bing_page.search_content(self.content)
        try:
            bing_page.btn_click()
            sleep(3)
            print("查询成功")
        except Exception as Error:
            print(Error)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()