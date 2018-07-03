#encoding=utf-8
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
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path = "D:\\python\\Scripts\\chromedriver.exe")
		#仅能ie生效
        
    def test_rigthClickMouse(self):
        url = "http://www.sogou.com"
        # 访问搜狗首页
        self.driver.get(url)
        # 找到搜索输入框
        searchBox = self.driver.find_element_by_id("query")
        # 将焦点切换到搜索输入框
        searchBox.click()
        time.sleep(2)
        # 在搜索输入框上执行一个鼠标右键点击操作
        ActionChains(self.driver).context_click(searchBox).perform()
        # 将“gloryroad”数据设置到剪切板中，相当于执行了复制操作
        setText(u'gloryroad')
        # 发送一个粘贴命令，字符p指代粘贴操作
        ActionChains(self.driver).send_keys('P').perform()
        # 点击搜索按钮
        self.driver.find_element_by_id('stb').click()
        time.sleep(2)



    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
