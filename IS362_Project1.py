#!/usr/bin/env python
# coding: utf-8

# # IS 362 Project 1

# In[ ]:


import pandas as pd
import sys


# In[3]:


import csv
with open("IS362_Project1.csv") as csv_file:
    csvReader = csv.reader(csv_file)
    for row in csvReader:
        print(row)


# In[4]:


import pandas as pd
from pandas import DataFrame
df = pd.read_csv("IS362_Project1.csv")


#  <b>Desplaying Data</b>

# In[6]:


pd.read_csv("IS362_Project1.csv")


#  <b>Comparison of delayed ailines</b>

# In[8]:


print(df[['Alaska_delayed', 'AMWest_delayed']])


# *AMWest has more delayed flights than Alaska.

# In[ ]:




