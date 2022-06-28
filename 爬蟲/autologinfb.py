from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#設定要前往的網址
url = "https://www.facebook.com"

#透過Browser Driver 開啟 Chrome
driver = webdriver.Chrome("C:/Users/H98L/OneDrive/桌面/python/chromedriver.exe")        

#前往該網址
driver.get(url)        

#登入的帳號與密碼
username = "0972723890"
password = "k79130cassie"

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

#切換頁面
spec_url = 'https://www.facebook.com/moea.gov.tw'
driver.get(spec_url)