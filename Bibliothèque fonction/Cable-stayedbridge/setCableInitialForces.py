# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:19:45 2022

@author: hammad.eljisr
"""

def setCableInitialForces(SapModel,Cable_names,Cables_Ti):
    """
    This function sets the cable initial forces in the SAP2000 model
    Input:
        - SapModel: SAP Model object
        - Cable_names: List containing the names of the cable elements
        - Cables_Ti: Cable initial tensile forces
    """
    for i in range(Cable_names[0]):
        ret = SapModel.CableObj.SetCableData(Cable_names[1][i], 3, 1, 0, 0, Cables_Ti[i])   
        if ret != 0:
            print('Error in assigning initial tension to cable' + Cable_names[1][i])    