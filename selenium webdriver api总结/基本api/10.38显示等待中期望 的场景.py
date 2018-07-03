# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="D:\\python\\Scripts\\chromedriver.exe")

    # encoding=utf-8
    import unittest
    import time
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    class VisitSogouByIE(unittest.TestCase):
        def setUp(self):
            # 启动IE浏览器
            # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
            self.driver = webdriver.Ie(executable_path="D:\\python\\Scripts\\chromedriver.exe")

        def test_explicitWait(self):
            # 导入堆栈类
            import traceback
            # 导入By类
            from selenium.webdriver.common.by import By
            # 导入显示等待类
            from selenium.webdriver.support.ui import WebDriverWait
            # 导入期望场景类
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.common.exceptions import TimeoutException, NoSuchElementException
            url = "http://127.0.0.1/test_explicity_wait.html"
            # 访问自动以测试网页
            self.driver.get(url)
            try:
                wait = WebDriverWait(self.driver, 10, 0.2)
                wait.until(EC.title_is(u"你喜欢的水果"))
                print u"网页标题是“你喜欢的水果”"
                # 等待10秒，直到要找的按钮出现
                element = WebDriverWait(self.driver, 10).until \
                    (lambda x: x.find_element_by_xpath \
                        ("//input[@value='Display alert box']"))
                element.click()
                # 等待alert框出现
                alert = wait.until(EC.alert_is_present())
                # 打印alert框体消息
                print alert.text
                # 确认警告信息
                alert.accept()
                # 获取id属性值为“peach”的页面元素
                peach = self.driver.find_element_by_id("peach")
                # 判断id属性值为“peach”的页面元素是否能被选中
                peachElement = wait.until(EC.element_to_be_selected(peach))
                print u"下拉列表的选项“桃子”目前处于选中状态"
                # 判断复选框是否可见并且能被点击
                wait.until(EC.element_to_be_clickable((By.ID, 'check')))
                print u"复选框可见并且能被点击"
            except TimeoutException, e:
                # 捕获TimeoutException异常
                print traceback.print_exc()
            except NoSuchElementException, e:
                # 捕获NoSuchElementException异常
                print traceback.print_exc()
            except Exception, e:
                # 捕获其他异常
                print traceback.print_exc()

        def tearDown(self):
            # 退出IE浏览器
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

    def test_explicitWait(self):
        # 导入堆栈类
        import traceback
        # 导入By类
        from selenium.webdriver.common.by import By
        # 导入显示等待类
        from selenium.webdriver.support.ui import WebDriverWait
        # 导入期望场景类
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException, NoSuchElementException
        url = "http://127.0.0.1/test_explicity_wait.html"
        # 访问自动以测试网页
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)
            wait.until(EC.title_is(u"你喜欢的水果"))
            print u"网页标题是“你喜欢的水果”"
            # 等待10秒，直到要找的按钮出现
            element = WebDriverWait(self.driver, 10).until \
                (lambda x: x.find_element_by_xpath \
                    ("//input[@value='Display alert box']"))
            element.click()
            # 等待alert框出现
            alert = wait.until(EC.alert_is_present())
            # 打印alert框体消息
            print alert.text
            # 确认警告信息
            alert.accept()
            # 获取id属性值为“peach”的页面元素
            peach = self.driver.find_element_by_id("peach")
            # 判断id属性值为“peach”的页面元素是否能被选中
            peachElement = wait.until(EC.element_to_be_selected(peach))
            print u"下拉列表的选项“桃子”目前处于选中状态"
            # 判断复选框是否可见并且能被点击
            wait.until(EC.element_to_be_clickable((By.ID, 'check')))
            print u"复选框可见并且能被点击"
        except TimeoutException, e:
            # 捕获TimeoutException异常
            print traceback.print_exc()
        except NoSuchElementException, e:
            # 捕获NoSuchElementException异常
            print traceback.print_exc()
        except Exception, e:
            # 捕获其他异常
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



