#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv('banking_data.csv')
sorted_data = data.sort_values(by='Account_Balance', ascending=False).head(10)
data['Transaction_Rank'] = data.groupby('Branch')['Transaction_Amount'].rank(ascending=False)
print("Sorted Data by Account Balance (Descending):")
print(sorted_data)
print("\nData with Transaction Ranks within Each Branch:")
print(data)


# In[ ]:




