#!/usr/bin/env python
# coding: utf-8

# In[37]:


# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# In[38]:


from icecream import ic 
import chromedriver_autoinstaller
import time
import urllib
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
path ="D:/chromedriver-win64/chromedriver.exe"
# 
# driver.get('https://google.com')
# print(driver.title)
# driver.quit()
# driver.get('https://apps.usgs.gov/hivis/camera/FL_Sand_Key#&gid=1&pid=4180')


# In[39]:


import urllib.request
import requests


# In[ ]:


# to get the list of URLs

import pandas as pd
df=pd.read('webcam_link_list.csv')  #enter the file name here
URLs=list(df[df.columns[-1]])


# In[70]:


def openChrome(url):
    chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(path,options=chrome_options)

    # change above done by me Kumar Aditya

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver


# In[109]:


def folder_name(url):
    c = '/'
    lst=([pos for pos, char in enumerate(url) if char == c])
    y=int(lst[-1])+1
    folder_name=url[y:]
    return folder_name


# In[81]:


def findImages(driver):
    button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'MuiButton-outlined'))
    )
    driver.find_element(By.CLASS_NAME,'MuiButton-outlined').click()
    img_count=driver.find_element(By.CLASS_NAME,'pswp__counter').text
    oblic_index=img_count.index('/')
    start_index=oblic_index+2
    img_count=int(img_count[start_index:])
    
    # print(button.get_attribute('class'))
    # actions.click(button)
    print('clicked mui')
    return img_count

def findImage(driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'pswp__img'))
    )
    print('found images')
    return element
    # time.sleep(5)


# In[82]:


def saveImage(element,x,driver,folder_name):
    element=driver.find_element(By.XPATH,"//img[contains(@class,'pswp__img')]")

    src=element.get_attribute('src')
    src
    
    sample_path=r"C:\Users\Kumar Aditya\Desktop\SoCE_Winter_Project'23\images\{}\{}.jpg"
    path=sample_path.format(folder_name,x)
    
    urllib.request.urlretrieve(src,path)


# In[83]:


def something(driver):
    but = WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//body")))
    hover = ActionChains(driver).move_to_element(but)
    hover.perform()
    time.sleep(1)


# In[84]:


def rightClick(driver):
    button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'pswp__button--arrow--right'))
    )
    driver.find_element(By.CLASS_NAME,'pswp__button--arrow--right').click()
    # actions.click(button)
    print('clicked')


# In[85]:


def iterate(x,driver):
    element=findImage(driver)
    saveImage(element,x,driver)

    # once image is saved
    something(driver)
    rightClick(driver)

    # after this increment x by 1 until x becomes equal to length
    x=x+1
    if (x<=length):
        iterate(x,driver)
    else: pass


# In[86]:


# so it will go like this

for url in URLs:
    driver=openChrome(url)  #open the chrome tab
    length=findImages(driver)  #find the images

    # now we have to save the image one by one
    # so we will reiterate some functions as 
    
    print(length)
    
    # initialize x=1
    x=1
    
    iterate(x,driver)
    
    # close the driver
    driver.close()


# In[ ]:


import time
time.sleep(10)
# "Step through or download individual frames"
# print(driver.title)
# driver.close()

