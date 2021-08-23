import os
import socket
import time
import requests
import win32api
import win32con
import win32gui
from io import BytesIO
from PIL import Image
from lxml import etree


def get_wallpaper():
    # 等待联网
    s = socket.socket()
    s.settimeout(3)
    while 1:
        try:
            status = s.connect_ex(('cn.bing.com', 443))
            print(status)
            break
        except socket.gaierror as e:
            time.sleep(3)
            print("err")

    # 发送请求
    url = "https://cn.bing.com"
    res = requests.get(url=url)
    bing = res.text

    # 解析网页
    xml = etree.HTML(bing)
    pic = xml.xpath('//a[@download = "BingWallpaper.jpg"]/@href')
    pic = str(pic)[2:-2]  # 地址
    title = xml.xpath('//a[@class = "title"]/text()')
    title = str(title)[2:-2]  # 标题

    # 保存图片
    folder_path = './photo'
    save_dir = "photo\\" + str(title) + ".jpg"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print(str(url) + str(pic))
    html = requests.get(url + pic)
    image = Image.open(BytesIO(html.content))
    image.save(save_dir)

    # 设置壁纸
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0,
                                    win32con.KEY_SET_VALUE)  # 打开指定注册表
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "10")  # 2拉伸,0剧中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")  # 1平铺,0拉伸剧中等
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, "photo\\" + str(title) + ".jpg",
                                  win32con.SPIF_SENDWININICHANGE)  # 设置桌面


if __name__ == '__main__':
    get_wallpaper()
