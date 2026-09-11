# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

import numpy as np
from Selection.getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000

def variableAreaGroupThicknessPatternSAP2000(SapModel,Group,tmin_tmax,offset,var,range_group):
    """
    This function modifies the thickness of a group of area elements in 1 direction by defining a joint pattern
    Input:
        SapModel: SAP Model object
        Group: Name of the group
        tmin_tmax: Minimum/maximum thickness of the area object [tmin,tmax]
        offset: Offset value corresponding to a fraction of the thickness (e.g. 0.5 offset half the thickness in the positive z, -0.25 offsets quarter of the thickness in the negative z)
        var: Variable section type 1, 2 or 3 representing the direction along which the thickness varies
        (1 for  x, 2 for y, 3 for z)
        range_group: Range of the coordinates at which the minimum and maximum thicknesses occur respectively
        
    """
    
    # Get join pattern constants (solve matrix)
    a = np.array([[range_group[0],1],[range_group[1],1]])
    b = np.array(tmin_tmax)
    constants = np.linalg.solve(a,b)
     
    if var == 1:
        A = constants[0]
        B = 0
        C = 0
        D = constants[1]
    elif var == 2:
        A = 0
        B = constants[0]
        C = 0
        D = constants[1]
    else:
        A = 0
        B = 0
        C = constants[0]
        D = constants[1]
    
    # Add joint pattern
    pattern_name = Group + '_t'
    SapModel.PatternDef.SetPattern(pattern_name)
    
    # Assign joint pattern XYZ
    SapModel.PointObj.SetPatternByXYZ(Group, pattern_name, A, B, C, D, 1)
    
    # Get area objects
    area_objects = getGroupAreaObjSAP2000(SapModel,Group)
    
    for a in range(len(area_objects)):
        SapModel.AreaObj.SetThickness(area_objects[a], 1, pattern_name, 1)
        SapModel.AreaObj.SetOffsets(area_objects[a], 1, pattern_name, offset)
          
    return None





