# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:12:03 2020

@author: raque
"""

#Define a function sum_multiples(n) 
#that returns the sum of all the natural numbers that are a multiple of 3 or 5 up until n (inclusive)

def sum_multiples(n):
    return sum([(x ) for x in range(1,n+1) if x % 5 == 0 or x % 3 == 0])


