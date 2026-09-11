# -*- coding: utf-8 -*-
"""
Created on Fri Apr  12 15:56:54 2024

@author: hammad.eljisr
"""


from getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000

def disconnectMeshPointsSAP2000(SapModel,group,points):
    """
    This function creates disconnects the points in a mesh belonging to two separate groups and returns two list of the created points
    Input:
        SapModel: SAP Model object
        group: Groups in which the joints will be disconnected e.g. 'Group1'
        points: List of labels of the points, belonging to the group, at the interface that will be disconnected
    Output: 
        points_group_merged : List of disconnected points belonging to the group
        points_outside_merged : List of disconnected points not belonging to the group
    """
    # Get group area objects
    group_area_objects = getGroupAreaObjSAP2000(SapModel,group)   

    # Disconnect and merge points in the specified groups
    points_group_merged = [] # List of merged points in group 1
    points_outside_merged = [] # List of merged points in group 2
    for n in range(len(points)):
        point_label = points[n]
        # Disconnect connected points in area object
        SapModel.SelectObj.ClearSelection()
        SapModel.PointObj.SetSelected(point_label, True)
        disconnected_points = SapModel.EditPoint.Disconnect()
        # Merge points in the same specified group
        points_group = []
        points_outside = []
        for i in range(len(disconnected_points[1])):
            element = SapModel.PointObj.GetConnectivity(disconnected_points[1][i])[2][0]
            try:
                group_area_objects.index(element) > 0
                points_group.append(disconnected_points[1][i])
            except: 
                points_outside.append(disconnected_points[1][i])
        # In group
        SapModel.SelectObj.ClearSelection()
        for p1 in points_group: 
            SapModel.PointObj.SetSelected(p1, True)       
        if len(points_group)>1:
            points_group_merged.append(SapModel.EditPoint.Merge(1, 1)[1][0]) # Last point in the list remains
        else:
            points_group_merged.append(points_group[0])
        # Outside group
        SapModel.SelectObj.ClearSelection()
        for p2 in points_outside: 
            SapModel.PointObj.SetSelected(p2, True)       
        if len(points_outside)>1:
            points_outside_merged.append(SapModel.EditPoint.Merge(1, 1)[1][0]) # Last point in the list remains
        else:
            points_outside_merged.append(points_outside[0])
        
    return points_group_merged,points_outside_merged



