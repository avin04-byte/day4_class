#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.DataFrame({
    'Transaction_Amount': [100, 1500, 2500, 4000, 1500, 300],
    'Account_Balance': [3000, 6000, 7000, 8000, 2000, 500],
    'Transaction_Type': ['Deposit', 'Loan Payment', 'Withdrawal', 'Loan Payment', 'Deposit', 'Deposit'],
    'Branch': ['Uptown', 'Downtown', 'Uptown', 'Uptown', 'Downtown', 'Uptown']
})
filtered_by_transaction_amount = data[data['Transaction_Amount'] <= 2000]
loan_payment_above_5000 = data[(data['Transaction_Type'] == 'Loan Payment') & (data['Account_Balance'] > 5000)]
uptown_transactions = data[data['Branch'] == 'Uptown']
print("Filtered by Transaction Amount (<= 2000):")
print(filtered_by_transaction_amount)
print("\nLoan Payment with Account Balance > 5000:")
print(loan_payment_above_5000)
print("\nTransactions from the Uptown branch:")
print(uptown_transactions)


# In[3]:


import pandas as pd
data = pd.DataFrame({
    'Transaction_Amount': [100, 1500, 2500, 4000, 1500, 300],
    'Account_Balance': [3000, 6000, 7000, 8000, 2000, 500],
    'Transaction_Type': ['Deposit', 'Loan Payment', 'Withdrawal', 'Loan Payment', 'Deposit', 'Deposit'],
    'Branch': ['Uptown', 'Downtown', 'Uptown', 'Uptown', 'Downtown', 'Uptown']
})
data['Transaction_Fee'] = data['Transaction_Amount'] * 0.02
data['Balance_Status'] = data['Account_Balance'].apply(lambda x: 'High Balance' if x > 5000 else 'Low Balance')
print("Updated Data with New Columns:")
print(data)


# In[ ]:




