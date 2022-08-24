# 导入模块

import requests
from bs4 import BeautifulSoup
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
    path = '/home/cong/Music/{0}/{1}'.format(author, title)
    print('歌曲:{0}-{1},正在下载...'.format(title, author))

    # r = requests.get(url)
    urlretrieve(url, path)
    print('下载完毕,{0}-{1},请试听'.format(title, author))


def get_music_name(name, page):
    """
  搜索歌曲名称
  :return:
  """

    protocol = "https:"
    # name = '白月光与朱砂痣'
    url = 'https://zhaoziyuan.me/s/?title={0}&page={1}'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        # 判断请求是异步还是同步
        "x-requested-with": "XMLHttpRequest",
    }

    res = requests.get(url=url.format(name, page), headers=headers)
    # json_text = res.text
    soup = BeautifulSoup(res.text, "html.parser")
    for link in soup.find_all('a', class_='news_btn'):
        # print(link)
        a = str(link)
        b = a[a.index("//"):a.index("',this")]
        c = b.split("','")
        print(c[0])
        print(c[1])
        song_download(protocol + c[0], c[1], name)
    # title = jsonpath.jsonpath(json_text, '$..title')
    # author = jsonpath.jsonpath(json_text, '$..author')
    # url = jsonpath.jsonpath(json_text, '$..url')
    # print(title, author, url)
    # for i in range(0, len(url)):
    #     song_download(url[i], title[i], author[i])


if __name__ == '__main__':
    singer = ["董真"]
    for s in singer:
        for i in range(0, 1):
            get_music_name(s, i)
