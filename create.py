import os

# 生成两个文件 , 一个快捷方式
import winshell
from win32com.client import Dispatch


def create_file():
    path = os.getcwd()  # 获取当前路径
    print(path)
    text = "@echo off\r\n" + path[0:3] + "\r\ncd " + path + "\r\nstart pythonw main.py\r\nexit\r\n"
    file = open(path + "\\" + 'wallpaper' + '.bat', 'w')
    file.write(text)
    file.close()

    text = 'Set ws = CreateObject("Wscript.Shell")\r\nws.run "cmd /c ' + path + '\wallpaper.bat",vbhide'
    file = open(path + "\\" + 'wallpaper' + '.vbs', 'w')
    file.write(text)
    file.close()

    filepath = path + "\wallpaper.vbs"
    startup = winshell.startup()
    startup_path = os.path.join(startup, "startBingWallpaper.lnk")
    target = filepath
    wDir = path
    icon = path + "\icon.ico"
    print(icon)

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(startup_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

if __name__ == '__main__':
    create_file()
