#!/usr/bin/env python
# coding: utf-8

# In[40]:


def gcd(m: int,n: int)->int:
    """ function of finding a greatest common divisor """
    if m <= 0 or n <= 0:
        print("-------------------------------------")
        print("Please enter a number greater than 0.")
        print("-------------------------------------")
        a = int(input("Enter first positive integer (m):"))
        b = int(input("Enter second positive integer (n):"))
        gcd(a, b)
    else:
        if m >= n:
            quotient = m // n
            remainder = m % n
            if remainder == 0:
                print("Greatest common divisor:", n)
            else:
                gcd(n, remainder)     
        else:
            gcd(n, m)


# In[41]:


gcd(1304, 560)


# In[42]:


gcd(0, 5)


# In[43]:


get_ipython().run_line_magic('pinfo', 'gcd')


# In[ ]:




