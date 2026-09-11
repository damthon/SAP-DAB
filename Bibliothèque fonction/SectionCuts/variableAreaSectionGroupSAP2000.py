# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""
import numpy as np
from getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000
from getGroupPointObjSAP2000 import getGroupPointObjSAP2000
from variableAreaSectionSAP2000 import variableAreaSectionSAP2000

def variableAreaSectionGroupSAP2000(SapModel,group_areas,tmin_tmax,omin_omax,var,trace,skew_tol):
    """
    This function applies a variable shell section (in the x-y plane) to a group of areas with a quadrilareal STRUCTURED mesh. 
    Works for straight or slightly curved monotonic decks.
    Input:
        - SapModel: SAP Model object
        - Area_label: Name of the area object
        - tmin_tmax: Minimum/maximum thickness of the area object [tmin,tmax]
        - omin_omax: Minimum/maximum offset of the area object at the corresponding min/max thicknesses [offset_min,offset_max]
        - var: Variable section type 1, -1, 2, -2 representing the location of the minimum thickness
        (-1 for min x, 1 for max x, -2 for min y, 2 for max y)
        - trace: Points along which mesh is aligned (e.g. points corresponding to centerline). 
        Should ideally correspond to points along the mesh. Should contain at least 2 points on the mesh 
        - skew_tol: Skew tolerance measures difference between trace and row orientation (between 0 and 1)
        0.7 recommended, 0.6 more tolerance: severe skew, 0.9 stricter: slight skew
    """
    
    """ Split mesh """
    # Get areas in the group
    area_objects = getGroupAreaObjSAP2000(SapModel,group_areas)
    
    # Get points in area objects and sort
    area_points = [[] for _ in range(len(area_objects))]
    x_points = [[] for _ in range(len(area_objects))]
    y_points = [[] for _ in range(len(area_objects))]
    for a in range(len(area_objects)):
        # Get coordinates of area object points 
        area_points[a] = SapModel.AreaObj.GetPoints(area_objects[a])[1]
        for i in range(len(area_points[a])):
            x_points[a].append(SapModel.PointObj.GetCoordCartesian(area_points[a][i])[0])
            y_points[a].append(SapModel.PointObj.GetCoordCartesian(area_points[a][i])[1])
    
    # Centroid of each area element
    c_area = np.zeros((len(area_objects),2))
    for a in range(len(area_points)):
        c_area[a,0] = sum(x_points[a])/len(x_points[a])
        c_area[a,1] = sum(y_points[a])/len(y_points[a])   
     
    # Find trace points
    trace_point_labels = trace
    trace_points = []
    for i in range(len(trace_point_labels)):
        # Compute longitudinal positions along trace_points
        x_t = SapModel.PointObj.GetCoordCartesian(trace_point_labels[i])[0]
        y_t = SapModel.PointObj.GetCoordCartesian(trace_point_labels[i])[1]
        if trace_point_labels[i] in (sum(area_points, ())): 
            trace_points.append([x_t,y_t])
    
    # Sort longitudinally along trace
    trace_points = np.array(trace_points)
    ordered = [0]
    remaining = list(range(1, len(trace_points)))
    while remaining:
        last = ordered[-1]
        d = np.linalg.norm(trace_points[remaining] - trace_points[last], axis=1)
        next_idx = remaining[np.argmin(d)]
        ordered.append(next_idx)
        remaining.remove(next_idx)
    trace_points = trace_points[ordered]
    # Use global longitudinal reference (increasing x)
    start = trace_points[0]
    end   = trace_points[-1]   
    # If going backwards in X
    if end[0] < start[0]:
        trace_points = trace_points[::-1]
   
    # Find trace vectors
    seg_vectors = trace_points[1:] - trace_points[:-1]
    seg_lengths = np.linalg.norm(seg_vectors, axis=1)
    seg_unit = seg_vectors / seg_lengths[:,None]
    
    # Assign local trace direction to each element
    elem_dir = np.zeros_like(c_area)
    for i, c in enumerate(c_area):
        min_dist = np.inf
        best_dir = None
        for j in range(len(seg_vectors)):
            v = c - trace_points[j]
            proj = np.dot(v, seg_unit[j])
            proj = np.clip(proj, 0, seg_lengths[j])
            closest = trace_points[j] + proj * seg_unit[j]
            d = np.linalg.norm(c - closest)
            if d < min_dist:
                min_dist = d
                best_dir = seg_unit[j]
        elem_dir[i] = best_dir     
        
    # Build adjacency (elements sharing an edge)
    adj = {i: [] for i in range(len(area_objects))}
    for i in range(len(area_objects)):
        for j in range(i+1, len(area_objects)):
            # Count shared points
            shared = len(set(area_points[i]) & set(area_points[j]))
            if shared >= 2:  # share an edge
                adj[i].append(j)
                adj[j].append(i)
                  
    # Starting corner
    start = [i for i in adj if len(adj[i]) == 2][0] # Start from a corner (only 2 neighbors)                
    
    # Build first longitudinal row
    row = [start]
    prev = None
    current = start
    while True:
        neighbors = adj[current] 
        # Remove where we came from
        if prev is not None:
            neighbors = [n for n in neighbors if n != prev]
        if not neighbors:
            break
        # Choose one direction (first row)
        best = None
        best_score = -np.inf
        
        for n in neighbors:
            if n in row:
                continue
            step_vec = c_area[n] - c_area[current]
            step_len = np.linalg.norm(step_vec)
            if step_len == 0:
                continue
            
            step_dir = step_vec / step_len
            trace_dir = elem_dir[current]
            score = np.dot(step_dir, trace_dir)
            
            if score < skew_tol: # Only neighbours strongly aligned with the trace are allowed
                continue
            
            if score > best_score:
                best_score = score
                best = n
        
        if best is None:
            break
        
        nxt = best
        if nxt in row:
            break
     
        row.append(nxt)
        prev = current
        current = nxt
    
    # Build full grid from first row
    rows = []
    visited = set()
    current_row = row
    
    while current_row:
        rows.append(current_row)
        visited.update(current_row)
        next_row = []
        
        for el in current_row:
            for n in adj[el]:
                if n not in visited:
                    next_row.append(n)
        
        # Remove duplicates while preserving order
        next_row = list(dict.fromkeys(next_row))
        
        # Sort next row consistently (same direction as first row)
        if next_row:
            c_next = np.array([c_area[i] for i in next_row])
            # Project onto transverse direction = perpendicular to trace
            t_dir = np.array([-elem_dir[current_row[0]][1], elem_dir[current_row[0]][0]])
            proj = c_next @ t_dir
            I_sort = np.argsort(proj)
            next_row = [next_row[i] for i in I_sort]
            if len(rows) > 0:
                prev_row = rows[-1]
                
                c_prev_start = c_area[prev_row[0]]
                c_next_start = c_area[next_row[0]]
                c_next_end   = c_area[next_row[-1]]
                
                d_start = np.linalg.norm(c_prev_start - c_next_start)
                d_end   = np.linalg.norm(c_prev_start - c_next_end)
                
                # if reversed, flip row
                if d_end < d_start:
                    next_row = next_row[::-1]
        current_row = next_row
    
    # If groups is inside a mesh (no corner), detect number of rows
    l_row = len(rows[0])
    for n in range(len(rows)):
        if len(rows[n]) != l_row:
            n_rows = n
            break
        else:
            n_rows = len(rows)
            
    # Correct number of rows if only 1
    if n_rows == 1:
       rows = [[item for r in rows for item in r]]
       
    # Sort rows 
    rows_sorted = []
    for r in rows:
        c_row = np.array([c_area[i] for i in r])
        # Use average longitudinal direction for the row
        dir_avg = np.mean([elem_dir[i] for i in r], axis=0)
        dir_avg = dir_avg / np.linalg.norm(dir_avg)
        # Project centroids onto longitudinal direction
        s_local = c_row @ dir_avg
        I_sort = np.argsort(s_local)
        r_sorted = [r[i] for i in I_sort]
        rows_sorted.append(r_sorted)
    rows = rows_sorted  
    
    # Get area_objects in each row (longitudinally)
    area_objects_long = []
    for r in rows:
        area_objects_long.append([area_objects[i] for i in r])
    
    # Split area objects transversally
    area_objects_tr = [[] for _ in range(len(area_objects_long[0]))]
    for t in range(len(area_objects_long[0])):
        for r in range(len(area_objects_long)):
            area_objects_tr[t].append(area_objects_long[r][t])
    
    # Split areas depending on orientation of variable sections
    if abs(var) == 1:
        area_objects_split = area_objects_long
    else:
        area_objects_split = area_objects_tr
         
        
    """ Assign variable thickness for each area in the object"""
    # Get thicknesses/offsets for each area element
    l_area = [[] for _ in range(len(area_objects_split))]
    for i in range(len(area_objects_split)):
        for j in range(len(area_objects_split[i])):
            index_a = area_objects.index(area_objects_split[i][j]) # Index of the area object
            x_p = np.sort(x_points[index_a]) # Sort increasing x
            y_p = np.sort(y_points[index_a]) # Sort increasing y
            if abs(var) == 1: # Variable in x direction
                l_area[i].append(abs((x_p[0] + x_p[1])/2 -(x_p[2] + x_p[3])/2)) # Length in the direction of variable section (x)
            else: # Variable in y direction
                l_area[i].append(abs((y_p[0] + y_p[1])/2 -(y_p[2] + y_p[3])/2)) # Length in the direction of variable section (y)
        l_area[i].insert(0,0)
    
    tmin_max_areas = [[] for _ in range(len(area_objects_split))] # Thicknesses for each area element
    omin_max_areas = [[] for _ in range(len(area_objects_split))] # Offset for each area element
    d_area = [[] for _ in range(len(area_objects_split))]  # Distances from minimum thickness
    for i in range(len(l_area)):
        d_area[i] = list(np.cumsum(l_area[i]))
    
    # Get interpolated thicknesses and offsets
    if var > 0 :
        tmin_tmax_pos = tmin_tmax[::-1]
        omin_omax_pos = omin_omax[::-1]
        for i in range(len(d_area)):
            tmin_max_areas[i] = np.interp(d_area[i],[d_area[i][0],d_area[i][-1]],tmin_tmax_pos)
            omin_max_areas[i] = np.interp(d_area[i],[d_area[i][0],d_area[i][-1]],omin_omax_pos)
    else:
        tmin_tmax_neg = tmin_tmax
        omin_omax_neg = omin_omax
        for i in range(len(d_area)):
            tmin_max_areas[i] = np.interp(d_area[i],[d_area[i][0],d_area[i][-1]],tmin_tmax_neg)
            omin_max_areas[i] = np.interp(d_area[i],[d_area[i][0],d_area[i][-1]],omin_omax_neg)
    
    # Apply variable sections to each area element
    for a in range(len(area_objects_split)):
        for j in range(len(area_objects_split[a])):
            t_var = list(tmin_max_areas[i][j:j+2]) # Thicknesses in each element
            o_var = list(omin_max_areas[i][j:j+2]) # Offsets in each element
            if var > 0:
                t_var.reverse()
                o_var.reverse()
            variableAreaSectionSAP2000(SapModel,area_objects_split[a][j],t_var,o_var,var)
        
    return None

# for i in range(len(area_objects_split[j])):
#     SapModel.AreaObj.SetSelected(area_objects_split[j][i],True,0)  
 
# r = row[48:95]
# for i in range(len(r)):
#     SapModel.AreaObj.SetSelected(area_objects[r[i]],True,0)  