# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Chrome(executable_path="e:\\chromedriver")

    def test_getcurrentpageurl(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 获取当前窗口句柄
        currentpageurl = self.driver.current_url
        print currentpageurl
        self.assertEqual(currentpageurl,"https://www.sougou.com","当前网址非预期")

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()