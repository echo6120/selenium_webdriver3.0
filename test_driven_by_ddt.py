# encoding=utf-8
from selenium import webdriver
import unittest, time
import logging, traceback
import ddt
from selenium.common.exceptions import NoSuchElementException

# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level = logging.INFO,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # 打印日志的时间
    datefmt = '%a, %d %b %Y %H:%M:%S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    filename = 'd:/report.log',
    # 打开日志文件的方式
    filemode = 'w'
)

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "D:\\python\\Scripts\\chromedriver.exe")
    @ddt.data([u"神奇动物在哪里", u"叶茨"],
              [u"疯狂动物城", u"古德温"],
              [u"大话西游之月光宝盒", u"周星驰"])
    @ddt.unpack   #解包，将测试数据对应到testdata 和 expectdata
    def test_dataDrivenByObj(self, testdata, expectdata):
        url = "http://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        # 设置隐式等待时间为10秒
        self.driver.implicitly_wait(10)
        try:
            # 找到搜索输入框，并输入测试数据
            self.driver.find_element_by_id("kw").send_keys(testdata)
            # 找到搜索按钮，并点击
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            # 断言期望结果是否出现在页面源代码中
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException, e:
            logging.error(u"查找的页面元素不存在，异常堆栈信息：" \
                          + str(traceback.format_exc()))
        except AssertionError, e:
            logging.info(u"搜索“%s”，期望“%s”，失败" %(testdata, expectdata))
        except Exception, e:
            logging.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
        else:
            logging.info(u"搜索“%s”，期望“%s”通过" %(testdata, expectdata))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()