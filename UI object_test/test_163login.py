# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
import time


class TestLoginByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")


    def test_a_ke163login(self):
        url = "https://ke.youdao.com/login"
        # 访问搜狗首页，焦点会自动定位到搜索输入框中
        self.driver.get(url)
        #显式等待，判断文本内容“网易邮箱登录 是否出现在了元素中
        try:
            #wait = WebDriverWait(self.driver,10,0.2)
            #当class的属性值，中间有空格时，通过by方法会报错：Compound class names not permitted
            #wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"_1_E34"),u"手机号登录"))
            #emailelement = self.driver.find_element_by_xpath('//div[@class = "_1_E34 "]')
            emailelement = self.obj.getElementObject(self.driver,"163login","emailelement")
            emailelement.click()
            time.sleep(5)
            #wait1 = WebDriverWait(self.driver, 10, 0.2)
            #wait1.until(EC.visibility_of(self.driver.find_element_by_id("unameInput")))
            usernameelement = self.driver.find_element_by_id("unameInput")
            usernameelement.clear()
            usernameelement.send_keys("huihuitestecho9@163.com")
            userpwdelement = self.driver.find_element_by_id("pwdInput")
            userpwdelement.clear()
            userpwdelement.send_keys("1qaz2wsx")
            confirmbutton = self.driver.find_element_by_class_name("_3sT09")
            confirmbutton.click()
            time.sleep(5)
            #判断是否登录成功跳转回主页
            title= self.driver.title
            self.assertEqual(title,u"有道精品课 - 为你精选好课","error occur ")

        except TimeoutException,e:
            print traceback.print_exc()
        except NoSuchElementException,e:
            print traceback.print_exc()
        except Exception,e:
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
