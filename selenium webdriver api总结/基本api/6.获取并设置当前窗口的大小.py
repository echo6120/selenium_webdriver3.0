#encoding=utf-8
from selenium import webdriver
import unittest
import time

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_window_size(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        sizedict = self.driver.get_window_size()
        print "当前浏览器的宽：",sizedict['width']
        print "当前浏览器的高：", sizedict['height']
        self.driver.set_window_size(width = 200,height=400,windowHandle='current')
        print  self.driver.get_window_size(windowHandle='current')


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()