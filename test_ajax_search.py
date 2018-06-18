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
from selenium.webdriver.common.keys import Keys


class TestLoginByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")


    def test_a_ke163login(self):
        url = "https://ke.youdao.com"
        # 访问搜狗首页，焦点会自动定位到搜索输入框中
        self.driver.get(url)
        #找到搜索框元素
        searchbox = self.driver.find_element_by_class_name("_3l-Kp")
        searchbox.clear()
        searchbox.send_keys(u"四六级")
        time.sleep(5)
        suggestion_option = self.driver.find_elements_by_xpath("//div[@class='_3O_cN _1aHnD']/child")
        for i in range(3):
            searchbox.send_keys(Keys.DOWN)
            time.sleep(0.5)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title,u"搜索结果-有道精品课-为你精选好课 - 为你精选好课")

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()