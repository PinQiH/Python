#爬蟲練習

'''
import urllib.request as req
url = 'https://www.dcard.tw/f/funny'
with req.urlopen(url) as response:
    data = response.read().decode('utf-8')
print(data) #被認為是外部入侵者，被拒絕取得原始碼
'''


import urllib.request as req
url = 'https://www.dcard.tw/f/funny'
request = req.Request(url, headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}) #偽造成一般使用者，增加request header 的資訊(開發人員工具network)
with req.urlopen(request) as response: #打開request物件
    data = response.read().decode('utf-8')

'''
print(data) #印出所有程式碼
'''

#解析原始碼，取得所需項目(使用第三方套件beautifulsoup4)
import bs4
root = bs4.BeautifulSoup(data, 'html.parser')

'''
print(root.title) #抓網頁標籤
print(root.title.string) #抓標籤內文字
'''


titles = root.find('a', class_ = "tgn9uw-3 bbdvDs") #只找一個
print(titles.span.string) 


'''
titles = root.find_all('a', class_ = "tgn9uw-3 bbdvDs") 
print(titles) #得到標題列表
'''


titles = root.find_all('a', class_ = "tgn9uw-3 bbdvDs") 
for title in titles:
    print(title.span.string) 
