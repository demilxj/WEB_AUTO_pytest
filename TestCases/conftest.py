# -*- coding: utf-8 -*-
# @Time : 2021/3/19 10:36
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : conftest.py

import pytest
from selenium import webdriver
from TestDatas import Common_Datas as CD
from PageObjects.login_page import LoginPage


driver = None

@pytest.fixture(scope="class")   # 默认为scope="function"级别。一般接口用例连接数据库用session级别
def access_web():
    # 前置条件
    global driver
    print("===============所有测试用例之前的setUp，整个用例类只执行一次===============")
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)   # 前置后置分隔线 # 后面借返回值
    # 后置条件
    print("===============所有测试用例后前的tearDown，整个用例类只执行一次===============")
    driver.quit()


@pytest.fixture()
def refresh_page():
    global driver
    # 前置条件
    yield
    # 后置条件
    driver.refresh()
