# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:12:49 2020

@author: raque
"""

#Write a Python program that given a positive integer num, provided by the user, prints the sum of all its divisors.
#
#A divisor of an integer number n is a number that divides n without the remainder.
#
#For example:
#
#for num=35 the output is 48 (1+5+7+35)
#for num=27 the output is 40 (1+3+9+27)
#for num=23 the output is 24 (1+23)


num = int(input())
dvr= sum([i for i in range(1,num+1) if num % i == 0])
print(dvr)

