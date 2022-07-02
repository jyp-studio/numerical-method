#!/usr/bin/env python
# coding: utf-8

# In[20]:


import math

def cos(x:float)->float:
    """Compute the approximation of cos(x)"""
    N = 0
    total = 1.0
    while N < 12:
        N += 1
        N_fac = math.factorial(2 * N)
        total += ((-1) ** N) * (x ** (2 * N)) / (N_fac)

    print(f"cos({x}) approximation is {total}")


# In[22]:


cos(2.3)


# In[ ]:




