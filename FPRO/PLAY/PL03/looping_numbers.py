# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:24:43 2020

@author: raque
"""

#A number is called a Looping Number if all adjacent digits in it differ by 1. 
#The difference between 9 and 0 is considered as 1. All single digit numbers are considered looping numbers.
#
#Write a Python program that receives an integer n,
# provided by the user, and checks whether the number is a looping number or not.
# If the number is a looping number, 
# print the message Looping number, otherwise print the message Not a looping number.
#
#You can assume that all inputs are non-negative numbers.


n= int(input())
l= [int(char) for char in str(n)]
loop = []

for i in range(1,len(l)):
    if abs(l[i-1] - l [i] ) == 1:
        loop.append("Looping number")
    elif (l[i-1] - l[i]) == 9:
        loop.append("Looping number")
    else:
        loop.append("Not a looping number")

if "Not a looping number" in loop:
    print("Not a looping number")
else:
    print("Looping number")


