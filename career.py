from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

s = Service('C:/Users/ADMIN/Desktop/msedgedriver.exe')
driver = webdriver.Edge(service=s) 
driver.get('https://www.spsoftglobal.com/')
# time.sleep(2)
# disclaimer = driver.find_element(by=By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(13)
career = driver.find_element(by=By.XPATH,value='/html/body/app-root/div/app-header/nav/div/div[2]/ul/li[3]/a').click()
time.sleep(8)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('career.html','w',encoding='utf-8') as f:
    f.write(html)
    # for i in range(1,)
    # driver.find_element(by=By.XPATH,value=f'/html/body/app-root/app-career/div[2]/div/div/div[2]/div[{n}]/h2/button').click()
# cr1 = driver.find_element(by=By.XPATH,value='/html/body/app-root/app-career/div[2]/div/div/div[2]/div[1]/h2/button').click()
# time.sleep(3)
# cr2 = driver.find_element(by=By.XPATH,value='/html/body/app-root/app-career/div[2]/div/div/div[2]/div[2]/h2/button').click()
# time.sleep(3)
