# -*- coding: utf-8 -*-
"""
Created on Wed Aug  30 15:56:54 2023

@author: hammad.eljisr
"""

import numpy as np
import math

def bridgeTransverseCablesSAP2000(SapModel,Deck_points,tr_spacing,cable_coord,delta_offset,cable_prop):
    """
    This function creates the transverse prestressing cables along the deck of a bridge (profiles and section).
    Input:
        - SapModel: SAP Model object
        - Deck_points: Points along the centreline deck of the bridge. The first and last points correspond to the start and end of the deck. In the case of a box-girder section,
          the points are typically chosen at the center of the bottom flange. If the in-plane curve is severe, increase the number of points.
        - tr_spacing: Transverse spacing of the prestressing cables. tr_spacing = -1 if the cables are created at the deck points (excluding the last point)
        - cable_coord: Numpy array of the coordinates,x (longiudinal usually 0), y (vertical) and z (horizontal) of the transverse prestressing cable measured in the cross-section 
          from the reference Deck_points. Each element of the array is a list with the [x,y,z] coordinates
        - delta_offset: Offset from reference position specified by the deck points (delta_coord[0] = y, vertical offset; delta_coord[1] = z, horizontal offset])
        - cable_prop: List of cable properties (cable_prop[0] = Cable section name, cable_prop[1] = cable section area)
    Output: 
        - Tendon_objects_tr: List of the created transverse cables
    """
    
    # Cable properties
    cable_section = cable_prop[0]
    cable_area = cable_prop[1]
    
    # Coordinates of the points along the deck 
    x_points = []
    y_points = []
    z_points = []
    for i in range(len(Deck_points)):
        x_points.append(SapModel.PointObj.GetCoordCartesian(Deck_points[i])[0])
        y_points.append(SapModel.PointObj.GetCoordCartesian(Deck_points[i])[1])
        z_points.append(SapModel.PointObj.GetCoordCartesian(Deck_points[i])[2])
        
    # Transverse prestressing locations (along deck points)
    Tendon_cat_tr = len(Deck_points) - 1 # Tendon categories (number of deck regions or linear segements)
    l_deck_region = [] # Initialize length of the deck region in each category
    n_tr_region = [] # Initialize number of transverse cables in each catgeory
    x_tr_loc = [] # local x locations of the cables in each category
    # Get the locations for each deck region
    for i in range(Tendon_cat_tr):
        l_deck_region.append(((x_points[i]-x_points[i+1])**2 + (y_points[i]-y_points[i+1])**2 + (z_points[i]-z_points[i+1])**2)**0.5)
        if tr_spacing != -1:
            n_tr_region.append(math.floor(l_deck_region[i]/tr_spacing))
        else:
            n_tr_region = list(np.ones(Tendon_cat_tr))
        x_tr_loc.append(list(np.linspace(0,x_points[i+1]-x_points[i],int(n_tr_region[i]+1))))
    
    # Assign names based on category and location
    Tendon_names_tr = []
    for i in range(Tendon_cat_tr):
        for j in range(len(x_tr_loc[i])):
            if i < 10:
                pr = '00'
            elif i < 100:
                pr = '0'
            else:
                pr = ''
            Tendon_names_tr.append('PT_tr_' + pr + str(i) + '_' + str(round(x_tr_loc[i][j],2)))
        
    # Create tendon objects + properties
    Tendon_objects_tr = []
    n = 0
    for i in range(len(Tendon_names_tr)):
        SapModel.PropTendon.SetProp(cable_section, 'Tendon', 2, cable_area,255)
        # Create tendons
        m = int(Tendon_names_tr[i][6:9]) # Category
        if m!= 0:
            n = int(Tendon_names_tr[i-1][6:9]) # Category of previous tendon
            print('1')
        if m == n or tr_spacing == -1: # Do not add tendon when category (i.e., deck region changes) unless tendons are added at deck points (tr_spacing = -1)
            ret = SapModel.TendonObj.AddByPoint(Deck_points[m], Deck_points[m + 1], PropName = cable_section)
            Tendon_objects_tr.append(ret[0])
            print('2')
        else:
            Tendon_objects_tr.append(0)
            print('3')
        
    # Tendon coordinates
    x_PT_tr = []
    y_PT_tr= []
    z_PT_tr = []
    for i in range(Tendon_cat_tr):
        for j in range(len(x_tr_loc[i])):
            x_PT_tr.append(cable_coord[:,0] + x_tr_loc[i][j])
            y_PT_tr.append(cable_coord[:,1] + delta_offset[0]) 
            z_PT_tr.append(cable_coord[:,2] + delta_offset[1])
    
    # Set tendon profiles 
    SapModel.SetPresentUnits(6) # kN-m unit system
    for i in range(len(Tendon_names_tr)):
        n_control_points = int(len(x_PT_tr[i])) # Number of points to define the tendon profile
        type_control = np.ones(len(x_PT_tr[i]))*2
        type_control[0] = 1
        type_control = list(type_control)
        type_control = [int(x) for x in type_control]
        # Get local coordinates
        x = list(x_PT_tr[i])
        y = list(y_PT_tr[i])
        z = list(z_PT_tr[i])
        # Assign profile to tendon object (local coordinate system)
        if Tendon_objects_tr[i] != 0:
            SapModel.TendonObj.SetTendonData(Tendon_objects_tr[i], n_control_points, type_control, x, y, z, "Local") 
    
    return Tendon_objects_tr


