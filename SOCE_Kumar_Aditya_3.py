#!/usr/bin/env python
# coding: utf-8

# ### code to get the headings as columns list

# In[1]:


# import requests
# from bs4 import BeautifulSoup
# url='https://waterdata.usgs.gov/monitoring-location/05576100/#parameterCode=00065&period=P7D&showMedian=true'

# page=requests.get(url)
# page_html=page.text
# soup=BeautifulSoup(page_html, 'html')

# # find the required table
# table=soup.find_all('table')[-1]

# # find all the headings
# metadata_element=table.find_all('th', scope='row')
# col=[item.text.strip() for item in metadata_element]


# ### uncomment the following code to upload the files containing the links from which data need to be scrapped

# In[2]:


# from google.colab import files
# uploaded=files.upload()

# file_name=list(uploaded.keys())[0]


# In[3]:


def empty_df():
  # creating an empty dataframe for the task

  import pandas as pd
  links_file=pd.read_csv('/content/'+file_name, index_col=False)

  index=links_file['relevant_col']
  # index is basically the column containing URLs

  df=pd.DataFrame(columns=col, index=index)
  return df


# In[4]:


# function to extract the data

def scrap(x):
  url=df.index[x]
  page=requests.get(url)
  html=page.text
  soup=BeautifulSoup(html, 'html')

  # finding the relevant table
  table=soup.find_all('table')[-1]

  # get all the relevant values
  loc_metadata=table.find_all('td', class_='loc-metadata')

  # loc_metadata[1].text.strip()
  rows=[item.text.strip() for item in loc_metadata]
  df.iloc[x]=rows

# function is ready


# ### Once the following code is run, we will get a dataframe containing all the data
# ### Only thing left is to export it as a csv file

# In[5]:


# for x in range(len(df.index)):
#   scrap(x)


# ### code for exporting into csv file
# ### the file will be saved in the current runtime storage
# ### we have to download it from there

# In[6]:


# df.to_csv('data.csv', index=False)


# ### code for the second type of websites here

# In[7]:


# # upload file here

# from google.colab import files
# uploaded = files.upload()


# In[8]:


import pandas as pd


# In[9]:


# csv=list(uploaded.keys())[0]

# links=pd.read_csv('\content\'+csv, index_col=False)
# links.drop(links.columns[0], axis=1, inplace=True)

# URLs=links['0']


# In[10]:


# csv=list(uploaded.keys())[0]

links=pd.read_csv('webcam_link_list.csv', index_col=False)
links.drop(links.columns[0], axis=1, inplace=True)

URLs=links['0']


# In[11]:


from bs4 import BeautifulSoup


# In[12]:


def get_html(url):
    from selenium import webdriver
    from selenium.webdriver import FirefoxOptions

#     opts = FirefoxOptions()
#     opts.add_argument("--headless")
#     browser = webdriver.Firefox(options=opts)

    browser = webdriver.Firefox()
    browser.get(url)
    html=browser.page_source
    browser.quit()
    return html


# In[13]:


def scrap_data(x):
  url=df2.index[x]
  html=get_html(url)
  soup=BeautifulSoup(html, 'html')
  data=soup.find_all('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-8 jss26 css-45ujxc')
  lst=[]
  for item in data:
    lst.append(item.text)
  df2.iloc[x]=lst


# In[14]:


# code for getting the columns list of the dataframe

# take any link to get the columns name from the "URLs" list
# they are basically the headings of different values

dummy_url=URLs[0]
dummy_html=get_html(dummy_url)
dummy_soup=BeautifulSoup(dummy_html, 'html')
col_data=dummy_soup.find_all('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-4 jss26 css-1udb513')
col=[item.text for item in col_data]

# here we get the columns list
col


# In[15]:


# creating an empty dataframe

df2=pd.DataFrame(index=URLs, columns=col)
df2.index.name=''

df2


# In[23]:


scrap_data(0)
scrap_data(1)
scrap_data(2)
scrap_data(3)


# In[24]:


df2


# In[17]:


df2.to_csv('data2.csv')

# # don't put index=False because in this case the index_col is URLs
# # which will get lost in this case

# # again the file will be saved in the current runtime storage
# # download it from there


# In[18]:


# dict={
#     "Headings":lst,
#     "url":lst2,
# }
# final_data=pd.DataFrame(dict)

# # initial try to get a dataframe with values...this works for a single URL


# ### Shortcut method to directly extract tables from webpages

# In[19]:


import pandas as pd
html=pd.read_html('https://waterdata.usgs.gov/monitoring-location/05576100/#parameterCode=00065&period=P7D&showMedian=true')
len(html)


# In[20]:


html[0]


# In[21]:


html[1]


# In[22]:


# here=pd.read_html('https://apps.usgs.gov/hivis/camera/IL_Lick_Cre')
# no tables found in this website

