# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:10:43 2024

@author: hammad.eljisr
"""

def mainCableTension(q,l_m,f_m):
    """
    This function calculates the tension in the main cable due to dead load sag
    Input:
        q: Uniform load
        l_m: Main span
        f_m: Main span sag
        SC_spacing: Section cut spacing   
        
    Output:
        H:  Horizontal force at parabola ends
        T: Tension in the main cable
    """ 
    
    H = q*(l_m**2)/(8*f_m) # Horizontal component of cable tension
    T = H/l_m*(l_m**2 + 16*f_m**2)**0.5 # Tension in the main cable
    
    return H,T