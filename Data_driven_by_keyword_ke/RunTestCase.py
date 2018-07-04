#encoding=utf-8
from ProjectVar.var import test_data_excel_path
from Util.Exel import *
from ProjectVar.var import *
from Action.Action import *
from TestScript import Login163
from TestScript import basicinfo_rename

if __name__ == '__main__':
    Login163()
    basicinfo_rename()