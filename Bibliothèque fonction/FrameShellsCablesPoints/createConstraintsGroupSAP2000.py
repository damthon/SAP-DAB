# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

import numpy as np
from FrameShellsCablesPoints.getGroupPointObjSAP2000 import getGroupPointObjSAP2000


def beamShellBodyConstraintsSAP2000(SapModel,shell_points,beam_points,h,b,n,connection_name):
    """
    This function creates body constraints between points of a beam and shell to simulate welding or fully composite connection.
    Each beam point is connected to at least 1 shell point to ensure no beam points are free, and at most n unique shell points to avoid over-constraint. 
    Input:
        - SapModel: SAP Model object
        - shell_points:  List of the shell point labels  e.g. ['s1','s2','s3','s4','s5'...]
        - beam_points:  List of the beam point labels  e.g. ['p1','p2','p3'...]. Points should be SORTED
        - h: Distance on each side of beam point perpendicular to the beam (usually beam_width/2)
        - b: Distance on each side of beam point parallel to the beam (tolerance for welding/connection zone along the beam) 
        - n: Maximum number of shell points connected to the beam
        - connection_name: Name of the connection, used to create constraintg. e.g. 'Weld_Beam_Stiffener'
    
    Output:
        - created_constraints: List of created constraints at each beam point e.g. ['Weld_Beam_Stiffener_12','Weld_Beam_Stiffener_25','Weld_Beam_Stiffener_80']
    """
    
    # Get beam and shell points coordinates
    shell_points_coord = []
    beam_points_coords = []
    for sh in shell_points:
        x = SapModel.PointObj.GetCoordCartesian(sh)[0]
        y = SapModel.PointObj.GetCoordCartesian(sh)[1]
        z = SapModel.PointObj.GetCoordCartesian(sh)[2]
        shell_points_coord.append((x,y,z))
    for bm in beam_points:
        x = SapModel.PointObj.GetCoordCartesian(bm)[0]
        y = SapModel.PointObj.GetCoordCartesian(bm)[1]
        z = SapModel.PointObj.GetCoordCartesian(bm)[2]
        beam_points_coords.append((x,y,z))
    
    # Mapped beam-shell points indices
    mapped_indices = map_indices_bounded_tolerance(shell_points_coord,beam_points_coords,h,b,n,[])
    
    # Create and assign constraints
    created_constraints = []
    for n in range(len(mapped_indices)):
        constraint_group = [beam_points[n]] + [shell_points[s] for s in mapped_indices[n]]
        constraint_name = connection_name + '_' + beam_points[n]
        SapModel.ConstraintDef.SetBody(constraint_name,[True,True,True,True,True,True])
        if len(set(constraint_group)) > 1: # Exclude lists with 1 element
            for p in constraint_group:
                SapModel.PointObj.SetConstraint(p,constraint_name)
            created_constraints.append(constraint_name)
        
    return created_constraints


def pointShellBodyConstraintsSAP2000(SapModel,shell_points,beam_point,h,b,n,vector_b,connection_name):
    """
    This function creates body constraints between 1 points of a beam/column and shell to simulate a fixed connection with no moment release
    The beam/column point is connected to at least 1 shell point, and at most n unique shell points to avoid over-constraint. 
    Input:
        - SapModel: SAP Model object
        - shell_points:  List of the shell point labels  e.g. ['s1','s2','s3','s4','s5'...]
        - beam_point:  Beam point label  e.g. 'p1'
        - h: Distance on each side of beam point perpendicular to the beam (usually beam_width/2)
        - b: Distance on each side of beam point parallel to the beam (tolerance for welding/connection zone along the beam) 
        - n: Maximum number of shell points connected to the beam
        - vector_b: Vector corresponding to direction along which shell points are constrained e.g. [(1,0,-1)] represents vector along pier depth
          The distance h is defined as perpendicular to this vector
        - connection_name: Name of the connection, used to create constraintg. e.g. 'Weld_Beam_Stiffener'
    
    Output:
        - constraint_name: Created constraints at the beam/column point e.g. 'Pier_1_deck'
    """
    
    # Get beam and shell points coordinates
    shell_points_coord = []
    beam_point_coords = []
    for sh in shell_points:
        x = SapModel.PointObj.GetCoordCartesian(sh)[0]
        y = SapModel.PointObj.GetCoordCartesian(sh)[1]
        z = SapModel.PointObj.GetCoordCartesian(sh)[2]
        shell_points_coord.append((x,y,z))

    x = SapModel.PointObj.GetCoordCartesian(beam_point)[0]
    y = SapModel.PointObj.GetCoordCartesian(beam_point)[1]
    z = SapModel.PointObj.GetCoordCartesian(beam_point)[2]
    beam_point_coords.append((x,y,z))
    
    # Mapped beam-shell points indices
    mapped_indices = map_indices_bounded_tolerance(shell_points_coord,beam_point_coords,h,b,n,vector_b)
    
    # Create and assign constraints
    constraint_group = [beam_point] + [shell_points[s] for s in mapped_indices[0]]
    constraint_name = connection_name + '_' + beam_point
    SapModel.ConstraintDef.SetBody(constraint_name,[True,True,True,True,True,True])
    if len(set(constraint_group)) > 1: # Exclude lists with 1 element
        for p in constraint_group:
            SapModel.PointObj.SetConstraint(p,constraint_name)
        
    return constraint_name


def jointBodyConstraintsGroupSAP2000(SapModel,Group,tolerance):
    """
    This function creates constraint between points in a group within a certain tolerance
    Input:
        SapModel: SAP Model object
        Group: Group of points
        tolerance: Specified tolerance in x, y or z respectively. e.g. [0.1,None,None] combines points within x = 0.1 m
    """
        
    # Get all points in the group
    points = getGroupPointObjSAP2000(SapModel,Group)
    
    # Get coordinates of points in the group
    x_p = []
    y_p = []
    z_p = []
    for p in points:
        x_p.append(SapModel.PointObj.GetCoordCartesian(p)[0])
        y_p.append(SapModel.PointObj.GetCoordCartesian(p)[1])
        z_p.append(SapModel.PointObj.GetCoordCartesian(p)[2])
    
    # Tolerance (within x, y or z coordinates)
    if tolerance[0] != None:
        t = tolerance[0]
        coord = x_p
    elif tolerance[1] != None:
        t = tolerance[1]
        coord = y_p
    else:
        t = tolerance[2]
        coord = z_p
        
    # Group points within the specified tolerance in separate lists
    grouped_indices = group_indices_within_tolerance(coord,t)
    grouped_points = []
    for i in range(len(grouped_indices)):
        grouped_points.append([points[j] for j in grouped_indices[i]])
            
    # Create and assign constraints
    for n in range(len(grouped_points)):
        for p in grouped_points[n]:
            if len(grouped_points[n]) > 1: # Exclude lists with 1 element
                SapModel.ConstraintDef.SetBody(Group + '_' + str(n),[True,True,True,True,True,True])
                SapModel.PointObj.SetConstraint(p,Group + '_' + str(n))
    
    return None


def map_indices_bounded_tolerance(shell_points_coord,beam_points_coords,h,b,n,vector_b):
    """
    This function maps the indices of a set of beam points to shell points.
    Each beam point is mapped to at least 1 shell point to ensure no beam coordinate are free, and at most n unique shell points.
    Input:
        - shell_points_coord: List of shell points coordinates [(x_s,y_s,z_s), ...]
        - beam_points_coords: List of beam points coordinates [(x_b,y_b,z_b), ...]. Should be sorted
        - h: Distance on each side of beam point perpendicular to the beam (usually beam_width/2)
        - b: Distance on each side of beam point parallel to the beam (tolerance for welding/connection zone along the beam) 
        - vector_b: List vectors at each beam point corresponding to direction along which shell points are mapped e.g. [(1,0,-1),(2,2,0)...].
          The distance h is defined as perpendicular to this vector
          If empty vector, default value calculated from consecutive beam coordinates is considered
        - n: Maximum number of shell points connected to the beam
   
    Output:
        - mapped_indices: Dictionary with indices of beams points and indices of mapped shell points 
    """

    # Convert point coordinates to array of lists
    s_points = np.array(shell_points_coord) 
    b_points = np.array(beam_points_coords) 
    
    all_points_groups = {i: [] for i in range(len(b_points))} # Grouped shell points coordinates for each beam point index
    
    # Calculate local beam axis vector
    for i in range(len(b_points)):
        if len(vector_b) == 0: # Empty vector direction, default vectors calculated
            if i == 0: 
                # First point: direction from first to second point
                aligned_vector = b_points[i+1] - b_points[i]
            elif i == len(b_points) - 1: 
                # Last point: reuse the direction of the previous segment
                aligned_vector = b_points[i] - b_points[i-1]
            else: 
                # Middle points: central difference between next and previous points
                aligned_vector = b_points[i+1] - b_points[i-1]
        else:
            aligned_vector = np.array(vector_b[i])  # Defined vector at each point

        v_par = aligned_vector/np.linalg.norm(aligned_vector) # Parallel vector
        
        # Check if shell point falls within distance
        b_coord = b_points[i]
        for s_idx, s_coord in enumerate(s_points):
            # Vector from beam node to shell node
            v = s_coord - b_coord
            
            # Project onto beam axis
            proj_parallel = np.dot(v,v_par)
            
            # Perpendicular vector component
            v_perp = v - proj_parallel*v_par
            proj_perp = np.linalg.norm(v_perp)
            
            # Check if shell node falls within the perpendicular strip and the parallel tolerance corridor
            if (proj_perp <= h) and (abs(proj_parallel) <= b):
                all_points_groups[i].append((s_idx,proj_perp)) # Track by perp distance for sorting
                
    # Conflict resolution and uniqueness
    shell_assignments = {} # Shell point index: beam point index, distance
    # Sort shell points with closest perp distance first for each beam point
    for b_idx in all_points_groups:
        all_points_groups[b_idx].sort(key=lambda x: x[1]) 
        
    for b_idx, candidates in all_points_groups.items():
        for s_idx, dist in candidates:
            if s_idx not in shell_assignments:
                shell_assignments[s_idx] = (b_idx,dist)
            else:
                existing_b_idx, existing_dist = shell_assignments[s_idx]
                if dist < existing_dist:
                    shell_assignments[s_idx] = (b_idx,dist) # Beam point index, perpendicular distance
     
    # Filter shell points to n points connected to each beam point
    mapped_indices = {i: [] for i in range(len(beam_points_coords))} # Filtered shell point groups for each beam point index
    for s_idx, (b_idx, dist) in shell_assignments.items():
        # Only append if we have collected fewer than 'n' items for this specific b_idx
        if len(mapped_indices[b_idx]) < n:
            mapped_indices[b_idx].append(s_idx)
     
    # Fallback to ensure no beam node is left completely disconnected, i.e. at least 1 shell point is grouped with a beam node
    for b_idx, assigned_shells in mapped_indices.items():
        if not assigned_shells:
            distances = np.linalg.norm(s_points - b_points[b_idx], axis=1)
            closest_s_idx = np.argmin(distances)
            mapped_indices[b_idx].append(closest_s_idx)

    return mapped_indices


def group_indices_within_tolerance(numbers,t):
    """
    This function groups the indices of a set of numbers in a list wihin a specified toleranance together in separate lists
    Input:
        numbers: List of numbers
        t: Tolerance within which the numbers are grouped together in separate lists
   
    Output:
        grouped_indices: List of lists containing the grouped indices from the numbers list
    """
    
    grouped_indices = []
    visited_indices = set()

    for i in range(len(numbers)):
        if i not in visited_indices:
            current_group = [i]
            visited_indices.add(i)
            
            for j in range(i + 1, len(numbers)):
                if j not in visited_indices and abs(numbers[i] - numbers[j]) <= t:
                    current_group.append(j)
                    visited_indices.add(j)
            
            grouped_indices.append(current_group)
    
    return grouped_indices

            
