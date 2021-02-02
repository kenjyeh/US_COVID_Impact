#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Dependencies
import os
import csv
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from pandas.tseries.offsets import MonthEnd


# In[13]:


#Create file path 
#reference: https://www.zillow.com/research/data/ 
#mid-tier ZHVI
csvpath_zillow=os.path.join('..','Zillow.csv')
csvpath_covid=os.path.join('..','Covid_data_csv')


# In[14]:


#Pass the path into the read_csv(), this will create a dataframe from your file
zillow_df=pd.read_csv(csvpath_zillow)
covid_df=pd.read_csv(csvpath_covid)


# In[15]:


covid_df.head()


# In[17]:


zillow_df.head()


# In[18]:


#Start Data at State Name 
zlw1=zillow_df[zillow_df.columns[4:]]
zlw1.head()


# In[19]:


#Filter to Year of 2020
zlw2=zlw1[list(zlw1.columns[0:1])+list(zlw1.columns[289:])]
zlw2.head()


# In[20]:


#Reorganize date format to Month only 
df2.rename(columns={df2.columns[1]:"January",df2.columns[2]:"February",df2.columns[3]:"March",df2.columns[4]:"April",
                   df2.columns[5]:"May",df2.columns[6]:"June",df2.columns[7]:"July",df2.columns[8]:"August",
                   df2.columns[9]:"September",df2.columns[10]:"October",df2.columns[11]:"November",df2.columns[12]:"December"
                   },inplace=True)


# In[21]:


#df2['January']=df2['2020-01-31'].str.slice(0,7)
df2.head()


# In[ ]:





# In[22]:


clean_df=covid_df.loc[covid_df['Jurisdiction of Occurrence']!="United States"]
clean_df.head()


# In[23]:


#clean_df['Jurisdiction of Occurrence'].value_counts()


# In[24]:


clean_df['Month_Year'] = pd.to_datetime(clean_df['Week Ending Date'], errors='coerce')


# In[25]:


clean_df['Month'] = clean_df['Month_Year'].dt.strftime('%Y-%m')


# In[26]:


#Use Groupby to group by Month 
grouped_df=clean_df.groupby(clean_df["Month"],as_index=False)
print(grouped_df)


# In[27]:


totals_by_month=grouped_df["Week Ending Date"].sum()
totals_by_month.head()


# In[28]:


#Rename Columns to merge 
grouped_df.first()


# In[29]:


final_df=grouped_df[["Month","Jurisdiction of Occurrence","All Cause"]]
final_df.first()


# In[30]:


#Abbreviate States 
state_abbrev={'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'}
    


# In[32]:


final_df['abbrev'] =final_df['Jurisdiction of Occurrence'].replace(state_abbrev)


# In[ ]:


merge_df=pd.merge(final_df,zlw2,on="Jurisdiction of Occurrence")

