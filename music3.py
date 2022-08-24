# 导入模块
from tkinter import *
import requests
import jsonpath
import os
from urllib.request import urlretrieve

# 2.功能实现
"""
  1.url
  2.模拟浏览器请求
  3.解析网页源代码
  4.保存数据
"""


def song_download(url, title, author):
    # 创建文件夹
    os.makedirs(author, exist_ok=True)
    path = '{0}/{1}.mp3'.format(author, title)
    print('歌曲:{0}-{1},正在下载...'.format(title, author))

    r = requests.get(url)
    urlretrieve(r.url, path)
    print('下载完毕,{0}-{1},请试听'.format(title, author))


def get_music_name(name, page, platfrom):
    """
  搜索歌曲名称
  :return:
  """

    # name = '白月光与朱砂痣'
    url = 'https://music.liuzhijin.cn/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        # 判断请求是异步还是同步
        "x-requested-with": "XMLHttpRequest",
    }
    param = {
        "input": name,
        "filter": "name",
        "type": platfrom,
        "page": page,
    }
    res = requests.post(url=url, data=param, headers=headers)
    json_text = res.json()

    title = jsonpath.jsonpath(json_text, '$..title')
    author = jsonpath.jsonpath(json_text, '$..author')
    url = jsonpath.jsonpath(json_text, '$..url')
    print(title, author, url)
    for i in range(0, len(url)):
        song_download(url[i], title[i], author[i])


if __name__ == '__main__':
    singer = ["董真","心然","河图","银临","μ's","绯村柯北","fripSide","玄觞","澤野弘之"]
    for s in singer:
        for i in range(0, 5):
            get_music_name(s, i, "netease")
