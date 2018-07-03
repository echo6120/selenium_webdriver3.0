#encoding=utf-8
from selenium import webdriver
import unittest
import time

def addAttribute(driver, elementObj, attributeName, value):
    # 封装向页面标签中添加新属性方法
    # 调用JavaScript代码给页面标签添新属性，arguments[0]－［2］分别会用后面的
    # element、attributeName和value参数值进行替换，并执行该JavaScript代码
    # 添加新属性的JavaScript代码语法为：element.attributeName = value
    # 比如input.name="test"
    driver.execute_script("arguments[0].%s=arguments[1]" %attributeName,\
                          elementObj, value)

def setAttribute(driver, elementObj, attributeName, value):
    # 封装设置页面对象的属性值的方法
    # 调用JavaScript代码修改页面元素的属性值，arguments[0]－［2］分别会用后面的
    # element、attributeName和value参数值进行替换，并执行该JavaScript代码
    driver.execute_script("arguments[0].setAttribute\
    (arguments[1],arguments[2])", elementObj, attributeName, value)

def getAttribute(elementObj, attributeName):
    # 封装获取页面对象的属性值的方法
    return elementObj.get_attribute(attributeName)

def removeAttribute(driver, elementObj, attributeName):
    # 封装删除页面元素属性的方法
    # 调用JavaScript代码删除页面元素的指定的属性，arguments[0]－［1］分别会用后面的
    # element、attributeName参数值进行替换，并执行该JavaScript代码
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",\
                          elementObj, attributeName)

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Chrome(executable_path = "e:\\chromedriver")
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
    def test_dataPicker(self):
        url = "http://127.0.0.1/test_change_attr.html"
        # 访问自定义网页
        self.driver.get(url)
        # 找到页面上标签名为input的页面元素
        element = self.driver.find_element_by_xpath("//input")

        # 向页面文本框input标签中添加新属性name="search"
        addAttribute(self.driver, element, 'name', "search")
        # 添加新属性后，查看一下新添加的属性
        print u'添加的新属性值%s="%s"' %("name", getAttribute(element, "name"))

        # 查看修改前文本框input标签的value属性值
        print u"更改文本框中的内容前的内容：", getAttribute(element, "value")
        # 更改input页面元素的value属性值为“这是更改后的文字内容”
        setAttribute(self.driver, element, "value", u"xxxxxxx")
        # 更改input页面元素的value属性值后，再次查看其value属性值
        print u"更改文本框中内容后的内容：", getAttribute(element, "value")
        time.sleep(3)

        # 查看修改前文本框input页面元素中的size属性值
        print u"更改前文本框标签中的size属性值：", getAttribute(element, "size")
        # 更改input页面元素的size属性值为“20”
        setAttribute(self.driver, element, "size", 20)
        # 更改input页面元素的size属性值后，再次查看其size属性值
        print u"更改后文本框标签中的size属性值：", getAttribute(element, "size")
        time.sleep(3)

        # 查看删除input页面元素value属性前value属性值
        print u"文本框value属性值：", getAttribute(element, "value")
        # 删除文本框的value属性
        removeAttribute(self.driver, element, "value")
        # 删除文本框的value属性后，再次查看value属性值
        print u"删除value属性值后value属性值：", getAttribute(element, "value")
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()