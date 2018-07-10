#encoding=utf-8
import unittest
from selenium import webdriver
from PageObject.login_page  import *
import time

class testlogin126(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")

    def login(self):
        self.driver.get("https://mail.126.com/")
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_id("x-URS-iframe"))
        time.sleep(2)
        username = self.driver.find_element_by_name("email")
        username.clear()
        username.send_keys("testman1980")
        password = self.driver.find_element_by_name("password")
        password.send_keys("wulaoshi1978")
        loginbutton = self.driver.find_element_by_id("dologin")
        loginbutton.click()
        time.sleep(5)

    def test_send_email(self):
        self.login()
        write_lettre_link = self.driver.find_element_by_xpath("//span[text()='写 信']")
        write_lettre_link.click()
        time.sleep(5)
        mail_address = self.driver.find_element_by_xpath("//input[@role='combobox' and @tabindex='1']")
        mail_subject = self.driver.find_element_by_xpath("//input[@tabindex='1' and @maxlength='256']")
        file_element = self.driver.find_element_by_xpath("//input[@type='file']")
        mail_address.send_keys("111111111@qq.com")
        mail_subject.send_keys(u"测试邮件")
        file_element.send_keys("d:\\a.txt")
        time.sleep(5)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@tabindex=1]"))
        # editBox = driver.find_element_by_xpath("/html/body")
        self.driver.execute_script("document.getElementsByTagName('body')\
                        [0].innerHTML='<b>美丽的小赤赤，该下班了<b>;'")
        # 另外一种方法：editBox.click()执行两次，在调用editBox.send_keys函数来输入内容
        self.driver.switch_to.default_content()

        send_mail_button = self.driver.find_element_by_xpath("//footer//span[text()='发送']")
        send_mail_button.click()
        time.sleep(5)
        assert u"发送成功" in self.driver.page_source

        logout_link = self.driver.find_element_by_xpath("//a[text()='退出']")
        time.sleep(3)
        assert u"登录" in self.driver.page_source



if __name__=="__main__":
    #testcase1 = unittest.TestLoader().loadTestsFromTestCase(test_login)
    suite = unittest.TestSuite()
    suite.addTest(testlogin126("test_send_email"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

