# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:19:45 2022

@author: hammad.eljisr
"""

def getCableInitialForces(SapModel,Cable_names):
    """
    This function obtains the cable initial tensile forces from the SAP2000 model
    Input:
        - SapModel: SAP Model object
        - Cable_names: List containing the names of the cable elements
    Output:
        - Cables_Ti: Cable initial tensile forces (end i)
    """
    Cables_Ti = []
    for i in range(Cable_names[0]): 
        Cables_Ti.append(SapModel.CableObj.GetCableData(Cable_names[1][i])[6][0])
    return Cables_Ti
