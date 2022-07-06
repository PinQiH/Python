#網路連接
import urllib.request as request

'''
src = 'https://www.ntu.edu.tw/'
with request.urlopen(src) as response:
    data = response.read().decode('utf-8') #取得網頁原始碼
print(data)
'''

#串接、擷取公開資料
import json
src = 'https://api.kcg.gov.tw/api/service/get/3e092ef1-9a19-4e52-b567-eef48120147c'
with request.urlopen(src) as response:
    data = json.load(response) 

'''
print(data)
'''

clist = data['data'] #從資料中取得所需材料

'''
print(clist)
'''

with open('data.txt', 'w', encoding = 'utf-8') as file: #將所需資料寫入檔案
    for date in clist:
        file.write(date['發生日期'] + '\n') #寫入材料中所需特定項目