#!/usr/bin/env python
# coding: utf-8

# In[113]:


import requests
from bs4 import BeautifulSoup


# In[114]:


import selenium


# In[115]:


from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[116]:


url='https://mesonet.agron.iastate.edu/sites/networks.php?network=IA_ASOS'


# In[133]:


def stations(url):
    html=requests.get(url).text

    soup=BeautifulSoup(html,'html')

    soup=soup.find('select','iemselect2')

    #type(soup)
    stations=[option.text for option in soup.find_all('option')]

    stations=stations[1:]
    #len(stations)

    return stations


# In[134]:


stations=stations(url)
# type(stations)


# In[125]:


browser=webdriver.Chrome()
browser.get(url)


# In[126]:


import os
path='stations'
if not os.path.exists(path):
    os.mkdir(path)
else:
    print("folder already exists")


# In[135]:


def browse(browser,station):
    menu=browser.find_element(By.TAG_NAME,'select')

    select=Select(menu)
    
    select.select_by_visible_text(station) 

    # button=browser.find_element(By.TAG_NAME,'input')
    # button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div/form/table[1]/tbody/tr[4]/td/input')))

    # browser.implicitly_wait(10)
    # ActionChains(browser).move_to_element(button).click(button).perform()
    button.click()

    # finally the button gets clicked

    url=browser.current_url
    url
    
    import pandas as pd
    table=pd.read_html(url)
    table[1].to_csv('stations\{}.csv'.format(station))


# In[136]:


for station in stations[:10]:
    browse(browser,station)


# In[137]:


browser.close()


# In[138]:


# code completed

