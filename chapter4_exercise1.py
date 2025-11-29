# Chapter 4 - Try This: Manipulating Strings and Numbers

""" Description
In this exercise, we experiment with Python variables including strings, integers, floats, and complex numbers. 
We explore operations between them and also use the `math` and `cmath` modules."""

## Step 1: Variables
# Create variables of different types
s = "Zahra"
i = 3
f = 2.5
c = 1 + 2j


## Step 2: Operations

# String * int
print(s * i)  # hellohellohello

# String * float or complex
try:
    print(s * f)
except Exception as e:
    print(e)

try:
    print(s * c)
except Exception as e:
    print(e)

# String + int
try:
    print(s + i)
except Exception as e:
    print(e)

# Numeric operations
print(i + f)  
print(i * f)  
print(f * c)  
print(c + i)  
print(c * c)  

import math


x = 9
y = -9
z = 2.5

# math module
print(math.sqrt(x))
print(math.sqrt(z))
 
import cmath

# cmath module
print(cmath.sqrt(x))
print(cmath.sqrt(y))
print(cmath.sqrt(z))

# math vs cmath
print(cmath.sin(0.5))
print(math.sin(0.5))
