# -*- coding: utf-8 -*-
"""
Created on Thurs Sep  21 11:02:54 2023

@author: hammad.eljisr
"""

import numpy as np

def centroidAreaObjectSAP2000(SapModel,Area_object):
    """
    This function selects the points belonging to the selected area elements.
    Input:
        - SapModel: SAP Model object
        - Area_object: Area object label
    Output:
        - centroid : List of the centroid coordinates [X_c,Y_c,Z_c]
    """
    
    
    points_area_objects_sel = list(SapModel.AreaObj.GetPoints(Area_object)[1])
    p = [[] for _ in range(len(points_area_objects_sel))]
    for i in range(len(points_area_objects_sel)):
        p[i] = np.array(SapModel.PointObj.GetCoordCartesian(points_area_objects_sel[i])[0:3])
     
    centroid = list(sum(p)/len(p))
    
    return centroid

    

      