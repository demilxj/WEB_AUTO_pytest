# -*- coding: utf-8 -*-
# @Time : 2021/3/17 13:29
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : index_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.indexpage_locators import IndexPageLocators as ioc
import random
from Common.basepage import BasePage


class IndexPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def isExist_logout_ele(self):
        # 如果存在就返回True 不存在就返回False
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ioc.exit_button))
            return True
        except:
            return False

    # 修改任务操作-默认选未启动任务中的第一个   --元素定位的时候，过滤掉不可以修改（已启动）的任务
    def click_first_task(self):
        doc = '任务管理页面-点击第一个编辑任务按钮功能'
        self.click_element(ioc.edit_task_button, doc)

    # 修改任务操作-从未启动任务中随机选一个   --元素定位的时候，过滤掉不可以修改（已启动）的任务
    def click_random_task(self):
        doc = '任务管理页面-点击随机一个编辑任务按钮功能'
        # 找到所有符合的任务
        eles = self.get_elements(ioc.edit_task_button, doc)
        # 随机数
        index = random.randint(0, len(eles)-1)
        eles[index].click()



