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

    def test_Handleconfirm(self):
        from selenium.common.exceptions import NoAlertPresentException
        import time
        url = "http://127.0.0.1/test_confirm.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 通过id属性值查找页面上的按钮元素
        button = self.driver.find_element_by_id("button")
        # 单击按钮元素，则会弹出一个confirm提示框，
        # 上面显示“这是一个 confirm 弹出框”、“确定”和“取消”按钮
        button.click()
        try:
            # 较高版本的selenium推荐使用driver.switch_to.alert方法代替
            # driver.switch_to_alert()方法来获取alert对象
            alert = self.driver.switch_to.alert
            time.sleep(2)
            # 使用alert.text属性获取confirm框中的内容，
            # 并断言文字内容是否是“这是一个 confirm 弹出框”
            self.assertAlmostEqual(alert.text, u"这是一个 confirm 弹出框")
            # 调用alert对象的accept()方法，模拟鼠标单击confirm弹窗上的“确定”按钮
            # 以便关闭confirm窗
            # alert.accept()
            # 取消下面一行代码的注释，就会模拟单击confirm框上的“取消”按钮
            alert.dismiss()
        except NoAlertPresentException, e:
            # 如果confirm框未弹出显示在页面上，则会抛出NoAlertPresentException的异常
            self.fail("尝试操作的confirm框未被找到")
            print e

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()