#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


Pop_Kor = pd.read_csv("C:\\Users\\USER\\DataScience\\data\\Population_Korea_2023.csv")
Pop_Kor.head()


# In[3]:


import googlemaps

gmaps_key = "AIzaSyBKHoIYHjTuLZ-vhtDUg1w4rsX3xdcpttg"
gmaps = googlemaps.Client(key=gmaps_key)


# In[4]:


Hos_Kor = pd.read_csv("C:\\Users\\USER\\DataScience\\data\\Hospital_in_Korea.csv", encoding = "utf-8")
Hos_Kor.head(10)


# In[5]:


gmaps.geocode('가톨릭대학교인천성모병원',language = 'ko')


# In[6]:


Hos_name = []

for name in Hos_Kor['요양기관명']:
    Hos_name.append(str(name[:-1])+'병원')
    
Hos_name


# In[ ]:


Hos_address = []  ## 병원 전체 주소
Hos_lat = []      ## 병원 위도
Hos_lng = []      ## 병원 경도

for name in Hos_name:
    try: 
        tmp = gmaps.geocode(name, language = 'ko')
        Hos_address.append(tmp[0].get("formatted_address"))
        tmp_loc = tmp[0].get("geometry")
    
        Hos_lat.append(tmp_loc['location']['lat'])
    
        Hos_lng.append(tmp_loc['location']['lng'])
    
        print(name + '>>'+tmp[0].get("formatted_address"))
    except:
        pass


# In[ ]:


## 병원 주소
Hos_address


# In[ ]:


## 병원 위도
Hos_lat


# In[ ]:


## 병원 경도
Hos_lng


# In[ ]:


## 


# In[ ]:





# In[ ]:





# In[ ]:




