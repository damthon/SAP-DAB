# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

def deleteFloatingPointsSAP2000(SapModel):
    """
    This function deletes all the floating points in a model
    Input:
        SapModel: SAP Model object
    """
    
    # Select all points
    SapModel.SelectObj.ClearSelection()
    SapModel.PointObj.SetSelected('All',True,1)
    point_objects = list(SapModel.PointObj.GetNameList()[1])
    for p in range(len(point_objects)):
        SapModel.PointObj.DeleteSpecialPoint(point_objects[p])  
    return 
