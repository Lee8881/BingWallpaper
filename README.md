# BingWallpaper
设置BingWallpaper作为桌面背景
批处理执行

@echo off
D:
cd D:\Gits\BingWallpaper
start pythonw main.py
exit

利用.vbs文件去执行上述批处理（隐藏批处理运行窗口）
Set ws = CreateObject("Wscript.Shell")
ws.run "cmd /c D:\Startup.bat",vbhide
