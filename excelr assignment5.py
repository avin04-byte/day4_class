#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a valid positive integer.")
else:
    
    print("Numbers from 1 to", n, ":")
    for i in range(1, n + 1):
        print(i)

   
    total_sum = 0
    count = 1

    while count <= n:
        total_sum += count
        count += 1

    print(f"The sum of all numbers from 1 to {n} is: {total_sum}")


# In[2]:


def calculate_square(n):
    return n ** 2  

try:
    num = int(input("Enter a positive integer: "))
    
    if num < 1:
        print("Please enter a valid positive integer.")
    else:
        
        result = calculate_square(num)
        print(f"The square of {num} is: {result}")

except ValueError:
    print("Invalid input! Please enter a positive integer.")


# In[ ]:




