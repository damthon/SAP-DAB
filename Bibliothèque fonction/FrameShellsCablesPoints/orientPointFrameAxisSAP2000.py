# -*- coding: utf-8 -*-
"""
Created on Mon Sep  08 15:56:54 2025

@author: hammad.eljisr
"""

def orientPointFrameAxisSAP2000(SapModel,Point_label,Plane,Dir):
    """
    This function orient the axes of a point object in the direction of the connected frame object. If 2 frame objects are connected the average orientation is assigned
    Input:
        SapModel: SAP Model object
        Point_label: Label of the point object (string)
        Plane: This is 12 or 13 (integer), indicating that the plane determined by the 2 joints is the 1-2 plane or the 1-3 plane
        1 is in the global X, while 2 is in the global Y
        Dir: Direction of the local axis 1 positive X, -1 negative X
    """
    
    frame_conn = SapModel.PointObj.GetConnectivity(Point_label)[2]
    p = [[] for _ in range(len(frame_conn))]
    for i in range(len(frame_conn)):
        p[i] = [SapModel.FrameObj.GetPoints(frame_conn[i])[0],SapModel.FrameObj.GetPoints(frame_conn[i])[1]]
        p[i].remove(Point_label)

    if len(p)==2: # Connected to two frames
        joints = [p[0][0],p[1][0]]
    else: # Connected to 1 frame (edge element)
        joints = [Point_label,p[0][0]]
    # Sort joints 
    x1 = SapModel.PointObj.GetCoordCartesian(joints[0])[0]
    x2 = SapModel.PointObj.GetCoordCartesian(joints[1])[0]
    if (Dir == 1 and x1 > x2) or (Dir == -1 and x1 < x2):
        joints.reverse()

    SapModel.PointObj.SetLocalAxesAdvanced(Point_label,True,2,'Global',[],joints,[],Plane,3,'Global',[],[],[0,0,1],0)
    
    return None



