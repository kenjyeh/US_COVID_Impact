#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Dependencies
import os
import csv
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from pandas.tseries.offsets import MonthEnd


# In[15]:


#Create file path 
#reference: https://www.zillow.com/research/data/ 
#mid-tier ZHVI
csvpath_zillow=os.path.join('..','Zillow.csv')
csvpath_covid=os.path.join('..','Covid_data_csv')


# In[16]:


#Pass the path into the read_csv(), this will create a dataframe from your file
zillow_df=pd.read_csv(csvpath_zillow)
covid_df=pd.read_csv(csvpath_covid)


# In[17]:


print(zillow_df.columns)


# In[45]:


zillow_df.head()


# In[48]:


state_clean['Month']=state_clean['index'].str.slice(0,4)
state_clean.head()


# In[50]:


new_df=state_clean.loc[state_clean['Month']=='2020']
new_df[:3]


# In[54]:


new_df_3=zillow_df['StateName']
new_df_3[:3]


# In[52]:


df2=new_df[['Month','index']]
df2.head()


# In[61]:


df_4=zillow_df.iloc[0,289,290,291,292,293,294,295,296,297,298,299,300,301,:]
df_4


# In[47]:


state_clean=zillow_df.iloc[:,4:].transpose().reset_index()
state_clean


# In[46]:


state_clean['index'].value_counts()


# In[19]:


state_clean['index'].str.slice(0,7)


# In[21]:


clean_df=covid_df.loc[covid_df['Jurisdiction of Occurrence']!="United States"]
clean_df


# In[22]:


clean_df['Jurisdiction of Occurrence'].value_counts()


# In[23]:


clean_df['Month_Year'] = pd.to_datetime(clean_df['Week Ending Date'], errors='coerce')


# In[24]:


clean_df['Month'] = clean_df['Month_Year'].dt.strftime('%Y-%m')


# In[33]:


#Use Groupby to group by Month 
grouped_df=clean_df.groupby(clean_df["Month"],as_index=False)
print(grouped_df)


# In[34]:


totals_by_month=grouped_df["Week Ending Date"].sum()
totals_by_month.head()


# In[37]:


#Rename Columns to merge 
grouped_df.first()


# In[43]:


final_df=grouped_df[["Month","Jurisdiction of Occurrence","All Cause"]]
final_df.first()


# In[44]:


type(final_df)


# In[ ]:




