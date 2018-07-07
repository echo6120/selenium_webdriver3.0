#encoding=utf-8
#encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素对象
def getElement(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 5).until\
            (lambda x: x.find_element(by = locateType, value = locatorExpression))
        return element
    except Exception, e:
        raise e

# 获取多个相同页面元素对象，以list返回
def getElements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 10).until\
            (lambda x:x.find_elements(by = locateType, value = locatorExpression))
        return elements
    except Exception, e:
        raise e

if __name__ == '__main__':
    from selenium import webdriver
    # 进行单元测试
    driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
    driver.get("http://mail.126.com")
    searchBox = getElement(driver, "xpath", "//input[@name='email']")
    driver.quit()