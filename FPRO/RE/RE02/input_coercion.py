# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:31:00 2020

@author: raque
"""

#Use Spyder3 to write a program that asks the user to input a number n (0-9),
# calculates the expression n + nn + nnn and prints its value.
#
#For example: for a user input 5, the output must be 5 + 55 + 555 = 615.

n = int(input())
nn = n*10 + n
nnn = nn * 10 +n
print( n + nn + nnn)


