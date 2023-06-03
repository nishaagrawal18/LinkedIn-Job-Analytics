#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[31]:


pip install webdriver_manager


# In[5]:


#reading jobid csv file

df=pd.read_csv("jobid.csv")
df


# In[21]:


# creating a list of job id dataframe

li=df.id.values.tolist()


# In[32]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:




#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com/login')
sleep(3)
# login into linkedln

username=driver.find_element(By.ID,'username')
username.send_keys('kartikeyabhatia@gmail.com')                            ###################################################### <<<<<ADD EMAIL ID HERE 
password=driver.find_element(By.ID,'password')
password.send_keys('7877237706')                            ###################################################### <<<<<ADD PASSWORD HERE
login_button=driver.find_element(By.CLASS_NAME,'btn__primary--large')
login_button.click()
sleep(5)
project_data=[]
# this loop will give final raw data , but loop execution will take a lot of time maybe more than 45 minutes, depends on length of li list.

for i in li:
    try:
        driver.get(f'https://www.linkedin.com/jobs/view/{i}')
        sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2)

        soup=BeautifulSoup(driver.page_source,"html.parser")
        sleep(1)

        tit=soup.find('h1',class_="t-24 t-bold jobs-unified-top-card__job-title")
        titlee=tit.text.strip()

        com=soup.find('span',class_="jobs-unified-top-card__company-name")
        companyy=com.text.strip()

        loc=soup.find('span',class_="jobs-unified-top-card__bullet")
        locationn=loc.text.strip()

        workplace=soup.find('span',class_="jobs-unified-top-card__workplace-type")
        workplacee=workplace.text.strip()

        applicants=soup.find('span',class_='jobs-unified-top-card__subtitle-secondary-grouping t-black--light')
        applicantss=applicants.text.strip()

        involvement=soup.find('li',class_="jobs-unified-top-card__job-insight")
        involvementt=involvement.text.strip()

        followers=soup.find('div',class_='artdeco-entity-lockup__subtitle ember-view t-16')
        followerss=followers.text.strip()

        a=soup.find('div',class_="t-14 mt5")
        typee=a.text.strip()

        job_dict={
            'job_title':titlee,
            'company':companyy,
            'location':locationn,
            'workplace':workplacee,
            'applicants':applicantss,
            'involvement':involvementt,
            'followers':followerss,
            'industry and employees':typee
            }

        project_data.append(job_dict)
        sleep(2)
    except:
        continue
driver.close()


# In[ ]:


df=pd.DataFrame(project_data)
df


# In[ ]:


# converting dataframe into csv file
df.to_csv("project_database.csv")


# In[ ]:





# In[ ]:




