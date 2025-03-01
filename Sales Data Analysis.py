#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_csv(r"C:\Users\Downloads\Sales_Data.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.head(1)


# In[7]:


df.drop(columns='Date')


# In[8]:


df['Manager']


# In[9]:


df.Manager.unique()


# In[10]:


df['Manager']=df['Manager'].str.strip().str.replace(r'\s+',' ',regex=True)


# In[11]:


df.head()


# In[12]:


df.Manager.unique()


# In[13]:


df.Manager.nunique()


# In[14]:


df[df.duplicated()]


# In[15]:


df.describe()


# In[16]:


df


# In[ ]:





# In[18]:


df[df['Order ID'].duplicated()]


# In[19]:


df.dtypes


# In[21]:


df['Date'] = pd.to_datetime(df.Date)


# In[22]:


df.dtypes


# In[24]:


df.Quantity = df.Quantity.astype(float)


# In[25]:


df.info()


# In[26]:


df.Price = df.Price.astype(int)


# In[27]:


df.info()


# In[28]:


df.head()


# In[29]:


df['Payment Method'].value_counts()


# In[33]:


round(df['Payment Method'].value_counts(normalize= True)*100,2)


# In[38]:


df['Payment Method'].value_counts().plot(kind='bar');


# In[39]:


df.head(2)


# In[46]:


round(df.groupby('Product')['Quantity'].sum(),0)


# In[49]:


round(df.groupby('Product')['Quantity'].sum(),0).sort_values().plot(kind='bar')


# In[51]:


a=df.groupby('Product')['Price'].sum().sort_values()
a


# In[54]:


type(a)


# In[59]:


b=a.reset_index()
b


# In[60]:


type(b)


# In[82]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.bar(b['Product'],b['Price'],color=['Red','Green','Blue','Yellow','Pink'],width=0.6);
plt.title('Sale on each procducts')
plt.xlabel("Product")
plt.ylabel("Price");


# In[83]:


df['Revenue'] = df['Price']*df['Quantity']


# In[86]:


df.head(),df.shape


# In[89]:


df.groupby('Product')['Revenue'].sum().sort_values().plot(kind='bar');


# In[94]:


sd=df.groupby('City').Revenue.sum().sort_values()
sd


# In[95]:


sd.reset_index()


# In[99]:


sd.plot(kind='bar',color=('Red','Green'));


# In[103]:


df.groupby('Manager').Revenue.sum().sort_values()


# In[105]:


df.groupby('Date').Revenue.sum().sort_values()


# In[107]:


df.plot('Date','Revenue',color='Red')


# In[108]:


df['Revenue'].mean()


# In[111]:


df['year'] = df['Date'].dt.year


# In[112]:


df['Month'] = df['Date'].dt.month


# In[113]:


df.head()


# In[117]:


df[df['Month'].isin([11,12])].Revenue.mean()


# In[118]:


df['Revenue'].std()


# In[119]:


df['Quantity'].std()


# In[120]:


df['Revenue'].var()


# In[121]:


df['Quantity'].var()


# In[122]:


df.describe()


# In[125]:


df.groupby('Month').Revenue.sum().plot(kind='bar')


# In[127]:


df.groupby('Product').Revenue.mean().plot(kind='bar')


# In[126]:


df.head()


# In[128]:


df.groupby('Product').Revenue.mean()


# In[129]:


df.groupby('Product').Quantity.mean()


# In[ ]:




