# encoding=utf-8
from selenium import webdriver
import unittest, time, os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32api
import win32con

VK_CODE ={'enter':0x0D, 'down_arrow':0x28}

#键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
#键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class TestDemo(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Chrome(executable_path="e:\\chromedriver")
    def test_dataPickerByRightKey(self):
        # 定义将要访问的网址
        url = "http://ftp.mozilla.org/pub/mozilla.org//firefox/releases/35.0b8/win32/zh-CN/"
        self.driver.get(url)
        # 将窗口最大化
        self.driver.maximize_window()
        # 暂停5秒，目的防止页面有一些多余的弹窗占据焦点
        time.sleep(5)
        # 找到文本内容为“Firefox Setup 35.0b8.exe”超链接元素
        a = self.driver.find_element_by_link_text("Firefox Setup 35.0b8.exe")
        time.sleep(2)
        # 在找到的链接元素上模拟点击鼠标右键，
        # 以便调出选择“另存为”选项的菜单
        ActionChains(self.driver).context_click(a).perform()
        # 暂停2秒，防止命令执行太快
        time.sleep(2)
        for i in range(4):
            # 循环按4次下箭头，将焦点切换到“另存为”选项上
            # 不同浏览器此选项的位置可能不同
            #a.send_keys(Keys.DOWN)
            keyDown("down_arrow")
            keyUp("down_arrow")
            print i
            time.sleep(2)
        time.sleep(2)
        # 当焦点切换到“另存为”选项上后，模拟点击回车键
        # 调出保存下载文件路径的Windows窗体
        keyDown("enter")
        keyUp("enter")
        time.sleep(3)
        # 通过执行AutoIt编写的操作弹窗的Windows文件保存窗体
        # 完成文件保存路径的设置
        os.system("e:\\upload_file1.exe")
        # 等待文件下载完成，根据各自的网络带宽情况设定等待相应的时间
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()