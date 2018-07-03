# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer")

    def test_Cookie(self):
        url = "http://www.sogou.com"
        # 访问sogou首页
        self.driver.get(url)
        # 得到当前页面下所有的Cookies，并输出它们所在域、name、value、有效期和路径
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print "%s -> %s -> %s -> %s -> %s" \
                  % (cookie['domain'], cookie["name"], cookie["value"], \
                     cookie["expiry"], cookie["path"])

        # 根据Cookie的name值获取该条Cookie信息，获取name值为'SUV'的Cookie信息
        ck = self.driver.get_cookie("SUV")
        print "%s -> %s -> %s -> %s -> %s" \
              % (ck['domain'], ck["name"], ck["value"], \
                 ck["expiry"], ck["path"])

        # 删除cookie有2种方法
        # 第一种：通过Cookie的name属性，删除name值为“ABTEST”的Cookie信息
        print self.driver.delete_cookie("ABTEST")

        # 第二种：一次性删除全部Cookie信息
        self.driver.delete_all_cookies()
        # 删除全部Cookie后，再次查看Cookies，确认是否已被全部删除
        cookies = self.driver.get_cookies()
        print cookies

        # 添加自定义Cookie信息
        self.driver.add_cookie({"name": "gloryroadTrain", 'value': '1479697159269020'})
        # 查看添加的Cookie信息
        cookie = self.driver.get_cookie("gloryroadTrain")
        print cookie

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()