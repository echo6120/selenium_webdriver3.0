#encoding=utf-8
from selenium import webdriver
import unittest

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_refreshCurrentPage(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 刷新当前页面
        self.driver.refresh()


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()