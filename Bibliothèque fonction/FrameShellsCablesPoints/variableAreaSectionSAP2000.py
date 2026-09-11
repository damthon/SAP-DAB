# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""
import numpy as np

def variableAreaSectionSAP2000(SapModel,Area_label,tmin_tmax,omin_omax,var):
    """
    This function modifies the thickness and offset of a 4-point area object
    Input:
        SapModel: SAP Model object
        Area_label: Name of the area object
        tmin_tmax: Minimum/maximum thickness of the area object [tmin,tmax]
        omin_omax: Minimum/maximum offset of the area object at the corresponding min/max thicknesses [offset_min,offset_max]
        var: Variable section type 1, -1, 2, -2 or 3, -3 representing the location of the minimum thickness
        (-1 for min x, 1 for max x, -2 for min y, 2 for max y, -3 for min z, 3 for max z)
    """
    
    
    # Get coordinates of area object points 
    area_points = SapModel.AreaObj.GetPoints(Area_label)[1]
    x_points = []
    y_points = []
    z_points = []
    for i in range(len(area_points)):
        x_points.append(SapModel.PointObj.GetCoordCartesian(area_points[i])[0])
        y_points.append(SapModel.PointObj.GetCoordCartesian(area_points[i])[1])
        z_points.append(SapModel.PointObj.GetCoordCartesian(area_points[i])[2])
    
    # Get rank of points
    if abs(var) == 1:
        array = np.array(x_points)
    elif abs(var) == 2 :
        array = np.array(y_points)
    else:
        array = np.array(z_points)    
    order = array.argsort()
    ranks = order.argsort()
    
    # Set thickness and offset
    thickness = []
    offset = []
    if len(ranks) == 4: # quad elements
        if var<0:
            for r in ranks:
                if r<=1:
                    thickness.append(tmin_tmax[0])
                    offset.append(omin_omax[0])
                else:
                    thickness.append(tmin_tmax[1])
                    offset.append(omin_omax[1])
        if var>0:
            for r in ranks:
                if r>=2:
                    thickness.append(tmin_tmax[0])
                    offset.append(omin_omax[0])
                else:
                    thickness.append(tmin_tmax[1])
                    offset.append(omin_omax[1])
    elif len(ranks) == 3: # triangular elements
        if var<0:
            for r in ranks:
                if r<1:
                    thickness.append(tmin_tmax[0])
                    offset.append(omin_omax[0])
                else:
                    thickness.append(tmin_tmax[1])
                    offset.append(omin_omax[1])
        if var>0:
            for r in ranks:
                if r>=1:
                    thickness.append(tmin_tmax[0])
                    offset.append(omin_omax[0])
                else:
                    thickness.append(tmin_tmax[1])
                    offset.append(omin_omax[1])
        thickness.append(thickness[2])
        offset.append(offset[2])
      
            
    # Apply thickness and offset        
    SapModel.AreaObj.SetThickness(Area_label, 2, '', 1, thickness)
    SapModel.AreaObj.SetOffsets(Area_label, 2, '', 1, offset)
            
    return None





