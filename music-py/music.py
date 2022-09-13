import requests
import re
import json

# 存放rid值的url
url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=董真&pn=1&rn=30&httpsStatus=1&reqId=b287f1e0-37c9-11eb-846b-ed84ae20f627"
# 设置headers，伪装成浏览器
header = {
    "Cookie": "Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1607262271; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1607262271; _ga=GA1.2.1231848360.1607262271; _gid=GA1.2.1396442198.1607262271; kw_token=Z32FDL7NMN",
    "csrf": "Z32FDL7NMN",
    "Host": "www.kuwo.cn",
    "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
# 使用get方法进行获取文件中的资源
res = requests.get(url, headers=header)
# 由于获取下来的是json格式的数据，所以我们使用Python的json模块进行解析
dicts = json.loads(res.text)
# print(dicts)
rids = []  # 定义一个空列表用来存放爬取的rid
names = []  # 定义一个空列表用来存放音乐名
# print(len(dicts['data']['list']))
for i in range(len(dicts['data']['list'])):
    rids.append(dicts['data']['list'][i]['rid'])
    names.append(dicts['data']['list'][i]['name'])
# 设置一个存放歌曲文件的地址，这里需要大家改一下路径，改成自己电脑中有的文件夹，否则后面会报错
dir = "/home/cong/Music/"
# print(names)
count = 1
for rid, name in zip(rids, names):
    # 利用原有的url构造一个新的url
    url2 = "http://www.kuwo.cn/url?format=mp3&rid=" + str(
        rid) + "&response=url&type=convert_url3&br=128kmp3&from=web&t=1607262358400&httpsStatus=1&reqId=5ed69f10-37c9-11eb-bcbe-c7b03e63588b"
    res2 = requests.get(url2, headers=header)
    # 解析出文件中存放mp3文件的url地址
    text = json.loads(res2.text)
    print(text)
    music_url = text['url']
    res3 = requests.get(music_url)
    filename = dir + name + ".mp3"
    # 将文件写入文件中去
    with open(filename, "wb") as f:
        f.write(res3.content)
        print('第' + str(count) + '首歌曲下载成功')
        count += 1
