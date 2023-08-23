#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Create a python program to sort the given list of tuples based on integer value using a 
# lambda function. 
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

data = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_data = sorted(data,key=lambda x : x[1])

for player,runs in sorted_data:
    print(player,runs)


# In[3]:


# Q2.Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x*x,data)))


# In[4]:


#Q3.Write a python program to convert the given list of integers into a tuple of strings. Use map and 
#lambda functions.Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(map(lambda x: str(x),data)))


# In[13]:


#Q4.Write a python program using reduce function to compute the product of a list containing numbers 
#from 1 to 25.

from functools import reduce
data = list(range(1,26))
print(data)

Sum = reduce(lambda x,y:x*y,data)
print("the product is: ",Sum)


# In[16]:


#Q5.Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the 
#filter function. [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

data = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
print(list(filter(lambda x: x%2==0 and x%3==0,data)))


# In[17]:


#Q6.Write a python program to find palindromes in the given list of strings using lambda and filter 
#function.['python', 'php', 'aba', 'radar', 'level']

l6 = ['python', 'php', 'aba', 'radar', 'level']
print(list(filter(lambda x: x == x[::-1] , l6)))


# In[ ]:




