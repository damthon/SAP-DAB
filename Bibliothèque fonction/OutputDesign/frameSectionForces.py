# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:11:26 2022

@author: hammad.eljisr
"""

def frameSectionForces(SapModel,frame_labels,Load_combination):
    """
    This function reads the frame section forces from the SAP2000 model.
    Input:
        - SapModel: SAP Model object
        - section_labels: Frame section labels in the SAP2000 model
        - Load_combination: Load combination for which the frame section forces are obtained
    Output:
        P: Axial forces along in each frame
        M: Bending moments in each frame
        V: Shear force in each frame
    """

    # Deselect results for all cases
    SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    # Select desired load case
    SapModel.Results.Setup.SetComboSelectedForOutput(Load_combination)

    # Get deck forces
    P = [[] for _ in range(len(frame_labels))]
    M =  [[] for _ in range(len(frame_labels))]
    V =  [[] for _ in range(len(frame_labels))]
    for i in range(len(frame_labels)):   
        frame_forces = SapModel.Results.FrameForce(frame_labels[i],0)
        if frame_forces[len(frame_forces)-1] != 0:
            print('No results found: Run analysis')
        else:
            for j in range(frame_forces[0]):
                P[i].append(frame_forces[8][j])
                M[i].append(frame_forces[13][j])
                V[i].append(frame_forces[9][j])
    
    return P,M,V
