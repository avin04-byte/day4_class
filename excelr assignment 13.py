#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Pharma_data.csv')
print(data.head())
print(data.isnull().sum())
print(data.duplicated().sum())
data = data.drop_duplicates()


# In[5]:


plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=data, estimator=sum)
plt.title('Total Sales per Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[6]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Spend', y='Sales', data=data)
plt.title('Relationship Between Marketing Spend and Sales')
plt.xlabel('Marketing Spend')
plt.ylabel('Sales')
plt.show()


# In[7]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Age_Group', y='Effectiveness', data=data)
plt.title('Drug Effectiveness Across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Effectiveness')
plt.xticks(rotation=45)
plt.show()


# In[12]:


plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Trial_Period', y='Sales', hue='Product_Name', marker='o')
plt.title('Sales Trend for Each Product Over Different Trial Periods')
plt.xlabel('Trial Period')
plt.ylabel('Sales')
plt.legend(title='Product')
plt.show()


# In[11]:


correlation_matrix = data[['Sales', 'Marketing_Spend', 'Effectiveness']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# In[ ]:




