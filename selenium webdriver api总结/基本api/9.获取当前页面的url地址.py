# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Chrome(executable_path="e:\\chromedriver")

    def test_operateWindowHandle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 获取当前窗口句柄
        now_handle = self.driver.current_window_handle
        # 打印当前获取的窗口句柄
        print now_handle
        # 百度搜索输入框中输入“selenium”
        self.driver.find_element_by_id("kw").send_keys("w3cschool")
        # 点击搜索按钮
        self.driver.find_element_by_id("su").click()
        # 导入time包
        import time
        # 等待3秒，以便网页加载完成
        time.sleep(3)
        # 点击w3school在线教育链接
        self.driver.find_element_by_xpath('//div[@id="1"]//a[text()="w3"]').click()
        time.sleep(5)
        # 获取所有窗口句柄
        all_handles = self.driver.window_handles
        print "++++", self.driver.window_handles[-1]
        # 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
        for handle in all_handles:
            if handle != now_handle:
                # 输出待选择的窗口句柄
                '''
                切换窗口，也可以用下面的方法，
                但此种方法在selenium3.x以后官方已经不推荐使用了
                self.driver.switch_to_window(handle)
                '''
                # 切换窗口
                self.driver.switch_to.window(handle)
                # 点击HTML5链接
                self.driver.find_element_by_link_text('HTML5').click()
                time.sleep(3)
                # 关闭当前的窗口
                self.driver.close()
        time.sleep(3)
        # 打印主窗口句柄
        print now_handle
        # 返回主窗口
        self.driver.switch_to.window(now_handle)
        time.sleep(2)
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试培训")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()