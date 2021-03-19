# -*- coding: utf-8 -*-
# @Time : 2021/3/17 17:03
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : loginpage_locators.py

from selenium.webdriver.common.by import By


class LoginPageLocators:
    # 元素定位
    # 用户名输入框
    name_text = (By.XPATH, '//input[@name="username"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_button = (By.XPATH, '//input[@id="login_btn"]')
    # 记住账号密码复选框
    remember = (By.XPATH, '//input[@name="remember-me"]')
    # 错误提示框确定按钮
    errorMsg_from_loginAreaCentre1 = (By.XPATH, '//div[@id="layui-layer1"]//a[text()="确定"]')
    # 错误提示框文本
    errorMsg_from_loginAreaCentre2 = (By.XPATH, '//div[@class="layui-layer-content"]/div')
    # 错误信息
    errorMsg_from_loginArea2 = (By.XPATH, '//p[@textname="warnTip0"]')