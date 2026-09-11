# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:19:45 2022

@author: hammad.eljisr
"""

def getCableAreas(SapModel,Cable_names,Cable_mat):
    """
    This function obtains the cable cross-sectional areas from the SAP2000 model
    Input:
        - SapModel: SAP Model object
        - Cable_names: List containing the names of the cable elements
        - Cable_mat: Cable material
    Output:
        - A_cables: Cable cross-sectional areas
    """
    # Get new cable cross-sectional areas
    A_cables = []
    for i in range(Cable_names[0]): 
        Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][i])
        A_cables.append(SapModel.PropCable.GetProp(Cables_assignments[0], Cable_mat)[1])
    return A_cables