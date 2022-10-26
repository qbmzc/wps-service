import requests
import json
import time
import random

'''
瑞金医院：59689365b676439d87b2a650001af23a
浙江省人民医院：7edcdfdd0aa4475f838aa650001af23a
太美第一人民医院: 16a67708-597c-11e8-a539-00163e02f99a
上海市第一人民医院：b861be59f22b49829747a650001af23a
'''

select_url = "https://file.trialos.com.cn/selectSql?token=4028e9027186ba05017186bc63ca0038"

update_url = "https://file.trialos.com.cn/updateSql?token=4028e9027186ba05017186bc63ca0038"

pdf_url = "https://file.trialos.com.cn/file/pdf/convert/{}?safety=true&repeatable=true&reserve=false"

sql = "select sharding_table_name from t_id_mapping where table_name ='t_fs_file' and id = '{}' limit 1;"

update_sql = "update {0} set transfer_status=0 where id='{1}';"

headers = {
    'TM-Header-Token': 'f9a461535f454c15bd7cfd42164c365c',
    'Content-Type': 'application/json'
}

# for i in range(1, 101):
#     table = file_sql.format(i)
#     print(table)
#     response = requests.request("POST", select_url, headers=headers, data=table)
#     data = json.loads(response.text)
#     print(data)
#     for file_id in data:
#         print(file_id)
#         payload = update_sql.format(file_id)
#         print(payload)
#         time.sleep(random.randint(1, 5))
#
#         u = update_sql.format(i, file_id)
#         print(u)
#         # response = requests.request("POST", update_url, headers=headers, data=u)
#         # print(response.text)
#         a = pdf_url.format(file_id)
#         print(a)
# response = requests.request("POST", a, headers=headers)

# print(response.text)
#
count = 0
with open('./a.txt', 'r') as f:
    for i in f.readlines():
        file_id = i.strip()
        print(file_id)
        # 查询表名
        payload = sql.format(file_id)
        print(payload)

        response = requests.request("POST", select_url, headers=headers, data=payload)
        data = json.loads(response.text)
        print(data)
        t = data['sharding_table_name']
        print(t)
        u = update_sql.format(t, file_id)
        print(u)
        # 更新状态
        response = requests.request("POST", update_url, headers=headers, data=u)
        print(response.text)
        # 请求转换
        a = pdf_url.format(file_id)
        print(a)
        time.sleep(random.randint(1, 3))

        response = requests.request("POST", a, headers=headers)
        print(response.text)
        count = count + 1
        print(count)
