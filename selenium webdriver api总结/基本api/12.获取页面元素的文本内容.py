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

    def test_getWebElementText(self):
        url = "https://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        time.sleep(3)
        # 通过xpath定位方式找到id属性值为“u1”的div元素下的第一个链接元素
        aElement = self.driver.find_element_by_xpath("//*[@class='mnav'][1]")
        # 通过找到的链接元素对象的text属性获取到链接元素的文本内容
        a_text = aElement.text
        print "text content:", a_text
        self.assertEqual(a_text, u"新闻")

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()