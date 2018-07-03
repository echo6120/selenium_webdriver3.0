#encoding=utf-8
from selenium import webdriver
import unittest, time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 创建一个FirefoxProfile实例，用于存放自定义配置
        profile = webdriver.FirefoxProfile()
        # 指定下载路径，默认只会自动创建一级目录，如果指定了
        # 多级不存在的目录，将会下载到默认路径
        profile.set_preference('browser.download.dir', 'd:\\iDownload')
        # 将browser.download.folderList设置为2，表示将文件下载到指定路径
        # 设置成2表示使用自定义下载路径；
        # 设置成0表示下载到桌面；设置成1表示下载到默认路径
        profile.set_preference('browser.download.folderList', 2)
        # browser.helperApps.alwaysAsk.force对于未知的 MIME 类型文件会弹出窗口
        # 让用户处理，默认值为true，设定为False表示不会记录打开未知 MIME 类型
        # 文件的方式
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        # 在开始下载时是否显示下载管理器
        profile.set_preference('browser.download.manager.showWhenStarting',\
                               False)
        # 设定为 False 会把下载框进行隐藏
        profile.set_preference("browser.download.manager.useWindow", False)
        # 默认值为 true，设定为 False 表示不获取焦点
        profile.set_preference("browser.download.manager. focusWhenStarting",\
                               False)
        # 下载.exe文件弹出警告，默认值是 true，设定为False 则不会弹出警告框
        profile.set_preference("browser.download.manager.alertOnEXEOpen",\
                               False)
        # browser.helperApps.neverAsk.openFile表示直接打开下载文件，不显示确认框
        # 默认值为空字符串，下行代码行设定了多种文件的 MIME类型，
        # 例如application/exe，表示.exe类型的文件，
        # application/excel表示 Excel 类型的文件
        profile.set_preference("browser.helperApps.neverAsk.openFile", \
                               "application/pdf")
        # 对所给出文件类型不再弹出框进行询问，直接保存到本地磁盘
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', \
                               'application/zip, application/octet-stream')
        # browser.download.manager.showAlertOnComplete设定下载文件结束后是否显示下
        #载完成提示框，默认为true，设定为False表示下载完成后不显示下载完成提示框
        profile.set_preference("browser.download.manager. showAlertOnComplete",\
                               False);
        # browser.download.manager.closeWhenDone设定下载结束后是否自动
        # 关闭下载框，默认值为true，设定为False 表示不关闭下载管理器
        profile.set_preference("browser.download.manager.closeWhenDone",\
                               False)

        # self.driver = webdriver.Ie(executable_path="c:\\IEDriverServer")
        # 启动浏览器时，通过firefox_profile参数
        # 将自动以配置添加到FirefoxProfile对象中
        self.driver = webdriver.Firefox(executable_path="e:\\geckodriver",\
                                        firefox_profile = profile)

    def test_dataPicker(self):
        # 访问WebDriver驱动Firefox的驱动文件下载网址
        url1 = "https://github.com/mozilla/geckodriver/releases"
        self.driver.get(url1)
        # 选择下载zip类型文件，使用application/zip指代此类型文件
        self.driver.find_element_by_xpath\
            ('//strong[.="geckodriver-v0.19.1-arm7hf.tar.gz"]').click()
        # 等待加载下载文件
        time.sleep(10)

        # 访问Python2.7.12文件下载页面，下载扩展名为msi文件
        # 使用application/octet-stream来指明此类文件类型
        url = "https://www.python.org/downloads/release/python-2712/"
        self.driver.get(url)
        # 找到Python2.7.12下载页面中链接文字为“Windows x86-64 MSI installer”
        # 的链接页面元素，点击进行无人工干预的下载Python2.7.12解释器文件
        self.driver.find_element_by_link_text\
            ("Windows x86-64 MSI installer").click()
        # 等待文件下载完成，根据各自的网络带宽情况设定等待相应的时间
        time.sleep(100)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()