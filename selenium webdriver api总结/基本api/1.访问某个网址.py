#encoding=utf-8
from selenium import webdriver
import unittest

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_visitURL(self):
        visitURL = "http://www.sogou.com"
        self.driver.get(visitURL)
        assert self.driver.title.find(u"搜狗搜索引擎")>=0, "assert error"



    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()