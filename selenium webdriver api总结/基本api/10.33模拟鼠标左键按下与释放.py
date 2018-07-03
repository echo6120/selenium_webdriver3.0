#encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# 导入模拟组合按键需要的包
import win32api
import win32con
import time

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
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def test_simulationCombinationKeys(self):
        url = "http://www.sogou.com

"
        # 访问搜狗首页
        self.driver.get(url)
        # 找到搜索输入框元素
        searchBox = self.driver.find_element_by_id("query")
        # 将焦点切换到搜索输入框中
        searchBox.click()
        # 搜索输入框中输入“光荣之路自动化测试”
        searchBox.send_keys(u"光荣之路自动化测试")
        # 稍微等待几秒，防止太快串命令
        time.sleep(3)
        # 模拟Ctrl + a，选中输入框中所有的内容
        keyDown('ctrl')
        keyDown('a')
        # 释放Ctrl + a组合键
        keyUp('a')
        keyUp('ctrl')
        # 模拟Ctrl + x剪切所选中的内容
        keyDown('ctrl')
        keyDown('x')
        keyUp('x')
        keyUp('ctrl')
        # 访问百度首页
        self.driver.get("http://www.baidu.com

")
        # 将焦点切换到搜索输入框中
        self.driver.find_element_by_id("kw").click()
        # 模拟Ctrl + v组合键，进行粘贴
        keyDown("ctrl")
        keyDown("v")
        keyUp('v')
        keyUp('ctrl')
        # 模拟回车键
        keyDown('enter')
        keyUp('enter')
        time.sleep(5)



    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
