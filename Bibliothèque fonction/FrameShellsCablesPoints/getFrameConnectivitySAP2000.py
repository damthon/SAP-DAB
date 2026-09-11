# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2024

@author: hammad.eljisr
"""

def getFrameConnectivitySAP2000(SapModel,Frame_object):
    """
    This function returns the points objects connected a frame objects
    Input:
        SapModel: SAP Model object
        Frame_object: Frame object label 
    Output:
        point_objects_frame: Point objects 
    """

    point_objects = list(SapModel.PointObj.GetNameList()[1])
    # Get selected frame objects
    point_objects_frame = []
    for i in range(len(point_objects)):
        if Frame_object in SapModel.PointObj.GetConnectivity(point_objects[i])[2] and SapModel.PointObj.GetConnectivity(point_objects[i])[1][0]==2:
            point_objects_frame.append(point_objects[i])
                 
    return point_objects_frame

