#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# read data
data = pd.read_csv("dataset.csv")
# print all data
# however, in vscode type data will not show anying,
# we should use "print(data)"
data


# In[15]:


# sort 
top10_income = data.sort_values(by = "Income", ascending = False)
# show top 10
top10_income.head(10)


# In[ ]:




