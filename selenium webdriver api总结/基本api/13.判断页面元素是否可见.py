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

    def test_getWebElementIsDisplayed(self):
        url = "http://127.0.0.1/test_visible.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 通过id="div2"找到第二个div元素
        div2 = self.driver.find_element_by_id("div2")
        # 判断第二个div元素是否在页面上可见
        print div2.is_displayed()
        # 点击第一个切换div按钮，将第二个div显示在页面上
        self.driver.find_element_by_id("button1").click()
        # 再次判断第二个div元素是否可见
        print div2.is_displayed()
        # 通过id="div4"找到第四个div元素
        div4 = self.driver.find_element_by_id("div4")
        # 判断第四个div元素是否在页面上可见
        print div4.is_displayed()
        # 点击第二个切换div按钮，将第四个div显示在页面上
        self.driver.find_element_by_id("button2").click()
        # 再次判断第四个div元素是否可见
        print div4.is_displayed()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()