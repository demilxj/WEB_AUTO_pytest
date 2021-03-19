# -*- coding: utf-8 -*-
# @Time : 2021/3/18 10:04
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : taskpage_locators.py

from selenium.webdriver.common.by import By


class TaskPageLocators:
    # 元素定位
    # 任务名输入框
    taskname_text = (By.ID, 'task_name')
    # 保存按钮
    save_button = (By.ID, 'wd_save_taskout')