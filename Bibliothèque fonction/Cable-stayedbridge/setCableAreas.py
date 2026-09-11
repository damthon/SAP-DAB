# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:19:45 2022

@author: hammad.eljisr
"""

def setCableAreas(SapModel,Cable_names,A_cables,Cable_mat):
    """
    This function sets the cable cross-sectional areas in the SAP2000 model
    Input:
        - SapModel: SAP Model object
        - Cable_names: List containing the names of the cable elements
        - A_cables: Cable cross-sectional areas
        - Cable_mat: Cable material
    """
    for i in range(Cable_names[0]): 
        Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][i])
        ret = SapModel.PropCable.SetProp(Cables_assignments[0], Cable_mat, A_cables[i])
        if ret != 0:
            print('Error in assigning cross-sectional area to cable ' + Cable_names[1][i])   