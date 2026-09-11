# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

def getGroupAreaObjSAP2000(SapModel,Group):
    """
    This function returns the area objects in a group
    Input:
        SapModel: SAP Model object
        Group: Group name
    Output:
        area_objects_group: Group area objects 
    """
    
    SapModel.SelectObj.ClearSelection()
    SapModel.AreaObj.SetSelected(Group,True,1)
    area_objects = list(SapModel.AreaObj.GetNameList()[1])
    # Get selected area objects
    area_objects_group = []
    for i in range(len(area_objects)):
        if SapModel.AreaObj.GetSelected(area_objects[i], True)[0] == True:
            area_objects_group.append(area_objects[i])
                 
    return area_objects_group





