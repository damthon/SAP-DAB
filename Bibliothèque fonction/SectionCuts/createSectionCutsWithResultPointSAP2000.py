# -*- coding: utf-8 -*-
"""
Created on Tues Aug  29 15:56:54 2023

@author: hammad.eljisr
"""
import math
import numpy as np
from Plane import Plane
import vg
from getCenterGravity import compute_cg_from_plane

def createSectionCutsSAP2000(SapModel,Group_name,Points_path,Z_axis,SC_limits,SC_spacing):
    """
    This function creates section cuts 
    Input:
        SapModel: SAP Model object
        Group_name: Name of the group to which section cut is applied
        Points_path: Point labels that define the path along which the section cuts are made (e.g. ['200',53','13'...]) OR list of point coordinates (e.g. [[0,1,1],[1,2,-5]...])
        e.g.: In the case of a bridge deck, the points lie along the deck curvature. The first and last points correspond to the start and end of the deck
        Z_axis = 1 if global z-axis is parallel to local axis 1 (e.g. walls, pylons) global x-axis parallel to local axis 2, 2 if global z-axis is parallel to local axis 2 (e.g. slabs, decks)
        SC_limits: Absolute value of the limit coordinates in the plane of the section cut [X,Y,Z] in mm; None if no limit is applied
        SC_spacing: Section cut spacing    
        
    Output:
        plane_cuts : section cut planes
        SC_angles: angle between local axes 1 (normal to section) and global X-axis
        cut_names: name of the section cuts
    """ 
    
    """
    Create Cutting Planes
    """
    p_coord = [[] for _ in range(len(Points_path))]
    # Get point coordinates
    for i in range(len(Points_path)):
        if isinstance(Points_path[i],str) == True:
            p_coord[i] = SapModel.PointObj.GetCoordCartesian(Points_path[i])[0:3]
        else:
            p_coord[i] = Points_path[i]
        
    # Get vectors, length and segments between section cuts
    vectors = []
    vectors_len = []
    vectors_segments = []
    for i in range(len(Points_path)-1):
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
        k = 1
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
        ret = SapModel.SectCut.SetByQuad(Group_name + '_SC_' + str(i) , Group_name, 2*Z_axis, list(x_quad),list(y_quad),list(z_quad))
        
    SC_angles = []
    for i in range(len(points_planes)):
        for j in range(len(points_planes[i])):
            if np.linalg.norm(np.cross(vectors[i],vg.basis.z)) != 0: # Vector not parallel to z-axis
            # Get angle from global X-axis to local axes 1 (normal to section) 
                X_vector = np.array([1,0,0])
                SC_angles.append(vg.signed_angle(X_vector,vectors[i],look=vg.basis.z))
            else:
            # Set angle from global X-axis to local axes 2 to zero
                SC_angles.append(0)
    
    cut_names = []
    for i in range(len(planes_cuts)):
        SapModel.SectCut.SetLocalAxesAngleDesign(Group_name + '_SC_' + str(i), SC_angles[i])
        cut_names.append(Group_name + '_SC_' + str(i))

        # Set the results location
        xcg,ycg,zcg = compute_cg_from_plane(SapModel,Group_name,planes_cuts[i]) 
        SapModel.SectCut.SetResultLocation(cut_names[i],False,xcg,ycg,zcg)
    
    return planes_cuts , SC_angles, cut_names
