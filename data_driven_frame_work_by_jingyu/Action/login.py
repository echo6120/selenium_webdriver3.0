#encoding=utf-8
from selenium import webdriver

from PageObject.login_page import *
from Util.FormatTime import *
from Util.Log import *


def login(driver,username, password):
    driver.get("https://ke.youdao.com/login")
    time.sleep(2)
    lp = LoginPage(driver)
    time.sleep(2)
    lp.emaillogin().click()
    lp.username().send_keys(username)
    lp.password().send_keys(password)
    time.sleep(5)
    lp.loginbutton().click()
    time.sleep(4)
    #from Util2.Log import info
    info("login successfully!")
    print date_time_chinese()

if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
    login(driver,"huihuitestecho@163.com", "Firewood612")
