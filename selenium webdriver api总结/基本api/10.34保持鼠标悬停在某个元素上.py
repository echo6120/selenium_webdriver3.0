# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import win32clipboard as w
import win32con


# 设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer")

    def test_simulationLeftClickMouseOfProcess(self):
        url = "http://127.0.0.1/test_mouse.html"
        # 访问自定义的html网页
        self.driver.get(url)
        div = self.driver.find_element_by_id("div1")
        from selenium.webdriver import ActionChains
        import time
        # 在id属性值为“div1”的元素上执行按下鼠标左键，并保持
        ActionChains(self.driver).click_and_hold(div).perform()
        time.sleep(2)
        # 在id属性值为“div1”的元素上释放一直释放的鼠标左键
        ActionChains(self.driver).release(div).perform()
        time.sleep(2)
        ActionChains(self.driver).click_and_hold(div).perform()
        time.sleep(2)
        ActionChains(self.driver).release(div).perform()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

