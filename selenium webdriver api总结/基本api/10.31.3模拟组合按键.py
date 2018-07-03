#encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

 
class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Chrome(executable_path = "D:\\python\\Scripts\\chromedriver.exe")
		#仅chrome和ie11的最新版本生效
    def test_simulationCombinationKeys(self):
        url = "http://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        # 将焦点切换到搜索输入框中
        input = self.driver.find_element_by_id("kw")
        input.send_keys(u"光荣之路")
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').\
        key_up(Keys.CONTROL).perform()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('x').\
        key_up(Keys.CONTROL).perform()
        self.driver.get(url)
        self.driver.find_element_by_id("kw").click()
        # 模拟Ctrl + V组合键，将从剪切板中获取到的内容粘贴到搜索输入框中
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').\
        key_up(Keys.CONTROL).perform()
        # 点击“百度一下”搜索按钮
        self.driver.find_element_by_id('su').click()
        time.sleep(3)


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
