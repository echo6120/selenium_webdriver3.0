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

    def test_roverOnElement(self):
        url = "http://127.0.0.1/test_mouse_hover.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 找到页面上第一个链接元素
        link1 = self.driver.find_element_by_partial_link_text(u"指过来1")
        # 找到页面上第二个链接元素
        link2 = self.driver.find_element_by_partial_link_text(u"指过来2")
        # 找到页面上的p元素
        p = self.driver.find_element_by_xpath("//p")
        print link1.text, link2.text
        # 导入需要的Python包
        from selenium.webdriver import ActionChains
        import time
        # 将鼠标悬浮到第一个链接元素上
        ActionChains(self.driver).move_to_element(link1).perform()
        time.sleep(2)
        # 将鼠标从第一个链接元素移动到p元素上
        ActionChains(self.driver).move_to_element(p).perform()
        time.sleep(2)
        # 将鼠标悬浮到第二个链接元素上
        ActionChains(self.driver).move_to_element(link1).perform()
        time.sleep(2)
        # 将鼠标从第二个链接元素移动到p元素上
        ActionChains(self.driver).move_to_element(p).perform()
        time.sleep(2)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()