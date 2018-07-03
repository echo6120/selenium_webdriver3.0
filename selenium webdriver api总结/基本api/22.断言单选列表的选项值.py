# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer")

    def test_checkSelectText(self):
        url = "http://127.0.0.1/test_select.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 导入Select模块
        from selenium.webdriver.support.ui import Select
        # 使用xpath定位方式获取select页面元素对象
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # 获取所有选择项的页面元素对象
        actual_options = select_element.options
        # 声明一个list对象，存储下拉列表中所期望出现的文字内容
        expect_optionsList = [u"桃子", u"西瓜", u"橘子", u"猕猴桃", u"山楂", u"荔枝"]
        # 使用Python内置map()函数获取页面中下拉列表展示的选项内容组成的列表对象
        actual_optionsList = map(lambda option: option.text, actual_options)
        # 断言期望列表对象和实际列表对象是否完全一致
        self.assertListEqual(expect_optionsList, actual_optionsList)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()