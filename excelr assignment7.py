#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
file_path = "sales_data.csv"  
df = pd.read_csv(file_path)
print("First 5 rows of the dataset:")
print(df.head())
print("\nBasic statistics of numerical columns:")
print(df.describe())


# In[4]:


import pandas as pd
file_path = "sales_data.csv"  
df = pd.read_csv(file_path)
total_sales_by_region = df.groupby('Region')['Sales'].sum()
print("Total sales for each region:")
print(total_sales_by_region)
most_sold_product = df.groupby('Product')['Quantity'].sum().idxmax()
print("\nMost sold product (based on quantity):", most_sold_product)
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100
average_profit_margin = df.groupby('Product')['Profit Margin (%)'].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin)


# In[ ]:




