#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

data = pd.read_csv('Civil_Engineering_Regression_Dataset.csv')


X = data[['Building_Height', 'Material_Quality_Index', 'Labor_Cost', 'Concrete_Strength', 'Foundation_Depth']]
y = data['Construction_Cost']


X_with_const = sm.add_constant(X)


model = sm.OLS(y, X_with_const).fit()


def backward_elimination(X, y, significance_level=0.05):
    X_with_const = sm.add_constant(X)
    model = sm.OLS(y, X_with_const).fit()
    while True:
        p_values = model.pvalues
        max_p_value = p_values.max()
        if max_p_value > significance_level:
            excluded_variable = p_values.idxmax()
            X = X.drop(columns=[excluded_variable])
            model = sm.OLS(y, sm.add_constant(X)).fit()
        else:
            break
    return model, X

final_model, remaining_variables = backward_elimination(X, y)


print(final_model.summary())
print("\nRemaining Variables:")
print(remaining_variables.columns)


# In[3]:


from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


lasso = Lasso(alpha=0.1) 
lasso.fit(X_scaled, y)

lasso_coefficients = lasso.coef_
remaining_variables_lasso = X.columns[lasso_coefficients != 0]

print("Remaining Variables after Lasso Regression:")
print(remaining_variables_lasso)


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns
residuals = final_model.resid
plt.figure(figsize=(10, 6))
sns.scatterplot(x=final_model.fittedvalues, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Fitted Values')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.show()


# In[6]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=data[['Building_Height', 'Material_Quality_Index', 'Labor_Cost', 'Concrete_Strength', 'Foundation_Depth', 'Construction_Cost']])
plt.title('Box Plot for Outlier Detection')
plt.show()


# In[8]:


from scipy import stats
z_scores = stats.zscore(data[['Building_Height', 'Material_Quality_Index', 'Labor_Cost', 'Concrete_Strength', 'Foundation_Depth', 'Construction_Cost']])
abs_z_scores = abs(z_scores)
outliers = (abs_z_scores > 3).any(axis=1)
outlier_data = data[outliers]
print("Outliers detected:")
print(outlier_data)


# In[ ]:




