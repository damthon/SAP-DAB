# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2024

@author: hammad.eljisr
"""

def getGroupFrameObjSAP2000(SapModel,Group):
    """
    This function returns the frame objects in a group
    Input:
        SapModel: SAP Model object
        Group: Group name
    Output:
        frame_objects_group: Group frame objects 
    """
    
    SapModel.SelectObj.ClearSelection()
    SapModel.FrameObj.SetSelected(Group,True,1)
    frame_objects = list(SapModel.FrameObj.GetNameList()[1])
    # Get selected area objects
    frame_objects_group = []
    for i in range(len(frame_objects)):
        if SapModel.FrameObj.GetSelected(frame_objects[i], True)[0] == True:
            frame_objects_group.append(frame_objects[i])
                 
    return frame_objects_group
