#encoding=utf-8
from selenium import webdriver
import unittest, time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 创建Chrome浏览器配置对象实例
        chromeOptions = webdriver.ChromeOptions()
        # 设定下载文件的保存目录为C盘的iDownload目录，
        # 如果该目录不存在，将会自动创建
        prefs = {"download.default_directory": "d:\\iDownload"}
        # 将自定义设置添加到Chrome配置对象实例中
        chromeOptions.add_experimental_option("prefs", prefs)
        # 启动带有自定义设置的Chrome浏览器
        self.driver = webdriver.Chrome(executable_path="e:\\chromedriver",\
                                       chrome_options=chromeOptions)

    def test_downloadFileByChrome(self):
        url = "http://pypi.python.org/pypi/selenium"
        # 访问将要下载文件的网址
        self.driver.get(url)
        # 找到要下载的文件链接页面元素，并点击进行下载
        self.driver.find_element_by_partial_link_text\
            ("standalone-3.12.0.jar").click()
        # 等待100s，以便文件下载完成
        time.sleep(20)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
