from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv
import time
# import os
# load_dotenv()
s = Service('C:/Users/ADMIN/Desktop/msedgedriver.exe')
driver = webdriver.Edge(service=s)  # Corrected from Chrome to Edge
driver.get('https://www.linkedin.com/')
time.sleep(16)
login = driver.find_element(by=By.XPATH,value='/html/body/main/section[1]/div/div/a').click()
time.sleep(3)
email = driver.find_element(by=By.XPATH,value='/html/body/div/main/div[2]/div[1]/form/div[1]/input')
password = driver.find_element(by=By.XPATH,value='/html/body/div/main/div[2]/div[1]/form/div[2]/input')
time.sleep(3)
detail1 = 'mohammedabubakar3678@gmail.com'
detail2 = 'Football cr7'
email.send_keys(detail1)
time.sleep(3)
password.send_keys(detail2)
time.sleep(3)
password.send_keys(Keys.ENTER)
#sign = driver.find_element(by=By.XPATH,value='/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
time.sleep(3)
menu = driver.find_element(by=By.XPATH,value='/html/body/div[6]/header/div/nav/ul/li[4]/a').click()



