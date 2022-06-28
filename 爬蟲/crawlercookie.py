#利用cookie在爬蟲時，偽造成一般使用者
import urllib.request as req
def getdata(url):
    #偽造成一般使用者，增加request header 的資訊(開發人員工具network)
    request = req.Request(url, headers = {
        'cookie' : 'over18=1',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }) 

    with req.urlopen(request) as response: #打開request物件
        data = response.read().decode('utf-8')

    #解析原始碼，取得所需項目(使用第三方套件beautifulsoup4)
    import bs4
    root = bs4.BeautifulSoup(data, 'html.parser')

    titles = root.find_all('div', class_ = "title") #利用class搜索
    for t in titles:
        print(t.a.string) #印出該頁標題
    
    nextpage = root.find_all('a', string = '‹ 上頁') #利用內文搜索
    for page in nextpage:
        return page['href'] #找到上頁網址

'''
pageurl = 'https://www.ptt.cc/bbs/Gossiping/index.html'
pageurl = 'https://www.ptt.cc' + getdata(pageurl)
print(pageurl) #印出上頁網址
'''

'''
#印3頁法一while
pageurl = 'https://www.ptt.cc/bbs/Gossiping/index.html'
count = 0
while count < 3:
    pageurl = 'https://www.ptt.cc' + getdata(pageurl)
    count += 1
    print()
'''

#印三頁法二(for)
pageurl = 'https://www.ptt.cc/bbs/Gossiping/index.html'
for i in range(3):
    pageurl = 'https://www.ptt.cc' + getdata(pageurl) #getdata(pageurl)得到上頁短網址
    #pageurl等於完整上頁網址
    print()
