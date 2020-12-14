# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:06:55 2020

@author: raque
"""

#You're helping a teller decide how to give change. 
#Write a Python script that given the price of the sale and the amount received by user input, 
#then prints a string indicating how many notes of each amount they have to give as change. 
#Consider that the largest note available is the 50€ note and that all prices and amounts received are multiples of 5 
#(no coins!).
#
#The result should be a string with the number of notes of each amount, separated by a space: "#50 #20 #10 #5".
#
#Hint: To help format the result, use type conversions to string.


price = int(input())
received = int(input())
chg = received - price 

n50 = chg // 50 
n20 = (chg -n50 *50) // 20
n10 = (chg- n50 *50 -n20 *20)// 10
n5 = (chg -n50 *50 - n20 *20 - n10 *10)// 5
print(n50,n20,n10,n5)