# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

import numpy as np
from getGroupPointObjSAP2000 import getGroupPointObjSAP2000
from getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000
from shapely.geometry import LineString

def assignMC3SAP2000(SapModel,O,n,e,a,a_t,r_inf,roadway,centerline,l_pattern,Qk):
    """
    This function creates the area sections for the tyre loads and links to existing mesh - modèle de charge 3, SIA 261/1 §14.2 and Figure 10a
    Input:
        SapModel: SAP Model object
        O: Center of applied axle loads along centerline of the deck in m
        n: Number of tyres per load train
        e: Load eccentricity from centerline in m (positive or negative)
        a: Longitudinal distance between each train of axle loads in m
        a_t: Transverse distance between the axle loads in m
        r_inf: Radius of influence in m, includes the joints at which the axle load is distributed (e.g. use 0.2 m + 10% tolerance)
        roadway: Group of the roadway to which the tyre loads are added
        centerline: Group corresponding to centerline nodes
        l_pattern: Load pattern
        Qk: Total axle load in kN
    
    """
    
    # Set kN-m unit system
    SapModel.SetPresentUnits(6)
    
    # Obtian tyre loads
    Q1_value = 0.5*Qk/(2*n)
    
    # Get coordinates of axle loads along centerline
    cl_points = getGroupPointObjSAP2000(SapModel,centerline) # CL points
    x_cl_points = [] # x-coordinates
    y_cl_points = [] # y-coordinates
    for i in range(len(cl_points)):
        x_cl_points.append(SapModel.PointObj.GetCoordCartesian(cl_points[i])[0])
        y_cl_points.append(SapModel.PointObj.GetCoordCartesian(cl_points[i])[1])
    
    # Sort increasing x
    I_x = np.argsort(x_cl_points)
    x_cl_points = list(np.array(x_cl_points)[I_x])    
    y_cl_points = list(np.array(y_cl_points)[I_x])    
    
    # Get stations
    stations = [0]
    for i in range(1,len(cl_points)):
        d_temp = (x_cl_points[i]**2 + y_cl_points[i]**2)**0.5 - (x_cl_points[i-1]**2 + y_cl_points[i-1]**2)**0.5
        s = stations[i-1] + d_temp
        stations.append(s)
    
    # Axle coordinates along centerline
    # Stations of the loads
    s_O = np.interp(O[0],x_cl_points,stations)
    s_axle = [s_O-a/2,s_O+a/2]
    for i in range(n-1):
        s_axle_temp_i = s_axle[0] - 1.8
        s_axle_temp_f = s_axle[-1] + 1.8
        s_axle.insert(0,s_axle_temp_i)
        s_axle.append(s_axle_temp_f)
    
    # Remove s_axle outside stations
    s_axle = [s for s in s_axle if s <= stations[-1] and s >= stations[0]]
    # Coordinates of the loads along the centerline
    x_axle_cl = np.interp(s_axle,stations,x_cl_points)
    y_axle_cl = np.interp(s_axle,stations,y_cl_points)

    # Offset centerline coordinates and O in postive and negative direction
    ls = [() for _ in range(len(x_axle_cl))]
    for i in range(len(x_axle_cl)):
        ls[i] = (x_axle_cl[i],y_axle_cl[i])
    cl_string = LineString(ls)
    # Positive distance = left side, Negative = right side
    axle_string_pos = cl_string.parallel_offset(a_t/2+e, side='left',join_style=2)
    axle_string_neg = cl_string.parallel_offset(-a_t/2+e, side='left',join_style=2)

    # List of offset coordinates
    x_pos = []
    y_pos = []
    x_neg = []
    y_neg = []
    for i in range(len(axle_string_pos.coords)):
        x_pos.append(axle_string_pos.coords[i][0])
        y_pos.append(axle_string_pos.coords[i][1])
        
    for i in range(len(axle_string_neg.coords)):
        x_neg.append(axle_string_neg.coords[i][0])
        y_neg.append(axle_string_neg.coords[i][1])
    
    # Check roadway joints that lie within the circle of influemce
    rw_joints_loaded_pos = [[] for _ in range(len(x_pos)) ] # Loaded roadway joints at each tyre
    rw_joints_loaded_neg = [[] for _ in range(len(x_neg)) ] # Loaded roadway joints at each tyre
    rw_area_objects = getGroupAreaObjSAP2000(SapModel,roadway) # Roadway area objects
    
    for i in range(len(rw_area_objects)):
        area_points = SapModel.AreaObj.GetPoints(rw_area_objects[i])[1]
        for j in range(len(area_points)):
            x_joint = SapModel.PointObj.GetCoordCartesian(area_points[j])[0]
            y_joint = SapModel.PointObj.GetCoordCartesian(area_points[j])[1]
            # Check if joint within circle of each axle load
            for k in range(len(x_pos)): # 12 axles
                if ((x_joint - x_pos[k])**2 + (y_joint - y_pos[k])**2)**0.5 <= r_inf: 
                    rw_joints_loaded_pos[k].append(area_points[j])
            for k in range(len(x_neg)): # 12 axles
                if ((x_joint - x_neg[k])**2 + (y_joint - y_neg[k])**2)**0.5 <= r_inf:
                    rw_joints_loaded_neg[k].append(area_points[j])
                    
    for k in range(len(rw_joints_loaded_pos)):
        rw_joints_loaded_pos[k] = list(set(rw_joints_loaded_pos[k]))
        rw_joints_loaded_neg[k] = list(set(rw_joints_loaded_neg[k]))
        if len(rw_joints_loaded_pos[k]) == 0 or len(rw_joints_loaded_neg[k]) == 0:
            print('Axles for ' + l_pattern + ' outside roadway!')
                  
    ### Load joints POSITIVE ###
    for i in range(len(rw_joints_loaded_pos)):
        for j in range(len(rw_joints_loaded_pos[i])):
            SapModel.PointObj.SetSelected(rw_joints_loaded_pos[i][j],True,0) # Select positive
                
    d_pos = [[] for _ in range(len(rw_joints_loaded_pos))]# Distance from each loaded joint to center of each axle load POS
    for i in range(len(rw_joints_loaded_pos)): # Number of axles
        for j in range(len(rw_joints_loaded_pos[i])): # Loaded joints
            x_ij = SapModel.PointObj.GetCoordCartesian(rw_joints_loaded_pos[i][j])[0]
            y_ij = SapModel.PointObj.GetCoordCartesian(rw_joints_loaded_pos[i][j])[1]
            d_ij = ((x_ij - x_pos[i])**2 + (y_ij - y_pos[i])**2)**0.5
            d_pos[i].append(d_ij)
   
    # Ratio of axle load at each joint (inverse-distance weighting)
    w_pos = [[] for _ in range(len(rw_joints_loaded_pos))] # Weights
    r_pos = [[] for _ in range(len(rw_joints_loaded_pos))] # Ratio at each loaded joint
    for i in range(len(rw_joints_loaded_pos)): # Number of axles
        for j in range(len(d_pos[i])):
            w_pos[i].append(1/(d_pos[i][j]+0.01)) # 0.01 to remove singularity 
    for i in range(len(rw_joints_loaded_pos)): # Number of axles  
        for j in range(len(d_pos[i])):
            r_pos[i].append(w_pos[i][j]/sum(w_pos[i]))         
   
    # Assign loads
    for i in range(len(rw_joints_loaded_pos)): # Number of axles  
        for j in range(len(rw_joints_loaded_pos[i])):
            SapModel.PointObj.SetLoadForce(rw_joints_loaded_pos[i][j],l_pattern,[0,0,-Q1_value*r_pos[i][j],0,0,0],1,'Global',0)


    ### Load joints NEGATIVE ###
    for i in range(len(rw_joints_loaded_neg)):
        for j in range(len(rw_joints_loaded_neg[i])):
            SapModel.PointObj.SetSelected(rw_joints_loaded_neg[i][j],True,0) # Select negative
                
    d_neg = [[] for _ in range(len(rw_joints_loaded_neg))]# Distance from each loaded joint to center of each axle load POS
    for i in range(len(rw_joints_loaded_neg)): # Number of axles
        for j in range(len(rw_joints_loaded_neg[i])): # Loaded joints
            x_ij = SapModel.PointObj.GetCoordCartesian(rw_joints_loaded_neg[i][j])[0]
            y_ij = SapModel.PointObj.GetCoordCartesian(rw_joints_loaded_neg[i][j])[1]
            d_ij = ((x_ij - x_neg[i])**2 + (y_ij - y_neg[i])**2)**0.5
            d_neg[i].append(d_ij)
   
    # Ratio of axle load at each joint (inverse-distance weighting)
    w_neg = [[] for _ in range(len(rw_joints_loaded_neg))] # Weights
    r_neg = [[] for _ in range(len(rw_joints_loaded_neg))] # Ratio at each loaded joint
    for i in range(len(rw_joints_loaded_neg)): # Number of axles
        for j in range(len(d_neg[i])):
            w_neg[i].append(1/(d_neg[i][j]+0.01)) # 0.01 to remove singularity 
    for i in range(len(rw_joints_loaded_neg)): # Number of axles  
        for j in range(len(d_neg[i])):
            r_neg[i].append(w_neg[i][j]/sum(w_neg[i]))         
   
    # Assign loads
    for i in range(len(rw_joints_loaded_neg)): # Number of axles  
        for j in range(len(rw_joints_loaded_neg[i])):
            SapModel.PointObj.SetLoadForce(rw_joints_loaded_neg[i][j],l_pattern,[0,0,-Q1_value*r_neg[i][j],0,0,0],1,'Global',0)

    return None
