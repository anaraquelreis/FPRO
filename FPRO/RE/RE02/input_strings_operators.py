# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:30:59 2020

@author: raque
"""

#Use Spyder3 to write a program that asks the user to input a string tag and a string text 
#and prints an HTML valid element of the form <tag>text</tag>.
#
#For example: for a user input tag="h1" and a text="I’m an HTML text",
# the output must be "<h1>I'm an HTML text</h1>".


tag = input()
text = input()
print('<'+ tag+'>'+text +'</' +tag+'> ' )