# -*- coding: utf-8 -*-
# @Time : 2021/3/18 15:10
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : dir_config.py

import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 测试数据路径
testdatas_dir = os.path.join(base_dir, "TestDatas")

# 测试用例路径
testcases_dir = os.path.join(base_dir, "TestCases")

# 测试报告路径
htmlreport_dir = os.path.join(base_dir, "Outputs/reports")

# 日志文件路径
# logs_dir = os.path.join(base_dir, "Outputs/logs")
logs_dir = os.path.join(base_dir, 'Outputs', 'logs', 'test_log.txt')

# 文件配置路径
# config_dir = os.path.join(base_dir, "Config")

# 截图文件路径
screenshot_dir = os.path.join(base_dir, "Outputs/screenshots")
