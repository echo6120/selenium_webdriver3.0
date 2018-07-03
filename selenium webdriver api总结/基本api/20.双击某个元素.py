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

    def test_doubleClick(self):
        url = "http://127.0.0.1/test_doubleclick.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 获取页面输入元素
        inputBox = self.driver.find_element_by_id("inputBox")
        # 导入支持双击操作的模块
        from selenium.webdriver import ActionChains
        # 开始模拟鼠标双击操作
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).perform()

        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()