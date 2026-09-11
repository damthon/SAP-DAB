# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:19:45 2022

@author: hammad.eljisr
"""

import numpy as np
import copy
from setCableAreas import setCableAreas
from setCableInitialForces import setCableInitialForces
from getCableAreas import getCableAreas
from getCableAxialForces import getCableAxialForces

def iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters):
    """
    This function iterates over the cross-sectional areas and forces in the cables of a cable-stayed bridge in order to limit the vertical deflection
    of the deck anchor points (tolerance = 1%). The function returns the updated cable cross-sectional area, initial tensile force and stress ratios at the last converged step 
    Input:
        - SapModel: SAP Model object
        - Load_Case: Considered load case
        - Cable_Parameters: Parameters of the cables defined as follows: 
            1- Cable_Parameters[0]: List containing the names of the cable elements: first element is the number of cables, second element is a tuple of the cable names
            2- Cable_Parameters[1]: List containing the cross-sectional of the cable elements (initial assignment)
            3- Cable_Parameters[2]: List containing the stress ratios in the cable elements (initial assignment) 
        - Cable_Properties: Properties of the cables defined as follows:
            1- Cable_Properties[0]: Cable material 
            2- Cable_Properties[1]: Ultimate tensile strength of the cables
            3- Cable_Properties[2]: Cross-sectional area of the strands, None if the cross-sectional area of the cables is not iterated over
            4- Cable_Properties[3]: Minimum number of strands to be used, None if the cross-sectional area of the cables is not iterated over
            5- Cable_Properties[4]: Maximum number of strands to be used, None if the cross-sectional area of the cables is not iterated over
            6- Cable_Properties[5]: Minimum allowable stress ratio in the cables
            7- Cable_Properties[6]: Maximum allowabe stress ratio in the cables
        - Iteration_Parameters: Parameters for the iteration procedure defined as follows:
            1- Iteration_Parameters[0]: List containing the targeted displacements (each displacement represents a convergence step)
            2- Iteration_Parameters[1]: Maximum number of iterations 
            3- Iteration_Parameters[2]: Boolean for iteration over the cross-sectional area (1 for iterate over cross-sectional area, 0 otherwise)
    Output:
        - A_cables: Updated cross-sectional area of the cables at convergence
        - Cables_Ti: Updated initial tensile force in the cables at convergence
        - Cables_S: Updated stress ratios in the cables at convergence
        - Deck_v_allow: Maximum vertical displacement of the deck at convergences
    """
    tol = 0.01
    
    Cable_names = Cable_Parameters[0]
    A_cables = Cable_Parameters[1]
    Cables_Ti = Cable_Parameters[2]
    Cables_S = Cable_Parameters[3]
    Cable_mat = Cable_Properties[0]
    f_u_cables = Cable_Properties[1]
    A_strands = Cable_Properties[2]
    A_strands_min = Cable_Properties[3]
    A_strands_max = Cable_Properties[4]
    Cable_si_min = Cable_Properties[5]
    Cable_si_max = Cable_Properties[6] 
    Deck_v_allow_v = Iteration_Parameters[0]
    max_iter = Iteration_Parameters[1]
    iter_Area = Iteration_Parameters[2]
    
    # Initialization
    A_cables_o = A_cables
    Cables_Ti_o = Cables_Ti
    Cables_S_o = Cables_S
    counter_a = 0
    step = 0 
    step_completed = 0
    Deck_v_allow = Deck_v_allow_v[0]
    Deck_v_allow_o = Deck_v_allow
    
    # Iterations to obtaine the force in the cables
    for k in range(max_iter):
        # Iterate on cross-sectional area to obtain stress ratios within the limits
        if step_completed > 1 and iter_Area == 1:
            for i in range(Cable_names[0]):  
                Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][i])
                if (Cables_S[i] < Cable_si_min/(1+tol)) and Cables_S[i] > 0:
                    F_A = Cables_S[i]/Cable_si_min
                    counter_a = counter_a + 1
                elif (Cables_S[i] > Cable_si_max*(1+tol)):
                    F_A = Cables_S[i]/Cable_si_max
                    counter_a = counter_a + 1
                else:
                    F_A = 1
                N_strands = min(max(A_cables[i]*F_A/A_strands,A_strands_min),A_strands_max) # Number of required strands (unrounded) 
                A_cables[i]= N_strands*A_strands 
                SapModel.PropCable.SetProp(Cables_assignments[0], Cable_mat, A_cables[i]*F_A)  
        step_completed = 0         
        
        # Get new cable cross-sectional areas
        A_cables = getCableAreas(SapModel,Cable_names,Cable_mat)
                
        # Run analysis
        SapModel.Analyze.RunAnalysis()
        
        # Deselect results for all cases
        SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
        # Select desired load case
        SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
        
        # Track displacements at deck anchor points
        Deck_Anchor_V_Disp = []            # Initialize vertical displacements in at the deck anchor points
        for i in range(Cable_names[0]): 
            Deck_Cable_Joints_Disp = SapModel.Results.JointDispl(Deck_Cable_Joints[i],0)
            Deck_Anchor_V_Disp.append(Deck_Cable_Joints_Disp[8][0])
        print('***********************************************************************************************************************************************')
        print('Anchor points vertical displacements:')
        print (Deck_Anchor_V_Disp)  
        print('***********************************************************************************************************************************************')
        # Track axial force in the cables due to permanent load
        Cables_Fo = getCableAxialForces(SapModel,Cable_names)
        # Stress ratios in the cables   
        Cables_S = np.array(Cables_Fo)/np.array(A_cables)/f_u_cables  
        
        # Unlock model
        SapModel.SetModelIsLocked(0)
        
        # Update step criteria
        Deck_v_allow = Deck_v_allow_v[step]
        
        # Track adjustments
        counter_i = 0
        counter_d = 0
        
        # Adjust maximum area and tension in cables to maintain the 0.4fu_cables (bisection method)
        for j in range(len(Deck_Anchor_V_Disp)):
            if (Deck_Anchor_V_Disp[j]< -Deck_v_allow*(1+tol)) and Cables_S[j] > 0:
                SF = abs(Deck_Anchor_V_Disp[j]/Deck_v_allow)
                counter_i = counter_i + 1
            elif (Deck_Anchor_V_Disp[j] > Deck_v_allow*(1+tol)) and Cables_S[j] > 0:
                SF = 1/abs(Deck_Anchor_V_Disp[j]/Deck_v_allow)
                counter_d = counter_d + 1
            else:
                SF = 1.0 
            Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][j])
            if SF < 1.0:
                Cables_Ti[j] = Cables_Ti[j]*SF
                SapModel.CableObj.SetCableData(Cable_names[1][j], 3, 1, 0, 0, Cables_Ti[j])
                print('Tensile force of cable ' + Cable_names[1][j] + ' decreased by a factor = ' + str(SF))
            elif SF > 1.0: 
                # Adjust force in the cable
                Cables_Ti[j] = Cables_Ti[j]*SF
                SapModel.CableObj.SetCableData(Cable_names[1][j], 3, 1, 0, 0, Cables_Ti[j])
                print('Tensile force of cable ' + Cable_names[1][j] + ' increased by a factor = ' + str(SF))
        print('Number of cables the tensile force of which shall be increased:' + str(counter_i))
        print('Number of cables the tensile force of which shall be decreased:' + str(counter_d))
        print('***********************************************************************************************************************************************')
        print('Stress ratios:')
        print(Cables_S)
        for n in range(len(Cables_S)):
            if SapModel.CableObj.GetCableData(Cable_names[1][n])[6][10] > 1.0:
                print('WARNING: Cable ' + Cable_names[1][n] + " is slack")
                # Assign cable parameters of the previous converged step
                setCableAreas(SapModel,Cable_names,A_cables_o,Cable_mat)
                setCableInitialForces(SapModel,Cable_names,Cables_Ti_o)  
                print('Cable parameters for the previous convergence step assigned')    
                print('Maximum vertical displacement of the deck within ' + str(Deck_v_allow_o) + ' mm')
                print('***********************************************************************************************************************************************')
                return A_cables_o, Cables_Ti_o, Cables_S_o, Deck_v_allow_o
            elif iter_Area == 0:
                for l in range(len(Cables_S)):
                    if (Cables_S[l] > 0 and Cables_S[l] < Cable_Properties[5]/1.2) or Cables_S[l] > Cable_Properties[6]*1.2:
                       # Asign cable parameters of the previous converged step
                       setCableAreas(SapModel,Cable_names,A_cables_o,Cable_mat)
                       setCableInitialForces(SapModel,Cable_names,Cables_Ti_o)
                       print('Stress ratios exceeds 20% of the limits') 
                       print('Cable parameters for the previous convergence step assigned')    
                       print('Maximum vertical displacement of the deck within ' + str(Deck_v_allow_o) + ' mm')
                       print('***********************************************************************************************************************************************')
                       return A_cables_o, Cables_Ti_o, Cables_S_o, Deck_v_allow_o
        if counter_i == 0 and counter_d == 0:
            step_completed = 1
            print('All anchor point displacements are within ' + str(Deck_v_allow) + ' mm')
            print('Convergence in ' + str(k) + ' iterations')
            if iter_Area == 1:
                for l in range(len(Cables_S)):
                    if Cables_S[l] > Cable_si_max*(1+tol):
                        print('Area of cable ' + Cable_names[1][l] + ' shall be increased') 
                        step_completed = step_completed + 1
                    elif Cables_S[l] < Cable_si_min/(1+tol) and Cables_S[l] > 0:
                        print('Area of cable ' + Cable_names[1][l] + ' shall be decreased') 
                        step_completed = step_completed + 1
            if step_completed == 1:
                if iter_Area == 1:
                    print('Stress ratios within the limits')
                    # Convergence values for the step
                A_cables_o = copy.copy(A_cables)
                Cables_Ti_o = copy.copy(Cables_Ti)
                Deck_v_allow_o = copy.copy(Deck_v_allow)
                Cables_S_o = copy.copy(Cables_S)
                step = step + 1
                if Deck_v_allow == Deck_v_allow_v[len(Deck_v_allow_v)-1]:
                    print('Target anchor points displacement = ' + str(Deck_v_allow) + ' mm attained')
                    break 
        elif k == max_iter:
            print('***********************************************************************************************************************************************')
            print('Convergence failed at step ' + str(step) + '- Try increasing the number of convergence steps or iterations') 
            print('Maximum displacement at the anchor ends = ' + str(max(Deck_Anchor_V_Disp)) + ' mm')  
            print('Minumum displacement at the anchor ends = ' + str(min(Deck_Anchor_V_Disp)) + ' mm')  
            print('***********************************************************************************************************************************************')
    return A_cables, Cables_Ti, Cables_S, Deck_v_allow
