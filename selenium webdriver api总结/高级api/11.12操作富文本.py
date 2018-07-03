#encoding=utf-8
from selenium import webdriver
import unittest, time, traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Firefox浏览器
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Firefox(executable_path="e:\\geckodriver")

    def test_SohuMailSendEMail(self):
        url = "http://mail.sohu.com"
        # 访问搜狐邮箱登录页
        self.driver.get(url)
        try:
            userName = self.driver.find_element_by_xpath\
                (u'//input[@placeholder="请输入您的邮箱"]')
            userName.clear()
            userName.send_keys("fosterwu")
            passWord = self.driver.find_element_by_xpath\
                (u'//input[@placeholder="请输入您的密码"]')
            passWord.clear()
            passWord.send_keys("1111")
            login = self.driver.find_element_by_xpath(u'//input[@value="登 录"]')
            login.click()
            wait = WebDriverWait(self.driver, 10)
            # 显示等待，确定页面是否成功登录并跳转到登录成功后的首页
            wait.until(EC.element_to_be_clickable\
                           ((By.XPATH, '//li[text()="写邮件"]')))
            self.driver.find_element_by_xpath(u'//li[text()="写邮件"]').click()
            time.sleep(2)
            receiver = self.driver.find_element_by_xpath\
                ('//div[@arr="mail.to_render"]//input')
            # 输入收件人
            receiver.send_keys("fosterwu@sohu.com")
            subject = self.driver.find_element_by_xpath\
                ('//input[@ng-model="mail.subject"]')
            # 输入邮件标题
            subject.send_keys(u"一封测试邮件！")
            # 获取邮件正文编辑区域的iframe页面元素对象
            iframe = self.driver.find_element_by_xpath\
                ('//iframe[contains(@id, "ueditor")]')
            # 通过switch_to.frame()方法切换进入富文本框中
            self.driver.switch_to.frame(iframe)
            # 获取富文本框中编辑页面元素对象
            editBox = self.driver.find_element_by_xpath("/html/body")
            # 输入邮件正文
            editBox.send_keys(u"邮件的正文内容")
            # 从富文本框中切换出，回到默认页面
            self.driver.switch_to.default_content()
            # 找到页面上的“发送”按钮，并单击它
            self.driver.find_element_by_xpath('//span[.="发送"]').click()
            # 显示都等待含有关键字串“发送成功”的页面元素出现在页面中
            wait.until(EC.visibility_of_element_located\
                           ((By.XPATH, '//span[.="发送成功"]')))
            print u"邮件发送成功"
        except TimeoutException:
            print u"显示等待页面元素超时"
        except NoSuchElementException:
            print u"寻找的页面元素不存在", traceback.print_exc()
        except Exception:
            # 打印其他异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()