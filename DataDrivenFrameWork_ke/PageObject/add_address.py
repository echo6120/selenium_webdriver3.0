#encoding=utf-8
import time
from Util2.ObjectMap import *
from Util2.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from Action.login import *
from selenium.webdriver.support.ui import Select
import random


class AddressPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.address_items=self.parse_config_file.getItemsFromSection("ke_address")
        print self.address_items

    def address(self):
        locateType, locateExpression = self.address_items['add_address.address'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def name(self):
        locateType, locateExpression = self.address_items['add_address.name'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def mobile(self):
        locateType, locateExpression = self.address_items['add_address.mobile'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def submitbutton(self):
        locateType, locateExpression = self.address_items['add_address.submitbutton'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def addaddresselement(self):
        locateType, locateExpression = self.address_items['add_address.addaddresselement'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def province(self):
        locateType, locateExpression = self.address_items['add_address.province'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def city(self):
        locateType, locateExpression = self.address_items['add_address.city'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def area(self):
        locateType, locateExpression = self.address_items['add_address.area'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def defaultbutton(self):
        locateType, locateExpression = self.address_items['add_address.defaultbutton'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)
'''
    def select_options(self,element):
        select_element = Select(element)
        # 获取所有选项对象
        all_options_element = select_element.options
        # 将选项值存在列表里
        choiceelementtext = []
        for i in all_options_element:
            choiceelementtext.append(i)
        # 从所有选项值中，随机选一个
        selectedelement = random.choice(choiceelementtext)
        select_element.select_by_visible_text(selectedelement.text)
        # 断言是否选中了想选的年份
        assert(select_element.all_selected_options[0].text == selectedelement.text)
        time.sleep(5)'''


if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
    login(driver, "huihuitestecho@163.com", "Firewood612")
    driver.get("https://ke.youdao.com/user/address/")
    time.sleep(2)
    Ad = AddressPage(driver)
    Ad.addaddresselement().click()
    time.sleep(5)
    Select(Ad.province()).select_by_index(1)
    Select(Ad.city()).select_by_index(1)
    Select(Ad.area()).select_by_index(1)
    Ad.address().send_keys("test")
    Ad.name().send_keys("testname")
    Ad.mobile().send_keys("15677777777")
    Ad.submitbutton().click()
    time.sleep(5)