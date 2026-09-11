# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:16:24 2022

@author: hammad.eljisr
"""
import math
import numpy as np

def expFit(x,y):
    """
    This function finds exponential fit parameters (a and b) for a scatter of points
    y = a*exp(-b*x)
    Input:
        - x: x values for the scatter points
        - y: y values for the scatter points
    """
    ln_y = []
    for i in range(len(y)):
        ln_y.append(math.log(y[i]))
    Fit = np.polyfit(x,ln_y,1)
    b = -Fit[0]
    ln_a = Fit[1]
    a = math.exp(ln_a)
    return a, b