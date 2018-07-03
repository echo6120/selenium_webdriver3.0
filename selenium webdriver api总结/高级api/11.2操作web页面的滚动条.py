#encoding=utf-8
from selenium import webdriver
import unittest
import traceback
import time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_scroll(self):
        url = "http://www.sohu.com/"
        # 访问selenium官网首页
        try:
            self.driver.get(url)
            # 使用JavaScript的scrollTo函数和document.body.scrollHeight参数
            # 将页面的滚动条滑动到页面的最下方
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 停顿3秒，用于人工验证滚动条是否滑动到指定的位置。
            # 根据测试需要，可注释下面的停顿代码
            time.sleep(3)

            # 使用JavaScript的scrollIntoView函数将被遮挡的元素滚动到可见屏幕上
            # scrollIntoView(true)表示将元素滚到屏幕中间
            # scrollIntoView(false)表示将元素滚动屏幕底部
            self.driver.execute_script("document.getElementsByTagName('a')[500].scrollIntoView(true);")
			#for i in range(10,900):
            #driver.execute_script("document.getElementsByTagName('a')[%s].scrollIntoView(true);" %i)

			#("document.getElementById('choice').scrollIntoView(true);")
            # 停顿3秒，用于人工验证滚动条是否滑动到指定的位置。
            # 根据测试需要，可注释下面的停顿代码
            time.sleep(3)

            # 使用JavaScript的scrollTo方法，使用0和400横纵坐标参数，
            # 将页面纵向向下滚动400像素
            self.driver.execute_script("window.scrollBy (0,400);")
            # 停顿3秒，用于人工验证滚动条是否滑动到指定的位置。
            # 根据测试需要，可注释下面的停顿代码
            time.sleep(3)
        except Exception, e:
            # 打印异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


    ## 横轴滚动document.body.scrollWidth/2，滚动横轴的一半坐标
