from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

s = Service('C:/Users/ADMIN/Desktop/msedgedriver.exe')
driver = webdriver.Edge(service=s) 
driver.get('https://www.spsoftglobal.com/about-us')

time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('aboutus.html','w',encoding='utf-8') as f:
    f.write(html)