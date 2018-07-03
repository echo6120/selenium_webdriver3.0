#encoding=utf-8
from selenium import webdriver
import unittest

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_maximizeWindow(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 最大化浏览器窗口，以便占满整个电脑屏幕
        self.driver.maximize_window()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()