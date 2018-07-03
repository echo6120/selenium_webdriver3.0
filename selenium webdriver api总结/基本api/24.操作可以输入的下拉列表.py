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

    def test_operateMultipleOptionDropList(self):
        url = "http://127.0.0.1/test_input_select.html"
        # 访问自定义的html网页
        self.driver.get(url)
        from selenium.webdriver.common.keys import Keys
        # element.send_keys("some text")
        self.driver.find_element_by_id("select").clear()

        # 输入的同时按下箭头键
        self.driver.find_element_by_id("select").send_keys("c")
        self.driver.find_element_by_id("select").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_id("select").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_id("select").send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
pass

if __name__ == '__main__':
    unittest.main()