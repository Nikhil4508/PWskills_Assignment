#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1.Which keyword is used to create a function? Create a function to return a list of odd numbers in the 
# range of 1 to 25.

# Answer => def keyword is used to create a function

def get_odd_list():
    odd_number = []
    for num in range(1,26):
        if num%2 != 0:
            odd_number.append(num)
            
    return odd_number

result = get_odd_list()
print(result)
    
    


# In[2]:


# Q2.Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs 
# to demonstrate their use.


def print_args(*args):
    for arg in args:
        print(arg)

        
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Using *args:")
print_args(1, 2, 3, "hello", [4, 5])
print("\n")

print("Using **kwargs:")
print_kwargs(name="nikhil", age=23, city="pune")


# In[4]:


# Q3.What is an iterator in python? Name the method used to initialise the iterator object and the method 
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

my_list = [2,4,6,8,10,12,14,16,18,20]
my_iterator = iter(my_list)

print("First five elements are: ")

for _ in range(5):
    elements = next(my_iterator)
    print(elements)


# In[5]:


# Q4.What is a generator function in python? Why yield keyword is used? Give an example of a generator function.

# Answer => A generator function in Python is a special type of function that returns an iterator, which can be used to 
# generate a sequence of values on-the-fly.

# Answer => The yield keyword is used in a generator function to indicate where the function should pause and yield the 
# current value to the caller. 

def countdown(n):
    while n > 0:
        yield n
        n -= 1
        
        
countdown_iterator = countdown(5)
for value in countdown_iterator:
    print(value)


# In[6]:


# Q5.Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_generator(limit):
    num = 2
    while num < limit:
        if is_prime(num):
            yield num
        num += 1


prime_gen = primes_generator(1000)
for _ in range(20):
    print(next(prime_gen))


# In[7]:


# Q6.Write a python program to print the first 10 Fibonacci numbers using a while loop.

def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

first_10_fibonacci = fibonacci_sequence(10)
for num in first_10_fibonacci:
    print(num)


# In[8]:


# Q7.Write a List Comprehension to iterate through the given string: ‘pwskills’.
# Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's'] 

input_string = 'pwskills'
output_list = [char for char in input_string if char in 'pwskills']
print(output_list)


# In[9]:


# Q8.Write a python program to check whether a given number is Palindrome or not using a while loop

def is_palindrome(number):
    original_number = number
    reversed_number = 0
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    
    return original_number == reversed_number


num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


# In[10]:


# Q9.Write a code to print odd numbers from 1 to 100 using list comprehension.

odd_numbers = [num for num in range(1, 101) if num % 2 != 0]

print(odd_numbers)


# In[ ]:




