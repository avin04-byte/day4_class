#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_of_evens(n):
    even_sum = 0
    for i in range(2, n + 1, 2):  
        even_sum += i
    return even_sum

n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    result = sum_of_evens(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")


# In[ ]:




