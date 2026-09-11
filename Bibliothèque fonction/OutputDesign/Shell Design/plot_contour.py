# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:20:43 2024

@author: hammad.eljisr
"""

from scipy.interpolate import griddata
import numpy as np
import alphashape
from shapely.geometry import Point

def plotContourValues(x,y,z,resolution,contour_method):
    """
    This function converts x,y,z coordinates into X,Y,Z arrays for input in countour plots
    Input:
        - x: X coordinates
        - y: y coordinates
        - z: Z coordinates
        - resolution: mesh grid resolution (use 1000)
        - contour_method: interpolation method ('linear','nearest','cubic')
    """
    resolution = str(resolution)+'j'
    X,Y = np.mgrid[min(x):max(x):complex(resolution),  min(y):max(y):complex(resolution)]
    points = [[a,b] for a,b in zip(x,y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    
    return X,Y,Z



def checkPointInside(x,y,test_point):
    """
    This function checks if a points is within a set of points
    Input:
        - x: X coordinates of set of points
        - y: y coordinates of points
        - test_point: (x,y) coordinate of the point to check
    Ouput: 
       - is_inside: boolean 1 if inside set of points,0 if outside
    """
    
    # Get points
    points = list(zip(x, y))
    
    # Generate the concave hull (adjust alpha to fit your shape)
    # alpha=0 is convex; higher values follow curves more tightly
    hull = alphashape.alphashape(points, alpha=2.0)
    
    # Check if a specific point is inside
    test_point = Point(x, y)
    is_inside = hull.contains(test_point)
    
    return is_inside
