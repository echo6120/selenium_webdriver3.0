 #encoding=utf-8
from selenium import webdriver
from Util2.Log import *
from Util2.FormatTime import *
from Util2.Exel import *
import time
from Action.add_address import *
from Action.login import *
from ProjectVar.var import *

import sys
reload(sys)
sys.setdefaultencoding("utf8")

pe = ParseExcel(test_data_excel_path)
#操作登录表
pe.set_sheet_by_index(2)
print pe.get_default_name()
rows = pe.get_all_rows()[1:]
for id,row in enumerate(rows):
    if row[is_executed_col_no].value=='y':
        print "username:", row[username_col_no].value
        print "password:", row[password_col_no].value
        username = row[username_col_no].value
        password = row[password_col_no].value
        driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
        try:
            login(driver, username, password)
            driver.quit()
        except Exception,e:
            print e



'''

login(driver, username, password)
add_address(driver,name,mobile,address,index_provience,index_provience,index_provience,is_default)
driver.quit()'''
