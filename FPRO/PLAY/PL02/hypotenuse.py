# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:01:32 2020

@author: raque
"""

##     Write a Python script that given the length n,
#      by user input, which corresponds to two sides of a right-angled triangle, 
#     prints the length of the hypotenuse. Please use round with two decimal places.

import math
n = int(input())
print(round(math.sqrt(2*(n**2)),2))