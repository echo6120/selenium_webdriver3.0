#encoding=utf-8
from selenium import webdriver
import unittest
import time
import traceback
import win32clipboard as w
import win32api
import win32con
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# 用于设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

# 键盘按键映射字典
VK_CODE = {
    'enter':0x0D,
    'ctrl':0x11,
    'v':0x56}

# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_uploadFileByKeyboard(self):
        url = "http://127.0.0.1/test_upload_file.html"
        # 访问自定义网页
        self.driver.get(url)
        try:
            # 创建一个显示等待对象
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的上传文件按钮是否处于可被点击状态
            wait.until(EC.element_to_be_clickable((By.ID, 'file')))
        except TimeoutException, e:
            # 捕获TimeoutException异常
            print traceback.print_exc()
        except NoSuchElementException, e:
            # 捕获NoSuchElementException异常
            print traceback.print_exc()
        except Exception, e:
            # 捕获其他异常
            print traceback.print_exc()
        else:
            # 将即将要上传的文件名及路径设置到剪切板中
            setText(u"c:\\test.txt")
            # 查找页面上ID属性值为“file”的文件上传框,
            # 并点击调出选择文件上传框
            self.driver.find_element_by_id("file").click()
            time.sleep(2)
            # 模拟键盘按下ctrl + v组合键
            keyDown("ctrl")
            keyDown("v")
            # 模拟键盘释放Ctrl + v组合键
            keyUp("v")
            keyUp("ctrl")
            time.sleep(1)
            # 模拟键盘按下回车键
            keyDown("enter")
            # 模拟键盘释放回车键
            keyUp("enter")
            # 暂停查看上传的文件
            time.sleep(2)
            # 找到页面上ID属性值为“filesubmit”的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            # 因为文件上传需要时间，所以这里可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title
            # 值是否符合期望，如果匹配将继续执行后续代码
            #wait.until(EC.title_is(u"文件上传成功"))

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
