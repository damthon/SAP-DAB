# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:29:09 2024

@author: hammad.eljisr
"""


def circleThreepoints(P1,P2,P3):
    """
    This function fits a circle (chord) through three points in a plane
    Input:
        - P1, P2, P3: Points [x,y]
    Output:
        - O: Circle origin [x,y]
        - r0: Circle radius
    """
    
    x1 = P1[0]
    y1 = P1[1]
    x2 = P2[0]
    y2 = P2[1]
    x3 = P3[0]
    y3 = P3[1]
    s1 = x1**2 + y1**2
    s2 = x2**2 + y2**2
    s3 = x3**2 + y3**2
    M11 = x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)
    M12 = s1*y2 + s2*y3 + s3*y1 - (s2*y1 + s3*y2 + s1*y3)
    M13 = s1*x2 + s2*x3 + s3*x1 - (s2*x1 + s3*x2 + s1*x3)
    x0 =  0.5*M12/M11
    y0 = -0.5*M13/M11
    r0 = ((x1 - x0)**2 + (y1 - y0)**2)**0.5
    
    O = [x0,y0]
    
    return O, r0
