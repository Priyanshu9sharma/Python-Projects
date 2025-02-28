#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df= pd.read_csv(r"C:\Users\Downloads\Netflix_data.csv")


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.size


# In[7]:


df.columns


# In[8]:


df.dtypes


# In[9]:


df.info()


# In[10]:


df[df.duplicated()]


# In[11]:


df.drop_duplicates(inplace= True)


# In[12]:


df.shape


# In[13]:


df[df.duplicated()]


# In[14]:


df.isnull().sum()


# In[15]:


import seaborn as sns


# In[16]:


sns.heatmap(df.isnull())


# In[17]:


df.head()


# In[18]:


df[df['Title'].isin(['House of Cards'])]


# In[19]:


df[df['Title'].str.contains('House of Cards')]


# In[20]:


df.head(2)


# In[21]:


df.dtypes


# In[22]:


df['Release_Date']= pd.to_datetime(df.Release_Date)


# In[23]:


df.dtypes


# In[24]:


df['year'] = df.Release_Date.dt.year


# In[25]:


df.head(2)


# In[26]:


df.groupby('year')['Type'].count()


# In[27]:


df.year.value_counts()


# In[28]:


df.year.value_counts().plot(kind='bar')


# In[29]:


df.head()


# In[30]:


df.groupby('Category').Category.count()


# In[31]:


df['Category'] = df['Category'].astype('category')  # Ensure categorical type
sns.countplot(x=df['Category'])


# In[32]:


df.head()


# In[40]:


df[(df['Category'] == 'Movie') & (df['year'] == 2013)]


# In[44]:


len(df[(df['Category'] == 'TV Show') & (df['Country'] == 'India')]['Title'])


# In[48]:


df['Director'].value_counts().sort_values(ascending = False)


# In[61]:


df[(df['Category'] == 'Movie') & (df['Type'] == 'Comedies') | (df['Country'] =='United Kingdom')]


# In[53]:


df.head()


# In[60]:


df[df['Cast'] == 'Tom Cruise']


# In[67]:


df[df['Cast'].str.contains('Tom Cruise')]


# In[68]:


data_new = df.dropna()


# In[69]:


data_new.head(2)


# In[70]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# In[71]:


df.Rating.value_counts()


# In[72]:


df.Rating.nunique()


# In[73]:


df.Rating.unique()


# In[78]:


len(df[(df['Rating'] == 'TV-14') & (df['Country'] == 'Canada') & (df['Category'] == 'TV Show')])


# In[79]:


len(df[(df['Rating'] == 'R') &  (df['year'] > 2018) & (df['Category'] == 'Movie')])


# In[86]:


df['Duration'].unique()


# In[92]:


df[['Minutes','unit'] ]= df['Duration'].str.split(' ', expand= True)


# In[93]:


df.head()


# In[101]:


df[df['Category'] == 'TV Show'].Country.value_counts()


# In[102]:


df['year'].sort_values()


# In[103]:


df.sort_values(by= 'year')


# In[111]:


df[(df['Category'] == 'Movie') & (df['Type'] == 'Dramas') ]


# In[113]:


df[(df['Category'] == 'TV Show') & (df['Type']=="Kids' TV")]


# In[115]:


df[(df['Category'] == 'Movie') & (df['Type'] == 'Dramas') | (df['Category'] == 'TV Show') & (df['Type']=="Kids' TV")]


# In[ ]:




