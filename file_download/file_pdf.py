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

file_ids = ['8a81811c840a27b901840ab1f3f90c62', '8a81819e840a25ef01840aacf4050d63',
            '8a81811b840a25e501840aa99faf0ddf', '8a81811c840a27b901840aa3ce400be6']

# url = "https://file.trialos.com.cn/file/pdf/convert/{}?safety=true&repeatable=true&reserve=false"

# update_url = "https://file.trialos.com.cn/updateSql?token=4028e9027186ba05017186bc63ca0038"
#
# sql = "select sharding_table_name from t_id_mapping where table_name ='t_fs_file' and id = '{}' limit 1;"
#
# update_sql = "update {0} set transfer_status=0 where id='{1}';"
headers = {
    'TM-Header-Token': 'f9a461535f454c15bd7cfd42164c365c',
    'Content-Type': 'application/json'
}

# for file_id in file_ids:
#     print(file_id)
#     payload = sql.format(file_id)
#     print(payload)
#     time.sleep(random.randint(1, 5))
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     data = json.loads(response.text)
#     print(data)
#     t = data['sharding_table_name']
#     print(t)
#     u = update_sql.format(t, file_id);
#     print(u)
#     response = requests.request("POST", update_url, headers=headers, data=u)
#     print(response.text)

url = "https://file.trialos.com.cn/file/pdf/convert/"

with open('./a.txt', 'r') as f:
    for i in f.readlines():
        file_id = i.strip()
        print(file_id)
        a = url+file_id+"?safety=true&repeatable=true&reserve=false"
        print(a)
        time.sleep(random.randint(1, 3))

        response = requests.request("POST", a, headers=headers)

        print(response.text)
