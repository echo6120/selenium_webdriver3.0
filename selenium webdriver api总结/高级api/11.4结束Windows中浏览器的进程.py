#encoding=utf-8
from selenium import webdriver
import unittest
import os

class VisitSogouByIE(unittest.TestCase):


    def test_killWindowsProcess(self):
        # 启动火狐浏览器
        firefoxDriver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        # 启动IE浏览器
        ieDriver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        # 启动Chrome浏览器
        chromeDriver = webdriver.Chrome(executable_path="e:\\chromedriver")
        # 导入Python的os包
        import os
        # 结束Firefox浏览器进程
        returnCode = os.system("taskkill /F /iM firefox.exe")
        if returnCode == 0:
            print u"成功结束Firefox浏览器进程！"
        else:
            print u"结束Firefox浏览器进程失败！"
        # 结束IE浏览器进程
        returnCode = os.system("taskkill /F /iM iexplore.exe")
        if returnCode == 0:
            print u"成功结束IE浏览器进程！"
        else:
            print u"结束IE浏览器进程失败！"
        # 结束Chrome浏览器进程
        returnCode = os.system("taskkill /F /iM chrome.exe")
        if returnCode == 0:
            print u"成功结束Chrome浏览器进程！"
        else:
            print u"结束Chrome浏览器进程失败！"


if __name__ == '__main__':
    unittest.main()