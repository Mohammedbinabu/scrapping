from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/GPU/Desktop/msedgedriver.exe")
driver = webdriver.Edge(service = s)
driver.get('https://www.spsoftglobal.com/')
time.sleep(5)

cross = driver.find_element(by=By.XPATH,value='//*[@id="DefaultHomeDisclaimerModal"]')
cross.click()
time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for content to load

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # reached bottom
    last_height = new_height
time.sleep(5)

html = driver.page_source

with open('spsoft_C&IND.html','w',encoding='utf-8') as f:
    f.write(html)





