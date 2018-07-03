#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import unittest
import traceback
import time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        #self.driver = webdriver.Chrome(executable_path = "c:\\chromedriver")
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_executeScript(self):
        url = "http://www.sogou.com"
        # 访问baidu首页
        self.driver.get(url)
        # 构造JavaScript查找百度首页的搜索输入框的代码字符串
        searchInputBoxJS = "document.getElementById('query').value='光荣之路';"
        # 构造JavaScript查找百度首页的搜索按钮的代码字符串
        searchButtonJS = "document.getElementById('stb').click()"
        try:
            # 通过JavaScript代码在百度首页搜索输入框中输入“光荣之路”
            self.driver.execute_script(searchInputBoxJS)
            time.sleep(2)
            # 通过JavaScript代码点击百度首页上的搜索按钮
            self.driver.execute_script(searchButtonJS)
            time.sleep(2)
            self.assertTrue(u"光荣之路" in self.driver.page_source)
        except WebDriverException, e:
            # 当定位失败时，会抛出WebDriverException异常
            print u"在页面中没有找到要操作的页面元素 ",traceback.print_exc()
        except AssertionError, e:
            print u"页面不存在断言的关键字串"
        except Exception, e:
            # 发生其他异常时，打印异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()