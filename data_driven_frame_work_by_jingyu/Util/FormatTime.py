#encoding=utf-8
import time
from datetime import timedelta,date

def date_time_chinese():
    u"returns the current time string,format for YYYY年mm月dd日 HH时MM分SS秒"
    return time.strftime("%Y年%m月%d日 %H时%M分%S秒",time.localtime())

def date_chinese():
    u"returns the current time string,format for YYYY年mm月dd日"
    return time.strftime("%Y年%m月%d日",time.localtime())

def time_chinese():
    u"returns the current time string,format for HH时MM分SS秒"
    return time.strftime("%H时%M分%S秒",time.localtime())

def date_time():
    "returns the current time string,format for YYYY-mm-dd HH:MM:SS"
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def date_time_slash():
    "returns the current time string,format for YYYY/mm/dd HH:MM:SS"
    return time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())

def dates():
    "returns the current time string,format for YYYY-mm-dd"
    return time.strftime("%Y-%m-%d",time.localtime())

def date_slash():
    "returns the current time string,format for YYYY/mm/dd"
    return time.strftime("%Y/%m/%d",time.localtime())

def times():
    "returns the current time string,format for HH:MM:SS"
    return time.strftime("%H:%M:%S",time.localtime())

def year():
    "returns the current time string,format for Year"
    return time.strftime("%Y",time.localtime())

def month():
    "returns the current time string,format for month"
    return time.strftime("%m",time.localtime())

def day():
    "returns the current time string,format for day"
    return time.strftime("%d",time.localtime())

def hour():
    "returns the current time string,format for Hour"
    return time.strftime("%H",time.localtime())

def minute():
    "returns the current time string,format for minute"
    return time.strftime("%M",time.localtime())

def seconds():
    "returns the current time string,format for seconds"
    return time.strftime("%S",time.localtime())

def str_to_tuple(stime):
    "returns the string variable into time tuples"
    return time.strptime(stime,"%Y-%m-%d %H:%M:%S")


def add_date(day_num):
    "returns in the current date and a time interval"
    today=date.today()
    times=today+timedelta(days=day_num)
    return times

def sub_date(day_num):
    "returns in the current date minus one time interval"
    today=date.today()
    times=today-timedelta(days=day_num)
    return times