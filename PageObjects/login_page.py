# -*- coding: utf-8 -*-
# @Time : 2021/3/17 13:28
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : login_page.py

from PageLocators.loginpage_locators import LoginPageLocators as loc
from Common.basepage import BasePage


class LoginPage(BasePage):

    # 登录操作
    def login(self, username, passwd, remember_user=False):
        # 输入用户名
        # 输入密码
        # 点击登录
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.name_text, doc=doc)   # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.name_text))
        self.input_text(loc.name_text, username, doc=doc)   # self.driver.find_element(*loc.name_text).send_keys(username)
        self.input_text(loc.pwd_text, passwd, doc=doc)   # self.driver.find_element(*loc.pwd_text).send_keys(passwd)
        # 判断以下remember_user的值，来决定 是否勾选
        if remember_user is True:
            self.click_element(loc.remember, doc=doc)   # self.driver.find_element(*loc.remember).click()
        self.click_element(loc.login_button, doc=doc)   # self.driver.find_element(*loc.login_button).click()

    # 注册入口
    def register_enter(self):
        pass

    # 忘记密码入口
    def forgetpwd_enter(self):
        pass

    # 获取错误的提示信息-登录区域弹出
    def get_errorMsg_from_loginArea1(self):
        pass

    # 获取错误的提示信息-页面中间弹出
    def get_errorMsg_from_loginAreaCentre(self):
        doc = "登录页面_获取错误的提示信息1"
        self.wait_eleVisible(loc.errorMsg_from_loginAreaCentre1, doc=doc)
        return self.get_text(loc.errorMsg_from_loginAreaCentre2)

    # 获取错误的提示信息-登录区域提示
    def get_errorMsg_from_loginArea2(self):
        doc = "登录页面_获取错误的提示信息2"
        self.wait_eleVisible(loc.errorMsg_from_loginArea2, doc=doc)
        return self.get_text(loc.errorMsg_from_loginArea2)