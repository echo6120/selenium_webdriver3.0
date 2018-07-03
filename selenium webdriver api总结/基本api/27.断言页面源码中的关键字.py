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

    def test_assertKeyWord(self):
        url = "http://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        self.driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试")
        self.driver.find_element_by_id("su").click()
        time.sleep(4)
        # 通过断言页面是否存在某些关键字来确定页面按照预期加载
        assert u"首页--光荣之路" in self.driver.page_source, u"页面源码中不存在该关键字！"

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()