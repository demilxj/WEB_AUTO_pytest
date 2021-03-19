# -*- coding: utf-8 -*-
# @Time : 2021/3/18 15:59
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : main.py

# import unittest
# from HTMLTestRunnerNew import HTMLTestRunner
# from Common.dir_config import *
#
# # 实例化套件对象
# s = unittest.TestSuite()
# # TestLoader的用法
# # 1.实例化TestLoader对象
# # 2.使用discover去找到一个目录下的所有
# # 3.使用s
# loader = unittest.TestLoader()
# s.addTests(loader.discover(testcases_dir))
# # # 运行
# # runner = unittest.TextTestRunner(testcases_dir)
# # runner.run(s)
#
# fp = open(htmlreport_dir+'/autoTest_report.html',  'wb')
# runner = HTMLTestRunner(stream=fp,
#                         title='单元测试报告',
#                         description='单元测试报告',
#                         tester='demi')
# runner.run(s)