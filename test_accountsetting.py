#encoding=utf-8
from selenium import webdriver
import unittest
import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import email
import os


class Testaccountsetting(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")

    @classmethod
    def tearDownClass(self):
        # 退出IE浏览器
        self.driver.quit()


    def test_login(self):
        email.test_a_ke163login(self)
#使用AutoIt脚本上传文件
    def test_uploadFileBySendKeys(self):
        url = "https://ke.youdao.com/user/account/"
        # 访问自定义网页
        self.driver.get(url)
        try:
            # 创建一个显示等待对象
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的上传文件按钮是否处于可被点击状态
            wait.until(EC.element_to_be_clickable((By.ID, 'upload-btn')))
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
            fileBox = self.driver.find_element_by_id("upload-btn")
            fileBox.click()
            time.sleep(5)
            os.system("C:\\Users\\jingyu\\Desktop\\1.exe")
            time.sleep(5)
            # 找到页面上ID属性值为“filesubmit”的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("submit-btn")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            time.sleep(5)
            comfirmtext = self.driver.find_element_by_xpath('//h2[text()="保存成功"]')
           #*[@id="dialog-alert"]/div/table/tbody/tr/td[2]/div[1]/h2
            self.assertTrue(comfirmtext,"没有上传成功的弹框")
            comfirmbutton = self.driver.find_element_by_xpath("//div[@class='box-content']/div[@class='tac']/input[@class='g-btn-green finish box-ok']")
            comfirmbutton.click()
            # 因为文件上传需要时间，所以这里可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title
            # 值是否符合期望，如果匹配将继续执行后续代码
            #wait.until(EC.title_is(u"文件上传成功"))


if __name__ == '__main__':
    #unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(Testaccountsetting("test_login"))
    suite.addTest(Testaccountsetting("test_uploadFileBySendKeys"))
    runner = unittest.TextTestRunner()
    runner.run(suite)