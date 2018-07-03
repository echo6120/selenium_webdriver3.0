#encoding=utf-8
from selenium import webdriver
import unittest
import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")


    def test_uploadFileBySendKeys(self):
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
            # 查找页面上ID属性值为“file”的文件上传框
            fileBox = self.driver.find_element_by_id("file")
            # 在文件上传框的路径框里输入要上传的文件路径“c:\\test.txt”
            fileBox.send_keys("c:\\test.txt")
            # 暂停查看上传的文件
            time.sleep(4)
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
