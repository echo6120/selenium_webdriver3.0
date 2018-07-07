#encoding=utf-8
import os

#获取工程所在的目录的绝对路径
project_path=os.path.dirname(os.path.dirname(__file__))

#获取页面对象库文件的绝对路径
page_object_repository_path=project_path.decode("utf-8")+u"/Conf/PageObjectRepository.ini"

#测试数据excel文件的绝对路径
test_data_excel_path=project_path.decode("utf-8")+u"/TestData/data.xlsx"
#登录表,读数据从0开始，写数据从1开始
login_username_col_no=1
login_password_col_no=2
login_info_col_no=3
login_is_executed_col_no=4
login_test_result_col_no=6

#address表
address_name_col_no=1
address_mobile_col_no=2
address_address_col_no=3
address_provience_col_no=4
address_city_col_no=5
address_area_col_no=6
address_is_default_col_no=7
address_assert_keyword_col_no=8
address_is_executed_col_no2=9
address_excuted_time_col_no=11
address_test_result_col_no2=12


if __name__=='__main__':
    print project_path
    print page_object_repository_path
    print test_data_excel_path
    print os.path.exists(page_object_repository_path)
    print os.path.exists(test_data_excel_path)