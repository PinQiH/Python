from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import re

# 網站抽象類別
class Website(ABC):
 
    def __init__(self, profile_url):
        self.profile_url = profile_url  # 連結屬性
 
    @abstractmethod
    def scrape(self):  # 爬取資料抽象方法
        pass

# 臉書爬蟲
class Facebook(Website):
 
    def scrape(self):
 
        result = []  # 回傳結果
 
        if self.profile_url:  # 如果輸入連結非空值
 
            #允許權限
            options = webdriver.ChromeOptions()
            options.add_experimental_option("prefs", { \
                "profile.default_content_setting_values.notifications": 2     
            })
            driver = webdriver.Chrome(chrome_options = options)
                
            #設定要前往的網址
            url = "https://www.facebook.com"

            #前往該網址
            driver.get(url)        

            #登入的帳號與密碼
            username = "projectprojectp@gmail.com"
            password = "project123"

            #輸入賬號密碼
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
            elem = driver.find_element_by_id("email")
            elem.send_keys(username)

            elem = driver.find_element_by_id("pass")
            elem.send_keys(password)        

            elem.send_keys(Keys.RETURN)
            time.sleep(5)

            #檢查有沒有被擋下來
            if len(driver.find_elements_by_xpath("//*[contains(text(), '你的帳號暫時被鎖住')]")) > 0:
                driver.find_elements_by_xpath("//*[contains(text(), '是')]")[1].click()

            if self.profile_url.count('profile.php') == 0:
                about_url = self.profile_url + "/about_contact_and_basic_info"
                like_url = self.profile_url + "/likes_all"
                friend_url = self.profile_url + "/friends"
            else:
                about_url = self.profile_url + "&sk=about_contact_and_basic_info"
                like_url = self.profile_url + "&sk=likes_all"
                friend_url = self.profile_url + "&sk=friends"

            driver.get(self.profile_url)
            time.sleep(1)

            #網頁下滑
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            #開始爬蟲
            htmltext = driver.page_source
            soup = BeautifulSoup(htmltext, "lxml")
  
            #姓名
            name = soup.find("span", class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 l1jc4y16 fe6kdd0r mau55g9w c8b282yb rwim8176 mhxlubs3 p5u9llcw hnhda86s oo9gr5id oqcyycmt")
            result.append(dict(name=name.text)) 

            #性別
            driver.get(about_url)
            time.sleep(1)
                
            htmltext = driver.page_source
            soup = BeautifulSoup(htmltext, "lxml")
            
            genders = soup.find_all("span", class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m")
            if genders != None:
                for gender in genders:
                    if gender != None:
                        if gender.text == "男性":
                            result.append(dict(gender=1)) 
                            break
                        elif gender.text == "女性":
                            result.append(dict(gender=2)) 
                            break
                        else:
                            continue
                    else:
                        result.append(dict(gender=0)) 
                        break
            else:
                result.append(dict(gender=0)) 

            #貼文
            numbers = soup.find_all("div", class_="j83agx80 cbu4d94t")
            if numbers == None:
                result.append(dict(post_num=0)) 
                result.append(dict(post1=0, post2=0, post3=0, post4=0, post5=0))
            else:
                if len(numbers) <= 9:
                    for number in numbers:
                        #內文
                        content = number.find("div", class_="ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a")
                        if content != None:
                            result.append(dict(post1=content.text)) #內文
                        else:
                            result.append(dict(post1="無內文")) 
                            
                        #發文時間
                        post_time = number.find("a", class_="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw")
                        result.append(dict(post2=post_time.text)) #發布時間
                        
                        #相差時間
                        lst = []
                        for j in post_time.text:
                            lst.append(j)
                            
                        today = datetime.date.today()       #今天日期
                        year = today.strftime("%Y")         #今年年分
                        day = today.strftime("%d")          #今天幾號
                        num = [int(s) for s in re.findall(r'-?\d+\.?\d*', post_time.text)]      #暫存begin_day
                        
                        if ( "月" or "日" ) in lst:
                            if ( "年" and "月" and "日") in lst:  #年月日
                                begin_day = datetime.date(num[0], num[1], num[2])
                                result = today - begin_day
                                result.append(dict(post3=str(result.days))) #相差時間
                            elif ( "年" and "月" ) in lst and ( "日" ) not in lst:  #年月
                                num.insert(2, int(day))            #加日期
                                begin_day = datetime.date(num[0], num[1], num[2])
                                result = today - begin_day
                                result.append(dict(post3=str(result.days)))
                            else:  #月日
                                num.insert(0, int(year))  #加年分
                                begin_day = datetime.date(num[0], num[1], num[2])
                                result = today - begin_day
                                result.append(dict(post3=str(result.days)))
                        else:
                            result.append(dict(post3=str(post_time.text)))
                        
                        #按讚數
                        thumb = number.find("span", class_="pcp91wgn")
                        if thumb != None:
                            result.append(dict(post4=str(thumb.text))) #按讚數
                        else:
                            result.append(dict(post4=0))
                        
                        #留言數
                        comment = number.find("span", class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain")
                        if comment != None:
                            result.append(dict(post5=''.join(filter(str.isdigit, comment.text)))) #留言數
                        else:
                            result.append(dict(post5=0))
                        
                else:
                    i = 0
                    for number in numbers:
                        if i >= 9:
                            break
                        
                        content = number.find("div", class_="ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a")
                        if content != None:
                            result.append(dict(post1=content.text)) #內文
                        else:
                            result.append(dict(post1=0)) 
                            
                        #發文時間
                        post_time = number.find("a", class_="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw")
                        result.append(dict(post2=post_time.text)) #發布時間
                        
                        #相差時間
                        lst = []
                        for j in post_time.text:
                            lst.append(j)
                            
                        today = datetime.date.today()       #今天日期
                        year = today.strftime("%Y")         #今年年分
                        day = today.strftime("%d")          #今天幾號
                        num = [int(s) for s in re.findall(r'-?\d+\.?\d*', post_time.text)]      #暫存begin_day
                        
                        if ( "月" or "日" ) in lst:
                            if ( "年" and "月" and "日") in lst:  #年月日
                                begin_day = datetime.date(num[0], num[1], num[2])
                                result = today - begin_day
                                result.append(dict(post3=str(result.days))) #相差時間
                            elif ( "年" and "月" ) in lst and ( "日" ) not in lst:  #年月
                                num.insert(2, int(day))            #加日期
                                begin_day = datetime.date(num[0], num[1], num[2])
                                result = today - begin_day
                                result.append(dict(post3=str(result.days)))
                            else:  #月日
                                num.insert(0, int(year))  #加年分
                                begin_day = datetime.date(num[0], num[1], num[2])
                                result = today - begin_day
                                result.append(dict(post3=str(result.days)))
                        else:
                            result.append(dict(post3=str(post_time.text)))
                        
                        #按讚數
                        thumb = number.find("span", class_="pcp91wgn")
                        if thumb != None:
                            result.append(dict(post4=str(thumb.text))) #按讚數
                        else:
                            result.append(dict(post4=0))
                        
                        #留言數
                        comment = number.find("span", class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain")
                        if comment != None:
                            result.append(dict(post5=''.join(filter(str.isdigit, comment.text)))) #留言數
                        else:
                            result.append(dict(post5=0))
                        i += 1
                    
                result.append(dict(post_num=len(numbers)))

            #簡介
            abouts = soup.find_all("div", class_="rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr o8rfisnq p8fzw8mz pcp91wgn iuny7tx3 ipjc6fyt") 
            i = 1
            for about in abouts:
                record = []
                record.append(about.text)
                i += 1

            result.append(dict(about=record)) 
            result.append(dict(about_num=i-1)) #總筆數

            #相片
            photos = soup.find_all("div", class_="qno324ep l9j0dhe7 tvmbv18p j83agx80")
            count = 0
            for photo in photos:
                record = []
                record.append(photo.img["src"])
                count += 1

            result.append(dict(photo=record)) 
            result.append(dict(photo_num=count)) #總張數
            
            #大頭貼
            propic = soup.find("div", class_="rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t gs1a9yip owycx6da btwxx1t3 ihqw7lf3 cddn0xzi")
            link = []
            for j in propic:
                link.append(str(j))
            if 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.30497-1/143086968_2856368904622192_1959732218791162458_n.png?' in link[0]:
                result.append(dict(propic=0)) #無大頭貼
            else:
                if propic.image != None:
                    result.append(dict(propic=propic.image["xlink:href"]))
                else:
                    result.append(dict(propic=propic.a["href"]))
            
            #封面照片
            cover = soup.find(attrs={"data-imgperflogname": "profileCoverPhoto"})
            if cover == None:
                result.append(dict(cover=0)) #無封面照片
            else:
                result.append(dict(cover=cover["src"]))

            #好友
            driver.get(friend_url)
            time.sleep(1)
            
            #網頁下滑
            last_height = driver.execute_script("return document.body.scrollHeight")
            for i in range(1):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            
            #開始爬蟲
            htmltext = driver.page_source
            soup = BeautifulSoup(htmltext, "lxml")
            
            friends = soup.find_all("div", class_="bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr")
            if friends == None:
                result.append(dict(friend=0))
            else:
                i = 0
                temp = 0
                linklst =[]
                for f in friends:
                    friend = f.find("span", class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb mdeji52x a5q79mjw g1cxx5fr lrazzd5p oo9gr5id")
                    if temp == 10:
                        break
                    link = f.a["href"]
                    linklst.append(link)
                    temp += 1
                    if friend != None:
                        i += 1
                        record = []
                        record.append(friend.text)
                        result.append(dict(friend=record)) #好友清單
                    else:
                        continue
            
            #朋友數
            num = soup.find("span", class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh e9vueds3 j5wam9gi knj5qynh q66pz984")
            if num != None:
                result.append(dict(friend_num=num.text)) #總好友數
            else:
                result.append(dict(friend_num=-1))  #可能是權限不足
            
            #性別比
            male = 0 #前10位好友的男生數
            female = 0 #前10位好友的女生數
            
            for i in range(len(linklst)):
                if linklst[i].count('profile.php') == 0:
                    about_url = linklst[i] + "/about_contact_and_basic_info"
                else:
                    about_url = linklst[i] + "&sk=about_contact_and_basic_info"
                    
                driver.get(about_url)
                time.sleep(1)
                
                #開始爬蟲
                htmltext = driver.page_source
                soup = BeautifulSoup(htmltext, "lxml")
                
                genders = soup.find_all("span", class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m")
                
                for gender in genders:
                    if gender != None:
                        if gender.text == "男性":
                            male += 1
                            break
                        elif gender.text == "女性":
                            female += 1
                            break
                        else:
                            continue
                    else:
                        break
            
            if female != 0:
                ratio = male / female
                result.append(dict(friend_ratio=ratio))
            else:
                result.append(dict(friend_ratio=10))
                
            #說讚的內容
            driver.get(like_url)
            time.sleep(1)
            
            #網頁下滑
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            
            #開始爬蟲
            htmltext = driver.page_source
            soup = BeautifulSoup(htmltext, "lxml")
            
            likes = soup.find_all("span", class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p oo9gr5id hzawbc8m")
            if len(likes) >= 9:
                temp = 1
                for i in likes:
                    temp += 1
                    if temp == 9:
                        for j in range(temp):
                            record = []
                            record.append(likes[j].text)
                            result.append(dict(likes=record)) #說讚的內容
                result.append(dict(likes_num=temp-1)) #總筆數

            elif len(likes) == 0:
                result.append(dict(likes=0))
                result.append(dict(likes_num=0))

            else:
                for x in likes:
                    record = []
                    record.append(x.text)
                    result.append(dict(likes=record))
                result.append(dict(likes_num=len(likes)))

            driver.close()

        return result