# -*- coding: utf-8 -*-
"""
Created on Tues Aug  29 15:56:54 2023

@author: hammad.eljisr
"""
from scipy.interpolate import interp1d
import numpy as np
import bisect

def adjustYZTendonSAP2000(SapModel,Tendon_object,Points):
    """
    This function adjusts the Y and Z coordinates of a tendon to follow a set of points along the longitudinal direction (X globally).
    Input:
        SapModel: SAP Model object
        Tendon_object: Label of the tendon object
        Points: Points through which the centroid axis pass through. The first and last point correspond to the points passing through the initial tendon line.
        e.g.: In the case of a bridge deck, the points lie along the deck curvature. The first and last points correspond to the start and end of the deck
    """
    
    SapModel.SetPresentUnits(6) # Unit system kN-m 
    
    """
    Get Y and Z adjustment values
    """
    # Get coordinates of specified points
    x_points = []
    y_points = []
    z_points = []
    for i in range(len(Points)):
        x_points.append(SapModel.PointObj.GetCoordCartesian(Points[i])[0])
        y_points.append(SapModel.PointObj.GetCoordCartesian(Points[i])[1])
        z_points.append(SapModel.PointObj.GetCoordCartesian(Points[i])[2])
    
    # Get tendon global coordinates
    x_tendon = SapModel.TendonObj.GetTendonData(Tendon_object,CSys = 'Global')[2]
    x_tendon = list(x_tendon)
    y_tendon = SapModel.TendonObj.GetTendonData(Tendon_object,CSys = 'Global')[3]
    y_tendon = list(y_tendon)
    z_tendon = SapModel.TendonObj.GetTendonData(Tendon_object,CSys = 'Global')[4]
    z_tendon = list(z_tendon)
    
    # Add all x coordinates of the points that lie within the tendon range
    x_points_m = []
    x_tendon_adj = x_tendon[:] 
    for i in range(len(x_points)):
        if x_points[i] > x_tendon[0] and x_points[i] < x_tendon[len(x_tendon)-1]:
            x_points_m.append(x_points[i])
    for i in range(len(x_points_m)):
        bisect.insort(x_tendon_adj, x_points_m[i])   
                
    # Get interpolation functions along points
    y_interp_o = interp1d(x_points, y_points,'linear',fill_value = 'extrapolate') # y interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    z_interp_o = interp1d(x_points, z_points,'linear',fill_value = 'extrapolate') # z interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    
    # Get interpolation functions along initial tendon line (straight line)
    y_interp_i = interp1d([x_points[0],x_points[len(x_points)-1]], [y_points[0],y_points[len(y_points)-1]],'linear',fill_value = 'extrapolate') # y interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    z_interp_i = interp1d([x_points[0],x_points[len(x_points)-1]], [z_points[0],z_points[len(z_points)-1]],'linear',fill_value = 'extrapolate') # z interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    
    # Get interpolation functions along the existing tendon
    y_interp_e = interp1d(x_tendon, y_tendon,'linear',fill_value = 'extrapolate') # y interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    z_interp_e = interp1d(x_tendon, z_tendon,'linear',fill_value = 'extrapolate') # z interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    
    # Get tendon interpolated coordinates along the points
    y_tendon_o = y_interp_o([x_tendon_adj])[0]  # y interpolation 
    z_tendon_o = z_interp_o([x_tendon_adj])[0]  # z interpolation 
    
    # Get tendon interpolated coordinates along the initial tendon line
    y_tendon_i = y_interp_i([x_tendon_adj])[0]  # y interpolation 
    z_tendon_i = z_interp_i([x_tendon_adj])[0]  # z interpolation 
    
    # Get tendon interpolated coordinates of the existing tendon at the x coordinates
    y_tendon_e = y_interp_e([x_tendon_adj])[0]  # y interpolation 
    z_tendon_e = z_interp_e([x_tendon_adj])[0]  # z interpolation 
    
    """
    Modify tendon coordinates at intermediate points
    """
    # Adjust interpolated coordinates
    y_tendon_adj = list(np.array(y_tendon_e) - np.array(y_tendon_i) + np.array(y_tendon_o))
    z_tendon_adj = list(np.array(z_tendon_e) - np.array(z_tendon_i) + np.array(z_tendon_o))
    
    # Update tendon data  
    n_control_points = int(len(x_tendon_adj)) # Number of points to define the tendon profile
    type_control = np.ones(len(x_tendon_adj))*2
    type_control[0] = 1
    type_control = list(type_control)
    type_control = [int(x) for x in type_control]                 
    SapModel.TendonObj.SetTendonData(Tendon_object, n_control_points,type_control, x_tendon_adj, y_tendon_adj, z_tendon_adj, "Global")
    
    return None





