# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:06:53 2020

@author: raque
"""

#Write a script that given an hour and minutes by user input, 
#prints at what time the alarm clock will ring,
# knowing that the current hour is hour and the current minutes are minutes. 
#The clock goes off after 6 hour and 51 minutes.

hour = int(input())
minutes = int(input())
tl_mn = hour * 60 + minutes + 6 * 60 + 51
tl_hrs = tl_mn // 60
tl_sub = tl_mn - tl_hrs * 60 
if tl_hrs > 24:
    tl_hrs = tl_hrs - 24
tl_hrs = ("0" if tl_hrs < 10 else "") + str(tl_hrs)        
tl_sub = ("0" if tl_sub < 10 else "") + str(tl_sub)    
print(  tl_hrs + ":" + tl_su