# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="D:\\python\\Scripts\\chromedriver.exe")

    def test_HandleIFrame(self):
        url = "http://127.0.0.1/frameset.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 改变操作区域，切换进入页面上第一个frame，也就是左边的frame
        self.driver.switch_to.frame(0)
        # 断言页面是否存在“这是左侧 frame 页面上的文字”关键字串，
        # 以判断是否成功切换进frame页面
        assert u"这是左侧 frame 页面上的文字" in self.driver.page_source

        # 改变操作区域，切换进入id为“showIfame”的iframe页面
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe"))
        # 断言页面是否存在“这是iframe页面上的文字”这样的关键字串，
        # 以便判断是否成功切换进iframe页面
        assert u"这是iframe页面上的文字" in self.driver.page_source

        # 将操作区域切换到frameset页面，以便能成功进入其他frame
        self.driver.switch_to.default_content()
        # 断言页面的title值是否为“frameset 页面”
        assert u"frameset 页面" == self.driver.title

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()