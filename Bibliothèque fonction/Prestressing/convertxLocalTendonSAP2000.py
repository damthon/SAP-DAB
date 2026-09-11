# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 11:50:26 2025

@author: hammad.eljisr
"""

import numpy as np

def convertxLocalTendonSAP2000(SapModel,x_tendon,Points,anchor_point):
    """
    This function converts the x coordinates of a given tendon to the local coordinate 1 along the straight between the two end points of the span
    Input:
        SapModel: SAP Model object
        x_tendon: Tendon x coordinates
        Points: Start and end points of the tendon axis (along deck)
        Anchor point: Unscaled point (usually corresponds to the start point)
    """
    
    # Get x coordinates of the points along deck
    x_points = []
    y_points = []
    z_points = []
    for i in range(len(Points)):
        x_points.append(SapModel.PointObj.GetCoordCartesian(Points[i])[0])
        y_points.append(SapModel.PointObj.GetCoordCartesian(Points[i])[1])
        z_points.append(SapModel.PointObj.GetCoordCartesian(Points[i])[2])
        
    # Sort points in increasing x coordinates
    I = np.argsort(x_points)
    x_points = list(np.array(x_points)[I])
    y_points = list(np.array(y_points)[I])
    z_points = list(np.array(z_points)[I])
    Points = list(np.array(Points)[I])
    
    # Get x coordinate of anchor point
    x_anchor_point = SapModel.PointObj.GetCoordCartesian(anchor_point)[0]
    
    # Get scale factor
    #Length between the connecting points (local axes)
    length_connecting = ((x_points[-1] - x_points[0])**2 + (y_points[-1] - y_points[0])**2 + (z_points[-1] - z_points[0])**2)**0.5
    
    # Length x in global coordinates
    length_x = abs(max(x_points) - min(x_points))
    s_factor = length_connecting/length_x
    
    # Scale the global x coordinates of the existing tendon
    x_tendon_local = []
    for i in range(len(x_tendon)):
        x_t_l = (x_tendon[i] - x_anchor_point)*s_factor + x_anchor_point
        x_tendon_local.append(x_t_l)
    
    return x_tendon_local