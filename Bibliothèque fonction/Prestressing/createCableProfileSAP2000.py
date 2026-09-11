# -*- coding: utf-8 -*-
"""
Created on Thu May  28 15:56:54 2026

@author: hammad.eljisr
"""

import numpy as np
import math
from getOffsetPoints import getOffsetPoints

def createCableProfileSAP2000(SapModel,stations_cl,proj_line_coord,plane_angle,cable_stations,cable_dz,segments_type,radii,add_points,accuracy):
    """
    This function creates the profile of a prestressing cable in  a deck
    Input:
        - SapModel: SAP Model object
        - stations_cl: Deck centerline stations
        - proj_line_coord: List of points coordinates corresponding to cable projected on deck [(x1,y1,z1),(x2,y2,z2)...]. Add points to ensure meshing at certain locations (e.g. piers)
        - plane_angle: Cable plane angle measured clockwise from the vertical z-axis in degrees
        - cable_stations: Stations at reference points of the cable in elavation view
        - cable_dz: Delta elevation at reference points of the cable in elavation view measured from projected line on the deck
        - segment_types: Type of segment, 'L' for linear and 'A' for arc
        - radii: Radius of each segment 0 if linear, R = value if arc
        - add_points: List containing boolean and group name, e.g. [1,'Cable-1'] 
          Boolean to create points in SAP2000, 1 or 0, group name is the name of the group with points
        - accuracy: Number of decimal places for calculating stations (1 recommended for 10th digit m, -2 for 100s digit mm)
    Output:
        - cable_coords: List of cable points coordinates e.g. [(x1,y1,z1),(x2,y2,z2)...]
        - cable_points: List of cable points created in the SAP2000 model 
        - delta_offsets_z: Cable data offsets in vertical direction
    """

    ######################
    ###### ELEVATION VIEW ###### 
    ####################### 
    stations_cl = [round(s,accuracy) for s in stations_cl] # Round to decimal places
    # Get elevation
    elevations_pl = [c[2] for c in proj_line_coord] # Projected line elevation 
    
    # Trim to cable stations
    start_station = sum(np.array(stations_cl) < cable_stations[0])
    end_station = len(stations_cl) - sum(np.array(stations_cl) > cable_stations[-1])
    stations_cl = stations_cl[start_station:end_station]
    elevations_pl = elevations_pl[start_station:end_station]
    proj_line_coord = proj_line_coord[start_station:end_station]
    
    ######################
    ###### CABLE COORDINATES ###### 
    #######################
    # Get absolute s,z coordinates of the reference points in elevation view
    elevations_cable = np.interp(cable_stations,stations_cl,elevations_pl) # Elevation at cable reference points
    cable_z = elevations_cable + np.array(cable_dz)
    cable_points = [(cable_stations[i],cable_z[i]) for i in range(len(cable_stations))]
    cable_coords_sz = generateCableCoordinatesElevation(cable_points,segments_type,radii,10**(1-accuracy)*0.2) # Cable coordinates in each segment
    cable_coords_sz_all = np.vstack(cable_coords_sz) # Combine all segments
    # Get coordinates at stations
    cable_coords_s = [c[0] for c in cable_coords_sz_all]
    cable_coords_z = [c[1] for c in cable_coords_sz_all]
    cable_coords_interp = np.interp(stations_cl,cable_coords_s,cable_coords_z)
    # Get delta vertical offsets, z direction
    delta_offsets_z = []
    for i in range(len(cable_coords_interp)):
        delta_offsets_z.append((cable_coords_interp[i] - elevations_pl[i])/math.cos(math.radians(plane_angle)))
        
    # Get absolute x,y,z coordinates of the cable by offseting projected line along plane
    # Get plane normals
    nx = 0
    ny = 1
    nz = math.tan(math.radians(plane_angle))
    normal = np.array([nx,ny,nz])
    plane_normal = normal/np.linalg.norm(normal) 
    plane_normals = np.tile(plane_normal,(len(cable_coords_interp),1))
    
    # Cable points coord obtained by offseting projected lin
    cable_coords = getOffsetPoints(proj_line_coord,delta_offsets_z,plane_normals)

    # Create cable points
    cable_points = []
    if add_points[0] == 1:
        for i in range(len(cable_coords)):
            pt = SapModel.PointObj.AddCartesian(cable_coords[i][0],cable_coords[i][1],cable_coords[i][2])
            cable_points.append(pt[0])
        # Add points to group
        SapModel.GroupDef.SetGroup(add_points[1])
        for p in cable_points:
            SapModel.PointObj.SetGroupAssign(p,add_points[1])
        
    return cable_coords,cable_points,delta_offsets_z

     
def generateCableCoordinatesElevation(cable_points,segment_types,radii,div):
    """
    This function generates cable coordinates in elavation view using mixed linear and arc segments.
    Input:
        - cable_points: List of reference points coordinates of the cable in elavation view [(s1,z1),(s2,z2)...]
        - segment_types: Type of segment, 'L' for linear and 'A' for arc
        - radii: Radius of each segment 0 if linear, R = value if arc
        - div: Cable discretization length
    
    Output:
        - cable_coords: List of all points coordinates of the cable in elavation view [(s1,y1),(s2,y2)...]
    """
    
    points = np.array(cable_points, dtype=float)
    num_segments = len(segment_types)
    cable_coords = []
    
    for i in range(num_segments):
        p1 = points[i]      # Segment start
        p2 = points[i+1]    # Segment end
        
        # Track endpoint options to prevent duplicate stitched points
        is_last_seg = (i == num_segments - 1)
        endpoint_option = is_last_seg
        
        if segment_types[i] == 'L':
            # Linear interpolation 
            num_points = int(abs(p2[0] - p1[0])/div)+1 # Number of divisions
            seg_points = np.linspace(p1,p2,num=num_points,endpoint=endpoint_option)
            seg_points = [tuple(s) for s in seg_points]
            cable_coords.append(seg_points)
            
        elif segment_types[i] == 'A':
            # Tangent arc segment interpolation
            R = float(radii[i])
            
            # Get incoming line direction (tangent vector at start of arc)
            if i > 0: 
                u_incoming = (points[i] - points[i-1])
                u_incoming /= np.linalg.norm(u_incoming) # Unit vector
            else: # If first segment, use the arc chord direction as a fallback
                chord = p2 - p1
                u_incoming = chord/np.linalg.norm(chord) # Unit vector
                
            # Get outgoing line direction (tangent vector at end of arc)
            if i < num_segments - 1:
                u_outgoing = (points[i+1] - points[i])
                u_outgoing /= np.linalg.norm(u_outgoing)
            else: # If last segment, use the arc chord direction as a fallback
                chord = p2 - p1
                u_outgoing = chord/np.linalg.norm(chord)
            
            
            # Calculate center using normal directions
            # The normal vector of a tangent line points directly toward the circle center.
            # For 2D right-hand system normal: (-y, x)
            n_start = np.array([-u_incoming[1],u_incoming[0]])
            
            # Chord midpoint and length
            chord_mid = (p1 + p2)/2.0
            chord_len = np.linalg.norm(p2 - p1)
            
            if chord_len > 2*R:
                raise ValueError(f"Arc segment {i} span ({chord_len:.2f}) exceeds diameter ({2*R}).")
            
            # Distance from chord midpoint to circle center (Pythagorean theorem)
            h = np.sqrt(R**2 - (chord_len/2.0)**2) 
            
            # The perpendicular direction away from the chord
            chord_dir = (p2 - p1)/chord_len
            perp_dir = np.array([-chord_dir[1],chord_dir[0]])
            
            # Flip based on  concavity
            turn_direction = u_incoming[0]*u_outgoing[1] - u_incoming[1]*u_outgoing[0]
            if turn_direction > 0: # Concave up, center must go ABOVE or LEFT
                if np.dot(perp_dir, n_start) < 0:
                    perp_dir = -perp_dir
            else: # Concave down, center must go below or right
                if np.dot(perp_dir, n_start) >= 0:
                    perp_dir = -perp_dir
            
            center = chord_mid + perp_dir*h
            
            # Generate angular sweep from center to p1 and p2
            v_start = p1 - center # Vector from start point to center
            v_end = p2 - center # Vector from end point to center
            
            # Compute absolute angles relative to the center
            angle_start = np.arctan2(v_start[1], v_start[0])
            angle_end = np.arctan2(v_end[1], v_end[0])
            
            # Find the raw angular distance
            angle_arc = angle_end - angle_start

            # Force the sweep to take the shortest path (-pi to +pi)
            delta_theta = (angle_arc + np.pi)%(2*np.pi) - np.pi

            #  Interpolate linearly from 0% to 100% of the true delta
            arc_len = abs(angle_arc)*R
            num_points = int(arc_len/div)+1
            steps = np.linspace(0, 1, num=num_points, endpoint=endpoint_option)
            angles = angle_start + steps*delta_theta

            # Generate coordinates
            arc_x = center[0] + R * np.cos(angles)
            arc_y = center[1] + R * np.sin(angles)
            
            seg_points = np.column_stack((arc_x, arc_y))
            seg_points = [tuple(s) for s in seg_points]
            cable_coords.append(seg_points)
            
    return cable_coords



