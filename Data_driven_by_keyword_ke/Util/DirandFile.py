#encoding=utf-8
import os
from FormatTime import *
from ProjectVar.var import *

def createDir(path,dirName):
    dirPath = os.path.join(path,dirName)
    if os.path.exists(dirPath):
        pass
    else:os.mkdir(dirPath)

if __name__=="__main__":
    createDir(project_path+"\\ScreenPicture\\CapturePicture\\",dates())