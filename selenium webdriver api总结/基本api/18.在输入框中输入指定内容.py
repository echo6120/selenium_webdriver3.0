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

    def test_clearInputBoxText(self):
        url = "http://www.baidu.com"
        # 访问自定义的html网页
        self.driver.get(url)
        # 获取输入框页面对象
        input = self.driver.find_element_by_id("kw")
        input.send_keys(u"光荣之路自动化测试")
        time.sleep(3)
        # 清除输入框中默认内容
        input.clear()
        # 等待3秒，主要看清空输入框内容后的效果
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()