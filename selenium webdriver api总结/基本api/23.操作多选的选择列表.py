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

    def test_operateMultipleOptionDropList(self):
        url = "http://127.0.0.1/test_multiple_select.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 导入Select模块
        from selenium.webdriver.support.ui import Select
        # 使用xpath定位方式获取select页面元素对象
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # 通过序号选择第一个元素
        select_element.select_by_index(0)
        # 通过选项的文本选择“山楂”选项
        select_element.select_by_visible_text("山楂")
        # 通过选项的value属性值选择value=“mihoutao”的选项
        select_element.select_by_value("mihoutao")
        # 打印所有的选中项文本
        for option in select_element.all_selected_options:
            print option.text
        # 取消所有已选中项
        select_element.deselect_all()
        time.sleep(2)
        print u"-----------再次选中3个选项--------------"
        select_element.select_by_index(1)
        select_element.select_by_visible_text("荔枝")
        select_element.select_by_value("juzi")
        # 通过选项文本取消已选中的文本为“荔枝”选项
        select_element.deselect_by_visible_text("荔枝")
        # 通过序号取消已选中的序号为1的选项
        select_element.deselect_by_index(1)
        # 通过选项的value属性值取消已选中的value=“juzi”的选项
        select_element.deselect_by_value("juzi")

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()