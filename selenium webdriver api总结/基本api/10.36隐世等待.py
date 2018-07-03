# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer")

    def test_implictWait(self):
        # 导入异常类
        from selenium.common.exceptions import NoSuchElementException, TimeoutException
        # 导入堆栈类
        import traceback
        url = "http://www.sogou.com"
# 访问sogou首页
self.driver.get(url)
# 通过driver对象implicitly_wait()方法来设置隐式等待时间，最长等待10秒，如果10秒内返回则继续执行后续脚本
self.driver.implicitly_wait(10)
try:
    # 查找sogou首页的搜索输入框页面元素
    searchBox = self.driver.find_element_by_id("query")
    # 在搜索输入框中输入“光荣之路自动化测试”
    searchBox.send_keys(u"光荣之路自动化测试")
    # 查找sogou首页搜索按钮页面元素
    click = self.driver.find_element_by_id("stb")
    # 点击搜索按钮
    click.click()
except (NoSuchElementException, TimeoutException), e:
    # 打印异常的堆栈信息
    traceback.print_exc()


def tearDown(self):
    # 退出IE浏览器
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()