# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:33:03 2020

@author: raque
"""

#Use Spyder3 to write a program that replaces these letters with something a bit more human-readable 
#and calculate the final amount () at the end of the second year, for some varying amounts of money (), 
#payment frequency () at realistic interest rates ().
#
#Please round the result for 3 digits.
#
#For example:
#
#for P = 1000, n = 2, and r = 1% the result is 1020.151
#for P = 650, n = 1 and r = -0.05% the result is 643.516


P = float(input())
n= float(input())
r = float(input())
A = P*(1+(r / n)) **(n*2)
print(round(A,3))v





