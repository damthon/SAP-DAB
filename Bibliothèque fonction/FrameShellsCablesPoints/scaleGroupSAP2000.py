# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

from getGroupPointObjSAP2000 import getGroupPointObjSAP2000

def scaleGroupSAP2000(SapModel,Group,Factor,Origin):
    """
    This function creates constraint between points in a group within a certain tolerance
    Input:
        SapModel: SAP Model object
        Group: Group of elements to be scaled
        Factor: Scale factor in each direction, list [X,Y,Z]
        Origin: Origin about which the elements are scaled, can be a string correspondin to the point label or list  of x,y,z coordinates
    """

    # Scale factors (adjust to 1 if less than or equal to 0)
    Factor_adjusted = []
    for s in Factor:
        if s > 0:
            Factor_adjusted.append(s)
        else:
            Factor_adjusted.append(1)
  
    # Get all points in the group
    points = getGroupPointObjSAP2000(SapModel,Group)
    
    
    # Get coordinates of origin
    if type(Origin) == str:
        x_o = SapModel.PointObj.GetCoordCartesian(Origin)[0]
        y_o = SapModel.PointObj.GetCoordCartesian(Origin)[1]
        z_o = SapModel.PointObj.GetCoordCartesian(Origin)[2]
    else:
        x_o = Origin[0]
        y_o = Origin[1]
        z_o = Origin[2]
    
    # Get coordinates of points in the group
    x_p = []
    y_p = []
    z_p = []
    for p in points:
        x_p.append(SapModel.PointObj.GetCoordCartesian(p)[0])
        y_p.append(SapModel.PointObj.GetCoordCartesian(p)[1])
        z_p.append(SapModel.PointObj.GetCoordCartesian(p)[2])

    # Get distances to the origin point
    x_dist = []
    y_dist = []
    z_dist = []
    for i in range(len(points)):
        x_dist.append((x_p[i] - x_o))
        y_dist.append((y_p[i] - y_o))
        z_dist.append((z_p[i] - z_o))
    
    # Get scaled distances
    x_dist_scaled = []
    y_dist_scaled = []
    z_dist_scaled = []
    for i in range(len(points)):
        x_dist_scaled.append(x_dist[i]*Factor_adjusted[0])
        y_dist_scaled.append(y_dist[i]*Factor_adjusted[1])
        z_dist_scaled.append(z_dist[i]*Factor_adjusted[2])
    
    # Get new scaled coordinates
    x_p_scaled = []
    y_p_scaled = []
    z_p_scaled = []
    for i in range(len(points)):
        x_p_scaled.append(x_p[i] + x_dist_scaled[i] - x_dist[i])
        y_p_scaled.append(y_p[i] + y_dist_scaled[i] - y_dist[i])
        z_p_scaled.append(z_p[i] + z_dist_scaled[i] - z_dist[i])
    
    # Interactive database editing
    # Coordinates table
    # Select group
    SapModel.PointObj.SetSelected(Group,True,1)
    T_coord = SapModel.DatabaseTables.GetTableForEditingArray('Joint Coordinates',Group)
    
    # Table data 
    T_len = T_coord[2] # Table length
    T_data = list(T_coord[3]) # List
    
    # Adjust coordinates
    for i in range(T_len):
        point_label = T_data[9*i] 
        flag = any(x == point_label for x in points)
        if  flag == True: # Check if point_label in group
            point_index = points.index(point_label)
            x_point_label = x_p_scaled[point_index]
            y_point_label = y_p_scaled[point_index]
            z_point_label = z_p_scaled[point_index]
            # Adjust coordinates
            T_data[9*i+3] = str(x_point_label)
            T_data[9*i+4] = str(y_point_label)
            T_data[9*i+6] = str(z_point_label)
    
    # Set new coordinates data table
    T_coord_new = SapModel.DatabaseTables.SetTableForEditingArray('Joint Coordinates',1,T_coord[1],T_coord[2],tuple(T_data))
    SapModel.DatabaseTables.ApplyEditedTables(0)   
                                                
    return None
