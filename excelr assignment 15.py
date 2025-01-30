#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset
df = pd.read_csv('Healthcare_data.csv')

# Display the first few rows of the dataset
df.head()


# In[2]:


# Get a summary of the dataset
df.info()

# Check for missing values
missing_values = df.isna().sum()
missing_percentage = (missing_values / len(df)) * 100

# Create a DataFrame to summarize missing values
missing_summary = pd.DataFrame({'Missing Values': missing_values, 'Percentage': missing_percentage})
print(missing_summary)


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt

# Visualize missing data using a heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df.isna(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()


# In[7]:


# Impute numerical columns with mean or median
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    if df[col].isna().sum() > 0:
        df[col].fillna(df[col].mean(), inplace=True)  # or use median


# In[5]:


# Impute categorical columns with mode
for col in df.select_dtypes(include=['object']).columns:
    if df[col].isna().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)


# In[6]:


from sklearn.impute import KNNImputer

# KNN Imputation
knn_imputer = KNNImputer(n_neighbors=5)
df_knn_imputed = pd.DataFrame(knn_imputer.fit_transform(df.select_dtypes(include=['float64', 'int64'])), columns=df.select_dtypes(include=['float64', 'int64']).columns)


# In[ ]:




