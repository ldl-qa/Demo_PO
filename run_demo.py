#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/11/22 0022 18:49
# @Author  : liudinglong
# @File    : run_demo.py
# @Description: 
# @Question: 
'''


import unittest

from Common import HTMLTestRunner3
import time
import os

root_file_path = os.path.split(os.path.realpath(__file__))[0]
report_path = os.path.join(root_file_path,'Report')


def run():
    test_dir = './Testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test_*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner3.HTMLTestRunner(
            stream=f,
            title=u'UI自动化测试报告，测试结果如下：',
            description=u'用例执行情况：'
        )
        runner.run(suite)
run()