#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


df = pd.read_csv('Tours_and_Travels.csv')


print("Initial Data:")
print(df.head())


print("\nMissing Values:")
print(df.isnull().sum())


if 'Rating' in df.columns:
    df['Rating'].fillna(df['Rating'].median(), inplace=True) 
if 'Customer_Age' in df.columns:
    df['Customer_Age'].fillna(df['Customer_Age'].median(), inplace=True)  


if 'Review_Text' in df.columns:
    df['Review_Text'].fillna('No review provided', inplace=True)


print("\nMissing Values After Imputation:")
print(df.isnull().sum())


duplicates = df.duplicated()
print("\nNumber of Duplicates:", duplicates.sum())
df = df[~duplicates]


if 'Rating' in df.columns:
    df['Rating'] = df['Rating'].clip(lower=1, upper=5)  


if 'Tour_Package' in df.columns:
    df['Tour_Package'] = df['Tour_Package'].str.replace('Tropical Paradise', 'Tropical Paradise', case=False)
    df['Tour_Package'] = df['Tour_Package'].str.replace('Mountain Adventure', 'Mountain Adventure', case=False)


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.boxplot(df['Package_Price'])
plt.title('Boxplot of Package Price')

plt.subplot(1, 2, 2)
plt.boxplot(df['Rating'])
plt.title('Boxplot of Rating')

plt.show()


if 'Package_Price' in df.columns:
    upper_limit_price = df['Package_Price'].quantile(0.95)
    df['Package_Price'] = np.where(df['Package_Price'] > upper_limit_price, upper_limit_price, df['Package_Price'])


if 'Tour_Package' in df.columns:
    le = LabelEncoder()
    df['Tour_Package'] = le.fit_transform(df['Tour_Package'])


df.to_csv('Cleaned_Tour_and_Travels.csv', index=False)
print("\nCleaned dataset saved as 'Cleaned_Tour_and_Travels.csv'.")


# In[ ]:




