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

    def test_getWebElementAttribute(self):
        url = "http://www.sogou.com"
        # 访问sogou首页
        self.driver.get(url)
        # 找到搜索输入框元素
        searchBox = self.driver.find_element_by_id("query")
        # 获取搜索输入框页面元素的name属性值
        print searchBox.get_attribute("name")
        # 向搜索输入框中输入“测试工程师指定的输入内容”内容
        searchBox.send_keys(u"测试工程师指定的输入内容")
        # 获取页面搜索框的value属性值（即搜索输入框的文字内容）
        print searchBox.get_attribute("value")

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()