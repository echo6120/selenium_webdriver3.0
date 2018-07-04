;新建一个名为loadFile.au3的AutoItScript编辑器，文件具体内容如下：
;ControlFocus("title","text",controlID)
;表示将焦点切换到标题为title窗体中的controlID上
;Edit1表示第一个可以编辑的实例
;title表示弹出的Window窗口标题，不同浏览器的标题可能不一样

;等待10秒以便window窗口加载成功
WinWait("[CLASS:#32770]","",10)

;将焦点切换到Edit1输入框中
ControlFocus("另存为","","Edit1")

;等待2秒
Sleep(2000)

;将要下载的文件名及路径写入Edit1编辑框中
ControlSetText("另存为","", "Edit1", "d:\iDownload\Firefox Setup 35.0b8.exe")

Sleep(2000)

;点击窗体中的第一个按钮，也就是保存按钮
ControlClick("另存为","","Button1")

;Send("{ENTER}")
;Send("{ENTER}")
;保存后将该文件编译成exe文件，并存放到本地磁盘。
;Sleep(2000)
Send("{LEFT}")
Send("{LEFT}")
Send("{ENTER}")
Send("{ENTER}")
