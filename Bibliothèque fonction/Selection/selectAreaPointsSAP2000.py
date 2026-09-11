# -*- coding: utf-8 -*-
"""
Created on Wed May  31 10:02:54 2023

@author: hammad.eljisr
"""

from functools import reduce
import operator

def selectAreaPointsSAP2000(SapModel):
    """
    This function selects the points belonging to the selected area elements.
    Input:
        SapModel: SAP Model object
    """

    # Get all area objects
    area_objects = list(SapModel.AreaObj.GetNameList()[1])
    # Get selected area objects
    area_objects_sel = []
    for i in range(len(area_objects)):
        if SapModel.AreaObj.GetSelected(area_objects[i], True)[0] == True:
            area_objects_sel.append(area_objects[i])
           
    # Get all points in selected area objects and select them
    area_objects_points = []
    for i in range(len(area_objects_sel)):
        pt = list(SapModel.AreaObj.GetPoints(area_objects_sel[i])[1])
        area_objects_points.append(pt)
    # Unflatten list and remove duplicates
    area_objects_points = reduce(operator.concat, area_objects_points)
    area_objects_points = [*{*area_objects_points}] # Removes duplicates
    # Select points belonging to the area elements
    for j in range(len(area_objects_points)):
        SapModel.PointObj.SetSelected(area_objects_points[j], True)
            
    return None

    

      