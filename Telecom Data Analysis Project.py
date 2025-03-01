#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_csv(r"C:\Users\Downloads\Telecom Dataset.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[6]:


df.info()


# In[7]:


df.columns


# In[9]:


df.nunique()


# In[11]:


df.dtypes


# In[12]:


df.describe()


# In[14]:


df.describe(include='object')


# In[15]:


df.head(1)


# In[17]:


df.isnull().sum()


# In[19]:


df.duplicated()


# In[20]:


df.isna().sum()


# In[21]:


df.notnull().sum()


# In[22]:


df.notna().sum()


# In[23]:


df[df.duplicated()]


# In[24]:


a= df.drop_duplicates()


# In[25]:


a


# In[27]:


a.shape


# In[28]:


df.head()


# In[29]:


df['churn'].unique()


# In[36]:


sd=df.churn.value_counts(normalize=True)*100 


# In[39]:


type(sd)


# In[40]:


sd.reset_index()


# In[41]:


import matplotlib.pyplot as plt


# In[69]:


plt.pie(sd,labels=['Not Churned','churned'], colors=['red','pink'],startangle=80,shadow=False, radius=1.4,explode=(0,0.2),
       autopct = '%1.1f%%',pctdistance=0.5);


# In[70]:


import seaborn as sns


# In[72]:


sns.countplot(df['churn'])


# In[73]:


df.nunique()


# In[74]:


df.state.nunique()


# In[75]:


df.state.unique()


# In[77]:


df.state.value_counts(normalize=True)


# In[89]:


df['state'] = df['state'].astype(str)  # Convert to string to ensure categorical data

plt.figure(figsize=(10,5))
sns.countplot(x=df['state'])
plt.xticks(rotation=90)  # Rotate x-axis labels if needed
plt.show()


# In[85]:


df.state.astype('str')


# In[86]:


df.dtypes


# In[ ]:





# In[ ]:





# In[ ]:




