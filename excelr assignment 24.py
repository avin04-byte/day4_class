#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
data = pd.read_csv('Civil_Engineering_Regression_Dataset.csv')
X_simple = data[['Building_Height']]  
y = data['Construction_Cost'] 
r_squared_multiple = r2_score(y_test, y_pred_multiple)
print(f'R-squared for Simple Linear Regression: {r_squared_simple:.4f}')
print(f'R-squared for Multiple Linear Regression: {r_squared_multiple:.4f}')
if r_squared_multiple > r_squared_simple:
    print("The multiple linear regression model performs better.")
else:
    print("The simple linear regression model performs better.")


# In[21]:


X = data[['Building_Height', 'Material_Quality_Index', 'Labor_Cost', 'Concrete_Strength', 'Foundation_Depth']]
y = data['Construction_Cost']

n = X_test.shape[0]
p = X_test.shape[1]
adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)


print(f'R-squared: {r_squared:.4f}')
print(f'Adjusted R-squared: {adjusted_r_squared:.4f}')


# In[26]:


from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm

vif_data = pd.DataFrame()
vif_data['Variable'] = X_with_const.columns
vif_data['VIF'] = [variance_inflation_factor(X_with_const.values, i) for i in range(X_with_const.shape[1])]
print(vif_data)


# In[ ]:




