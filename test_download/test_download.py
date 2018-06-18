
# encoding=utf-8

from selenium import webdriver
import unittest, time, os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32con
import win32api


VK_CODE ={'enter':0x0D, 'down_arrow':0x28}

#键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
#键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
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
            a.send_keys(Keys.DOWN)
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
        os.system("C:\Users\jingyu\Desktop\upload_file.exe")
        # 等待文件下载完成，根据各自的网络带宽情况设定等待相应的时间
        print "done"
        #等待下载完成
        time.sleep(100)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


'''
autiitscript文件~
;新建一个名为loadFile.au3的AutoItScript编辑器，文件具体内容如下：
;ControlFocus("title","text",controlID)
;表示将焦点切换到标题为title窗体中的controlID上
;Edit1表示第一个可以编辑的实例
;title表示弹出的Window窗口标题，不同浏览器的标题可能不一样
ControlFocus("请输入要保存的文件名...","","Edit1")

;等待10秒以便window窗口加载成功
WinWait("[CLASS:#32770]","",10)

;将焦点切换到Edit1输入框中
ControlFocus("另存为","","Edit1")

;等待2秒
Sleep(2000)

;将要下载的文件名及路径写入Edit1编辑框中
ControlSetText("另存为","", "Edit1", "D:\Downloads\Firefox Setup 35.0b8.exe")

Sleep(7000)

;点击窗体中的第一个按钮，也就是保存按钮
ControlClick("另存为","","Button1")

;Send("{ENTER}")
;Send("{ENTER}")
;保存后将该文件编译成exe文件，并存放到本地磁盘。
;Sleep(2000)
Send("{LEFT}")
Send("{LEFT}")
Send("{ENTER}")
Send("{ENTER}")
'''