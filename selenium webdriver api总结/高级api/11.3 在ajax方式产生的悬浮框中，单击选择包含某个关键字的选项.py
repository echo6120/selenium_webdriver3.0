#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_AjaxDivOptionByKeys(self):
        url = "http://www.sogou.com/"
        # 访问sogou的首页
        self.driver.get(url)
        # 找到搜狗首页中的搜索输入框页面元素
        searchBox = self.driver.find_element_by_id("query")
        # 在搜索输入框中输入“光荣之路”
        searchBox.send_keys(u"光荣之路")
        # 等待2秒，以便悬浮框加载完成
        time.sleep(2)
        for i in range(3):
            # 选择悬浮框中中第几个联想关键词选项就循环几次
            # 模拟键盘点击下箭头
            searchBox.send_keys(Keys.DOWN)
            time.sleep(0.5)
        # 当按下箭头到想要选择的选项后，再模拟键盘点击回车键，选中该选项
        searchBox.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()