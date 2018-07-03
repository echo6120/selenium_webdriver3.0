# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer")

    def test_getBasicInfo(self):
        url = "https://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        # 查找百度首页上的“新闻”链接元素
        newsElement = self.driver.find_element_by_xpath("//*[text()='新闻']")
        # 获取查找到的“新闻”链接元素的基本信息
        print u"元素的标签名：", newsElement.tag_name
        print u"元素的size：", newsElement.size

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()