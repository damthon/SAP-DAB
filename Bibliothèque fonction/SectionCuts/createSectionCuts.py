# -*- coding: utf-8 -*-
"""
Created on Tues Aug  29 15:56:54 2023

@author: hammad.eljisr
"""
import math
import numpy as np
import SectionCuts.Plane
import vg

def createSectionCutsSAP2000(SapModel,Group_name,points_path,SC_limits,SC_spacing):
    """
    This function adjusts the Y and Z coordinates of a tendon to follow a set of points along the longitudinal direction (X globally).
    Input:
        SapModel: SAP Model object
        Group_name: Name of the group to which section cut is applied
        Points: Points through which the centroid axis pass through. The first and last point correspond to the points passing through the initial tendon line.
        e.g.: In the case of a bridge deck, the points lie along the deck curvature. The first and last points correspond to the start and end of the deck
    """
    
    # SapModel.SetPresentUnits(6) # Unit system kN-m 
    


    # Group_name = 'All'  # Name of the groups in which the section cuts are made
    
    # points_path = ['6','27','12','29','30','31','32'] # Point labels that define the path along which the section cuts are made
    
    
    # SC_limits = [1e5,None,1e5] # Absolute value of the limit coordinates in the plane of the section cut [X,Y,Z] in mm; None if no limit is applied
    # SC_spacing = 400 # Section cut spacing [mm]


    """
    Create Cutting Planes
    """
    # Get point coordinates
    p_coord = []
    for i in range(len(points_path)):
        p_coord.append(SapModel.PointObj.GetCoordCartesian(points_path[i])[0:3])
        
    # Get vectors, length and segments between section cuts
    vectors = []
    vectors_len = []
    vectors_segments = []
    for i in range(len(points_path)-1):
        vectors.append(np.array(p_coord[i+1])-np.array(p_coord[i]))
        len_temp = round((vectors[i][0]**2 + vectors[i][1]**2 + vectors[i][2]**2)**0.5,0)
        vectors_len.append(len_temp)
        vectors_segments.append(math.floor(vectors_len[i]/SC_spacing))
        
    # Get points along each vector at which the planes are created
    points_planes = [[] for _ in range(len(vectors))]
    for i in range(len(vectors)):
        for j in range(vectors_segments[i]+1):
            s_temp = SC_spacing*j/vectors_len[i]
            p_temp = vectors[0]*s_temp + np.array(p_coord[i])
            points_planes[i].append(p_temp)
       
    # Create cutting planes  
    planes_cuts = []  
    for i in range(len(points_planes)):
        for j in range(len(points_planes[i])):
          planes_cuts.append(Plane.getPerpPlane(list(vectors[i]),points_planes[i][j]))
    
    """
    Get Bounding Points of Each Plane
    """
    # Intersection planes
    int_planes = [[] for _ in range(4)]
    for i in range(len(int_planes)):
        k = 0
        for j in range(len(SC_limits)):
            v = [0,0,0,0]
            if SC_limits[j] != None:
                k = k + 1
                v[j] = 1
                if i == 0:
                    v[3] = SC_limits[j]*(-1)**(k)
                elif i == 1:
                    v[3] = SC_limits[j]
                elif i == 2:
                    v[3] = SC_limits[j]*(-1)**(k+1)
                else:
                    v[3] = SC_limits[j]*(-1)
                int_planes[i].append(v)
    
    # Get bounding points for each cutting plane
    quad_points = [[] for _ in range(len(planes_cuts))]
    for i in range(len(planes_cuts)):
        for j in range(len(int_planes)):
            P1 = Plane(int_planes[j][0])
            P2 = Plane(int_planes[j][1])
            quad_points[i].append(planes_cuts[i].getIntPoint(P1,P2))
    
    """
    Create section cuts 
    """
    for i in range(len(planes_cuts)):
        x_quad = np.array(quad_points[i])[:,0]
        y_quad = np.array(quad_points[i])[:,1]
        z_quad = np.array(quad_points[i])[:,2]
        # Design slab section cut
        ret = SapModel.SectCut.SetByQuad(Group_name + '_SC_' + str(i) , Group_name, 4, list(x_quad),list(y_quad),list(z_quad))
        
    # Get angle between local axes 1 (normal to section) and global X-axis
    SC_angles = []
    X_vector = np.array([1,0,0])
    for i in range(len(points_planes)):
        for j in range(len(points_planes[i])):
            SC_angles.append(vg.signed_angle(X_vector,vectors[i],look=vg.basis.z))
    
    for i in range(len(planes_cuts)):
        SapModel.SectCut.SetLocalAxesAngleDesign(Group_name + '_SC_' + str(i), SC_angles[i])
    
    return planes_cuts, SC_angles





