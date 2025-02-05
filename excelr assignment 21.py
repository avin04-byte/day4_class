#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('Civil_Engineering_Regression_Dataset.csv')
print(df.head())


# In[3]:


import pandas as pd
file_path = "Civil_Engineering_Regression_Dataset.csv"
data = pd.read_csv(file_path)
print(data.isnull().sum())


# In[6]:


import pandas as pd
file_path = "Civil_Engineering_Regression_Dataset.csv"
data = pd.read_csv(file_path)
summary_stats = data.describe().transpose()
summary_stats["median"] = data.median()
summary_stats = summary_stats.loc[:, ["mean", "median", "std"]]
print(summary_stats)


# In[9]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file_path = "Civil_Engineering_Regression_Dataset.csv"
data = pd.read_csv(file_path)
correlation_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
cost_correlations = correlation_matrix["Construction_Cost"].sort_values(ascending=False)
print("Correlations with Construction_Cost:")
print(cost_correlations)


# In[ ]:




