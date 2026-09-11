# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:56:54 2024

@author: hammad.eljisr
"""

import numpy as np


def getShellForcesSAP2000(SapModel,Group,Load_case_combo):
    """
    This function outputs the shell elements forces enveloppe for a group of shell elements
    Input:
        SapModel: SAP Model object
        Group: Group containing the shell elements for which the forces are output
        Load_case_combo: Load case/combiniation considered
    Output:
        F11: F11 forces
        F22: F22 forces
        F12: F11 forces
        M11: M11 moments
        M22: M22 moments
        M12: M12 moments
        joints: Output joint labels 
        steptype: Type of envelope force (minimum or maximum)
    """

    SapModel.SetPresentUnits(6) # Change unit system to kN-m
    # Deselect results for all cases
    ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    # Select desired load case
    ret = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_case_combo)
    if ret == 1: # Load combination instead of load case
        SapModel.Results.Setup.SetComboSelectedForOutput(Load_case_combo)
                
    # Set to enveloppe
    output_options = SapModel.DatabaseTables.GetTableOutputOptionsForDisplay()
    SapModel.DatabaseTables.SetTableOutputOptionsForDisplay(output_options[0],output_options[1],output_options[2],output_options[3],output_options[4],output_options[5],output_options[6],output_options[7],
                                                            output_options[8],output_options[9],output_options[10],output_options[11],output_options[12],output_options[13],output_options[14],
                                                            output_options[15],1,output_options[17])
    
    # Get shell forces table
    t = SapModel.DatabaseTables.GetAvailableTables()
    for i in range(len(t[1])):
        if t[1][i] == 'Element Forces - Area Shells':
            index = i
    shell_forces_table = SapModel.DatabaseTables.GetTableForDisplayArray(t[1][index],'',Group)
    
    # Divide into data rows
    headers = shell_forces_table[2]
    n_rows = shell_forces_table[3]
    rows = np.array_split(shell_forces_table[4],n_rows)
        
    # Get data
    F11 = []
    F22 = []
    F12 = []
    M11 = []
    M22 = []
    M12 = []
    joints = []
    steptype = []
    F11_loc = headers.index('F11')
    F22_loc = headers.index('F22')
    F12_loc = headers.index('F12')
    M11_loc = headers.index('M11')
    M22_loc = headers.index('M22')
    M12_loc = headers.index('M12')
    joint_loc =  headers.index('Joint')
    steptype_loc = headers.index('StepType')
    
    for i in range(len(rows)):
        F11.append(float(rows[i][F11_loc]))
        F22.append(float(rows[i][F22_loc]))
        F12.append(float(rows[i][F12_loc]))
        M11.append(float(rows[i][M11_loc])) 
        M22.append(float(rows[i][M22_loc])) 
        M12.append(float(rows[i][M12_loc])) 
        joints.append(rows[i][joint_loc])
        steptype.append(rows[i][steptype_loc])
        
    return F11,F22,F12,M11,M22,M12,joints,steptype
