# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 13:57:31 2025

@author: hammad.eljisr
"""

import math
import numpy as np
import heapq

def getSectionSlabPoints(SapModel,deck_sec):
    """
    This function obtains the height and slope of a deck section
    Input:
        SapModel: SAP Model object 
        deck_sec: Deck section
  
    Output:
        top_slab_points: Top slab points
        bott_slab_points: Bottom slab points
    """   
    
    SapModel.PropFrame.GetSDSection(deck_sec)
    n_polygons = len(SapModel.PropFrame.GetSDSection(deck_sec)[2])
    for i in range(n_polygons):
        if SapModel.PropFrame.GetSDSection(deck_sec)[2][i] == 'Box':
            # Coordinates around the perimeter
            x_coordinates = [round(x,3) for x in SapModel.PropFrame.SDShape.GetPolygon(deck_sec,SapModel.PropFrame.GetSDSection(deck_sec)[2][i])[3]]
            y_coordinates = [round(y,3) for y in SapModel.PropFrame.SDShape.GetPolygon(deck_sec,SapModel.PropFrame.GetSDSection(deck_sec)[2][i])[4]]
            # Top slab top coordinates
            x_top_slab_1 = min(x_coordinates)
            y_top_slab_1 = 0
            for x_i in range(len(x_coordinates)):
                if x_coordinates[x_i] == x_top_slab_1:
                    y_top_slab_1 = max(y_coordinates[x_i],y_top_slab_1)
            x_top_slab_2 = max(x_coordinates)                             
            y_top_slab_2 = 0
            for x_i in range(len(x_coordinates)):
                if x_coordinates[x_i] == x_top_slab_2:
                    y_top_slab_2 = max(y_coordinates[x_i],y_top_slab_2) 
            slope_sec =  (y_top_slab_2 - y_top_slab_1) / (x_top_slab_2 - x_top_slab_1)   
            # Bottom slab
            x_bott_slab_1 = heapq.nsmallest(4, x_coordinates)[-1] #  4th smallest coordinate
            y_bott_slab_1 = 0
            for x_i in range(len(x_coordinates)):
                if x_coordinates[x_i] == x_bott_slab_1:
                    y_bott_slab_1 = max(y_coordinates[x_i],y_bott_slab_1)
            x_bott_slab_2 = heapq.nlargest(4, x_coordinates)[-1] # 4th largest coordinate
            y_bott_slab_2 = 0
            for x_i in range(len(x_coordinates)):
                if x_coordinates[x_i] == x_bott_slab_2:
                    y_bott_slab_2 = max(y_coordinates[x_i],y_bott_slab_2)
            top_slab_points = [(x_top_slab_1,y_top_slab_1),(x_top_slab_2,y_top_slab_2)]
            bott_slab_points = [(x_bott_slab_1,y_bott_slab_1),(x_bott_slab_2,y_bott_slab_2)]
    
    return top_slab_points, bott_slab_points

def angle_from_center(point, center):
    """
    This function finds the angle of a point on a polygon from the center
    Input:
        point: Point
        center: Center of polygon
  
    Output:
        angle: Point angle from center
    """  
    dx = point[0] - center[0]
    dy = point[1] - center[1]
    angle = math.atan2(dy, dx)
    return angle

def sort_clockwise(points, start_point):
    """
    This function sorts a list of points of a polygon in clockwise ordering starting from a specified point on the polygon
    Input:
        points: Polygon points
        start_point: Starting point
  
    Output:
        sorted_points: Sorted points
    """  
    if start_point not in points:
        raise ValueError("Start point must be one of the polygon vertices")

    # Calculate the centroid of the polygon (for angle reference)
    center_x = sum(p[0] for p in points) / len(points)
    center_y = sum(p[1] for p in points) / len(points)
    center = (center_x, center_y)

    # Sort points by angle (clockwise)
    sorted_points = sorted(points, key=lambda p: -angle_from_center(p, center))

    # Rotate list so it starts from the given start_point
    start_index = sorted_points.index(start_point)
    sorted_points = sorted_points[start_index:] + sorted_points[:start_index]

    return sorted_points

def getInterpSection(SapModel,deck_sections,x_relative,output_name):
    """
    This function creates a linearly interpolated section between two sections of similar shape (box girder with number of openings). The relative distance 
    from first section is specified and the section is interpolated at this location. The maximum number of opening should not be greater than 2.
    Input: 
        SapModel: SAP Model object 
        deck_sections: Deck sections between which the section is interpolated e.g. ['Sec-1','Sec-2'] sections 'Sec-1' and 'Sec-2'
        x_relative: The relative distance from the first section 'Sec-1'
        output_name: Name of the interpolated section created in the SAP model
    """  
    
    # Deck sections between which the interpolation is conducted
    deck_sec_1 = deck_sections[0]
    deck_sec_2 = deck_sections[1]
    
    # Get polygons for each deck section
    polygons_sec_1 = SapModel.PropFrame.GetSDSection(deck_sec_1)[2]
    polygons_sec_2 = SapModel.PropFrame.GetSDSection(deck_sec_2)[2]
   
    # Get material properties for the box section 
    box_material = SapModel.PropFrame.SDShape.GetPolygon(deck_sec_1,'Box')[0]
    # Create material for the openings
    SapModel.PropMaterial.SetMaterial('Open',3)
    SapModel.PropMaterial.SetMPIsotropic('Open',0,0,0)
    SapModel.PropMaterial.SetWeightAndMass('Open',1,0)
    
    # Box coordinates
    index_box_1 = polygons_sec_1.index('Box')
    index_box_2 = polygons_sec_2.index('Box')
    B_1 = SapModel.PropFrame.SDShape.GetPolygon(deck_sec_1,SapModel.PropFrame.GetSDSection(deck_sec_1)[2][index_box_1])[3:5]
    B_2 = SapModel.PropFrame.SDShape.GetPolygon(deck_sec_2,SapModel.PropFrame.GetSDSection(deck_sec_2)[2][index_box_2])[3:5]
    B_1_points = [] # Box 1 points
    for i in range(len(B_1[0])):
        x = round(B_1[0][i],3)
        y = round(B_1[1][i],3)
        B_1_points.append((x,y))      
    # Sort polygon 
    B_1_start = getSectionSlabPoints(SapModel,deck_sec_1)[0][0]
    B_1_points_sorted = sort_clockwise(list(set(B_1_points)),B_1_start)
    
    B_2_points = [] # Box 2 points
    for i in range(len(B_2[0])):
        x = round(B_2[0][i],3)
        y = round(B_2[1][i],3)
        B_2_points.append((x,y))      
    # Sort polygon 
    B_2_start = getSectionSlabPoints(SapModel,deck_sec_2)[0][0]
    B_2_points_sorted = sort_clockwise(list(set(B_2_points)), B_2_start)
    
    # Opening coordinates (if present)
    if 'O1' in polygons_sec_1:
        index_O1_1 = polygons_sec_1.index('O1')
        index_O1_2 = polygons_sec_2.index('O1')
        O1_1 = SapModel.PropFrame.SDShape.GetPolygon(deck_sec_1,SapModel.PropFrame.GetSDSection(deck_sec_1)[2][index_O1_1])[3:5]
        O1_2 = SapModel.PropFrame.SDShape.GetPolygon(deck_sec_2,SapModel.PropFrame.GetSDSection(deck_sec_2)[2][index_O1_2])[3:5]
        O1_1_points = [] # Opening 1 points
        for i in range(len(O1_1[0])):
            x = round(O1_1[0][i],3)
            y = round(O1_1[1][i],3)
            O1_1_points.append((x,y))      
        # Sort polygon 
        # Get start point (closest to top slab p1)
        dis = 10e10
        for i in range(len(O1_1_points)):
            p1 = getSectionSlabPoints(SapModel,deck_sec_1)[0][0]
            p2 = O1_1_points[i]
            if math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) < dis:
                dis = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
                index_start = i   
        O1_1_start = O1_1_points[index_start]
        O1_1_points_sorted = sort_clockwise(list(set(O1_1_points)), O1_1_start)
        
        O1_2_points = [] # Opening 2 points
        for i in range(len(O1_2[0])):
            x = round(O1_2[0][i],3)
            y = round(O1_2[1][i],3)
            O1_2_points.append((x,y))      
        # Sort polygon 
        # Get start point (closest to top slab p1)
        dis = 10e10
        for i in range(len(O1_2_points)):
            p1 = getSectionSlabPoints(SapModel,deck_sec_2)[0][0]
            p2 = O1_2_points[i]
            if math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) < dis:
                dis = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
                index_start = i   
        O1_2_start = O1_2_points[index_start]
        O1_2_points_sorted = sort_clockwise(list(set(O1_2_points)), O1_2_start)
        
    # Opening coordinates (if present)
    if 'O2' in polygons_sec_1:
        index_O2_1 = polygons_sec_1.index('O2')
        index_O2_2 = polygons_sec_2.index('O2')
        O2_1 = SapModel.PropFrame.SDShape.GetPolygon(deck_sec_1,SapModel.PropFrame.GetSDSection(deck_sec_1)[2][index_O2_1])[3:5]
        O2_2 = SapModel.PropFrame.SDShape.GetPolygon(deck_sec_2,SapModel.PropFrame.GetSDSection(deck_sec_2)[2][index_O2_2])[3:5]
        O2_1_points = [] # Opening 1 points
        for i in range(len(O2_1[0])):
            x = round(O2_1[0][i],3)
            y = round(O2_1[1][i],3)
            O2_1_points.append((x,y))      
        # Sort polygon 
        # Get start point (closest to top slab p1)
        dis = 10e10
        for i in range(len(O2_1_points)):
            p1 = getSectionSlabPoints(SapModel,deck_sec_1)[0][0]
            p2 = O2_1_points[i]
            if math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) < dis:
                dis = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
                index_start = i   
        O2_1_start = O2_1_points[index_start]
        O2_1_points_sorted = sort_clockwise(list(set(O2_1_points)), O2_1_start)
        
        O2_2_points = [] # Opening 2 points
        for i in range(len(O2_2[0])):
            x = round(O2_2[0][i],3)
            y = round(O2_2[1][i],3)
            O2_2_points.append((x,y))      
        # Sort polygon 
        # Get start point (closest to top slab p1)
        dis = 10e10
        for i in range(len(O2_2_points)):
            p1 = getSectionSlabPoints(deck_sec_2)[0][0]
            p2 = O2_2_points[i]
            if math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) < dis:
                dis = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
                index_start = i   
        O2_2_start = O2_2_points[index_start]
        O2_2_points_sorted = sort_clockwise(list(set(O2_2_points)), O2_2_start)
       
    # Set origin in middle of top slab and transform all coordinates
    # Deck section 1
    top_slab_mp_1 = (np.array(getSectionSlabPoints(SapModel,deck_sec_1)[0][0]) + np.array(getSectionSlabPoints(SapModel,deck_sec_1)[0][1]))/2
    delta_x_1 = -top_slab_mp_1[0]
    delta_y_1 = -top_slab_mp_1[1]
    # Deck section 2
    top_slab_mp_2 = (np.array(getSectionSlabPoints(SapModel,deck_sec_2)[0][0]) + np.array(getSectionSlabPoints(SapModel,deck_sec_2)[0][1]))/2
    delta_x_2 = -top_slab_mp_2[0]
    delta_y_2 = -top_slab_mp_2[1]
    
    # Transform all points
    B_1_points_trans = []
    for b in range(len(B_1_points_sorted)):
       x_pt = round(B_1_points_sorted[b][0] + delta_x_1,4)
       y_pt = round(B_1_points_sorted[b][1] + delta_y_1,4)
       B_1_points_trans.append((x_pt,y_pt))
    B_2_points_trans = []
    for b in range(len(B_2_points_sorted)):
       x_pt = round(B_2_points_sorted[b][0] + delta_x_2,4)
       y_pt = round(B_2_points_sorted[b][1] + delta_y_2,4)
       B_2_points_trans.append((x_pt,y_pt))
     
    if 'O1' in polygons_sec_1:
        O1_1_points_trans = []
        for b in range(len(O1_1_points_sorted)):
           x_pt = round(O1_1_points_sorted[b][0] + delta_x_1,4)
           y_pt = round(O1_1_points_sorted[b][1] + delta_y_1,4)
           O1_1_points_trans.append((x_pt,y_pt))
        O1_2_points_trans = []
        for b in range(len(O1_2_points_sorted)):
           x_pt = round(O1_2_points_sorted[b][0] + delta_x_2,4)
           y_pt = round(O1_2_points_sorted[b][1] + delta_y_2,4)
           O1_2_points_trans.append((x_pt,y_pt))
     
    if 'O2' in polygons_sec_1:
        O2_1_points_trans = []
        for b in range(len(O2_1_points_sorted)):
           x_pt = round(O2_1_points_sorted[b][0] + delta_x_1,4)
           y_pt = round(O2_1_points_sorted[b][1] + delta_y_1,4)
           O2_1_points_trans.append((x_pt,y_pt))
        O2_2_points_trans = []
        for b in range(len(O2_2_points_sorted)):
           x_pt = round(O2_2_points_sorted[b][0] + delta_x_2,4)
           y_pt = round(O2_2_points_sorted[b][1] + delta_y_2,4)
           O2_2_points_trans.append((x_pt,y_pt))
   
    # Interpolated section
    B_new_points = []
    if 'O1' in polygons_sec_1:
        O1_new_points = [] 
    if 'O2' in polygons_sec_1:
        O2_new_points = [] 
   
    # Get coordinates of the polygons
    # Box
    a = 1- x_relative
    b = x_relative
    for i in range(len(B_1_points_trans)):
        x_interp = B_1_points_trans[i][0]*a + B_2_points_trans[i][0]*b
        y_interp = B_1_points_trans[i][1]*a + B_2_points_trans[i][1]*b
        B_new_points.append((x_interp,y_interp))
    if 'O1' in polygons_sec_1:
        for i in range(len(O1_1_points_trans)):
            x_interp = O1_1_points_trans[i][0]*a + O1_2_points_trans[i][0]*b
            y_interp = O1_1_points_trans[i][1]*a + O1_2_points_trans[i][1]*b
            O1_new_points.append((x_interp,y_interp))   
    if 'O2' in polygons_sec_1:
        for i in range(len(O2_1_points_trans)):
            x_interp = O2_1_points_trans[i][0]*a + O2_2_points_trans[i][0]*b
            y_interp = O2_1_points_trans[i][1]*a + O2_2_points_trans[i][1]*b
            O2_new_points.append((x_interp,y_interp))   
    
    # Create SD section
    Deck_section_interp = output_name
    SapModel.PropFrame.SetSDSection(Deck_section_interp,box_material,0,255)
    
    # Polygons x and y coordinates
    B_new_points_x = []
    B_new_points_y = []
    for i in range(len(B_new_points)):
        B_new_points_x.append(B_new_points[i][0])
        B_new_points_y.append(B_new_points[i][1])
    B_new_points_x = tuple(B_new_points_x)
    B_new_points_y = tuple(B_new_points_y)
    if 'O1' in polygons_sec_1:
        O1_new_points_x = []
        O1_new_points_y = []
        for i in range(len(O1_new_points)):
            O1_new_points_x.append(O1_new_points[i][0])
            O1_new_points_y.append(O1_new_points[i][1])
        O1_new_points_x = tuple(O1_new_points_x)
        O1_new_points_y = tuple(O1_new_points_y)
    if 'O2' in polygons_sec_1:
        O2_new_points_x = []
        O2_new_points_y = []
        for i in range(len(O2_new_points)):
            O2_new_points_x.append(O2_new_points[i][0])
            O2_new_points_y.append(O2_new_points[i][1])
        O2_new_points_x = tuple(O2_new_points_x)
        O2_new_points_y = tuple(O2_new_points_y)
            
    # Create section polygons
    # Box
    SapModel.PropFrame.SDShape.SetPolygon(Deck_section_interp,'Box',box_material,'Default',len(B_new_points), B_new_points_x, 
                                                 B_new_points_y,tuple(np.zeros(len(B_new_points))),65280,False)
    # Opening 1
    if 'O1' in polygons_sec_1:
        SapModel.PropFrame.SDShape.SetPolygon(Deck_section_interp,'O1','Open','Default',len(O1_new_points), O1_new_points_x, 
                                                O1_new_points_y,tuple(np.zeros(len(O1_new_points))),16777215)
    # Opening 2
    if 'O2' in polygons_sec_1:
        SapModel.PropFrame.SDShape.SetPolygon(Deck_section_interp,'O2','Open','Default',len(O2_new_points), O2_new_points_x, 
                                                O2_new_points_y,tuple(np.zeros(len(O2_new_points))),16777215)
    return