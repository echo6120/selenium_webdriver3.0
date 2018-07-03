#encoding=utf-8
from selenium import webdriver
import unittest, time, traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_datePicker(self):
        url = "http://jqueryui.com/resources/demos/datepicker/other-months.html"
        # 访问指定的网址
        self.driver.get(url)
        try:
            # 创建一个显示等待对象
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的日期输入框是否可见并且能被点击
            wait.until(EC.element_to_be_clickable((By.ID, 'datepicker')))
        except TimeoutException, e:
            # 捕获TimeoutException异常
            print traceback.print_exc()
        except NoSuchElementException, e:
            # 捕获NoSuchElementException异常
            print traceback.print_exc()
        except Exception, e:
            # 捕获其他异常
            print traceback.print_exc()
        else:
            # 查找被测试页面上的日期输入框页面元素
            dateInputBox = self.driver.find_element_by_id("datepicker")
            # 查找到日期输入框，直接输入指定格式的日期字符串
            # 就可以变相模拟在日期控件上进行选择了
            dateInputBox.send_keys("11/24/2016")
            time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()