# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:06:55 2020

@author: raque
"""

#You are budgeting for a car trip and need to know how much you will spend on fuel. 
#Write a Python program that receives three inputs: the distance to travel (integer), 
#the number of litres of fuel needed to travel 100 km (float), 
#and the price per litre of fuel (float),
# then prints the total cost of fuel for the trip. 
# Use round with 2 decimal places.
#
#Hint: to read a float input, use float(input()).

dist = int(input())
ltrs = float(input()) #ltr of fuel to travel 100km
price = float(input()) # price per ltr
cost = ((ltrs * dist) / 100) * price
print(round(cost,2))








