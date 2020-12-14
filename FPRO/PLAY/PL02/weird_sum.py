# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:06:55 2020

@author: raque
"""

#Write a Python script that, given two integers a and b, prints the value of their sum.
#
#However, if the difference of a and b is an even number, the value of the sum is doubled.
#On the other hand, if the difference is an odd number,
# the value of the product of a and b gets added to the value of the sum.
#Do not use conditionals (e.g., if or while).

a = int(input())
b = int(input())
par = ((abs(a - b)) % 2 == 0)
impar = ((abs(a - b)) % 2 == 1)
weird_sum = (a + b) + par * (a + b) + impar * (a * b)
print(weird_sum)



