# -*- coding: utf-8 -*-
"""
Created on Tues Jun  04 15:56:54 2024

@author: hammad.eljisr
"""

import numpy as np

def getShellDesignSAP2000(SapModel,Group,Load_case_combo,type_combo):
    """
    This function outputs the shell design data for a group of shell elements
    Input:
        SapModel: SAP Model object
        Group: Group containing the shell elements for which the design is output
        Load_case_combo: Load case/combination considered
        type_combo: Combination type: 1 for Enveloppe, 3 for correspondence. Enveloppe also calculates each combination independently 
        and is much faster but does not include the correction forces in the last iteration, Delta_N
    Output:
        N11d_top: Design force in the top layer (1 direction)
        N11d_bot: Design force in the bottom layer (1 direction)
        N22d_top: Design force in the top layer (2 direction)
        N22d_bot: Design force in the bottom layer (2 direction)
        joints: Ouput joint labels 
    """

    SapModel.SetPresentUnits(6) # Change unit system to kN-m
    
    # Set load case/combo for output
    SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    r = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_case_combo)
    if r == 1: 
        SapModel.Results.Setup.SetComboSelectedForOutput(Load_case_combo) 
        
    # Set to enveloppe
    output_options = SapModel.DatabaseTables.GetTableOutputOptionsForDisplay()
    SapModel.DatabaseTables.SetTableOutputOptionsForDisplay(output_options[0],output_options[1],output_options[2],output_options[3],output_options[4],output_options[5],output_options[6],output_options[7],
                                                            output_options[8],output_options[9],output_options[10],output_options[11],output_options[12],output_options[13],output_options[14],
                                                            output_options[15],type_combo,output_options[17])
    
    # Get shell design table
    t = SapModel.DatabaseTables.GetAvailableTables()
    shell_design_table = SapModel.DatabaseTables.GetTableForDisplayArray(t[1][len(t[1])-1],'',Group)
    
    # Divide into data rows
    headers = shell_design_table[2]
    n_rows = shell_design_table[3]
    rows = np.array_split(shell_design_table[4],n_rows)
        
    # Get data
    N11d_top = []
    N11d_bot = []
    N22d_top = []
    N22d_bot = []
    joints = []
    N11d_top_loc = headers.index('Nd11Top')
    N11d_bot_loc = headers.index('Nd11Bot')
    N22d_top_loc = headers.index('Nd22Top')
    N22d_bot_loc = headers.index('Nd22Bot')
    joint_loc =  headers.index('Joint')
    
    for i in range(len(rows)):
        if rows[i][len(rows[i])-1] == 'No Messages':
            N11d_top.append(float(rows[i][N11d_top_loc]))
            N11d_bot.append(float(rows[i][N11d_bot_loc]))
            N22d_top.append(float(rows[i][N22d_top_loc]))
            N22d_bot.append(float(rows[i][N22d_bot_loc])) 
        else: # Desugn cannot be conducted assign 1e6
            N11d_top.append(np.nan)
            N11d_bot.append(np.nan)
            N22d_top.append(np.nan)
            N22d_bot.append(np.nan) 
        joints.append(rows[i][joint_loc])
    
    # Get unique forces nR at each joint
    I_joints = np.argsort(joints)
    joints = list(np.array(joints)[I_joints])
    N11d_top = list(np.array(N11d_top)[I_joints])
    N11d_bot = list(np.array(N11d_bot)[I_joints])
    N22d_top = list(np.array(N22d_top)[I_joints])
    N22d_bot = list(np.array(N22d_bot)[I_joints])
    N11d_top_ENV = [N11d_top[0]]
    N11d_bot_ENV = [N11d_bot[0]]
    N22d_top_ENV = [N22d_top[0]]
    N22d_bot_ENV = [N22d_bot[0]]
    joints_ENV = [joints[0]]
    N11d_top_max = 0
    N11d_bot_max = 0
    N22d_top_max = 0
    N22d_bot_max = 0
    for i in range(1,len(joints)):
        if joints[i] == joints[i-1]:
            N11d_top_max = max(N11d_top[i],N11d_top_max)
            N11d_bot_max = max(N11d_bot[i],N11d_bot_max)
            N22d_top_max = max(N22d_top[i],N22d_top_max)
            N22d_bot_max = max(N22d_bot[i],N22d_bot_max)
        else:
            N11d_top_ENV.append(N11d_top_max)
            N11d_bot_ENV.append(N11d_bot_max)
            N22d_top_ENV.append(N22d_top_max)
            N22d_bot_ENV.append(N22d_bot_max)
            joints_ENV.append(joints[i-1])
            N11d_top_max = 0
            N11d_bot_max = 0
            N22d_top_max = 0
            N22d_bot_max = 0
    N11d_top = N11d_top_ENV
    N11d_bot = N11d_bot_ENV
    N22d_top = N22d_top_ENV
    N22d_bot = N22d_bot_ENV
    joints = joints_ENV
        
    return N11d_top,N11d_bot,N22d_top,N22d_bot,joints
