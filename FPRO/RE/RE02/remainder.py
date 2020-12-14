# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:33:03 2020

@author: raque
"""

#Use Spyder3 to write a program that determines what is the actual time 
#(using now of class datetime from module datetime).
#
#Given that an alarm is set up for 8 hours and 30 minutes later,
# the program prints the time on display at the time of the alarm, using the format "hh:mm" (hours and minutes).
#
#Hint: You my find useful the following piece of code:
#
#import datetime
#now = datetime.datetime.now()
#h = now.hour
#m = now.minute

import datetime

now = datetime.datetime.now()

alrm = 8*60
mn_nw=int( now.strftime("%M"))

hrs_cnv = int((now.strftime("%H")))* 60 
mn_ttl = hrs_cnv + alrm + mn_nw + 30 # conversao em min do tempo no instante
#mn_fl = mn_nw + 30

fl_hr= ( mn_ttl // 60)
mn_f = mn_ttl - fl_hr *60
    
print(str(fl_hr) + ":" + str(mn_f))



