# -*- coding: utf-8 -*-
# @Time : 2021/3/17 17:03
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : indexpage_locators.py

from selenium.webdriver.common.by import By


class IndexPageLocators:
    # 元素定位
    # 退出按钮
    exit_button = (By.ID, 'user_a')
    # 未启动的任务的修改按钮
    edit_task_button = (By.XPATH, '//td[text()="未启动"]/following-sibling::td//a[@title="修改任务"]')
