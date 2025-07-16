from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

s = Service(r'C:\Users\GPU\Desktop\msedgedriver.exe')
driver = webdriver.Edge(service=s) 
driver.get('https://www.spsoftglobal.com/')
time.sleep(13)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
html = driver.page_source
with open('services.html','w',encoding='utf-8') as f:
    f.write(html)