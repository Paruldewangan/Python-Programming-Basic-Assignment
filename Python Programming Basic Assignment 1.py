#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to print "Hello Python"?
print("Hello Python")


# In[12]:


#Write a Python program to do arithmetical operations addition and division?
p=int(input("enter the first number"))
q=int(input("enter the second number"))
a=p+q
d=p/q
print("addition of number:" ,a)
print("division of number:" ,d)


# In[13]:


#Write a Python program to find the area of triangle?
a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5

print("The area of triange is",area)


# In[16]:


#Wirte a Python program to swap two vraiables?
x=int(input("enter the value of x :"))
y=int(input("enter the value of y :"))

x,y=y,x

print("x is",x)
print("y is",y)


# In[29]:


#Write a Python program to generate a random number?
import random
print(random.randint(0,100))

