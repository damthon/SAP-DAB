# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

def getGroupPointObjSAP2000(SapModel,Group):
    """
    This function returns the point objects in a group
    Input:
        SapModel: SAP Model object
        Group: Group name
    Output:
        point_objects_group: Group point objects 
    """
    
    SapModel.SelectObj.ClearSelection()
    SapModel.PointObj.SetSelected(Group,True,1)
    point_objects = list(SapModel.PointObj.GetNameList()[1])
    # Get selected area objects
    point_objects_group = []
    for i in range(len(point_objects)):
        if SapModel.PointObj.GetSelected(point_objects[i], True)[0] == True:
            point_objects_group.append(point_objects[i])
                 
    return point_objects_group
