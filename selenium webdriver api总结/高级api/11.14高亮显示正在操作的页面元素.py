#encoding=utf-8
import unittest
from selenium import webdriver
import time

def highLightElement(driver,element):
    # 封装好的高亮显示页面元素的方法
    # 使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜色分别设置为
    # 绿色和红色
    driver.execute_script("arguments[0].setAttribute('style',\
    arguments[1]);", element,"background:green; border:2px solid red;")

class TestDemo(unittest.TestCase):
    def setUp(self):
        # 获取浏览器驱动实例
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_HighLightWebElement(self):
        url = "http://sogou.com

"
        # 访问搜狗首页
        self.driver.get(url)
        searchBox = self.driver.find_element_by_id("query")
        # 调用高亮显示元素的封装函数，将搜索输入框进行高亮显示
        highLightElement(self.driver, searchBox)
        # 等待3秒，以便查看高亮效果
        time.sleep(3)
        searchBox.send_keys(u"光荣之路自动化测试")
        submitButton = self.driver.find_element_by_id("stb")
        # 调用高亮显示元素的封装函数，将搜索按钮进行高亮显示
        highLightElement(self.driver, submitButton)
        time.sleep(3)
        submitButton.click()
        time.sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()