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

    def test_capturescreenincurrentwindow(self):
        url = "http://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        try:
            result= self.driver.get_screenshot_as_file(r"d:\screenshot.png")
            print result
        except IOError,e:
            print e

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()