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

    def test_operateRadio(self):
        url = "http://127.0.0.1/test_radio.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 使用xpath定位获取value属性值为'berry'的input元素对象，也就是“草莓”选项
        berryRadio = self.driver.find_element_by_xpath("//input[@value='berry']")
        # 点击选择“草莓”选项
        berryRadio.click()
        # 断言“草莓”复选框被成功选中
        self.assertTrue(berryRadio.is_selected(), u"草莓复选框未被选中！")
        if berryRadio.is_selected():
            # 如果“草莓”复选框被成功选中，重新选择“西瓜”选项
            watermelonRadio = self.driver.find_element_by_xpath("//input[@value='watermelon']")
            watermelonRadio.click()
            # 选择“西瓜”选项以后，断言“草莓”选项处于未被选中状态
            self.assertFalse(berryRadio.is_selected())
        # 查找所有name属性值为“fruit”的单选框元素对象，并存放在radioList列表中
        radioList = self.driver.find_elements_by_xpath("//input[@name='fruit']")
        '''
        循环遍历radioList中的每个单选按钮，查找value属性值为“orange”的单选框，
        如果找到此单选框以后，发现未处于选中状态，则调用click方法选中该选项。
        '''
        for radio in radioList:
            if radio.get_attribute("value") == "orange":
                if not radio.is_selected():
                    radio.click()
                    self.assertEqual(radio.get_attribute("value"), "orange")

        time.sleep(5)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()