#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv(r"C:\Users\Downloads\file.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.index


# In[6]:


df.columns


# In[7]:


df.dtypes


# In[8]:


df.Temp_C.unique().sum()


# In[13]:


df['Press_kPa'].nunique()


# In[9]:


df.nunique()


# In[10]:


df.count()


# In[11]:


df['Weather'].value_counts()


# In[12]:


df.info()


# In[13]:


df[df['Weather'] == 'Clear']


# In[14]:


df.groupby('Weather').get_group('Clear')


# In[15]:


df.groupby('Wind Speed_km/h').get_group(4)


# In[16]:


df[df['Wind Speed_km/h']==4]


# In[17]:


df.isnull().sum()


# In[18]:


df.notnull().sum()


# In[19]:


df.rename(columns={'Weather': 'Weather Condition'})


# In[20]:


df.head()


# In[21]:


df.rename(columns={'Weather': 'Weather Condition'},inplace=True)


# In[22]:


df.head()


# In[23]:


df.Visibility_km.mean()


# In[24]:


df.Press_kPa.std()


# In[25]:


df['Rel Hum_%'].var()


# In[26]:


df[df['Weather Condition'] == 'Snow']


# In[27]:


df['Weather Condition'].value_counts()


# In[30]:


df[df['Weather Condition'] == 'Snow']


# In[31]:


df[df['Weather Condition'].str.contains('Snow')]


# In[35]:


df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)]


# In[37]:


df.groupby('Weather Condition').mean()


# In[38]:


df.groupby('Weather Condition').sum()


# In[39]:


df.groupby('Weather Condition').max()


# In[40]:


df.groupby('Weather Condition').min()


# In[44]:


df[df['Weather Condition'] == 'Fog']


# In[46]:


df[(df['Weather Condition'] == 'Clear') | (df['Visibility_km'] > 40)]


# In[47]:


df[(df['Weather Condition'] == 'Clear') & (df['Rel Hum_%'] > 50) | (df['Visibility_km']>40)]


# In[ ]:




