#encoding=utf-8
from selenium import webdriver
import unittest

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_visitRecentURL(self):
        firstVisitURL = "http://www.sogou.com"
        secondVisitURL = "http://www.baidu.com"
        # 首先访问sogou首页
        self.driver.get(firstVisitURL)
        # 然后访问baidu首页
        self.driver.get(secondVisitURL)
        # 返回上一次访问过的搜狗首页
        self.driver.back()
        # 再次回到百度首页
        self.driver.forward()



    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()