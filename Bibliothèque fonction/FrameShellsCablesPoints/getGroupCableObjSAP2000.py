# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2024

@author: hammad.eljisr
"""

def getGroupCableObjSAP2000(SapModel,Group):
    """
    This function returns the cable objects in a group
    Input:
        SapModel: SAP Model object
        Group: Group name
    Output:
        cable_objects_group: Group cable objects 
    """
    
    SapModel.SelectObj.ClearSelection()
    SapModel.CableObj.SetSelected(Group,True,1)
    cable_objects = list(SapModel.CableObj.GetNameList()[1])
    # Get selected area objects
    cable_objects_group = []
    for i in range(len(cable_objects)):
        if SapModel.CableObj.GetSelected(cable_objects[i], True)[0] == True:
            cable_objects_group.append(cable_objects[i])
                 
    return cable_objects_group
