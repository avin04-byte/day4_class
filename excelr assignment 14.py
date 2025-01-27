#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Pharma_data.csv')
print(data.head())
print(data.isnull().sum())
print(data.duplicated().sum())
data = data.drop_duplicates()


# In[5]:


plt.figure(figsize=(12, 6))
sns.barplot(y='Effectiveness', hue='Region', data=data, estimator='mean')
plt.title('Average Effectiveness for Each Drug Across Different Regions')
plt.ylabel('Average Effectiveness')
plt.xticks(rotation=45)
plt.legend(title='Region')
plt.show()


# In[8]:


plt.figure(figsize=(12, 6))
sns.violinplot(x='Product_Name', y='Effectiveness', data=data, inner='quartile')
plt.title('Distribution of Effectiveness for Each Product')
plt.xlabel('Product')
plt.ylabel('Effectiveness')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(x='Product_Name', y='Side_Effects', data=data, inner='quartile')
plt.title('Distribution of Side Effects for Each Product')
plt.xlabel('Product')
plt.ylabel('Side Effects')
plt.xticks(rotation=45)
plt.show()


# In[9]:


sns.pairplot(data[['Effectiveness', 'Side_Effects', 'Marketing_Spend']])
plt.suptitle('Pairplot of Effectiveness, Side Effects, and Marketing Spend', y=1.02)
plt.show()


# In[10]:


plt.figure(figsize=(10, 6))
sns.regplot(x='Marketing_Spend', y='Effectiveness', data=data)
plt.title('Effect of Marketing Spend on Drug Effectiveness')
plt.xlabel('Marketing Spend')
plt.ylabel('Effectiveness')
plt.show()


# In[ ]:




