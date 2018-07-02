#encoding=utf-8
import time
from Util2.ObjectMap import *
from Util2.ParsePageObjectRepository import ParsePageObjectRepositoryConfig

class LoginPage(object):

    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getItemsFromSection("163mail_login")
        print self.login_page_items

    def mobilelogin(self):
        locateType,locateExpression = self.login_page_items['login_page.mobilelogin'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def emaillogin(self):
        locateType,locateExpression = self.login_page_items['login_page.emaillogin'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def username(self):
        locateType,locateExpression=self.login_page_items['login_page.username'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

    def password(self):
        locateType,locateExpression=self.login_page_items['login_page.userpwd'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

    def loginbutton(self):
        locateType,locateExpression=self.login_page_items['login_page.loginbutton'].split(">")
        print "aaaaaaaaaaaaaa:",locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
    driver.get("https://ke.youdao.com/login")
    time.sleep(2)
    lp = LoginPage(driver)
    time.sleep(2)
    lp.emaillogin().click()
    lp.username().send_keys("huihuitestecho@163.com")
    lp.password().send_keys("Firewood612")
    time.sleep(5)
    lp.loginbutton().click()
    time.sleep(4)




