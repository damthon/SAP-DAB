# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

from getGroupPointObjSAP2000 import getGroupPointObjSAP2000

def jointBodyConstraintsGroupSAP2000(SapModel,Group,tolerance):
    """
    This function creates constraint between points in a group within a certain tolerance
    Input:
        SapModel: SAP Model object
        Group: Group of points
        tolerance: Specified tolerance in x, y or z respectively. e.g. [0.1,None,None] combines points within x = 0.1 m
    """

        
    # Get all points in the group
    points = getGroupPointObjSAP2000(SapModel,Group)
    
    # Get coordinates of points in the group
    x_p = []
    y_p = []
    z_p = []
    for p in points:
        x_p.append(SapModel.PointObj.GetCoordCartesian(p)[0])
        y_p.append(SapModel.PointObj.GetCoordCartesian(p)[1])
        z_p.append(SapModel.PointObj.GetCoordCartesian(p)[2])
    
    # Tolerance (within x, y or z coordinates)
    if tolerance[0] != None:
        t = tolerance[0]
        coord = x_p
    elif tolerance[1] != None:
        t = tolerance[1]
        coord = y_p
    else:
        t = tolerance[2]
        coord = z_p
        
    # Group points within the specified tolerance in separate lists
    grouped_indices = group_indices_within_tolerance(coord, t)
    grouped_points = []
    for i in range(len(grouped_indices)):
        grouped_points.append([points[j] for j in grouped_indices[i]])
            
    # Create and assign constraints
    for n in range(len(grouped_points)):
        for p in grouped_points[n]:
            if len(grouped_points[n]) > 1: # Exclude lists with 1 element
                SapModel.ConstraintDef.SetBody(Group + '_' + str(n),[True,True,True,True,True,True])
                SapModel.PointObj.SetConstraint(p,Group + '_' + str(n))
    
    return None


def group_indices_within_tolerance(numbers, t):
    """
    This function groups the indices of a set of numbers in a list wihin a specified toleranance together in separate lists
    Input:
        numbers: List of numbers
        t: Tolerance within which the numbers are grouped together in separate lists
   
    Output:
        grouped_indices: List of lists containing the grouped indices from the numbers list
    """
    
    grouped_indices = []
    visited_indices = set()

    for i in range(len(numbers)):
        if i not in visited_indices:
            current_group = [i]
            visited_indices.add(i)
            
            for j in range(i + 1, len(numbers)):
                if j not in visited_indices and abs(numbers[i] - numbers[j]) <= t:
                    current_group.append(j)
                    visited_indices.add(j)
            
            grouped_indices.append(current_group)
    
    return grouped_indices

