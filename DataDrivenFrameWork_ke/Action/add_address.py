#encoding=utf-8
from selenium import webdriver
from Util2.Log import *
import time
from PageObject.login_page import *
from PageObject.add_address import *
from ProjectVar.var import *

def add_address(driver,name="",mobile="",address="",index_provience=1,index_city=1,index_area=1,is_default=""):
    ad= AddressPage(driver)
    driver.get("https://ke.youdao.com/user/address/")
    time.sleep(2)
    Ad = AddressPage(driver)
    Ad.addaddresselement().click()
    time.sleep(5)
    Select(Ad.province()).select_by_index(index_provience)
    Select(Ad.city()).select_by_index(index_city)
    Select(Ad.area()).select_by_index(index_area)
    Ad.address().send_keys(address)
    Ad.name().send_keys(name)
    Ad.mobile().send_keys(mobile)
    if is_default== "True":
        ad.defaultbutton().click()
    Ad.submitbutton().click()
    time.sleep(5)



if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
    login(driver, "huihuitestecho@163.com", "Firewood612")
    add_address(driver)
    add_address(driver,"fosterwu","15899999999","test",1,1,4,True)
    driver.quit()