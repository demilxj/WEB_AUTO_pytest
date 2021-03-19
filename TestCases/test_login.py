# -*- coding: utf-8 -*-
# @Time : 2021/3/17 13:46
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : test_login.py

from PageObjects.index_page import IndexPage
from TestDatas import login_datas as LD
import pytest


@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    # # 异常用例-用户名为空、密码为空
    @pytest.mark.parametrize("data", LD.isnull_data)
    def test_login1_wrongFormat(self, data, access_web):
        # 步骤 输入用户名xxx 密码xxx 点击登录
        # 断言 首页当中 提示：请输入正确的手机号
        # 登录页面中 获取提示框的文本内容
        # 比对文本内容 与 期望的值 是否相等
        access_web[1].login(data["user"], data["passwd"])
        assert access_web[1].get_errorMsg_from_loginAreaCentre() == data["check"]

    # 异常用例-用户名密码不正确
    def test_login2_wrong(self, access_web):
        # 步骤 输入用户名xxx 密码xxx 点击登录
        # 断言 首页当中 提示：请输入正确的用户名
        access_web[1].login(LD.wrong_data["user"], LD.wrong_data["passwd"])
        assert access_web[1].get_errorMsg_from_loginArea2() == LD.wrong_data["check"]

    # 正常用例-登录成功
    @pytest.mark.smoke
    def test_login3_success(self, access_web):   # fixture的函数名称，用来接收它的返回值
        # 步骤 输入用户名xxx 密码xxx 点击登录
        access_web[1].login(LD.success_data["user"], LD.success_data["passwd"])
        # 断言 首页当中 能否找到 退出 这个元素
        assert IndexPage(access_web[0]).isExist_logout_ele()
