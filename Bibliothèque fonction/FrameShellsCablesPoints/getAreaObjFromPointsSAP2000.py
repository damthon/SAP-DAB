# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

def getAreaObjFromPointsSAP2000(SapModel,points,Group):
    """
    This function returns the area objects containing specified points. The area objects must include MUST NOT include points outside the specified list.
    Input:
        SapModel: SAP Model object
        points: List of points belonging to the area object. e.g. ['p1','p2','p3'...]
        Group: Group name containing area objects
    Output:
        point_objects_group: Group point objects 
    """
    
    SapModel.SelectObj.ClearSelection()
    SapModel.AreaObj.SetSelected(Group,True,1)
    area_objects = list(SapModel.AreaObj.GetNameList()[1])
    area_from_points = []
    for i in range(len(area_objects)):
        area_obj_points = SapModel.AreaObj.GetPoints(area_objects[i])[1]
        if all(item in points for item in area_obj_points):
            area_from_points.append(area_objects[i])
                   
    return area_from_points
