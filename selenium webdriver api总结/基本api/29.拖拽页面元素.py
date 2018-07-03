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

    def test_dragPageElement(self):
        url = "http://jqueryui.com/resources/demos/draggable/scroll.html"
        # 访问被测试网页
        self.driver.get(url)
        # 获取页面上第一个能拖拽的页面元素
        initialPosition = self.driver.find_element_by_id("draggable")
        # 获取页面上第二个能拖拽的页面元素
        targetPosition = self.driver.find_element_by_id("draggable2")
        # 获取页面上第三个能拖拽的页面元素
        dragElement = self.driver.find_element_by_id("draggable3")
        # 导入提供拖拽元素方法的模块ActionChains
        from selenium.webdriver import ActionChains
        import time
        '''
        创建一个新的ActionChains，将webdriver实例对象driver作为参数值传入
        然后通过WebDriver实例执行用户动作。
        '''
        action_chains = ActionChains(self.driver)
        # 将页面上第一个能被拖拽的元素拖拽到第二个元素位置
        action_chains.drag_and_drop(initialPosition, targetPosition).perform()
        # 将页面上第三个能拖拽的元素，向右下拖动10个像素，共拖动5次
        for i in xrange(5):
            action_chains.drag_and_drop_by_offset(dragElement, 10, 10).perform()
            time.sleep(2)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
