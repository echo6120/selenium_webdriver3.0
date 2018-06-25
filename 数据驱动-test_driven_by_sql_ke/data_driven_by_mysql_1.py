#encoding=utf-8
from selenium import webdriver
import time
import datetime
import MySQLdb
from selenium.webdriver.common.keys import Keys

def get_test_data():
    conn = MySQLdb.connect(
    host = "127.0.0.1", 
    port = 3306,
    user = "root",
    db = "ketest",
    charset = "utf8"
    )
    # 使用cursor()方法获取数据库的操作游标
    cursor = conn.cursor()
    cursor.execute("select * from testdata;")
    resSet = cursor.fetchall()
    print u"共%s条数据。" %len(resSet)
    print resSet
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()
    return resSet

def update_test_result(data,result):
    conn = MySQLdb.connect(
    host = "127.0.0.1", 
    port = 3306,
    user = "root",
    db = "ketest",
    charset = "utf8"
    )
    # 使用cursor()方法获取数据库的操作游标
    cursor = conn.cursor()
    print 'update testdata set test_result="'+result+'" where kename="'+data+'";'
    update=cursor.execute('update testdata set test_result="'+result+'" where kename="'+data+'";')
    
    print u"修改语句受影响的行数：", update
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()

driver=webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
test_result=[]
for data in get_test_data():
    try:
        driver.get("https://ke.youdao.com/")
        search = driver.find_element_by_class_name("_3l-Kp")
        search.send_keys(data[1])
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        assert data[2] in driver.page_source
        update_test_result(data[1],u"成功")
    except AssertionError,e:
        print data[2] +u"断言失败"
        update_test_result(data[1],u"断言失败")
    except Exception,e:
        print e
        print data[1] +u"测试执行出现异常"
        update_test_result(data[1],u"执行出现异常")

driver.quit()
