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

    def test_operateCheckBox(self):
        url = "http://127.0.0.1/test_checkbox.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 使用xpath定位获取value属性值为'berry'的input元素对象，也就是“草莓”选项
        berryCheckBox = self.driver.find_element_by_xpath("//input[@value='berry']")
        # 点击选择“草莓”选项
        berryCheckBox.click()
        # 断言“草莓”复选框被成功选中
        self.assertTrue(berryCheckBox.is_selected(), u"草莓复选框未被选中！")
        if berryCheckBox.is_selected():
            # 如果“草莓”复选框被成功选中，再次点击取消选中
            berryCheckBox.click()
            # 断言“草莓”复选框处于未选中状态
            self.assertFalse(berryCheckBox.is_selected())
        # 查找所有name属性值为“fruit”的复选框元素对象，并存放在checkBoxList列表中
        checkBoxList = self.driver.find_elements_by_xpath("//input[@name='fruit']")
        # 遍历遍历checkBoxList列表中的所有复选框元素，让全部复选框处于被选中状态
        for box in checkBoxList:
            if not box.is_selected():
                box.click()
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()