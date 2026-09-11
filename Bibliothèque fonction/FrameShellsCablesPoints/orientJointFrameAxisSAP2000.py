# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

def orientAreaAxisSAP2000(SapModel,Area_label,Plane,Axis_type):
    """
    This function orient the axes of an area object along the 31 or 32 plane.
    Input:
        SapModel: SAP Model object
        Area_label: Label of the area object (string)
        Plane: This is 31 or 32 (integer), indicating that the plane determined by the plane reference vector is the 3-1 plane or the 3-2 plane
        1 is in the global X, while 2 is in the global Y
        Axis_type: 0 for local axis, 1, 2 or 3  for global axis in the specified dimension
    """
    
    MyPlPt = [None,None]
    # Get point labels for the area object
    area_points = SapModel.AreaObj.GetPoints(Area_label)[1]
    
    if Axis_type == 0:
        # Get point labels that define the local axis orientation (aligned towards the positive global X or Y, starting from minimum X or Y coordinate)
        xy_area_points = []
        for j in range(len(area_points)):
            xy_area_points.append(SapModel.PointObj.GetCoordCartesian(area_points[j])[Plane-31])
            min_xy_index = xy_area_points.index(min(xy_area_points))
            if (min_xy_index != len(xy_area_points)-1):
                 if xy_area_points[min_xy_index-1]>xy_area_points[min_xy_index+1]:
                     MyPlPt[0] = area_points[min_xy_index]
                     MyPlPt[1] = area_points[min_xy_index-1]
                 else:
                     MyPlPt[0] = area_points[min_xy_index]
                     MyPlPt[1] = area_points[min_xy_index+1]
            else:
                if xy_area_points[min_xy_index-1]>xy_area_points[0]:
                    MyPlPt[0] = area_points[min_xy_index]
                    MyPlPt[1] = area_points[min_xy_index-1]
                else:
                    MyPlPt[0] = area_points[min_xy_index]
                    MyPlPt[1] = area_points[0]
                    
        # Align local axis along points MplPt
        SapModel.AreaObj.SetLocalAxesAdvanced(Area_label, True, Plane, 2, 'Global', [1,3], MyPlPt, [0,0,0])
        
    else:
        SapModel.AreaObj.SetLocalAxesAdvanced(Area_label, True, Plane, 1, 'Global', [Axis_type,3], MyPlPt, [0,0,0])   
    
    return None



