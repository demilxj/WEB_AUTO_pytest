# -*- coding: utf-8 -*-
# @Time : 2021/3/17 17:23
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : test_taskmanage.py


# 独立的账号，避免跟同事操作相互影响

# 正常用例

# 前提条件：（尽量不要依赖测试环境数据，如果没有，那就自己造环境）
# 用户已登录
# 有能够投资的标 # 如果没有，则先加标。通过接口的方式加标
# 用户有余额可以投资（1.充1个亿 2.接口方式，查询当前用户还有多少钱>xxx，不用充值，如果小于用例中的投资金额，那就充值xxxx）

# 步骤：
# 1.在首页选标-不跟据标名。根据抢投标按钮。默认选第一个标
# 2.标页面-投标输入框内获取投资前的可用余额
# 3.标页面-输入投资金额，点击投标按钮
# 4.标页码-点击投资成功的弹出框-查看并激活，进入个人页面

# 断言：
# 钱 投资后的金额，是不是少了投资的量
# 进入个人页面-获取投资后的金额
# 投资前的金额-投资后的金额=投资金额
# 投资记录对不对（可以额外设计用例）
# 利息对不对？（可以额外设计用例）


# 异常用例1：非常好创造环境，非常好写（做自动化）
# 异常用例2：1.全投操作 2.标的可投金额>个人余额 3.投资金额>标的可投金额  （不好创造环境的用例，可不做自动化，上线前手工跑）

# ===================课程100 28min 还有60min=============

# 正常用例，前提条件
# 用户已登录
# 有能够修改的任务


from PageObjects.index_page import IndexPage
from PageObjects.task_page import TaskPage
from TestDatas import login_datas as LD
import pytest


@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestEditTask:

    # 正常用例-修改任务名称
    @pytest.mark.smoke
    def test_edittaskname_success(self, access_web):
        access_web[1].login(LD.success_data["user"], LD.success_data["passwd"])
        # 步骤 修改任务名 点击保存
        IndexPage(access_web[0]).click_random_task()
        # 断言 首页当中 能否找到 退出 这个元素
        TaskPage(access_web[0]).general_edit("taskname")
