#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import traceback
import unittest
import time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_AjaxDivOptionByIndex(self):
        url = "http://www.sogou.com/"
        # 访问sogou的首页
        self.driver.get(url)
        try:
            # 找到搜狗首页中的搜索输入框页面元素
            searchBox = self.driver.find_element_by_id("query")
            # 在搜索输入框中输入“光荣之路”
            searchBox.send_keys(u"光荣之路")
            # 等待2秒，以便悬浮框加载完成
            time.sleep(2)
            # 查找浮动框中的第三选项，只要更改li[3]中的索引数字，
            # 就可以实现任意单击选项浮动框中的选项。注意，索引从1开始
            suggetion_option = self.driver. \
                find_element_by_xpath("//*[@id='vl']/div[1]/ul/li[3]")
            #print suggetion_option.text
            # 点击找到的选项
            suggetion_option.click()
            time.sleep(3)
        except NoSuchElementException, e:
            # 打印异常堆栈信息
            print traceback.print_exc()


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()