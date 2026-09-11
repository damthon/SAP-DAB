# -*- coding: utf-8 -*-
"""
Created on Thurs Sep  21 11:02:54 2023

@author: hammad.eljisr
"""

import numpy as np
from scipy.interpolate import LinearNDInterpolator
from Loads.centroidAreaObjectSAP2000 import centroidAreaObjectSAP2000

def applyInterpolatedUniformSAP2000(SapModel,Area_objects,Plane_2D,X,Y,U,Direction,Load_pattern):
    """
    This function applies uniform load on a set of selected area elements in a projected 2D plane (top face).
    The uniform load distribution is obtained using linear interpolation at centroid of the area elements 
    and applied as uniform pressure on the area elements.
    Input:
        - SapModel: SAP Model object
        - Area_objects_sel: Selected area objects
        - Plane_2D: SAP2000 global axes defining the projected 2D plane in which pressure interpolation is conducted (XY = [0,1]; XZ = [0,2]; YZ = [1,2])
        - X: x coordinates of a set of points at which the uniform load is defined (in the 2D plane)
        - Y: y coordinates of a set of points at which the uniform load is defined (in the 2D plane)
        - U: List of applied uniform load at the specified coordinates and load global direction 
        - Direction: 1 to 3 local xyz, 4 to 5 global XYZ, 10 gravity
        - Load_pattern: Load pattern to which the applied pressure is assigned
    """
    
    # Uniform load direction
    
    # Get interpolation function
    interp = LinearNDInterpolator(list(zip(X, Y)),U)

    # Get area labels centroid points
    centroid_area_objects = [[] for _ in range(len(Area_objects))]
    for i in range(len(Area_objects)):
        centroid_area_objects[i] = centroidAreaObjectSAP2000(SapModel,Area_objects[i])
              
    # Get interpolated pressure at centroid points
    x_c = np.transpose(centroid_area_objects)[Plane_2D[0]]
    y_c = np.transpose(centroid_area_objects)[Plane_2D[1]]
    u_c = interp(x_c,y_c)
    
    # Apply interpolated pressure at the element centroids as uniform surface pressure on the area elements 
    for i in range(len(Area_objects)):
        SapModel.AreaObj.SetLoadUniform(Area_objects[i], Load_pattern, u_c[i], Direction, True, "Global")
        #SapModel.AreaObj.SetLoadSurfacePressure(Area_objects[i], Load_pattern, -2, u_c[i],Replace=True)
        
    return 

    

      