# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

from getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000
from getGroupPointObjSAP2000 import getGroupPointObjSAP2000
import numpy as np
from scipy.spatial import ConvexHull

def assignWindShellSAP2000(SapModel,deck,deck_edge,centerline,h,qk1,tr_dir,qk3,ev_h,eh,l_patterns):
    """
    This function assignes the wind loads qk1 (horizontal) and qk3 (vertical) to a SLAB deck of shell elements
    Input:
        - SapModel: SAP Model object
        - deck: Deck group containing the shell elements
        - deck_edge: Group of deck edge points
        - centerline: Group consisting of centerline points
        - h: List of deck height at each station along deck centerline [s,h] (e.g. [[0,1,1.6,20],[0.4,0.5,0.5,0.9]])
        - qk1: Value of the horizontal load in kN/m2 (sign indicates direction)
        - tr_dir: 0 for x-direction, 1 for y-direction
        - qk3: Value of the vertical load in kN/m2 (sign indicates direction)
        - ev_h: Horizontal wind load eccentricity(Tableau 61, Annexe C, SIA 261)
        - eh: Vertical wind load eccentricity (Tableau 61, Annexe C, SIA 261)
        - l_patterns: Load patterns list [qk1_LP,qk3_LP]
    """
    
    # Set kN-m unit system
    SapModel.SetPresentUnits(6)
    
    # Horizontal wind loads, qk1
    # Get edge points and sort
    points_deck_edge = getGroupPointObjSAP2000(SapModel,deck_edge)
    points_edge_coordinates = [[] for _ in range(len(points_deck_edge))]
    for i in range(len(points_deck_edge)):
        x_p = SapModel.PointObj.GetCoordCartesian(points_deck_edge[i])[0]
        y_p = SapModel.PointObj.GetCoordCartesian(points_deck_edge[i])[1]
        points_edge_coordinates[i] = [x_p,y_p]
    # x and y edge coordinates
    x_edge = [sub[0] for sub in points_edge_coordinates]   
    y_edge = [sub[1] for sub in points_edge_coordinates] 
    
    I_edge = np.argsort(x_edge)
    x_edge = list(np.array(x_edge)[I_edge])
    y_edge = list(np.array(y_edge)[I_edge])
    points_edge_coordinates = list(np.array(points_edge_coordinates)[I_edge])
    points_deck_edge = list(np.array(points_deck_edge)[I_edge])
    
    # Get centerline points and sort
    points_CL = getGroupPointObjSAP2000(SapModel,centerline)
    points_CL_coordinates = [[] for _ in range(len(points_CL))]
    for i in range(len(points_CL)):
        x_c = SapModel.PointObj.GetCoordCartesian(points_CL[i])[0]
        y_c = SapModel.PointObj.GetCoordCartesian(points_CL[i])[1]
        points_CL_coordinates[i] = [x_c,y_c]
    # x and y centerline coordinates
    x_CL = [sub[0] for sub in points_CL_coordinates]   
    y_CL = [sub[1] for sub in points_CL_coordinates]  
       
    I_CL = np.argsort(x_CL)
    x_CL = list(np.array(x_CL)[I_CL])
    y_CL = list(np.array(y_CL)[I_CL])
    points_CL_coordinates = list(np.array(points_CL_coordinates)[I_CL])
    points_CL = list(np.array(points_CL)[I_CL])  
    
    # Project edge points on centerline
    # Projected x coordinates of edge points along the centerline
    points_edge_projected_x = [t[0] for s, t in zip(points_edge_coordinates, points_CL_coordinates)]
    
    # Interpolate h at edge joints
    h_edge = np.interp(points_edge_projected_x,h[0],h[1])
    
    # Obtain horizontal joint loads
    # Edge stations
    s_edge = [0]
    for i in range(1,len(x_edge)):
        s_edge_temp = s_edge[i-1] + ((x_edge[i]-x_edge[i-1])**2 + (y_edge[i]-y_edge[i-1])**2)**0.5
        s_edge.append(s_edge_temp)
        
    qk1_f = [] # Horizontal force
    qk1_m = [] # Moment due to eccentricity
    for i in range(len(points_deck_edge)):
        if i == 0:
            l_point = (s_edge[1]-s_edge[0])/2  # Tributary length of the joint
        elif i == len(points_deck_edge)-1:
            l_point = (s_edge[i]-s_edge[i-1])/2 # Tributary length of the joint
        else:
            l_point = (s_edge[i+1]-s_edge[i])/2  + (s_edge[i]-s_edge[i-1])/2 # Tributary length of the joint
        qk1_f.append(qk1*l_point*h_edge[i])
        ev = ev_h*h_edge[i] 
        qk1_m.append(qk1*l_point*h_edge[i]*ev)
    
    # Assign horizontal wind load
    for i in range(len(points_deck_edge)):
        if tr_dir == 0:
            qk1_forces = [qk1_f[i],0,0,0,qk1_m[i],0]
        else:
            qk1_forces = [0,qk1_f[i],0,-qk1_m[i],0,0]
        SapModel.PointObj.SetLoadForce(points_deck_edge[i],l_patterns[0],qk1_forces,1,'Global',0)   
        
    # Assign vertical loads
    points_deck, Fv = distribute_qk3(SapModel,deck,tr_dir,eh,-qk3)
    qk3_forces = []
    for f in range(len(Fv)):
        qk3_forces.append([0,0,Fv[f],0,0,0])
    
    for i in range(len(points_deck)):
        SapModel.PointObj.SetLoadForce(points_deck[i],l_patterns[1],qk3_forces[i],1,'Global',0) 
        
    return None


def distribute_qk3(SapModel,deck,tr_dir,eh,qk3):
    """
    This function distributes vertical wind forces on the deck 2D to account for the eccentricity
    Input:
        - SapModel: SAP Model object
        - deck: Deck group containing the shell elements
        - tr_dir: 0 for x-direction, 1 for y-direction
        - eh: Vertical wind load eccentricity (Tableau 61, Annexe C, SIA 261)
        - qk3: Value of the vertical load in kN/m2 (sign indicates direction)
    Output:
        - points_deck: Deck nodes
        - Fv: Vertical forces at each node
    """
    # Area elements of the deck
    area_deck = getGroupAreaObjSAP2000(SapModel,deck)
    # Get point objects of the deck
    points_deck_o = []
    for a in range(len(area_deck)):
        points_deck_o.append(SapModel.AreaObj.GetPoints(area_deck[a])[1])    

    # Area of  each element projected int the 2D xy plane
    surface_area_deck = [[] for _ in range(len(area_deck))] # Surface area of each element
    area_coords = [[] for _ in range(len(area_deck))] # Area objects xy coordinates
    for t in range(len(points_deck_o)):
        for p in range(len(points_deck_o[t])):
            x,y = SapModel.PointObj.GetCoordCartesian(points_deck_o[t][p])[0:2]
            area_coords[t].append((x,y))
        surface_area_deck[t] = calculate_area_2D(area_coords[t])
   
    points_deck = list(set([p for tup in points_deck_o for p in tup]))
    # Points x-y coordinates
    points_coordinates = [[] for _ in range(len(points_deck))]
    for i in range(len(points_deck)):
        x_pe = SapModel.PointObj.GetCoordCartesian(points_deck[i])[0]
        y_pe = SapModel.PointObj.GetCoordCartesian(points_deck[i])[1]
        points_coordinates[i] = [x_pe,y_pe]
    
    # Total resultant force
    total_f = qk3*sum(surface_area_deck)
    
    # Extract y-coordinates and convert to a np array for math operations
    if tr_dir == 1: 
        y = np.array([sub[1] for sub in points_coordinates]) 
        # Shift y to be relative to the centroid so eh (eccentricity) 
        # Creates a moment about the center of the points, not the global origin
        y_centroid = np.mean(y)
        y_rel = y - y_centroid
        
        # Construct 2x2 matrix using the relative coordinates
        n = len(points_deck)
        # A * [a, b]^T = [Moment, Total Force]
        A = np.array([[np.sum(y_rel**2), np.sum(y_rel)],[np.sum(y_rel), n]])
        # B contains the Moment (Force * eccentricity) and the Total Force
        B = np.array([total_f*eh, total_f])
    else:
        # Fallback if tr_dir is not 1 (e.g., x-direction)
        x = np.array([sub[0] for sub in points_coordinates])
        # Shift y to be relative to the centroid so eh (eccentricity) 
        # Creates a moment about the center of the points, not the global origin
        x_centroid = np.mean(x)
        x_rel = x - x_centroid
        
        # Construct 2x2 matrix using the relative coordinates
        n = len(points_deck)
        # A * [a, b]^T = [Moment, Total Force]
        A = np.array([[np.sum(x_rel**2), np.sum(x_rel)],[np.sum(x_rel), n]])
        # B contains the Moment (Force * eccentricity) and the Total Force
        B = np.array([total_f*eh, total_f])

    # Solve for a (slope) and b (intercept/average force)
    a, b = np.linalg.solve(A,B)
  
    # Force at each point depends only on its y-coordinate
    Fv = a*y_rel + b
    
    return points_deck, Fv

def calculate_area_2D(coords):
    """
    Calculates 2D area using shoelace (Gauss) formula. coords is a list of tuples (x,y)
    """
    n = len(coords)
    area = 0.0
    for i in range(n):
        # Use module to wrap around to the first point at the end
        j = (i + 1) % n
        x_i, y_i = coords[i]
        x_j, y_j = coords[j]
        
        area += x_i*y_j
        area -= x_j*y_i
        
    return abs(area)/2.0
