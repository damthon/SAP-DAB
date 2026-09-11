# -*- coding: utf-8 -*-
"""
Created on Tues Jun  04 15:56:54 2024

@author: hammad.eljisr
"""

import numpy as np
 
def getSectionCutForcesSAP2000(SapModel,Cut_names,Group,Load_case_combo,Delta_location,Type):
    """
    This function outputs the shell design data for a group of shell elements
    Input:
        SapModel: SAP Model object
        Cut_names: Section cut names
        Group: Group containing the shell elements for which the design is output
        Load_case_combo: Load case/combination considered
        Delta_location: The [d2,d3] about which the forces are calculated from the default location in local axes directions (in section cut plane)
        Type: 0 for Envelope, 1 for Correspondence 
        
    Output:
        P, V2, V3, T, M2,M3: Section cut forces
        X, Y, Z: Coordinates about which the section cut forces are calculated
        output_type: Max/Min if envelope chosen; MaxP/ M3/M2/V3/V2/T if correspondence chosen
    """

    SapModel.SetPresentUnits(6) # Change unit system to kN-m
    
    # Load case/combo
    SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    SapModel.Results.Setup.SetCaseSelectedForOutput(Load_case_combo,True)
    SapModel.Results.Setup.SetComboSelectedForOutput(Load_case_combo,True)
    
    # Set load combination type
    output_options = SapModel.DatabaseTables.GetTableOutputOptionsForDisplay()
    SapModel.DatabaseTables.SetTableOutputOptionsForDisplay(output_options[0],output_options[1],output_options[2],output_options[3],output_options[4],output_options[5],output_options[6],output_options[7],
                                                            output_options[8],output_options[9],output_options[10],output_options[11],output_options[12],output_options[13],output_options[14],
                                                            output_options[15],2*Type+1,output_options[17])
    
    # Select all section cuts
    SapModel.Results.Setup.SelectAllSectionCutsForOutput(False)
    for i in range(len(Cut_names)):
        SapModel.Results.Setup.SetSectionCutSelectedForOutput(Cut_names[i], True)
   
    # Get section cuts table    
    section_cut_results_table = SapModel.DatabaseTables.GetTableForDisplayArray('Section Cut Forces - Design','',Group)
    
    # Divide into data rows
    headers = section_cut_results_table[2]
    n_rows = section_cut_results_table[3]

    # Get data
    P = []
    V2 = []
    V3 = []
    T = []
    M2 = []
    M3 = []
    X = []
    Y  = []
    Z = []
    output_type = []

    if n_rows == 0:
        # Table vide : aucun resultat pour ce(s) Cut_names/Group/Load_case_combo
        # (cas normal documente par l'API : "If there is nothing to be shown
        # in the table then no data is returned"), pas une erreur en soi -
        # on retourne des listes vides plutot que de planter sur array_split.
        return P,V2,V3,T,M2,M3,X,Y,Z,output_type

    rows = np.array_split(section_cut_results_table[4],n_rows)

    # Indices
    # Forces
    P_i = headers.index('P')
    V2_i = headers.index('V2')
    V3_i = headers.index('V3')
    T_i = headers.index('T')
    M2_i =  headers.index('M2')
    M3_i =  headers.index('M3')
    # Location at which forces are calculated
    X_i =  headers.index('GlobalX')
    Y_i =  headers.index('GlobalY')
    Z_i =  headers.index('GlobalZ') 
    if 'StepType' in headers:
        output_type_i = headers.index('StepType')
    else:
        output_type_i = headers.index('CaseType')
    
    # Data
    for i in range(len(rows)):
        P.append(float(rows[i][P_i]))
        V2.append(float(rows[i][V2_i]))
        V3.append(float(rows[i][V3_i]))
        T.append(float(rows[i][T_i]))
        M2.append(float(rows[i][M2_i]))
        M3.append(float(rows[i][M3_i]))
        X.append(float(rows[i][X_i]))
        Y.append(float(rows[i][Y_i]))
        Z.append(float(rows[i][Z_i]))
        output_type.append(rows[i][output_type_i])
   
    # Adjusted data about the specified location
    for i in range(len(rows)):
        Y[i] = Y[i] + Delta_location[0]
        Z[i] = Z[i] + Delta_location[1]
        M3[i] = M3[i]+ P[i]*Delta_location[1]
        M2[i] = M2[i]+ P[i]*Delta_location[0]
        T[i] = T[i] + V3[i]*Delta_location[1] + V2[i]*Delta_location[0]
    if Delta_location != [0,0] and Type == 0:
        print('Adjustment of forces is not recommended for the envelope of forces')
        
    return P,V2,V3,T,M2,M3,X,Y,Z,output_type
