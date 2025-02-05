#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
data = pd.read_csv('Civil_Engineering_Regression_Dataset.csv')
X = data[['Building_Height']]
y = data['Construction_Cost']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('R-squared:', r2_score(y_test, y_pred))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Building Height')
plt.ylabel('Construction Cost')
plt.title('Building Height vs Construction Cost')
plt.legend()
plt.show()


# In[2]:


m = model.coef_[0] 
b = model.intercept_  
print(f'The equation of the regression line is: y = {m:.2f}x + {b:.2f}')


# In[3]:


mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R-squared (R²): {r_squared:.2f}')


# In[ ]:




