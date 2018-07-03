#encoding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32clipboard as w
import win32con
import time
import win32api


# 读取剪切板
def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

# 设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

VK_CODE ={
    'enter':0x0D,
    'ctrl':0x11,
    'a':0x41,
    'v':0x56,
    'x':0x58
    }

#键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)

#键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        self.driver = webdriver.Firefox(executable_path = "D:\\python\\Scripts\\geckodriver.exe")
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def test_copyAndPaste(self):
        url = "http://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        # 定义即将要被设置到剪切板中的内容
        content = u'光荣之路'
        # 将content变量中的内容设置到剪切板中
        setText(content)
        # 从剪切板中获取刚设置到剪切板中的内容
        getContent = getText()
        print getContent
        # 将焦点切换到搜索输入框中
        self.driver.find_element_by_id("kw").click()
        time.sleep(1)
        keyDown('ctrl')
        keyDown('v')
        # 释放Ctrl + v组合键
        keyUp('v')
        keyUp('ctrl')
        # 点击“百度一下”搜索按钮
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
