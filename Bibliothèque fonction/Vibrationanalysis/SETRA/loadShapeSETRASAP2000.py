# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 14:45:34 2025

@author: hammad.eljisr
"""

import numpy as np
from getGroupFrameObjSAP2000 import getGroupFrameObjSAP2000
from getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000

def loadShapeSETRASAP2000(SapModel,Case,Deck_slab_group,Deck_ele_type,Direction):
    """
    This function creates the load patterns for the dynamic analysis under pedestrain loading according to the SETRA guide. The loads are applied in the shape of the critical modes 
    for the direction specified.
    Input:
        - SapModel: SAP model object
        - Case: Load case 1,2, or 3
        - Deck_slab_group: Group containing the deck slab elements and nodes, all deck elements in case frame elements are used to model the deck
        - Deck_ele_type: 0 for frame elements, 1 for shell elements
        - Direction: Direction considered: 'V' for vertical and 'La' for the lateral (transverse) mode
        
    Output:
        - modes_SETRA: Modes to which SETRA loads shapes are applied
        - frequencies_SETRA: Frequencies of the modes to which the SETRA loads are applied
        - SETRA_patterns: Names of the created SETRA load patterns/cases
    """     
    
    # Run modal analysis only
    SapModel.SetModelIsLocked(False) # Unlock model
    SapModel.Analyze.SetRunCaseFlag("MODAL",False,'All')
    SapModel.Analyze.SetRunCaseFlag("MODAL",True)
    SapModel.Analyze.RunAnalysis()
    # Get modal periods
    Modal_analysis = SapModel.Results.ModalPeriod(1,'MODAL','Mode')
    n_modes = Modal_analysis[0] # Number of modes
    modes = Modal_analysis[3] # Mode numbers
    frequencies = Modal_analysis[5] # Modal frequencies
    if Case == 3: # To account for effect of second harmonic
        if Direction == 'V' and frequencies[n_modes-1] < 5.0:
            print('Maximum modal frequency less than 2.6 Hz. Increase the number of output modes')
        if Direction == 'La' and frequencies[n_modes-1] < 2.5:
            print('Maximum modal frequency less 1.3 Hz. Increase the number of output modes')   
    else:        
        if Direction == 'V' and frequencies[n_modes-1] < 2.6:
            print('Maximum modal frequency less than 2.6 Hz. Increase the number of output modes')
        if Direction == 'La' and frequencies[n_modes-1] < 1.3:
            print('Maximum modal frequency less 1.3 Hz. Increase the number of output modes')    
    
    # Get modes in the range of critical frequencies
    modes_in_range = []
    frequencies_in_range = []
    if Case == 3: # To account for effect of second harmonic
        # For the vertical direction
        if Direction == 'V':
            for i in range(len(frequencies)):
                if frequencies[i] >= 2.6 and frequencies[i] <= 5:
                    modes_in_range.append(modes[i])
                    frequencies_in_range.append(frequencies[i])
        # For the transverse direction
        if Direction == 'La':
            for i in range(len(frequencies)):
                if frequencies[i] >= 1.3 and frequencies[i] <= 2.5:
                    modes_in_range.append(modes[i])
                    frequencies_in_range.append(frequencies[i])
    else:
        # For the vertical direction
        if Direction == 'V':
            for i in range(len(frequencies)):
                if frequencies[i] >= 1.0 and frequencies[i] <= 2.6:
                    modes_in_range.append(modes[i])
                    frequencies_in_range.append(frequencies[i])
        # For the transverse direction
        if Direction == 'La':
            for i in range(len(frequencies)):
                if frequencies[i] >= 0.3 and frequencies[i] <= 1.3:
                    modes_in_range.append(modes[i])
                    frequencies_in_range.append(frequencies[i])
      
    # Get modal displacements for each mode
    SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    SapModel.Results.Setup.SetCaseSelectedForOutput("MODAL",True)
    Modal_shapes = SapModel.Results.ModeShape(Deck_slab_group,2)
    U1 = Modal_shapes[6] # Longitudinal direction
    U2 = Modal_shapes[7] # Transverse direction
    U3 = Modal_shapes[8] # Vertical direction
    U_Long = [[] for _ in range(len(modes))] # Longitudinal direction
    U_Trans = [[] for _ in range(len(modes))] # Transverse direction
    U_Vert = [[] for _ in range(len(modes))] # Vertical direction
    nodes = [[] for _ in range(len(modes))] # Nodes
    for m in range(len(modes)):
        for i in range(len(Modal_shapes[2])):
            if Modal_shapes[5][i] == modes[m]:
                U_Long[m].append(U1[i])
                U_Trans[m].append(U2[i])
                U_Vert[m].append(U3[i])
                nodes[m].append(Modal_shapes[2][i])
    
    # Sort nodes in order of increasing x
    x_nodes = [[] for _ in range(len(modes))] # Nodes
    for m in range(len(modes)):
        for i in range(len(nodes[m])):
            x_nodes[m].append(SapModel.PointObj.GetCoordCartesian(nodes[m][i])[0])
    # Sort indices
    for m in range(len(modes)):
        s_indices = np.argsort(x_nodes[m])
        x_nodes[m] = np.array(x_nodes[m])[s_indices]
        nodes[m] = np.array(nodes[m])[s_indices]
        U_Long[m] = np.array(U_Long[m])[s_indices]
        U_Trans[m] = np.array(U_Trans[m])[s_indices]
        U_Vert[m] = np.array(U_Vert[m])[s_indices]
    
    # Assign dominant mode ('V', 'La', or 'Lo')
    dominant_mode = []
    for m in range(len(modes)):
        if max(abs(U_Vert[m])) > max(abs(U_Trans[m])) and max(abs(U_Vert[m])) > max(abs(U_Long[m])) and max(abs(U_Vert[m])) > 0.01:
            dominant_mode.append('V') # Vertical mode
        elif max(abs(U_Trans[m])) > max(abs(U_Vert[m])) and max(abs(U_Trans[m])) > max(abs(U_Long[m])) and max(abs(U_Trans[m])) > 0.01 :
            dominant_mode.append('La') # Lateral (transverse) mode
        elif max(abs(U_Long[m])) > 0.01:
            dominant_mode.append('Lo') # Longitudinal mode
        else:
            dominant_mode.append('Local mode') # Local modes to be ignored
    
    # Get modes to which the SETRA loads will be applied
    modes_SETRA = [] # Modes to which the SETRA load shapes are applied
    for i in range(len(modes_in_range)):
        mode_index = modes.index(modes_in_range[i])
        if dominant_mode[mode_index] == Direction:
            modes_SETRA.append(modes_in_range[i])
    
    if Deck_ele_type == 0:
        # Get frame objects in the group
        frames = getGroupFrameObjSAP2000(SapModel,Deck_slab_group)
        frame_nodes = [[] for _ in range(len(frames))]
        # Sort nodes by each element
        for i in range(len(nodes[0])):
            f = SapModel.PointObj.GetConnectivity(nodes[0][i])[2]
            for j in range(len(f)):
                try:
                    f_index = frames.index(f[j]) # Index of the frame with the nodes
                    frame_nodes[f_index].append(nodes[0][i])
                except:
                    pass
        
        # Split frame elements (positive and negative U)
        if Direction == 'V':
            U = U_Vert
        elif Direction == 'La':
            U = U_Trans
        else:
            U = U_Long 
        frame_direction = [[] for _ in range(len(modes_SETRA))] # Load direction in each frame
        for m in range(len(modes_SETRA)): 
            mode_index = modes.index(modes_SETRA[m])
            for i in range(len(frame_nodes)):
                U_s = U[mode_index][list(nodes[mode_index]).index(frame_nodes[i][0])] # Displacement at start of frame
                U_e = U[mode_index][list(nodes[mode_index]).index(frame_nodes[i][1])] # Displacement at end of frame
                if U_s + U_e > 0:
                    frame_direction[m].append(1)
                elif U_s + U_e < 0:
                    frame_direction[m].append(-1)
                else: 
                    frame_direction[m].append(0)
    else:
        # Get area objects in the group
        areas = getGroupAreaObjSAP2000(SapModel,Deck_slab_group)
        area_nodes = [[] for _ in range(len(areas))]
        # Sort nodes by each element
        for i in range(len(nodes[0])):
            a = SapModel.PointObj.GetConnectivity(nodes[0][i])[2]
            for j in range(len(a)):
                try: # Only area elements
                    a_index = areas.index(a[j]) # Index of the area with the nodes
                    area_nodes[a_index].append(nodes[0][i])
                except:
                    pass
        
        # Split area elements (positive and negative U)
        if Direction == 'V':
            U = U_Vert
        elif Direction == 'La':
            U = U_Trans
        else:
            U = U_Long 
        area_direction = [[] for _ in range(len(modes_SETRA))] # Load direction in each frame
        for m in range(len(modes_SETRA)): 
            mode_index = modes.index(modes_SETRA[m])
            for i in range(len(area_nodes)):
                U_total = 0
                for n in range(len(area_nodes[i])):
                    U_total = U_total +  U[mode_index][list(nodes[mode_index]).index(area_nodes[i][n])] # Total nodal displacement
                if U_total > 0:
                    area_direction[m].append(1)
                elif U_total < 0:
                    area_direction[m].append(-1)
                else:
                    area_direction[m].append(0)
    
    # Create SETRA load pattern and apply load
    SETRA_patterns = [[] for _ in range(len(modes_SETRA))] # SETRA load patterns
    SapModel.SetModelIsLocked(False) # Unlock model
    
    # Load patterns
    if Direction == 'V':
        global_dir = 6 # Vertical along Z
    elif Direction == 'La':
        global_dir = 5 # Transversal along Y
    else:
        global_dir = 4 # Longitudinal along X
    for m in range(len(modes_SETRA)):
        SETRA_patterns[m] = 'SETRA Mode_' + str(int(modes_SETRA[m])) + Direction
        SapModel.LoadPatterns.Add(SETRA_patterns[m],3)
        # Assign loads
        if Deck_ele_type == 0:
            for f in range(len(frames)):
                SapModel.FrameObj.SetLoadDistributed(frames[f],SETRA_patterns[m],1,global_dir,0,1,frame_direction[m][f],frame_direction[m][f],'Global',1,1,0)
        else:
            for a in range(len(areas)):  
                SapModel.AreaObj.SetLoadUniform(areas[a],SETRA_patterns[m],area_direction[m][a],global_dir,True,'Global',0)
    
    # Frequencies SETRA
    frequencies_SETRA = [[] for _ in range(len(modes_SETRA))] # SETRA load patterns
    for  m in range(len(modes_SETRA)):
        frequencies_SETRA[m] = frequencies[modes.index(modes_SETRA[m])]
    
    # Remove linear static load cases created
    for s in range(len(SETRA_patterns)):
        SapModel.LoadCases.Delete(SETRA_patterns[s])
        
    return modes_SETRA, frequencies_SETRA, SETRA_patterns
    
        
        
            
        
        
        
        
        
    
    
    
    
