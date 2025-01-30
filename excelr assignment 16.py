#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load the Dataset
try:
    df = pd.read_csv('Healthcare_Data.csv')
except FileNotFoundError:
    print("The file 'Healthcare_Data.csv' was not found.")
    exit()

# Initial Data Inspection
print("Initial Data:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Data
if 'age' in df.columns:
    df['age'].fillna(df['age'].median(), inplace=True)
if 'gender' in df.columns:
    df['gender'].fillna(df['gender'].mode()[0], inplace=True)
if 'Blood_Pressure' in df.columns:
    df['Blood_Pressure'].fillna(df['Blood_Pressure'].mean(), inplace=True)

# Check for Missing Values After Imputation
print("\nMissing Values After Imputation:")
print(df.isnull().sum())

# Detect and Handle Duplicates
duplicates = df.duplicated()
print("\nNumber of Duplicates:", duplicates.sum())
df = df[~duplicates]

# Outlier Detection
plt.figure(figsize=(10, 5))
plt.boxplot(df['Blood_Pressure'])
plt.title('Boxplot of Blood Pressure')
plt.show()

# Capping Outliers
upper_limit = df['Blood_Pressure'].quantile(0.95)
df['Blood_Pressure'] = np.where(df['Blood_Pressure'] > upper_limit, upper_limit, df['Blood_Pressure'])

# Convert Categorical Variables
df = pd.get_dummies(df, columns=['gender'], drop_first=True)

# Scale Numerical Variables
scaler = MinMaxScaler()
numerical_cols = ['age', 'Blood_Pressure']
df[numerical_cols] = scaler.fit_transform(df)


# In[ ]:




