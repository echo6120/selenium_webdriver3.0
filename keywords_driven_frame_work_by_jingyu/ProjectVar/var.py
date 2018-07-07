#encoding=utf-8
import os
from Util.FormatTime import *
#获取工程所在的目录的绝对路径
project_path=os.path.dirname(os.path.dirname(__file__))

#获取页面对象库文件的绝对路径
#page_object_repository_path=project_path.decode("utf-8")+u"/Conf/PageObjectRepository.ini"

#测试数据excel文件的绝对路径
test_data_excel_path=project_path.decode("utf-8")+u"/TestData/testcase.xlsx"

#浏览器驱动文件所在的绝对路径
chromeDriverFilePath="D:\\python\\Scripts\\chromedriver.exe"
ieDriverFilePath='D:\\python\\Scripts\\geckodriver.exe'
firefoxDriverFilePath='D:\\python\\Scripts\\IEDriverServer.exe'

#截图存放的路径
filename = u"%s\\ScreenPicture\\CapturePicture\\%s\\%s.jpg" %( project_path,dates(),time_chinese())
errorfilename = u"%s\\ScreenPicture\\ErrorPicture\\%s\\%s.jpg" %( project_path,dates(),time_chinese())

#excel列的含义
action_name_col_no=2
locator_method_col_no=3
locator_expression_col_no=4
action_value_col_no=5
action_slapse_time_col_no=7
action_result_col_no=8
action_exception_info_col_no=9
capture_screen_path_onfo_col_no=10