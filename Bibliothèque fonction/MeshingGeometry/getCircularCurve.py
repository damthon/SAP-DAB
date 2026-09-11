# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:29:09 2024

@author: hammad.eljisr
"""

import math

def getCircularCurve(O,r,x,sign):
    """
    This function gets the cartesian y coordinates of a circle
    Input:
        - O: Circle origin [x,y]
        - r0: Circle radius 
        - x: x coordinate at which the circle y coordinates are calculated
        - sign: Positive or negative coordinates (1 or -1)
    Output:
        - y: y coordinates
    """
    
    y = sign*(math.sqrt(r**2 - (x-O[0])**2) + O[1])
    
    return y
