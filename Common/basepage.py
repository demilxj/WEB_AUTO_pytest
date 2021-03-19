# -*- coding: utf-8 -*-
# @Time : 2021/3/18 11:12
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : basepage.py

from Common.my_log import MyLog
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from Common import dir_config
import time

my_logger = MyLog()
# 1.封装基本函数--执行日志、异常处理、失败截图
# 2.所有页面的公共的部分
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, wait_times=30, poll_frequency=0.5, doc=""):
        """
        :param locator:元素定位。元组形式(元素定位类型，元素定位方式)
        :param times:等待时间
        :param poll_frequency:轮巡时间
        :param doc:模块名_页面名称_操作名称
        :return:None
        """
        my_logger.info('等待元素{0}可见'.format(locator))
        try:
            # 开始等待时间点
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间点
            end = datetime.datetime.now()
            # # 耗时
            during = end-start
            my_logger.info('{0}:元素{1}已可见，等待起始时间:{2},等待结束时间:{3}，等待时长为:{4}s'.format(doc, locator, start, end, during))
        except:
            my_logger.exception('等待元素可见失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc):
        my_logger.info('查找元素:{0}'.format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            # 捕获异常到日志中
            my_logger.exception('查找元素失败！！！')
            # 截图-保存到指定的目录。名字要想好怎么取
            self.save_screenshot(doc)
            raise

    # 查找元素
    def get_elements(self, locator, doc):
        my_logger.info('查找元素:{0}'.format(locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            # 捕获异常到日志中
            my_logger.exception('查找元素失败！！！')
            # 截图-保存到指定的目录。名字要想好怎么取
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        my_logger.info('{0}点击元素:{1}'.format(doc, locator))
        try:
            ele.click()
        except:
            my_logger.exception('元素点击操作失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 输入操作
        try:
            ele.send_keys(text)
        except:
            my_logger.exception('元素输入操作失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素文本内容
    def get_text(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.text
        except:
            my_logger.exception('获取元素文本内容失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素属性
    def get_element_attribute(self, locator, attr, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.get_attribute(attr)
        except:
            my_logger.exception('获取元素属性失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # alert处理
    def alert_action(self, action='accept'):
        pass

    # iFrame切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换

    # 截图函数
    def save_screenshot(self, doc):
        # 图片名称:模块名_页面名称_操作名称_年-月-日-时分秒.png
        filePath = dir_config.screenshot_dir + "/" + "{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()))
        # driver方法:self.driver.save_screenshot()
        try:
            self.driver.save_screenshot(filePath)
            my_logger.info('截取网页成功，文件路径为:{0}'.format(filePath))
        except:
            my_logger.exception("截图失败")