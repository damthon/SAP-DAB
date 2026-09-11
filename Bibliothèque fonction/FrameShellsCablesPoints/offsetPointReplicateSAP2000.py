# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

from getGroupPointObjSAP2000 import getGroupPointObjSAP2000
import numpy as np

group_points = 'B+'
offset_type = [1,'B+_v','X']
offset_value = 800

def offsetPointReplicateSAP2000(SapModel,group_points,offset_type,offset_value):
    """
    This function creates replicates of a group of points by specifying an offset value
    Input:
        SapModel: SAP Model object
        group_points: Group of points to be replicated with an offset
        offset_type: List consisting of 2 elements. First element 0 for vector and 1 for points, second element is a list of vectors (tuples) or group of points defining the vector from the
        points to be offset, third element is the global direction in which points are sorted (not needed in case vectors are defined).
        e.g. [0,[(-1,0,2),(3,4,-1)],'-'] or [1,'points_vector','X']. Length of the vectors/points should be equal to length of points to be replicated.
        offset_value: Offset value
    Output:
        replicated_group_name: Name of group containing replicated points
        
    """
    
    # Points to be replicated
    points = getGroupPointObjSAP2000(SapModel,group_points)
    
    # Get offset vectors
    op = 1
    if offset_type[0] == 1: # Reference points
        # Reference points defining the vector    
        points_vector = getGroupPointObjSAP2000(SapModel,offset_type[1])
        if len(points_vector) != len(points):
            print('Number of vectors do not correspond to points to be replicated. Operation aborted!')
            op = 0 
        else:
            # Point coordinates
            x_p, y_p, z_p = [], [], []
            x_pv, y_pv, z_pv = [], [], []
            for j in range(len(points)):
                # Points to be replicated
                x_p.append(SapModel.PointObj.GetCoordCartesian(points[j])[0])
                y_p.append(SapModel.PointObj.GetCoordCartesian(points[j])[1])
                z_p.append(SapModel.PointObj.GetCoordCartesian(points[j])[2])
                # Reference points defining the vector
                x_pv.append(SapModel.PointObj.GetCoordCartesian(points_vector[j])[0])
                y_pv.append(SapModel.PointObj.GetCoordCartesian(points_vector[j])[1])
                z_pv.append(SapModel.PointObj.GetCoordCartesian(points_vector[j])[2])
            # Sort ascending 
            if offset_type[2] == 'X':
               I_p = np.argsort(x_p)
               I_pv = np.argsort(x_pv)
            elif offset_type[2] == 'Y':
               I_p = np.argsort(y_p)
               I_pv = np.argsort(y_pv)
            else:
               I_p = np.argsort(z_p)
               I_pv = np.argsort(z_pv)
            # Sort points
            x_p = list(np.array(x_p)[I_p])
            y_p = list(np.array(y_p)[I_p])
            z_p = list(np.array(z_p)[I_p])
            x_pv = list(np.array(x_pv)[I_pv])
            y_pv = list(np.array(y_pv)[I_pv])
            z_pv = list(np.array(z_pv)[I_pv])
            points_sorted = list(np.array(points)[I_p])
            # Get vectors
            offset_v = []
            for v in range(len(points_vector)):
                v_temp = (x_pv[v]-x_p[v],y_pv[v]-y_p[v],z_pv[v]-z_p[v])
                offset_v.append(v_temp)
    else:
        offset_v = offset_type[1]
        if len(offset_v) != len(points):
            print('Number of vectors do not correspond to points to be replicated. Operation aborted!')
            op = 0
    
    if  op == 1:  
        for i in range(len(points_sorted)):
            SapModel.SelectObj.ClearSelection()
            SapModel.PointObj.SetSelected(points_sorted[i],True,0)    
            v_rep = unitVector(offset_v[i])
            x_rep, y_rep, z_rep = v_rep[0]*offset_value, v_rep[1]*offset_value, v_rep[2]*offset_value  # x, y, z replicate coordinates
            points_rep = SapModel.EditGeneral.ReplicateLinear(x_rep,y_rep,z_rep,1,1,[''],[1])[1:3]
            # Create group with replicated points
            replicated_group_name = group_points + '_' + str(round(offset_value,2)) # New group name
            SapModel.GroupDef.SetGroup(replicated_group_name) # Create group
            # Assign replicated elements to group
            p_index = [in_points for in_points,value in enumerate(points_rep[1]) if value == 1] # Point objects
            point_rep = np.array(points_rep[0])[p_index]
            SapModel.PointObj.SetGroupAssign(point_rep[0],replicated_group_name,0,0) 
            print('Point ' + str(i) + ' out of ' + str(len(points_sorted)) + ' replicated: ' + str(points_sorted[i]))
        else:
            replicated_group_name = None
          
    return replicated_group_name

def unitVector(v):
    """ This function transforms vector into a unit vector 
    Input:
        v: Vector 
    Output:
        v_u: Unit vector
    """
    
    # Magnitude
    x, y, z = v[0], v[1], v[2]
    abs_v = (x**2 + y**2 +z**2)**0.5
    # Unit vector
    x_u, y_u, z_u = x/abs_v, y/abs_v, z/abs_v
    v_u = (x_u,y_u,z_u)
    
    return v_u



