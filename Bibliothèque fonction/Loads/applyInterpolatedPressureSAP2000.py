# -*- coding: utf-8 -*-
"""
Created on Thurs Sep  21 11:02:54 2023

@author: hammad.eljisr
"""

import numpy as np
from scipy.interpolate import LinearNDInterpolator
from centroidAreaObjectSAP2000 import centroidAreaObjectSAP2000

def applyInterpolatedPressureSAP2000(SapModel,Area_objects,Plane_2D,X,Y,P,Load_pattern,Direction):
    """
    This function applies pressure on a set of selected area elements in a projected 2D plane (top face).
    The pressure distribution is obtained using linear interpolation at centroid of the area elements 
    and applied as uniform pressure on the area elements.
    Input:
        - SapModel: SAP Model object
        - Area_objects_sel: Selected area objects
        - Plane_2D: SAP2000 global axes defining the projected 2D plane in which pressure interpolation is conducted (XY = [0,1]; XZ = [0,2]; YZ = [1,2])
        - X: x coordinates of a set of points at which the pressure is defined (in the 2D plane)
        - Y: y coordinates of a set of points at which the pressure is defined (in the 2D plane)
        - P: Applied pressure at the specified coordinates
        - Load_pattern: Load pattern to which the applied pressure is assigned
        - Direction of the applied pressure: 
            -1: Bottom face pressure
            -2: Top face pressure
            10: Global gravity direction
            11: Projected global gravity direction (e.g. snow loads)
            
    """
    
    # Get interpolation function
    interp = LinearNDInterpolator(list(zip(X, Y)),P)

    # Get area labels centroid points
    centroid_area_objects = [[] for _ in range(len(Area_objects))]
    for i in range(len(Area_objects)):
        centroid_area_objects[i] = centroidAreaObjectSAP2000(SapModel,Area_objects[i])
              
    # Get interpolated pressure at centroid points
    x_c = np.transpose(centroid_area_objects)[Plane_2D[0]]
    y_c = np.transpose(centroid_area_objects)[Plane_2D[1]]
    p_c = interp(x_c,y_c)
    
    # Apply interpolated pressure at the element centroids as uniform surface pressure on the area elements 
    for i in range(len(Area_objects)):
        if Direction <0:
            SapModel.AreaObj.SetLoadSurfacePressure(Area_objects[i],Load_pattern,Direction,p_c[i],Replace=True)
        else:
            SapModel.AreaObj.SetLoadUniform(Area_objects[i], Load_pattern,p_c[i],Direction,True,'Global',0)
        
    return 

    

      