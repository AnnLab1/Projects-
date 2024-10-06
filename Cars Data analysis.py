#!/usr/bin/env python
# coding: utf-8

# In[107]:


import pandas as pd


# In[108]:


df = pd.read_csv("file.csv")


# In[109]:


df.head()


# In[110]:


df.shape


# In[111]:


### Find all null values and remove them


# In[112]:


df.isnull().sum()


# In[113]:


df.dropna(inplace=True)


# In[114]:


df.isnull().sum()


# In[115]:


###  What is the count of each Make


# In[116]:


df.head(1)


# In[117]:


df["Make"].value_counts()


# In[118]:


###  Show records where orgin is in Asia or Europe


# In[119]:


df.head(1)


# In[120]:


df[df["Origin"].isin(["Asia" , "Europe"])]


# In[121]:


###  Remove records where weight is above 4000


# In[122]:


df.head(1)


# In[123]:


df


# In[124]:


df = df[df["Weight"] > 4000]



# In[127]:


df.shape


# In[ ]:





# In[ ]:





# In[ ]:




