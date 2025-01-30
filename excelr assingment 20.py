#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer


df = pd.read_csv('E-Commerce_Data.csv')


print("Initial Data:")
print(df.head())


print("\nMissing Values:")
print(df.isnull().sum())


if 'Customer_Age' in df.columns:
    age_imputer = SimpleImputer(strategy='median')
    df['Customer_Age'] = age_imputer.fit_transform(df[['Customer_Age']])


if 'Rating' in df.columns:
    rating_imputer = SimpleImputer(strategy='median')
    df['Rating'] = rating_imputer.fit_transform(df[['Rating']])


if 'Review_Text' in df.columns:
    df['Review_Text'].fillna('No review provided', inplace=True)


print("\nMissing Values After Imputation:")
print(df.isnull().sum())


duplicates = df.duplicated()
print("\nNumber of Duplicates:", duplicates.sum())
df = df[~duplicates]


if 'Rating' in df.columns:
    df['Rating'] = df['Rating'].clip(lower=1, upper=5) 


if 'Product_Category' in df.columns:
    df['Product_Category'] = df['Product_Category'].str.replace('Electronics', 'Electronics', case=False)
    df['Product_Category'] = df['Product_Category'].str.replace('Clothing', 'Clothing', case=False)


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x=df['Product_Price'])
plt.title('Boxplot of Product Price')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Rating'])
plt.title('Boxplot of Rating')

plt.show()


if 'Product_Price' in df.columns:
    upper_limit_price = df['Product_Price'].quantile(0.95)
    df['Product_Price'] = np.where(df['Product_Price'] > upper_limit_price, upper_limit_price, df['Product_Price'])


if 'Product_Category' in df.columns:
    le = LabelEncoder()
    df['Product_Category'] = le.fit_transform(df['Product_Category'])


df.to_csv('Cleaned_E-Commerce_Data.csv', index=False)
print("\nCleaned dataset saved as 'Cleaned_E-Commerce_Data.csv'.")


# In[ ]:




