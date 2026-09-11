# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 10:22:36 2026

@author: hammad.eljisr
"""

from getGroupPointObjSAP2000 import getGroupPointObjSAP2000
import numpy as np
import math 


def replicateShellAlongAxisAP2000(SapModel,Axis_group,Axis_direction,Shell_group,Initial_point,Target_group):
    """
    This function replicates a group of shell elements at target points along a specified axis
    
    Input:
        SapModel: SAP Model object
        Axis_group: Group containing axis points
        Axis_direction: 0 for increasing/decreasing X, 1 for increasing/decreasing Y
        Shell_group: Group containing shell elements to be replicated
        Initial_point: Intial reference point. e.g. '1'
        Target_group: Group containing the target points
        
    Output: Shell_group_rep: Replicated shell groups  
    """
    
    """
    Get Axis and Target Points
    """
    # Check initial point
    if Initial_point in Axis_group == False:
        print('Target points should be part of the defined axis!')
            
    # Get axis point objects
    Axis_p = getGroupPointObjSAP2000(SapModel,Axis_group)
    
    # Point coordinates
    X_axis_p = []
    Y_axis_p = []
    Z_axis_p = []
    for i in range(len(Axis_p)):
        X_axis_p.append(SapModel.PointObj.GetCoordCartesian(Axis_p[i])[0])
        Y_axis_p.append(SapModel.PointObj.GetCoordCartesian(Axis_p[i])[1])
        Z_axis_p.append(SapModel.PointObj.GetCoordCartesian(Axis_p[i])[2]) 
    
    # Sort along axis direction
    if Axis_direction == 0:
        I = np.argsort(X_axis_p)
    else:
        I = np.argsort(Y_axis_p)
    X_axis_p = list(np.array(X_axis_p)[I])
    Y_axis_p = list(np.array(Y_axis_p)[I])
    Z_axis_p = list(np.array(Z_axis_p)[I])
    Axis_p = list(np.array(Axis_p)[I])
    
    # Get and check target points
    target_p = getGroupPointObjSAP2000(SapModel,Target_group)
    for i in range(len(target_p)):
        if target_p[i] in Axis_p == False:
            print('Target points should be part of the defined axis!')
    
    """
    Translate Shell Group
    """
    # Get translation vectors
    # Translation vectors
    trans_v = []
    for j in range(len(target_p)):
        trans_v.append(getVector2Points(SapModel,[Initial_point,target_p[j]]))
        
    Shell_group_rep = [[] for _ in range(len(target_p))] # Replicate shell groups
    for j in range(len(target_p)): 
        SapModel.SelectObj.ClearSelection()
        SapModel.AreaObj.SetSelected(Shell_group,True,1)
        Elements_rep = SapModel.EditGeneral.ReplicateLinear(trans_v[j][0],trans_v[j][1],trans_v[j][2],1,1,[],[5])[1:3] # Replicated elements + type
        group_name = Shell_group + '-' + target_p[j] # New group name
        Shell_group_rep[j] = group_name
        SapModel.GroupDef.SetGroup(group_name) # Create group
        # Assign replicated elements to group
        a_index = [in_area for in_area,value in enumerate(Elements_rep[1]) if value == 5] # Area objects
        p_index = [in_area for in_area,value in enumerate(Elements_rep[1]) if value == 1] # Point objects
        area_rep = np.array(Elements_rep[0])[a_index]
        point_rep = np.array(Elements_rep[0])[p_index]
        for a in range(len(area_rep)):
            SapModel.AreaObj.SetGroupAssign(area_rep[a],group_name,0,0)
        for p in range(len(point_rep)):
            SapModel.PointObj.SetGroupAssign(point_rep[p],group_name,0,0)  
    
    """
    Rotate Shell Group in Plane
    """
    # Get vector along initial point
    index_ip = Axis_p.index(Initial_point) # Index of the initial point
    if index_ip > 0:
        try:
            vector_initial_points = [Axis_p[index_ip-1],Axis_p[index_ip+1]]
        except:
            vector_initial_points = [Axis_p[index_ip-1],Axis_p[index_ip]]
    else:
         vector_initial_points = [Axis_p[index_ip],Axis_p[index_ip+1]]  
         
    # Get vectors along target points
    vector_target_points = [[] for _ in range(len(target_p))] # Vector points at 
    for i in range(len(target_p)):
        index_tp = Axis_p.index(target_p[i])
        vector_target_points[i] = [Axis_p[index_tp-1],Axis_p[index_tp+1]]
    
    # Get vector coordinates
    vector_initial_points_xy = getVector2Points(SapModel,vector_initial_points)
    vector_target_points_xy = [] 
    for i in range(len(target_p)):
        vector_target_points_xy.append(getVector2Points(SapModel,vector_target_points[i]))
    
    # Get rotation angle at each target point
    theta_p = [[] for _ in range(len(target_p))]
    for i in range(len(target_p)):
        theta_p[i] = angleBetweenVectors(vector_initial_points_xy[0:2],vector_target_points_xy[i][0:2])   
    
    # Rotate replicated shell groups
    x_target_pt = []
    y_target_pt = []
    z_target_pt = []
    for i in range(len(target_p)):
        x_target_pt.append(SapModel.PointObj.GetCoordCartesian(target_p[i])[0])
        y_target_pt.append(SapModel.PointObj.GetCoordCartesian(target_p[i])[1])
        z_target_pt.append(SapModel.PointObj.GetCoordCartesian(target_p[i])[2])
    
    for i in range(len(Shell_group_rep)):
        SapModel.SelectObj.ClearSelection()
        SapModel.AreaObj.SetSelected(Shell_group_rep[i],True,1)    
        SapModel.EditGeneral.ReplicateRadial(4,x_target_pt[i],y_target_pt[i],z_target_pt[i],x_target_pt[i],y_target_pt[i],z_target_pt[i]+10,1,theta_p[i]*180/math.pi,1,[],[5],1)

    return Shell_group_rep

def getVector2Points(SapModel,vector_points):
    """ This function returns the x, y, z coordinates of a vector defined by two points 
    Input:
        SapModel: SAP Model object
        vector_points: Vector points, [start_point, end_point] 
    Output:
        vector_xy: Vector x-y coordinates, [x, y, z] 
    """
    
    # Intial point coordinate
    x_initial = SapModel.PointObj.GetCoordCartesian(vector_points[0])[0]
    y_initial = SapModel.PointObj.GetCoordCartesian(vector_points[0])[1]
    z_initial = SapModel.PointObj.GetCoordCartesian(vector_points[0])[2]
    # Final point coordinates
    x_final = SapModel.PointObj.GetCoordCartesian(vector_points[1])[0]
    y_final = SapModel.PointObj.GetCoordCartesian(vector_points[1])[1]
    z_final = SapModel.PointObj.GetCoordCartesian(vector_points[1])[2]

    vector_xy = [x_final-x_initial,y_final-y_initial,z_final-z_initial]
   
    return vector_xy


def angleBetweenVectors(v1, v2):
    """ This function returns the signed angle between two vectors in the xy plane
    Input:
        v1: Vector 1
        v2: Vector 2
    Output:
        theta: Angle between the two vectors, positive is CCW
    """
    x1, y1 = v1
    x2, y2 = v2
    
    # Angle of v1 with respect to the positive x-axis
    angle1 = math.atan2(y1, x1)
    # Angle of v2 with respect to the positive x-axis
    angle2 = math.atan2(y2, x2)
    
    # Calculate the difference and normalize to the range (-pi, pi]
    angle = angle2 - angle1
    if angle <= -math.pi:
        angle += 2 * math.pi
    elif angle > math.pi:
        angle -= 2 * math.pi
        
    return angle

# Example
# Axis_group = 'Spine'
# Axis_direction = 0 # 0 for increasing/decreasing X, 1 for increasing/decreasing  Y
# Shell_group = 'Entretoise'  # Shell group to be replicated
# Initial_point = '5' # Initial point 
# Target_group = 'Ent_points' # Target replication points

# replicateShellAlongAxisAP2000(SapModel,Axis_group,Axis_direction,Shell_group,Initial_point,Target_group)


