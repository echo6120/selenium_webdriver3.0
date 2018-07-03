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

    def test_clickButton(self):
        url = "http://127.0.0.1/test_button.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 获取按钮页面对象
        button = self.driver.find_element_by_id("button")
        # 模拟鼠标左键单击操作
        button.click()

        time.sleep(3)
    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()