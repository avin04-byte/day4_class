#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


data = {
    'Name': ['Ashok', 'Anil', 'Babu', 'Dhana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}


df = pd.DataFrame(data)
print("Employee DataFrame:")
print(df)


# In[4]:


import pandas as pd


data = {
    'Name': ['Ashok', 'Anil', 'Babu', 'Dhana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data)


print("First 2 rows of the DataFrame:")
print(df.head(2))


df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding Bonus column:")
print(df)


average_salary = df['Salary'].mean()
print(f"\nThe average salary of employees: {average_salary}")


filtered_df = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(filtered_df)


# In[ ]:




