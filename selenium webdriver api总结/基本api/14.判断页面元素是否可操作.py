# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer")

    def test_getWebElementIsEnabled(self):
        url = "http://127.0.0.1/test_enable.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 通过id找到第一个input元素
        input1 = self.driver.find_element_by_id("input1")
        # 判断第一个input元素是否可操作
        print input1.is_enabled()
        # 通过id找到第二个input元素
        input2 = self.driver.find_element_by_id("input2")
        # 判断第二个input元素是否可操作
        print input2.is_enabled()
        # 通过id找到第三个input元素
        input3 = self.driver.find_element_by_id("input3")
        # 判断第三个input元素是否可操作
        print input3.is_enabled()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
