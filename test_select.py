#encoding=utf-8
from selenium import webdriver
import unittest
import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import email
import os
import random
from selenium.webdriver.support.ui import Select


class Testaccountsetting(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")

    @classmethod
    def tearDownClass(self):
        # 退出IE浏览器
        self.driver.quit()


    def test_login(self):
        email.test_a_ke163login(self)
    
    def test_birth(self):
        url = "https://ke.youdao.com/user/account/"
        # 访问自定义网页
        self.driver.get(url)
        #获取select页面元素对象，年份
        select_year = Select(self.driver.find_element_by_id("account-birth-y"))
        #获取所有选项对象
        all_options_year = select_year.options
        #将选项值存在列表里
        choiceyeartext=[]
        for i in all_options_year:
            choiceyeartext.append(i)
        #从所有选项值中，随机选一个
        selectedyear = random.choice(choiceyeartext)
        #选中随机选的年份
        select_year.select_by_visible_text(selectedyear.text)
        #断言是否选中了想选的年份
        self.assertEqual(select_year.all_selected_options[0].text,selectedyear.text)

        # 获取select页面元素对象，月份
        select_month = Select(self.driver.find_element_by_id("account-birth-m"))
        # 获取所有选项对象
        all_options_month = select_month.options
        # 将选项值存在列表里
        choicemonthtext = []
        for j in all_options_month:
            choicemonthtext.append(j)
        # 从所有选项值中，随机选一个
        selectedmonth = random.choice(choicemonthtext)
        # 选中随机选的年份
        select_month.select_by_visible_text(selectedmonth.text)
        # 断言是否选中了想选的年份
        self.assertEqual(select_month.all_selected_options[0].text, selectedmonth.text)

        #获取select页面元素对象,日期
        select_day = Select(self.driver.find_element_by_id("account-birth-d"))
        #获取所有选项对象
        all_options_day = select_day.options
        #将选项值存在列表里
        choicedaytext=[]
        for i in all_options_day:
            choicedaytext.append(i)
        #从所有选项值中，随机选一个
        selectedday = random.choice(choicedaytext)
        #选中随机选的年份
        select_day.select_by_visible_text(selectedday.text)
        #断言是否选中了想选的年份
        self.assertEqual(select_day.all_selected_options[0].text,selectedday.text)

        fileSubmitButton = self.driver.find_element_by_id("submit-btn")
        # 单击提交按钮，完成文件上传操作
        fileSubmitButton.click()
        time.sleep(5)
        comfirmtext = self.driver.find_element_by_xpath('//h2[text()="保存成功"]')
        # *[@id="dialog-alert"]/div/table/tbody/tr/td[2]/div[1]/h2
        self.assertTrue(comfirmtext, "没有上传成功的弹框")
        comfirmbutton = self.driver.find_element_by_xpath(
            "//div[@class='box-content']/div[@class='tac']/input[@class='g-btn-green finish box-ok']")
        comfirmbutton.click()
        time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Testaccountsetting("test_login"))
    suite.addTest(Testaccountsetting("test_birth"))
    runner = unittest.TextTestRunner()
    runner.run(suite)