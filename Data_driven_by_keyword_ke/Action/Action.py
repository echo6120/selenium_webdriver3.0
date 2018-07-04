# -- coding: utf-8 --
from  selenium import webdriver
import time
from Util.ObjectMap import *
from  ProjectVar.var import *
import traceback
from selenium.webdriver.chrome.options import Options
from Util.FormatTime import *
from Util.DirandFile import *

#定义全局浏览器driver变量
driver=None
def open_broswer(broswerName,*args):
    global driver
    try:
        if broswerName.lower().strip() =="chrome":
            chrome_options= Options()
            #添加屏蔽ignore-certificate-error提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignore-certificate-errors"]
            )
            driver = webdriver.Chrome(executable_path=chromeDriverFilePath,chrome_options = chrome_options)
        elif broswerName.lower() =="firefox":
            driver = webdriver.Chrome(executable_path=chromeDriverFilePath)
        elif broswerName.lower() =="ie":
            driver = webdriver.Chrome(executable_path=firefoxDriverFilePath)
    except Exception,e:
        print traceback.format_exc()
        raise e

def visit_url(url,*args):
    global driver
    try:
        driver.get(url)
    except Exception,e:
        print traceback.format_exc()
        raise e

def close_broswer(*args):
    global driver
    try:
        driver.quit()
    except Exception, e:
        print traceback.format_exc()
        raise e

def pause(seconds,*args):
    time.sleep(float(seconds))

def enter_frame(locatorMethod,locatorExpression,*args):
    global driver
    try:
        driver.switch_to.frame(getElement(driver,locatorMethod,locatorExpression))
    except Exception, e:
        print traceback.format_exc()
        raise e

def input_string(locatorMethod,locatorExpression,content,*args):
    try:
        getElement(driver, locatorMethod, locatorExpression).clear()
        getElement(driver,locatorMethod,locatorExpression).send_keys(content)
    except Exception,e:
        print traceback.format_exc()
        raise e

def click(locatorMethod,locatorExpression,*args):
    try:
        getElement(driver, locatorMethod, locatorExpression).click()
    except Exception,e:
        print traceback.format_exc()
        raise e

def login(usernameAndpassword,*args):
    username,password=usernameAndpassword.split("||")
    open_broswer("chrome")
    visit_url("http://mail.126.com")
    pause(3)
    enter_frame("id", "x-URS-iframe")
    pause(2)
    input_string("xpath", "//input[@name='email']", username)
    input_string("xpath", "//input[@name='password']", password)
    pause(2)
    click("id", "dologin")
    pause(2)
    assert_word(u"退出")

def assert_word(expected_word,*args):
    try:
        assert True ==(expected_word in driver.page_source)
    except AssertionError,e:
        raise e
    except Exception,e:
        raise e

def assert_button_word(locatorMethod,locatorExpression,expected_word,*args):
    try:
        text = getElement(driver, locatorMethod, locatorExpression).text
        print type(text)
        assert True ==(expected_word in text )
    except AssertionError,e:
        raise e
    except Exception,e:
        raise e

def assert_title(expected_word,*args):
    try:
        assert True ==(expected_word == driver.title)
    except AssertionError,e:
        raise e
    except Exception,e:
        raise e

def capture_screen():
    global driver
    createDir(project_path+"\\ScreenPicture\\CapturePicture\\",dates())
    try:
        driver.get_screenshot_as_file(filename)
    except Exception,e:
        raise e
    return filename

def capture_error_screen():
    global driver
    createDir(project_path+"\\ScreenPicture\\ErrorPicture\\",dates())
    try:
        driver.get_screenshot_as_file(errorfilename)
    except Exception,e:
        raise e
    return errorfilename


if __name__=="__main__":
    open_broswer("chrome")
    visit_url("https://ke.youdao.com")
    pause(3)
    assert_button_word("xpath","//*[@id='app']/div/div[1]/div/a[2]",u"首页")
    '''
    enter_frame("id", "x-URS-iframe")
    pause(2)
    input_string("xpath", "//input[@name='email']", "testman1980")
    input_string("xpath", "//input[@name='password']", "wulaoshi1978")
    pause(2)
    click("id", "dologin")
    pause(2)
    assert_word(u"退出")'''

    '''
    logininfo=("testman1980||wulaoshi1978","testman1980||wulaoshi1978")
    contact_info=[("g1","120999999@qq.com","15788888888",u"关键字驱动哦哦哦"),("g2","120999999@qq.com","15788888888",u"关键字驱动哦哦哦")]
    for i in logininfo:
        login(i)
        for j in contact_info:
            add_contact_info(j[0], j[1], j[2], j[3])
        driver.quit()'''







