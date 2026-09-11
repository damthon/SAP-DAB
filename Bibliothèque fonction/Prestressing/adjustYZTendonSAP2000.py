# -*- coding: utf-8 -*-
"""
Created on Tues Aug  29 15:56:54 2023

@author: hammad.eljisr
"""

from scipy.interpolate import interp1d
import numpy as np
import bisect
import math 



def adjustYZTendonSAP2000(SapModel,Tendon_object,Points):
    """
    This function adjusts the Y and Z coordinates of a tendon to follow a set of points along the longitudinal direction (X globally). The Z coordinates 
    are interpolated along the elevation of the Points while the Y coordinates are obtained by offsetting the local 3 coordinates of the tendon about the Points in plane
    
    Input:
        SapModel: SAP Model object
        Tendon_object: Label of the tendon object, 1 is the local coordinate along the Tendon axis, 2 is the local coordinate for the tendon profile and 3 is the local coordinate horizonally
        Points: Points through which the centroid axis pass through. The first and last point correspond to the points passing through the initial tendon line.
        e.g.: In the case of a bridge deck, the points lie along the deck curvature. The first and last points correspond to the start and end of the deck
    """
    
    SapModel.SetPresentUnits(6) # Unit system kN-m  
    
    """
    Get Y and Z adjustment values
    """

    # Get coordinates of specified points along curve and sort
    x_points_c = []
    y_points_c = []
    z_points_c = []
    for i in range(len(Points)):
        x_points_c.append(SapModel.PointObj.GetCoordCartesian(Points[i])[0])
        y_points_c.append(SapModel.PointObj.GetCoordCartesian(Points[i])[1])
        z_points_c.append(SapModel.PointObj.GetCoordCartesian(Points[i])[2])
    
    I = np.argsort(x_points_c)
    x_points_c = list(np.array(x_points_c)[I])
    y_points_c = list(np.array(y_points_c)[I])
    z_points_c = list(np.array(z_points_c)[I])
    
    # Get tendon global coordinates
    x_tendon = SapModel.TendonObj.GetTendonData(Tendon_object,CSys = 'Global')[2]
    x_tendon = list(x_tendon)
    y_tendon = SapModel.TendonObj.GetTendonData(Tendon_object,CSys = 'Global')[3]
    y_tendon = list(y_tendon)
    z_tendon = SapModel.TendonObj.GetTendonData(Tendon_object,CSys = 'Global')[4]
    z_tendon = list(z_tendon)
    
    # Get curve about which the tendons are interpolated
    s_offsets = SapModel.TendonObj.GetTendonData(Tendon_object,CSys = 'Local')[4] # Offsets at tendon coordinates
    s_interp_o = interp1d(x_tendon,s_offsets,'linear',fill_value = 'extrapolate') # y interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    s = s_interp_o([x_points_c])[0]  # y interpolation 
    
    # Offset to obtain global x and y coordinates
    points_polyline = []
    for p in range(len(x_points_c)):
        points_polyline.append((x_points_c[p],y_points_c[p]))
    offset_points = offset_polyline(points_polyline,-s)
    y_points = []
    x_points = []
    for p in range(len(offset_points)):
        y_points.append(offset_points[p][1])
        x_points.append(offset_points[p][0])
    z_points = z_points_c
    
    # Add all x coordinates of the points that lie within the tendon range
    x_points_m = []
    x_tendon_adj = x_tendon[:] 
    for i in range(len(x_points)):
        if x_points[i] > x_tendon[0] and x_points[i] < x_tendon[len(x_tendon)-1]:
            x_points_m.append(x_points[i])
    for i in range(len(x_points_m)):
        bisect.insort(x_tendon_adj, x_points_m[i])   
                
    # Get interpolation functions along points
    z_interp_o = interp1d(x_points, z_points,'linear',fill_value = 'extrapolate') # z interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    
    # Get interpolation functions along initial tendon line (straight line)
    z_interp_i = interp1d([x_points[0],x_points[len(x_points)-1]], [z_points[0],z_points[len(z_points)-1]],'linear',fill_value = 'extrapolate') # z interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    
    # Get interpolation functions along the existing tendon
    y_interp_e = interp1d(x_tendon, y_tendon,'linear',fill_value = 'extrapolate') # y interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    z_interp_e = interp1d(x_tendon, z_tendon,'linear',fill_value = 'extrapolate') # z interpolation function, extrapolation added in case cable ends lie outside the bridge end points
    
    # Get tendon interpolated coordinates along the points
    z_tendon_o = z_interp_o([x_tendon_adj])[0]  # z interpolation 
    
    # Get tendon interpolated coordinates along the initial tendon line
    z_tendon_i = z_interp_i([x_tendon_adj])[0]  # z interpolation 
    
    # Get tendon interpolated coordinates of the existing tendon at the x coordinates
    z_tendon_e = z_interp_e([x_tendon_adj])[0]  # z interpolation 
    
    y_interp_e = interp1d(x_points,y_points,'linear',fill_value = 'extrapolate') 
    y_tendon_adj = y_interp_e([x_tendon_adj])[0]  # y interpolation 
    
    """
    Modify tendon coordinates at intermediate points
    """
    # Adjust interpolated coordinates
    y_tendon_adj = list(y_tendon_adj) #list(np.array(y_tendon_e) - np.array(y_tendon_i) + np.array(y_tendon_o))
    z_tendon_adj = list(np.array(z_tendon_e) - np.array(z_tendon_i) + np.array(z_tendon_o))
    
    # Update tendon data  
    n_control_points = int(len(x_tendon_adj)) # Number of points to define the tendon profile
    type_control = np.ones(len(x_tendon_adj))*2
    type_control[0] = 1
    type_control = list(type_control)
    type_control = [int(x) for x in type_control]                 
    SapModel.TendonObj.SetTendonData(Tendon_object, n_control_points,type_control, x_tendon_adj, y_tendon_adj, z_tendon_adj, "Global")
    
    return None

 
def offset_polyline(points,offsets):
    """
    This function offsets a polyline perpendicularly, similar to AutoCAD offset.

    Input:
        points : List of (x, y), the original polyline vertices.
        offsets : Offset distance at each point in the global direction 
        Offset distances (positive = left, negative = right). Must match length of points.

    Output:
        new_points: list of (x, y) points of the offset polyline.
    """
    
    if len(points) != len(offsets):
        raise ValueError("Length of points and offsets must match")

    n = len(points)
    new_points = []

    for i, (x, y) in enumerate(points):
        # Get tangent direction
        if i == 0:  # start point, use segment (0-1)
            dx = points[i+1][0] - x
            dy = points[i+1][1] - y
        elif i == n-1:  # end point, use segment (n-2,n-1)
            dx = x - points[i-1][0]
            dy = y - points[i-1][1]
        else:  # middle, average of prev and next segment tangents
            dx1 = x - points[i-1][0]
            dy1 = y - points[i-1][1]
            dx2 = points[i+1][0] - x
            dy2 = points[i+1][1] - y
            dx, dy = dx1 + dx2, dy1 + dy2

        # Perpendicular (normal) vector
        nx, ny = normalize(-dy, dx)

        # Apply offset
        s = offsets[i]
        new_points.append((x + s * nx, y + s * ny))

    return new_points

def normalize(vx, vy):
    """This function normalizes a 2D vector
    
    Input:
        vx, vy : x and y components of the vectorght)

    Output:
        Normalized x and y components of the vector
    """
    length = math.hypot(vx, vy)
    if length == 0:
        return 0.0, 0.0
    return vx / length, vy / length
