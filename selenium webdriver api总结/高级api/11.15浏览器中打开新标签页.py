#encoding=utf-8
import unittest
from selenium import webdriver
import time
import win32api, win32con

VK_CODE ={'ctrl':0x11, 't':0x54, 'tab':0x09}

# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

# 封装的按键方法
def simulateKey(firstKey, secondKey):
    keyDown(firstKey)
    keyDown(secondKey)
    keyUp(secondKey)
    keyUp(firstKey)

class TestDemo(unittest.TestCase):
    def setUp(self):
        # 获取浏览器驱动实例
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
    def test_newTab(self):
        # 等待3秒，等待浏览器启动完成
        time.sleep(3)
        # 使用for循环，再新开两个新的标签页
        for i in range(2):
            simulateKey("ctrl", "t")
        # 通过Ctrl + tab组合键，将当前页面切换为默认页面，
        # 也就是最先打开的标签页
        simulateKey("ctrl", "tab")
        # 访问搜狗首页
        self.driver.get("http://sogou.com

")
        self.driver.find_element_by_id("query").send_keys(u"光荣之路")
        self.driver.find_element_by_id("stb").click()
        time.sleep(3)
        #self.assertTrue(u"乔什•卢卡斯" in self.driver.page_source)

        # 获取所有的打开的窗口句柄
        all_handles = self.driver.window_handles
        print len(all_handles)
        for handle in all_handles:
            # 将当前窗口句柄切换至第二个标签页
            self.driver.switch_to.window(handle)
            print self.driver.title
            if u"输入法" not in self.driver.page_source:
                self.driver.get("http://www.baidu.com

")
                self.driver.find_element_by_id("kw").send_keys(u"WebDriver实战宝典")
                self.driver.find_element_by_id("su").click()
                time.sleep(3)
                self.assertTrue(u"实战宝典" in self.driver.page_source)
            elif (u"输入法" not in self.driver.page_source) and ("WebDriver" not in self.driver.page_source):
            # 将当前窗口的句柄切换至第三个标签页
                self.driver.get("http://www.iciba.com

")
                time.sleep(3)
                self.assertTrue(u"查词" in self.driver.page_source)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
