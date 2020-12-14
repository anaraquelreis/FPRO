# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:06:55 2020

@author: raque
"""

#Two people go to a forest to explore the region.
#
#In order to cover more area, they decide to take two different directions and will communicate via Walkie Talkies.
#
#The Walkie Talkies they brought can operate up to 35 km. Once that limit is surpassed the connection is broken.
#
#Given the direction of each explorer, define a function: time_until_lost_connection(direction_A, direction_B) to find the time in minutes that takes the connection between the explorers to be broken. Both explorers walk at 5 km/h in a straight line.
#
#The directions are given in degrees, ranging from 0 to 359, counting counter-clockwise. Assume that at the start, both explorers are at the same place. Round your result to 3 decimal places using the function round.
#
#import math
#def time_until_lost_connection(direction_A, direction_B):
#    # my code here
#    return # FIXME
#The function abs(x) can be used to get the absolute value of a number. All trigonometric functions and constants can be obtained in the math module. For example:
#
#cos_x = math.cos(x)  # x in radians
#pi = math.pi         # pi constant


import math

def time_until_lost_connection(direction_A, direction_B):
    alfa = (abs(direction_B - direction_A) * math.pi) / 180
    hours = (math.sqrt(1225 / (2 - (2 * math.cos(alfa))))) / 5
    time_until_lost_connection = (hours * 60)
    return round(time_until_lost_connection, 3)