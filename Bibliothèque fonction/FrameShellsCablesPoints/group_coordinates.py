# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:06:34 2025

@author: hammad.eljisr
"""

import numpy as np

# Function to calculate Euclidean distance between two points
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to find clusters based on tolerance
def group_coordinates(coords, tol):
    """
    This function groups the coordinates of points within a certain tolerance
    Input:
        coords: Numpy array of coordinates [[x1,y1],[x2,y2]...]
        tol: Tolerance [distance]
    Output:
        Clusters: Groups of point coordinates with their corresponding indices
    """
    clusters = []
    visited = set()

    for i, point in enumerate(coords):
        if i in visited:
            continue
        # Create a new cluster and start with the current point
        cluster = {'points': [point], 'indices': [i]}
        visited.add(i)

        # Check all other points and add to the cluster if they are within tolerance
        for j, other_point in enumerate(coords):
            if i != j and j not in visited and distance(point, other_point) <= tol:
                cluster['points'].append(other_point)
                cluster['indices'].append(j)
                visited.add(j)
        
        clusters.append(cluster)
    
    # Return the cluster points and indices in the output
    return [(cluster['points'], cluster['indices']) for cluster in clusters]

