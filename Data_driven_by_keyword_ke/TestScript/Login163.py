#encoding=utf-8
from ProjectVar.var import test_data_excel_path
from Util.Exel import *
from ProjectVar.var import *
from Action.Action import *
from Util.Log import *

#设置此次测试的环境编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#创建解析Excel对象
test_data_file = ParseExcel(test_data_excel_path)
test_data_file.set_sheet_by_name(u"登录")
info("现在操作的Excel表是："+test_data_file.get_default_name())

action_name=''
locator_method=''
locator_expression=''
action_value=''
for id,row in enumerate(test_data_file.get_all_rows()[1:]):
    action_name = row[action_name_col_no].value
    locator_method = row[locator_method_col_no].value
    locator_expression = row[locator_expression_col_no].value
    action_value= row[action_value_col_no].value
    if locator_method is None and locator_expression is None and action_value is None:
        command_line = action_name+"()"
        print "command line:",command_line
    elif locator_method is not None and locator_expression is not None and action_value is None:
        #enter_frame("id", "x-URS-iframe")
        command_line = action_name +"('"+locator_method+"',"+"'"+locator_expression+ "')"
        print "command line:", command_line

    elif locator_method is  None and locator_expression is None and action_value is not None:
        #pause(2)
        command_line = "%s(u'%s')" %(action_name,action_value)
        print "command line:", command_line
    else:
        #input_string("xpath", "//input[@name='password']", password)
        #input_string('xpath','//input[@name='email']',testman1980)
        command_line = '%s("%s","%s",u"%s")' %(action_name,locator_method,locator_expression,action_value)
        print "command line:", command_line
    try:
        time1=time.time()
        result=eval(command_line)
        elapse_time ="%.2f" %(time.time()-time1)
        test_data_file.write_cell_content(id+2,action_slapse_time_col_no,elapse_time)
        test_data_file.write_cell_content(id + 2, action_result_col_no, u"成功")
        info("执行成功")
        test_data_file.write_cell_content(id + 2, capture_screen_path_onfo_col_no, result)
        test_data_file.save_excel_file()
    except Exception,e:
        elapse_time = "%.2f" % (time.time() - time1)
        error(u"出错，%s" % traceback.format_exc())
        #print traceback.format_exc()
        test_data_file.write_cell_content(id + 2, action_slapse_time_col_no, elapse_time)
        test_data_file.write_cell_content(id + 2, action_result_col_no, u"失败")
        result = capture_error_screen()
        test_data_file.write_cell_content(id + 2, capture_screen_path_onfo_col_no, result)
        test_data_file.write_cell_content(id + 2, action_exception_info_col_no, traceback.format_exc())
        test_data_file.save_excel_file()