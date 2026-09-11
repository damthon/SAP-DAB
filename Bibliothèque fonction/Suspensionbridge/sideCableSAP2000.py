# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:04:08 2024

@author: hammad.eljisr
"""

import math
import numpy as np

def sideCableSAP2000(SapModel,nodes_s,h_p,s_h,g,parameters):
    """
    This function creates the side span cable with break points at the hanger locations
    Input:
        SapModel: SAP model object
        nodes_s: Nodes connecting the main span pylon to deck or anchor (in that order, pylon node first)
        h_p: Pylon height from deck
        s_h: Hanger spacing (closer to pylons if span is not divisible by the spacing)
        g: Dead load of the deck [kN/m] per main cable
        parameters: [x_min,n_start,n_end] x_min is the minimum spacing allowed, if exceeded, hanger will be removed. nstart/n_end are the additional number of hangers to be removed at the start/end
        
    Output:
        x, y, z: Coordinates of points at which the hangers are connected
        s_s_cables: Cable segments
    """     
   
    # Get coordinates of the side span
    x_s = []
    y_s = []
    z_s = []
    x_s.append(SapModel.PointObj.GetCoordCartesian(nodes_s[0])[0]) 
    x_s.append(SapModel.PointObj.GetCoordCartesian(nodes_s[1])[0]) 
    y_s.append(SapModel.PointObj.GetCoordCartesian(nodes_s[0])[1])  
    y_s.append(SapModel.PointObj.GetCoordCartesian(nodes_s[1])[1])  
    z_s.append(SapModel.PointObj.GetCoordCartesian(nodes_s[0])[2])  
    z_s.append(SapModel.PointObj.GetCoordCartesian(nodes_s[1])[2])  
    
    # Side span length 
    l_s  = abs(x_s[1] - x_s[0])
    
    # Construct parabola using SAP2000 built-in function (100 divisions)
    s = SapModel.CableObj.AddByPoint(nodes_s[0],nodes_s[1])
    SapModel.CableObj.SetCableData(s[0], 9, 100, 0, g, 1, 1)
      
    # Get cable geometry
    x_o = SapModel.CableObj.GetCableGeometry(s[0])[1]
    y_o = SapModel.CableObj.GetCableGeometry(s[0])[2]
    z_o = SapModel.CableObj.GetCableGeometry(s[0])[3]
    
    # Delete cable
    SapModel.CableObj.Delete(s[0])
        
    # Get x at break points
    s_hp = s_h # Hanger spacing from pylon
    n_shp = (math.floor(l_s/s_hp)) # Number of division with s_hp spacing

    x_min = parameters[0]
    x = [x_s[0]]
#    x.append(s_hp+ x[0])
    for i in range(n_shp):
        x.append(x[i] + np.sign(x_s[1] - x_s[0])*s_hp)
    x.append(x_s[1])
    x = list(dict.fromkeys(x))
    
    diff_x = [abs(x_2 - x_1) for x_2, x_1 in zip(x, x[1:])]
    
    # Remove hanger at the end if spacing is less than the minimum specified
    for k in range(len(diff_x)):
        if diff_x[k] < x_min:
            index_x_removed = k
            break
    x.remove(x[index_x_removed])
    
    # Remove start hangers
    n_start = int(parameters[1])
    x = [x[0]] + x[1+n_start:len(x)]
    
    # Remove end hangers
    n_end = int(parameters[2])
    if n_end != 0:
        x = x[0:len(x)-n_end-1] + x[len(x)-n_end:len(x)]
    
    # Get coordinates of the connecting points    
    # Linear interpolation to find vertical and transverse coordinate
    if np.sign(x_s[1] - x_s[0]) > 0:
        y = np.interp(x,x_o,y_o)
        z = np.interp(x,x_o,z_o)  
    else:
        y = np.interp(x[::-1],x_o[::-1],y_o[::-1])
        z = np.interp(x[::-1],x_o[::-1],z_o[::-1])
        y = y[::-1]
        z = z[::-1]
    
    # Construct cable
    s_s_cables = []
    for i in range(len(x)-1):
        s = SapModel.CableObj.AddByCoord(x[i],y[i],z[i],x[i+1],y[i+1],z[i+1])
        SapModel.CableObj.SetCableData(s[0], 8, 1, 0, 0, 0, 0)
        # Set cable layout
        s_s_cables.append(s[0])
    
    return x, y, z, s_s_cables