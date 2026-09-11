# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:49:41 2026

@author: hammad.eljisr
"""

import numpy as np

def getOffsetPoints(line,distance,slope_normals):
    """
    Computes a 3D miter offset ensuring a strict 1:1 point correspondence
    with the original centerline array.
    Input:
        - line: List of line points coordinates to be offset [(x1,y1,z1),(x2,y2,z2)...]
        - distance: Offset distance float if constant, list of variable at each point if variable
        - slope_normals: Slope normal vectors at each point [[0,0,1],[0,0,1],...] if slope is 0 (i.e. flat plane).
    Output:
        - offset_points: List of offset tuples coordinates [(x1,y1,z1), ...]
    """
    
    points = np.array(line, dtype=float)
    num_points = len(points)
    
    if num_points < 2:
        return [tuple(p) for p in points.tolist()]
        
    # Standardize slope_normals and distance into numpy formats cleanly
    s_norms = np.array(slope_normals, dtype=float)
    s_norms /= np.linalg.norm(s_norms, axis=1, keepdims=True)
    
    # Handle variable vs scalar distance cleanly without try/except performance hits
    if isinstance(distance, (list, np.ndarray)):
        if len(distance) != num_points:
            print('Warning: Offset distances count mismatch!')
        dist_array = np.array(distance, dtype=float)[:, np.newaxis]
    else:
        dist_array = float(distance)

    # Calculate Segment Tangents
    segments = np.diff(points, axis=0)
    seg_lens = np.linalg.norm(segments, axis=1, keepdims=True)
    seg_lens = np.where(seg_lens == 0, 1e-12, seg_lens)
    normalized_segs = segments/seg_lens  # Shape: (N-1, 3)

    # Build Vertex Tangents (Average direction entering and leaving a vertex)
    tangents = np.zeros_like(points)
    tangents[0] = normalized_segs[0]
    tangents[-1] = normalized_segs[-1]
    # Internal vertices are the average of the segment before and segment after
    tangents[1:-1] = (normalized_segs[:-1] + normalized_segs[1:]) / 2.0
    
    tangent_lens = np.linalg.norm(tangents, axis=1, keepdims=True)
    tangent_lens = np.where(tangent_lens == 0, 1e-12, tangent_lens)
    tangents /= tangent_lens

    # Calculate local perpendicular normals using cross-product
    normals = np.cross(s_norms,tangents)
    normal_lens = np.linalg.norm(normals, axis=1, keepdims=True)
    normal_lens = np.where(normal_lens == 0, 1e-12, normal_lens)
    normals /= normal_lens

    # Compute 1:1 Miter vectors per vertex
    miter_vectors = np.zeros_like(points)
    
    # Endpoints use the perpendicular normal direction exactly
    miter_vectors[0] = normals[0]
    miter_vectors[-1] = normals[-1]
    
    # Compute miter joint scaling for internal vertices
    for i in range(1, num_points - 1):
        n_prev = normals[i-1]
        n_next = normals[i]
        
        bisector = n_prev + n_next
        bisector_len = np.linalg.norm(bisector)
        
        if bisector_len < 1e-6:
            miter_vectors[i] = n_prev
        else:
            bisector /= bisector_len
            # Project normal onto bisector to scale joint thickness
            cos_half_angle = np.dot(n_prev, bisector)
            
            # PROTECT: Prevent extreme spikes on tight near-180 degree snaps
            if abs(cos_half_angle) < 1e-3:
                miter_vectors[i] = bisector
            else:
                miter_vectors[i] = bisector/abs(cos_half_angle)

    # Generate final offset points vectorially
    offset_points = points + (miter_vectors * dist_array)
        
    return [tuple(point) for point in offset_points.tolist()]


def getSlopeNormals(line,slope):
    """
    Computes the normals along a line given the transverse slope
    Input:
        - line: List of line points coordinates to be offset [(x1,y1,z1),(x2,y2,z2)...]
        - slope: Slab slope in % (positive towards outer edge, that is positive offset)
    Output:
        - slope_normals: List of slope normals at each point
    """
    
    # Convert it to a numpy array for fast vector math
    coords = np.array(line)  # Shape: (N, 3)
    
    # Calculate tangent vectors along the path using forward differences
    tangents = np.diff(coords, axis=0)
    tangents = np.vstack([tangents, tangents[-1]])  # Shape: (N, 3)

    # Extract the horizontal direction (X,Y) and normalize it
    dx = tangents[:,0]
    dy = tangents[:,1]
    horizontal_lens = np.sqrt(dx**2 + dy**2)
    # Prevent division by zero if two consecutive coordinates are identical
    horizontal_lens[horizontal_lens == 0] = 1.0

    ux = dx/horizontal_lens
    uy = dy/horizontal_lens

    # Rotate the horizontal vector by 90 degrees to get the PERPENDICULAR direction
    perpendic_x = uy
    perpendic_y = -ux

    # Build the normal vectors using your formula layout
    s_val = slope/100
    nx = s_val*perpendic_x
    ny = s_val*perpendic_y
    nz = np.ones(len(coords))

    # Combine into an (N,3) array
    normals_unnorm = np.column_stack((nx, ny, nz))

    # Normalize the final perpendicular slope normals
    final_norms = np.linalg.norm(normals_unnorm, axis=1, keepdims=True)
    slope_normals = normals_unnorm / final_norms

    return slope_normals



