#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = 6
if num %2 == 0:
    print("even")
else:
    print("odd")


# In[2]:


num = 8
print("even") if num %2 == 0 else print("odd")


# In[3]:


x = 10
result = "Positive" if x > 0 else "Negative"
print(result)


# In[4]:


num = int(input("Enter a number"))
result = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
print(result)


# In[7]:


#List Comprehension
L = [1,3,4,2,5,7,6,508]
[2*x for x in L]


# #
# 

# In[8]:


#Print even numbers
[x for x in L if x%2 == 0]


# In[15]:


#Print updated salaries
#Condition is give 20%  hike for
#slalries <= 50000
sal = [40000,60000,80000,45000]
increment = x*20/100
for x in sal:
    if x < 50000:
        print(x+increment)


# In[19]:


[(x*1.2 if x <= 50000 else x) for x in sal]


# In[20]:


#Dictionary comprehension
d1 = {'Ram':[34,54,23,99], 'John':[56,67,87,87]}
d1


# In[22]:


{k:sum(v)/len(v) for k,v in d1.items()}


# In[30]:


given_list = [4,5,3,4,3,3,5,57,897]
def mean_value(given_list):
    total = sum(given_list)
    average_value = total/len(given_list)
    return average_value
print(given_list)


# In[31]:


def Greet(name):
    print(f"MG {name}!")


# In[32]:


Greet("Nava")


# In[42]:


#Define argument fuction
def greet(name = "Santhosh"):
    print(f"Good Evening {name}!")
greet()


# In[40]:


#Function with Variable number of arguments
def avg_value(*n):
    l = len(n)
    average = sum(n)/1
    return average


# In[41]:


avg_value(1,3,4,5,7,8,90,45)


# In[ ]:




