# -*- coding: utf-8 -*-
import sys
import traceback
from Util.Exel import *
from Action.login import *
from Action.add_address import *
from ProjectVar.var import *

reload(sys)
sys.setdefaultencoding("utf8")

pe = ParseExcel(test_data_excel_path)
#操作登录表，写操作是从1开始，读操作是从0开始
pe.set_sheet_by_index(0)
#确认是否切换到要读的登录表
print pe.get_default_name()
#获取所有行，因为第一行是标题行，所有从第二行开始读
rows = pe.get_all_rows()[1:]
for id,row in enumerate(rows):
    #判断是否要执行，如果是y就执行，否则：忽略
    if row[login_is_executed_col_no].value.lower()=='y':
        print "username:", row[login_username_col_no].value
        print "password:", row[login_password_col_no].value
        username = row[login_username_col_no].value
        password = row[login_password_col_no].value
        driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
        try:
            test_data_result_flag = True
            login(driver, username, password)
            #pe.set_sheet_by_index(2)
            #pe.write_cell_content(id+2,test_result_col_no,"pass")
            #切换到地址信息表
            pe.set_sheet_by_index(1)
            #确认是否切换到了地址信息表
            info(u"已切换到"+pe.get_default_name())
            #test_data_result_flag = True
            for id2, row in enumerate(pe.get_all_rows()[1:]):
                if row[address_is_executed_col_no2].value.lower() == 'y':
                    try:
                        info(row[address_name_col_no].value)
                        info(row[address_mobile_col_no].value)
                        info(row[address_address_col_no].value)
                        info(row[address_provience_col_no].value)
                        info(row[address_is_default_col_no].value)
                        #print str(row[address_name_col_no].value),str(row[address_mobile_col_no].value),str(row[address_address_col_no].value)
                        add_address(driver, row[address_name_col_no].value, str(row[address_mobile_col_no].value), row[address_address_col_no].value, row[address_provience_col_no].value, row[address_city_col_no].value, row[address_area_col_no].value, row[address_is_default_col_no].value)
                        #add_address(driver,"jingwu","15899999999","test",1,1,4,True)
                        pe.write_cell_content(id2 + 2, address_excuted_time_col_no, date_time())
                        print "assert word:", row[address_assert_keyword_col_no].value
                        assert row[address_assert_keyword_col_no].value in driver.page_source
                        pe.set_sheet_by_index(1)
                        pe.write_cell_content(id2 + 2, address_test_result_col_no2, "pass")
                        # assert 1==2
                    except Exception, e:
                        traceback.print_exc()
                        # pe.write_cell_content(id + 2, 9, date_time())
                        pe.set_sheet_by_index(1)
                        pe.write_cell_content(id2 + 2, address_excuted_time_col_no, date_time())
                        pe.write_cell_content(id2 + 2, address_test_result_col_no2, "fail")
                        test_data_result_flag = False
                else:
                    pe.set_sheet_by_index(1)
                    pe.write_cell_content(id2 + 2, address_test_result_col_no2, u"忽略")
                    continue
        except Exception,e:
            test_data_result_flag = False
            #pe.set_sheet_by_index(1)
            print u"异常信息：",e
            print traceback
            #pe.write_cell_content(id + 2,login_test_result_col_no, "fail")
            info("error:"+e.message)

        if test_data_result_flag == True:
            pe.set_sheet_by_index(0)
            pe.write_cell_content(id + 2, login_test_result_col_no, u"成功")
        else:
            pe.set_sheet_by_index(0)
            pe.write_cell_content(id + 2, login_test_result_col_no, u"失败")

        time.sleep(3)
        #driver.quit()
    else:
        pe.set_sheet_by_index(0)
        pe.write_cell_content(id + 2, login_test_result_col_no, u"忽略")
        continue

