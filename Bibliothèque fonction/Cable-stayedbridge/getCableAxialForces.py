# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:19:45 2022

@author: hammad.eljisr
"""

def getCableAxialForces(SapModel,Cable_names):
    """
    This function obtains the cable tensile forces from the SAP2000 model
    Input:
        - SapModel: SAP Model object
        - Cable_names: List containing the names of the cable elements
    Output:
        - Cables_Fo: Cable tensile forces
    """
    Cables_Fo = []
    for i in range(Cable_names[0]): 
        Cable_Force = SapModel.Results.FrameForce(Cable_names[1][i],1)[8][0] 
        Cables_Fo.append(Cable_Force)
    return Cables_Fo
