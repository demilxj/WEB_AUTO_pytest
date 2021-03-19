# -*- coding: utf-8 -*-
# @Time : 2021/3/18 9:44
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : task_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.taskpage_locators import TaskPageLocators as toc
from Common.basepage import BasePage


class TaskPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # 修改任务
    def general_edit(self, taskname):
        # 在输入框中修改任务名称
        # 点击保存按钮
        doc = "修改任务页面_修改任务名称功能"
        self.wait_eleVisible(toc.taskname_text, doc=doc)
        self.input_text(toc.taskname_text, taskname, doc=doc)
        self.click_element(toc.save_button, doc=doc)

