#!/usr/bin/env python
# coding: utf-8

# In[26]:


print('{:2}  {:3}  {:7}'.format('lb', 'oz', 'kg'))
for lb_value in range(1, 11):
    oz_value = lb_value * 16
    kg_value = lb_value * 0.45359
    print('{:>2d}, {:>3d}, {:.5f}'.format(lb_value, oz_value, kg_value))

