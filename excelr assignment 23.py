#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv('Civil_Engineering_Regression_Dataset.csv')
print(data.head())
X = data[['Building_Height', 'Material_Quality_Index', 'Labor_Cost', 'Concrete_Strength', 'Foundation_Depth']]
y = data['Construction_Cost'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R-squared (R²): {r_squared:.2f}')
coefficients = model.coef_
intercept = model.intercept_
print(f'Intercept: {intercept:.2f}')
for i, col in enumerate(X.columns):
    print(f'Coefficient for {col}: {coefficients[i]:.2f}')


# In[7]:


coefficients = model.coef_
intercept = model.intercept_
equation = f'Construction Cost = {intercept:.2f}'
for i, col in enumerate(X.columns):
    equation += f' + ({coefficients[i]:.2f} * {col})'
    
print(equation)


# In[19]:


coeff_df = pd.DataFrame({'Variable': X.columns, 'Coefficient': coefficients})
coeff_df['Absolute Coefficient'] = coeff_df['Coefficient'].abs()
most_impactful_variable = coeff_df.loc[coeff_df['Absolute Coefficient'].idxmax()]
print("Coefficients:")
print(coeff_df)
print("\nMost Impactful Variable:")
print(most_impactful_variable)


# In[ ]:




