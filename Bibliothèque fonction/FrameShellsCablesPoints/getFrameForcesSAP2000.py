# -*- coding: utf-8 -*-
"""
Created on Tue Apr  22 15:56:54 2024

@author: hammad.eljisr
"""

import numpy as np
 
def getFrameForcesSAP2000(SapModel,Group,Load_case_combo,Type):
    """
    This function outputs the forces in a group of frame elements in SAP2000
    Input:
        SapModel: SAP Model object
        Group: Group containing the frame elements for which the forces are output
        Load_case_combo: Load case/combination considered
        Type: 0 for Envelope, 1 for Correspondence 
        
    Output:
        P, V2, V3, T, M2, M3: Frame element forces
        Frame, Station: Frame element label, station
        output_type: Max/Min if envelope chosen; MaxP/ M3/M2/V3/V2/T if correspondence chosen
    """

    # Load case/combo
    SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    SapModel.Results.Setup.SetCaseSelectedForOutput(Load_case_combo,True)
    SapModel.Results.Setup.SetComboSelectedForOutput(Load_case_combo,True)
    
    # Set load combination type
    output_options = SapModel.DatabaseTables.GetTableOutputOptionsForDisplay()
    SapModel.DatabaseTables.SetTableOutputOptionsForDisplay(output_options[0],output_options[1],output_options[2],output_options[3],output_options[4],output_options[5],output_options[6],output_options[7],
                                                            output_options[8],output_options[9],output_options[10],output_options[11],output_options[12],output_options[13],output_options[14],
                                                            output_options[15],2*Type+1,output_options[17])
    
    # Get frame element forces table    
    frame_element_forces_table = SapModel.DatabaseTables.GetTableForDisplayArray('Element Forces - Frames','',Group)
    
    # Divide into data rows
    headers = frame_element_forces_table[2]
    n_rows = frame_element_forces_table[3]
    rows = np.array_split(frame_element_forces_table[4],n_rows)
        
    # Get data
    P = []
    V2 = []
    V3 = []
    T = []
    M2 = []
    M3 = []
    Frame = []
    Station = []
    output_type = []
    
    # Indices
    # Forces
    P_h = headers.index('P')
    V2_h = headers.index('V2')
    V3_h = headers.index('V3')
    T_h = headers.index('T')
    M2_h =  headers.index('M2')
    M3_h =  headers.index('M3')
    Frame_h = headers.index('Frame')
    Station_h = headers.index('Station')
    if 'StepType' in headers:
        output_type_h = headers.index('StepType')
    else:
        output_type_h = headers.index('CaseType')

    # Data
    for i in range(len(rows)):
        P.append(float(rows[i][P_h]))
        V2.append(float(rows[i][V2_h]))
        V3.append(float(rows[i][V3_h]))
        T.append(float(rows[i][T_h]))
        M2.append(float(rows[i][M2_h]))
        M3.append(float(rows[i][M3_h]))
        Frame.append(rows[i][Frame_h])
        Station.append(float(rows[i][Station_h]))
        output_type.append(rows[i][output_type_h])
        
    return P,V2,V3,T,M2,M3,Frame,Station,output_type
