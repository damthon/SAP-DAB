# -*- coding: utf-8 -*-
"""
Created on Tues Aug  29 15:56:54 2023

@author: hammad.eljisr
"""
import math
import numpy as np
from SectionCuts.Plane import Plane
import vg
 
def bridgeDeckSectionCutsSAP2000(SapModel,Deck_group,Points_path,Force_locations_bool,Delta_location,SC_spacing):
    """
    This function creates section cuts along a path of bridge deck at a defined spacing. Section cuts at start and end of path are also created.
    Input:
        SapModel: SAP Model object
        Deck_group: Name of the deck group to which section cut is applied
        Points_path: Point labels that define the path along which the section cuts are made (e.g. ['200',53','13'...]) OR list of point coordinates (e.g. [[0,1,1],[1,2,-5]...])
        Force_locations_bool: 1 if forces are calculated about the points along the specified path, 0 if the forces are calculated about the default section cut points
        Delta_location: The global delta [dX,dY,dZ] from the specified location about which the forces are calculated 
        SC_spacing: Section cut spacing   
        
    Output:
        plane_cuts : section cut planes
        SC_angles: angle between local axes 1 (normal to section) and global X-axis
        cut_names: name of the section cuts
    """ 
    
    # Units 
    ret = SapModel.SetPresentUnits(6)  # kN-m unit system
    
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
    
    # Get stations along path
    stations = [0]
    for i in range(len(p_coord)-1):
        st = ((p_coord[i+1][0] - p_coord[i][0])**2 + (p_coord[i+1][1] - p_coord[i][1])**2 + (p_coord[i+1][2] - p_coord[i][2])**2)**0.5 + stations[i]
        stations.append(st)
    path_length = stations[-1] - stations[0]
    
    # Get target stations at which section cuts are made
    n_div = int(path_length/SC_spacing)
    target_stations = list(np.linspace(stations[0],n_div*SC_spacing,n_div+1))
    if target_stations[-1] != stations[-1]: # Add end station
        target_stations.append(stations[-1])
    
    # Get vectors perpendicular to plane at section and points along each vector at which the planes are created
    v0 = list(np.array(p_coord[1]) - np.array(p_coord[0])) # Initial plane vector
    v0 = v0/np.linalg.norm(v0)
    vectors = [v0]
    for s in range(1,len(target_stations)-1):
        in_1 = sum(target_stations[s]>np.array(stations))-1
        in_2 = in_1 + 1 + sum(target_stations[s]==np.array(stations))
        v = list(np.array(p_coord[in_2]) - np.array(p_coord[in_1]))
        vectors.append(v/np.linalg.norm(v))
    vf = list(np.array(p_coord[-1]) - np.array(p_coord[-2])) # Final plane vector 
    vf = vf/np.linalg.norm(vf)
    vectors.append(vf)
    
    # Get points along each vector at which the planes are created
    x_pt = np.interp(target_stations,stations,np.transpose(p_coord)[0])
    y_pt = np.interp(target_stations,stations,np.transpose(p_coord)[1])
    z_pt = np.interp(target_stations,stations,np.transpose(p_coord)[2])
    points_planes = np.transpose([x_pt,y_pt,z_pt])
      
    # Create cutting planes  
    planes_cuts = []  
    for i in range(len(points_planes)):
        planes_cuts.append(Plane.getPerpPlane(list(vectors[i]),points_planes[i]))
    
    """
    Get Angles Between Normal Vector and X-axis
    """
    SC_angles = []
    X_vector = np.array([1,0,0])
    for i in range(len(points_planes)):
        # Get angle in degrees from global X-axis to local axes 1 (normal to section) 
        SC_angles.append(vg.signed_angle(X_vector,vectors[i],look=vg.basis.z))
    
    """
    Get Bounding Points of Each Plane
    """
    # Get absolute value of the limit coordinates in the plane of the section cut [X,Y,Z] in mm; None if no limit is applied
    for a in SC_angles:
        if abs(a) < 90:
            SC_limits = [None,100,100]
        else:
            SC_limits = [100,None,100]  
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
    force_locations = points_planes
        
    for i in range(len(planes_cuts)):
        x_quad = np.array(quad_points[i])[:,0]
        y_quad = np.array(quad_points[i])[:,1]
        z_quad = np.array(quad_points[i])[:,2]
        # Design slab section cut
        ret = SapModel.SectCut.SetByQuad(Deck_group + '_SC_' + str(i),Deck_group,4,list(x_quad),list(y_quad),list(z_quad))
        if Force_locations_bool == 1:
            SapModel.SectCut.SetResultLocation(Deck_group + '_SC_' + str(i),False,force_locations[i][0]+Delta_location[0],force_locations[i][1]+Delta_location[1],force_locations[i][2]+Delta_location[2])
         
    cut_names = []
    for i in range(len(planes_cuts)):
        SapModel.SectCut.SetLocalAxesAngleDesign(Deck_group + '_SC_' + str(i), SC_angles[i])
        cut_names.append(Deck_group + '_SC_' + str(i))

        
    return planes_cuts, SC_angles, cut_names
