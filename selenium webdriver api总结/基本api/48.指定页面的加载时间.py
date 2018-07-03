#encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class setPageLoadTime(unittest.TestCase):
    def setUp(self):
        # 启动火狐浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_PageLoadTime(self):
        # 设定页面加载限制时间为4秒
        self.driver.set_page_load_timeout(4)
        self.driver.maximize_window()
        try:
            startTime = time.time()
            self.driver.get("http://mail.126.com")
        except TimeoutException:
            print u'页面加载超过设定时间，超时'
            # 当页面加载时间超过设定时间，
            # 通过执行Javascript来stop加载，然后继续执行后续动作
            self.driver.execute_script('window.stop()')
        end = time.time() - startTime
        print end
        # 切换进frame控件
        self.driver.switch_to.frame("x-URS-iframe")
        # 获取用户名输入框
        userName = self.driver.find_element_by_xpath('//input[@name="email"]')
        # 输入用户名
        userName.send_keys("xxx")
        # 获取密码输入框
        pwd = self.driver.find_element_by_xpath("//input[@name='password']")
        # 输入密码
        pwd.send_keys("xxx")
        # 发送一个回车键
        pwd.send_keys(Keys.RETURN)
        time.sleep(5)
assert u"退出" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()