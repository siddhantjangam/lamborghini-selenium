#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

s=Service(r'C:\Users\kunal\OneDrive\Desktop\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url='https://www.lamborghini.com/en-en'
driver.get(url)
time.sleep(1)


try:
    cookie=driver.find_element(by=By.XPATH,value="/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]")
    cookie.click()
except Exception as ep:
    pass
else:
    pass

time.sleep(1)
job_title=driver.find_element(by=By.XPATH,value="/html/body/div[1]/header/nav/ul[1]/li[1]/a/span")
job_title.click()

time.sleep(1)
job_title=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/section[1]/div/a/div")
job_title.click()


# In[ ]:


from bs4 import BeautifulSoup as bs
import requests

currentwebsite=driver.current_url
print(currentwebsite)

#get request
r=requests.get(currentwebsite)
r
htmlcontent=r.content
soup=bs(htmlcontent,"html.parser")
print(soup.prettify())

