# -*- coding: utf-8 -*-
# @Time : 2021/3/17 16:02
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : login_datas.py

# 正常场景-测试数据
success_data = {"user": "lxj", "passwd": "123456"}

# 异常场景-用户名为空、密码为空、用户名及密码都为空   不同的场景check内容可以不同
isnull_data = [{"user": "", "passwd": "123456", "check": "登录超时，请重新登录！"},
               {"user": "lxj", "passwd": "", "check": "登录超时，请重新登录！"},
               {"user": "", "passwd": "", "check": "登录超时，请重新登录！"}]

# 异常场景-用户名密码不正确
wrong_data = {"user": "lxj1", "passwd": "1234561", "check": "用户名或密码错误，请重新输入！"}