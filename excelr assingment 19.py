#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer


df = pd.read_csv('E-commerce_Data.csv')


print("Initial Data:")
print(df.head())


print("\nMissing Data Information:")
print(df.isna().sum())
print("\nData Info:")
print(df.info())


missing_percentage = df.isna().mean() * 100
print("\nPercentage of Missing Values:")
print(missing_percentage[missing_percentage > 0])


plt.figure(figsize=(12, 6))
sns.heatmap(df.isna(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()


if 'Product_Price' in df.columns:
    df['Product_Price'].fillna(df['Product_Price'].median(), inplace=True)


if 'Product_Category' in df.columns:
    df['Product_Category'].fillna(df['Product_Category'].mode()[0], inplace=True)


if 'Order_Date' in df.columns:
    df['Order_Date'].fillna(method='ffill', inplace=True)  


numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
knn_imputer = KNNImputer(n_neighbors=5)
df[numerical_cols] = knn_imputer.fit_transform(df[numerical_cols])


print("\nSummary Statistics Before Imputation:")
print(df.describe())


plt.figure(figsize=(12, 6))
df['Product_Price'].hist(bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram of Product Price After Imputation')
plt.xlabel('Product Price')
plt.ylabel('Frequency')
plt.show()


report = {
    "Missing Values Before Imputation": missing_percentage[missing_percentage > 0].to_dict(),
    "Imputation Methods": {
        "Product_Price": "Median Imputation",
        "Product_Category": "Mode Imputation",
        "Order_Date": "Forward Fill",
        "Numerical Columns": "KNN Imputation"
    },
    "Summary Statistics After Imputation": df.describe().to_dict()
}


df.to_csv('Cleaned_E-commerce_Data.csv', index=False)
print("\nCleaned dataset saved as 'Cleaned_E-commerce_Data.csv'.")


print("\nReport:")
for key, value in report.items():
    print(f"{key}: {value}")


# In[ ]:




