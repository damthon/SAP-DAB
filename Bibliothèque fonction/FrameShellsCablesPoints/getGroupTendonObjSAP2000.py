# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2024

@author: hammad.eljisr
"""

def getGroupTendonObjSAP2000(SapModel,Group):
    """
    This function returns the tendon objects in a group
    Input:
        SapModel: SAP Model object
        Group: Group name
    Output:
        tendon_objects_group: Tendon objects 
    """
    
    SapModel.SelectObj.ClearSelection()
    SapModel.TendonObj.SetSelected(Group,True,1)
    tendon_objects = list(SapModel.TendonObj.GetNameList()[1])
    # Get selected tendon objects
    tendon_objects_group = []
    for i in range(len(tendon_objects)):
        if SapModel.TendonObj.GetSelected(tendon_objects[i], True)[0] == True:
            tendon_objects_group.append(tendon_objects[i])
                 
    return tendon_objects_group
