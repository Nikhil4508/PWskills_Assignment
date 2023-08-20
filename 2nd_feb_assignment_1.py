#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1.Explain with an example each when to use a for loop and a while loop.
# A "For" Loop is used to repeat a specific block of code a known number of times.
# For example, if we want to check the grade of every student in the class, we loop from 1 to that number.
# When the number of times is not known before hand, we use a "While" loop.


# In[10]:


# Q2.Write a python program to print the sum and product of the first 10 natural numbers using for 
# and while loop.

sum_of_numbers = 0
product_of_numbers = 1

for num in range(1, 11):
    sum_of_numbers += num
    product_of_numbers *= num

print("Using for loop:")
print("the sum of natural number is:", sum_of_numbers)
print("the product of natural number is:", product_of_numbers)
    


# In[11]:


# Q2.Write a python program to print the sum and product of the first 10 natural numbers using for 
# and while loop.

sum_of_numbers = 0
product_of_numbers = 1
num = 1

while num <= 10:
    sum_of_numbers += num
    product_of_numbers *= num
    num += 1

print("Using while loop:")
print("the sum of natural number is:", sum_of_numbers)
print("the product of natural number is:", product_of_numbers)


# In[13]:


# Q3.Create a python program to compute the electricity bill for a household.
# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per 
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will 
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.

def electricity_bill(units):
    total_bill = 0
    if units <=100:
        total_bill = units * 4.5
    elif units <=200:
        total_bill = 100 * 4.5 + (units - 100 ) * 6
    elif units <=300:
        total_bill = 100 * 4.5 + 100 * 6 + (units - 200) * 10
    else:
        total_bill = 100 * 4.5 + 100 * 6 +  100 * 10 + (units - 300) * 20
    
    return total_bill

units_consumed = float(input("Enter the number of units consumed: "))
Electricity_bill =  electricity_bill(units_consumed)
print("Electricity_bill", Electricity_bill,"rupees")
    
    


# In[15]:


# Q4.Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each 
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print 
# that list.

numbers = list(range(1,101))
result_list = []

for num in numbers:
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        result_list.append(num)

print("using for loop : ",result_list)
    


# In[16]:


# Q4.Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each 
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print 
# that list.

numbers = list(range(1, 101))
result_list = []
index = 0

while index < len(numbers):
    num = numbers[index]
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        result_list.append(num)
    index += 1

print("Using while loop:", result_list)


# In[17]:


# Q5.Write a program to filter count vowels in the below-given string. string = "I want to become a data scientist".

string = "I want to become a data scientist"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)


# In[ ]:




