# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer")

    def test_getPageSource(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 调用driver的page_source属性获取页面源码
        pageSource = self.driver.page_source
        # 打印页面源码
        print type(pageSource)
        print pageSource.encode("gbk", "ignore")
        # 断言页面源码中是否包含“购物”两个关键字，以此判断页面内容是否正确
        self.assertTrue(u"购物" in pageSource)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()