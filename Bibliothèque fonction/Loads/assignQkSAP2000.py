# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

from Selection.getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000

def assignQkSAP2000(SapModel,O,r_inf,lane,l_pattern,value):
    """
    This function creates the area sections for the tyre loads and links to existing mesh - modèle de charge 1, SIA 261
    Input:
        SapModel: SAP Model object
        O: Center of the tyre loads in m
        r_inf: Radius of influence in m, includes the joints at which the axle load is distributed (e.g. use 0.2 m + 10% tolerance)
        lane: Group of the lane to which the tyre loads are added
        l_pattern: Load pattern
        value: Tyre loads [Vertical load,Horizontal load,Moment due to horizontal load] in kNm per tyre. Horizontal load is in global X, vertical load is in global Z
    """

    # Set kN-m unit system
    SapModel.SetPresentUnits(6)

    # Create tyres
    # Tyre centerpoints
    dx = [-0.6,-0.6,0.6,0.6] # Delta_x for each tyre
    dy = [-1,1,1,-1] # Delta_y for each tyre

    # Tyre coordinates
    tyre_coord_x = [[],[],[],[]]
    tyre_coord_y = [[],[],[],[]]
    tyre_coord_z = [[],[],[],[]]
    for i in range(len(tyre_coord_x)):
        tyre_coord_x[i] = [O[0] + dx[i] - 0.4/2,O[0] + dx[i] - 0.4/2,O[0] + dx[i] + 0.4/2,O[0] + dx[i] + 0.4/2]
        tyre_coord_y[i] = [O[1] + dy[i] - 0.4/2,O[1] + dy[i] + 0.4/2,O[1] + dy[i] + 0.4/2,O[1] + dy[i] - 0.4/2]
        tyre_coord_z[i] = [O[2],O[2],O[2],O[2]]

    # Check lane joints that lie within the circle of influemce
    lane_joints_loaded = [[],[],[],[]] # Loaded lane joints at each tyre
    lane_area_objects = getGroupAreaObjSAP2000(SapModel,lane) # Lane area objects

    for i in range(len(lane_area_objects)):
        area_points = SapModel.AreaObj.GetPoints(lane_area_objects[i])[1]
        for j in range(len(area_points)):
            x_joint = SapModel.PointObj.GetCoordCartesian(area_points[j])[0]
            y_joint = SapModel.PointObj.GetCoordCartesian(area_points[j])[1]
            # print(y_joint)
            # Check if joint within circle of each tyre
            for k in range(4): # 4 tyres
                # print(((x_joint - sum(tyre_coord_x[k])/4)**2 + (y_joint - sum(tyre_coord_y[k])/4)**2)**0.5)
                if ((x_joint - sum(tyre_coord_x[k])/4)**2 + (y_joint - sum(tyre_coord_y[k])/4)**2)**0.5 <= r_inf:
                    lane_joints_loaded[k].append(area_points[j])

    for k in range(len(lane_joints_loaded)):
        lane_joints_loaded[k] = list(set(lane_joints_loaded[k]))
        if len(lane_joints_loaded[k]) == 0:
            print('Tyres for ' + l_pattern + ' outside lane!')

    for i in range(4):
        for j in range(len(lane_joints_loaded[i])):
            SapModel.PointObj.SetSelected(lane_joints_loaded[i][j],True,0)

    # Load joints
    d = [[],[],[],[]]# Distance from each loaded joint to center of each tyre
    for i in range(4): # Number of tyres
        for j in range(len(lane_joints_loaded[i])): # Loaded joints
            x_ij = SapModel.PointObj.GetCoordCartesian(lane_joints_loaded[i][j])[0]
            y_ij = SapModel.PointObj.GetCoordCartesian(lane_joints_loaded[i][j])[1]
            d_ij = ((x_ij - sum(tyre_coord_x[i])/4)**2 + (y_ij - sum(tyre_coord_y[i])/4)**2)**0.5
            d[i].append(d_ij)

    # Ratio of axle load at each joint (inverse-distance weighting)
    w = [[],[],[],[]] # Weights
    r = [[],[],[],[]] # Ratio at each loaded joint
    for i in range(4): # Number of tyres
        for j in range(len(d[i])):
            w[i].append(1/(d[i][j]+0.01)) # 0.01 to remove singularity
    for i in range(4): # Number of tyres
        for j in range(len(d[i])):
            r[i].append(w[i][j]/sum(w[i]))

    # Assign loads
    for i in range(4): # Number of tyres
        for j in range(len(lane_joints_loaded[i])):
            SapModel.PointObj.SetLoadForce(lane_joints_loaded[i][j],l_pattern,[value[1]*r[i][j],0,-value[0]*r[i][j],0,-value[2]*r[i][j],0],1,'Global',0)

    return None
