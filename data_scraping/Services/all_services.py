from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

s = Service(r'C:\Users\GPU\Desktop\msedgedriver.exe')
driver = webdriver.Edge(service=s) 
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
ai = driver.find_element(By.XPATH, "//a[contains(text(),'AI Development')]")
ai.click()
time.sleep(4)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('aiml_services.html','w',encoding='utf-8') as f:
    f.write(html)
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
da = driver.find_element(By.XPATH, "//a[contains(text(),'Data Analytics')]")
da.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('da_services.html','w',encoding='utf-8') as f:
    f.write(html)
time.sleep(3)
# ----------------------------------------------------------------------------------
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
ad = driver.find_element(By.XPATH, "//a[contains(text(),'Application Development')]")
ad.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('ad_services.html','w',encoding='utf-8') as f:
    f.write(html)
#----------------------------------------------------------------
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
mad = driver.find_element(By.XPATH, "//a[contains(text(),'Mobile App Development')]")
mad.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('mad_services.html','w',encoding='utf-8') as f:
    f.write(html)
#---------------------------------------------------------------
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
wd = driver.find_element(By.XPATH, "//a[contains(text(),'Web Development')]")
wd.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('wd_services.html','w',encoding='utf-8') as f:
    f.write(html)
#------------------------------------------------------------------
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
ts = driver.find_element(By.XPATH, "//a[contains(text(),'Testing')]")
ts.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('ts_services.html','w',encoding='utf-8') as f:
    f.write(html)
#----------------------------------------------------------------------------------
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
dm = driver.find_element(By.XPATH, "//a[contains(text(),'Digital Marketing')]")
dm.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('dm_services.html','w',encoding='utf-8') as f:
    f.write(html)
#------------------------------------------------------------------------
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
wfs = driver.find_element(By.XPATH, "//a[contains(text(),'Workforce solution')]")
wfs.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('wfs_services.html','w',encoding='utf-8') as f:
    f.write(html)
#--------------------------------------------------------------------------
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
pe = driver.find_element(By.XPATH, "//a[contains(text(),'Prompt Engineering')]")
pe.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('pe_services.html','w',encoding='utf-8') as f:
    f.write(html)
#--------------------------------------------------------------
driver.get('https://www.spsoftglobal.com/')
time.sleep(2)
driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[12]/div/div/div/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.nav-link > img[alt='menu']").click()
time.sleep(3)
services_element = driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
services_element.click()
time.sleep(3)
aws = driver.find_element(By.XPATH, "//a[contains(text(),'AWS')]")
aws.click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height = new_height
html = driver.page_source
with open('aws_services.html','w',encoding='utf-8') as f:
    f.write(html)