#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('banking_data.csv')
data.groupby('Account_Type')['Transaction_Amount'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Sum of Transaction Amount per Account Type')
plt.xlabel('Account Type')
plt.ylabel('Total Transaction Amount')
plt.show()
data['Branch'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Transactions per Branch')
plt.ylabel('')
plt.show()


# In[ ]:




