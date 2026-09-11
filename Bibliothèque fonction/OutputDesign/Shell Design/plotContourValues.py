# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:20:43 2024

@author: hammad.eljisr
"""

from scipy.interpolate import griddata
import numpy as np
import alphashape
from shapely.vectorized import contains 

def plotContourValues(x,y,z,resolution,contour_method):
    """
    This function converts x,y,z coordinates into X,Y,Z arrays for input in countour plots
    Input:
        - x: X coordinates
        - y: y coordinates
        - z: Z coordinates
        - resolution: mesh grid resolution (use 1000)
        - contour_method: interpolation method ('linear','nearest','cubic')
    Output: 
        - X,Y,Z: Grid contour coordinates
    """
    
    # Setup the grid
    res_complex = complex(0, resolution)
    X, Y = np.mgrid[min(x):max(x):res_complex, min(y):max(y):res_complex]
    
    # Interpolate data
    points_data = list(zip(x, y))
    Z = griddata(points_data, z, (X, Y), method=contour_method)
    
    # Generate hull
    hull = alphashape.alphashape(points_data, alpha=2.0)
    mask = contains(hull, X, Y)
    
    # Apply the mask to remove points outside set of x,y (where mask is False, set Z to NaN)
    Z[~mask] = np.nan
              
    return X, Y, Z
     
