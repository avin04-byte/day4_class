#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
file_path = "sales_data.csv"  
df = pd.read_csv(file_path)
high_sales_df = df[df['Sales'] > 1000]
print("Rows where sales are greater than 1000:")
print(high_sales_df)
specific_region = "East" 
east_region_sales = df[df['Region'] == specific_region]
print(f"\nSales records for the '{specific_region}' region:")
print(east_region_sales)


# In[7]:


import pandas as pd
data = {
    'Profit': [500, 1200, 800, 2000],
    'Quantity': [10, 50, 20, 100],
    'Sales': [800, 1500, 600, 1200]
}
df = pd.DataFrame(data)
df['Profit_Per_Unit'] = df['Profit'] / df['Quantity']
df['High_Sales'] = df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')
print(df)


# In[ ]:




