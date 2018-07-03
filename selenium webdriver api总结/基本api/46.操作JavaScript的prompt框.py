# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Firefox(executable_path="e:\\geckodriver")
        # self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def testHandlePrompt(self):
        url = "http://127.0.0.1/test_prompt.html"
        # 访问自定义网页
        self.driver.get(url)
        # 使用id定位方式，找到被测试网页上唯一按钮元素
        element = self.driver.find_element_by_id("button")
        element.click()
        time.sleep(2)
        # 单击按钮元素，弹出一个prompt提示框，
        # 上面将显示“这是一个prompt弹出框”、输入框、
        # “确定”按钮和“取消”按钮
        # 使用driver.switch_to_alert()方法获取Alert对象
        alert = self.driver.switch_to.alert
        # 使用alert.text方法获取prompt框上面的文字，
        # 并断言文字内容是否和“这是一个 prompt 弹出框”一致
        self.assertEqual(u"这是一个 prompt 弹出框", alert.text)
        time.sleep(1)
        # 调用alert.send_keys()方法，在prompt窗体的输入框中输入
        # “光荣之路：要想改变命运，必须每天学习2小时！”
        alert.send_keys(u"光荣之路：要想改变命运，必须每天学习2小时！")
        time.sleep(1)
        # 使用alert对象的accept方法，
        # 点击prompt框的“确定”按钮，关闭prompt框
        alert.accept()
        # 使用alert对象的dismiss方法，单击prompt框上的“取消”按钮，关闭prompt框
        # 取消下面一行代码的注释，就会模拟单击prompt框上的“取消”按钮
        # alert.dismiss()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()