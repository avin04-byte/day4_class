#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv('banking_data.csv')
print(df.head())
print(df.describe())
print(df.isnull().sum())


# In[4]:


import pandas as pd
data = pd.DataFrame({
    'Account_Type': ['Savings', 'Savings', 'Checking', 'Savings', 'Checking', 'Checking'],
    'Transaction_Amount': [100, 150, 200, 50, 300, 400],
    'Account_Balance': [1000, 1500, 2000, 500, 3000, 4000],
    'Branch': ['A', 'B', 'A', 'B', 'A', 'A']
})
grouped_by_account_type = data.groupby('Account_Type').agg(
    Total_Transaction_Amount=('Transaction_Amount', 'sum'),
    Average_Account_Balance=('Account_Balance', 'mean')
)
grouped_by_branch = data.groupby('Branch').agg(
    Total_Transactions=('Transaction_Amount', 'size'),
    Average_Transaction_Amount=('Transaction_Amount', 'mean')
)
print("Grouped by Account Type:")
print(grouped_by_account_type)
print("\nGrouped by Branch:")
print(grouped_by_branch)


# In[ ]:




