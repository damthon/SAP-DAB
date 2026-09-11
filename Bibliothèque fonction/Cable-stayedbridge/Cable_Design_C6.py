# -*- coding: utf-8 -*-
"""
Spyder Editor

This script
"""

import os
import sys
import comtypes.client
import numpy as np
import math 
from iterateCableAreasForces import iterateCableAreasForces
from tabulate import tabulate
from setCableAreas import setCableAreas
from setCableInitialForces import setCableInitialForces
from getCableAreas import getCableAreas
from getCableAxialForces import getCableAxialForces


"""
Input
"""
Unit_sytem = 'N_mm_C'  # INPUT FORMAT: Force_displacement_Temperature  (Force = lb, Kip, KN, Kgf, N, Tonf; Distance = ft, in, mm, m, cm, Temperature = F,C)
# Concrete material (C50/60)
E_c = 38700   # Modulus of elasiticy
nu_c = 0.2    # Poisson ratio
alpha_c = 9.9e-6 # Coefficient of thermal expansion of concrete 
w_c = 2.5e-5     # Weight of concrete per unit volume (N/mm3)

# Cables properties
E_s = 195000   # Modulus of elasiticy
nu_s = 0.3     # Poisson ratio
alpha_s = 1.0e-5   # Coefficient of thermal expansion of concrete 
w_s = 7.85e-5      # Weight of steel per unit volume (N/mm3)
f_u_cables = 1860  # Ultimate strength of the cables
A_strands = 150    # Area of 1 cable strand 
Cable_si_max = 0.4   # Maximum allowable cable tension as a fraction of the ultimate strength of the cables
Cable_si_min = 0.3   # Minimum allowable cable tension as a fraction of the ultimate strength of the cables
A_strands_max = 100  # Maximum allowable number of strands per cable
A_strands_min = 10   # Minimum allowable number of strands per cable
Make_Symm = 1        # Use equal areas for the symmetrical cables

# Cables horizontal spacing / edge cables
N_cable_sections = 32     # Number of cable sections
s_cables = 13000    # Horizontal distance between deck anchor points 
Edge_cables =['Cables-1','Cables-18','Cables-19'] # Edge cables
s_cables_e = 6500  # Edge cables deck tributary length 

# Loads
q_ballast = 50.8 # Ballast
q_rail = 4.5 # Rail
q_equip = 4.0 # Equipment

# Iteration parameters 
Deck_v_allow_v = [150,120,100,95,90,85,80,75,70] + list(np.linspace(69,10,60))
max_iter = 300 # Maximum number of allowable iterations

# Configuration
SYMM = [1,0]  # Symmetric configuration [Group 1, Group 2]
BS_cables = ['Cables-26','Cables-27','Cables-28','Cables-29','Cables-30','Cables-31','Cables-32'] # Backstay cables for unsymmetrical group


"""
Link to Running Instance of SAP2000 
"""                        
# Set the following flag to True to attach to an existing instance of the program 
# otherwise a new instance of the program will be started
AttachToInstance = True

# Full path to the model
# Set it to the desired path of your model
APIPath = 'D:\API_Test'

if not os.path.exists(APIPath):
        try:
            os.makedirs(APIPath)
        except OSError:
            pass

# Create API helper object
helper = comtypes.client.CreateObject('SAP2000v1.Helper')
helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)

if AttachToInstance:
    #Attach to a running instance of SAP2000
    try:
        # Get the active SapObject
        mySapObject = helper.GetObject("CSI.SAP2000.API.SapObject") 
    except (OSError, comtypes.COMError):
        print("No running instance of the program found or failed to attach")
        sys.exit(-1)

# Create SapModel object
SapModel = mySapObject.SapModel


"""
Implement Unit System
"""
# Set unit system
if Unit_sytem == 'lb_in_F':
    us = 1
elif Unit_sytem == 'lb_ft_F':
    us = 2
elif Unit_sytem == 'Kip_in_F':
    us = 3
elif Unit_sytem == 'Kip_ft_F':
    us = 4
elif Unit_sytem == 'KN_mm_C':
    us = 5
elif Unit_sytem == 'KN_m_C':
    us = 6  
elif Unit_sytem == 'Kgf_m_C':
    us = 7
elif Unit_sytem == 'Kgf_m_C':
    us = 8
elif Unit_sytem == 'N_mm_C':
    us = 9
elif Unit_sytem == 'N_m_C':
    us = 10
elif Unit_sytem == 'Tonf_mm_C':
    us = 11
elif Unit_sytem == 'Tonf_m_C':
    us = 12
elif Unit_sytem == 'KN_cm_C':
    us = 13
elif Unit_sytem == 'Kgf_cm_C':
    us = 14
elif Unit_sytem == 'N_cm_C':
    us = 15
elif Unit_sytem == 'Tonf_cm_C':
    us = 16
ret = SapModel.SetPresentUnits(us)
print('*Unit system changed to ' + Unit_sytem + '*')


"""
Define Material Properties
"""
# Define concrete material
Mat_Concrete = 1
ret = SapModel.PropMaterial.SetMaterial('Concrete', Mat_Concrete)

# Assign isotropic mechanical properties to concrete
ret = SapModel.PropMaterial.SetMPIsotropic('Concrete', E_c,
                                           nu_c, alpha_c)
# Assign weight per unit volume to concrete
ret = SapModel.PropMaterial.SetWeightAndMass('Concrete', 1, w_c)

# Define cable material
Mat_Cables = 7
ret = SapModel.PropMaterial.SetMaterial('Cables', Mat_Cables)

# Assign isotropic mechanical properties to concrete
ret = SapModel.PropMaterial.SetMPIsotropic('Cables', E_s, nu_s, alpha_s)
# Assign weight per unit volume to concrete
ret = SapModel.PropMaterial.SetWeightAndMass('Cables', 1, w_s)


"""
Assign Materials to Sections
""" 
# Concrete material assignment
ret = SapModel.PropFrame.SetSDSection('Deck_2.5m', 'Concrete')

# Cable material
for i in range(N_cable_sections):
    SapModel.PropCable.SetProp('Cables-'+str(i+1), 'Cables', 1)
print('*Material properties assigned*')


"""
Modify Deck Section (Section Designer)
"""  
# Get SD section properties
Deck_SD = SapModel.PropFrame.GetSDSection('Deck_2.5m')
# Get Shape name
Deck_SD_Shape_Name = Deck_SD[2][0]
# Get polygon parameters: x,y coordinates
Deck_SD_Parameters = SapModel.PropFrame.SDShape.GetPolygon('Deck_2.5m',Deck_SD_Shape_Name)
Deck_SD_x = Deck_SD_Parameters[3]
Deck_SD_y = Deck_SD_Parameters[4]
# Adjust origin
x_min = min(Deck_SD_x)
x_max = max(Deck_SD_x)
y_min = min(Deck_SD_y)
# Offsets
x_o = (x_min + x_max)/2
y_o = y_min
Deck_SD_x = tuple(np.array(Deck_SD_x)-x_o)
Deck_SD_y = tuple(np.array(Deck_SD_y)-y_o)
ret = SapModel.PropFrame.SDShape.SetPolygon('Deck_2.5m',Deck_SD_Shape_Name, Deck_SD_Parameters[0] , Deck_SD_Parameters[1], Deck_SD_Parameters[2], Deck_SD_x, 
                                            Deck_SD_y,Deck_SD_Parameters[5],Deck_SD_Parameters[6])
   
"""
Modify Pier/Pylons Section
"""      


"""
Get Cables Names,Angles, Stage and Corresponding Joints Connected to Deck
""" 
Cable_names = SapModel.CableObj.GetNameList()  # Number of cable objects: Cable_names[0], Cable names: Cable_names[1]  
Cables = []  # Initialize cable names
Cables_BS = []  # Backstay cable names
Cable_angles = [] # Initialize cable angles 
Cable_angles_BS = []  # Initialize cable angles for the backstay
Cables_Stage = [] # Intialize stage for each cable
Deck_Cable_Joints = []  # Initial cable-deck anchor joints
Pylon_Cable_Joints = [] # Initial cable-pylon anchor joints
# List of cables, stage and anchor point for each cable
for i in range(Cable_names[0]):
    Cables.append(Cable_names[1][i])
    if SapModel.CableObj.GetProperty(Cable_names[1][i])[0] in BS_cables:
        Cables_BS.append(Cable_names[1][i])
    Cables_Stage.append(SapModel.CableObj.GetGroupAssign(Cable_names[1][i])[1][1])
    Cable_Points = SapModel.CableObj.GetPoints(Cable_names[1][i])
    # Cable end points coordinates
    x_1 = SapModel.PointObj.GetCoordCartesian(Cable_Points[0])[0]
    x_2 = SapModel.PointObj.GetCoordCartesian(Cable_Points[1])[0]
    z_1 = SapModel.PointObj.GetCoordCartesian(Cable_Points[0])[2]
    z_2 = SapModel.PointObj.GetCoordCartesian(Cable_Points[1])[2]
    Cable_angles.append(math.atan(abs(z_1-z_2)/(abs(x_1-x_2)))*180/math.pi)
    if SapModel.PointObj.GetCoordCartesian(Cable_Points[0])[2] < SapModel.PointObj.GetCoordCartesian(Cable_Points[1])[2]:
        Deck_Cable_Joints.append(Cable_Points[0])
    else:
        Deck_Cable_Joints.append(Cable_Points[1])
Cables_names_BS = [len(Cables_BS),Cables_BS,0]
for i in range(Cables_names_BS[0]):
    Cable_Points_BS = SapModel.CableObj.GetPoints(Cables_names_BS[1][i])
    if SapModel.PointObj.GetCoordCartesian(Cable_Points_BS[0])[2] < SapModel.PointObj.GetCoordCartesian(Cable_Points_BS[1])[2]:
        Pylon_Cable_Joints.append(Cable_Points_BS[1])
    else:
        Pylon_Cable_Joints.append(Cable_Points_BS[0])  
for i in range(Cable_names[0]):
    for j in range(Cables_names_BS[0]):
        if Cables[i] == Cables_BS[j]:
            Cable_angles_BS.append(Cable_angles[i])
       
print('*Geometrical properties of the cables obtained*')


"""
Group Symmetrical Cables
""" 
z_Cable_Top = [] # Initialize top coordinates of each cables
for i in range(Cable_names[0]):
    Cable_Points = SapModel.CableObj.GetPoints(Cable_names[1][i])
    z_Cable_Top.append(round(SapModel.PointObj.GetCoordCartesian(Cable_Points[1])[2]))

# Get symmetrical cable numbers 
Symm_Cables = [[] for _ in range(len(z_Cable_Top))]
for i in range(len(z_Cable_Top)):
    Symm = np.array(z_Cable_Top) == z_Cable_Top[i]
    for j in range(len(Symm)):
        if Symm[j] == True:
           Symm_Cables[i].append(j)                
print('*Symmetrical cables grouped*')
 
  
"""
Restrain the Pylon Horizontal Displacement for the Unsymmetrical Group
"""
# Assign horizontal restraint to pylon anchor points
Pylon_Restraint = [True, True, False, False, False, False]  # Ux, Uy, Uz, Rx, Ry, Rz
for y in range(len(Pylon_Cable_Joints)):
    SapModel.PointObj.SetRestraint(Pylon_Cable_Joints[y], Pylon_Restraint)
     
"""
Assign Cross-sectional Area / Tension to Cables
"""
Load_Cases = ['Staged_Construction-1F','Staged_Construction-2F']
    
for l in range(len(Load_Cases)):
    Load_Case = Load_Cases[l]
    # Set load case to run
    SapModel.Analyze.SetRunCaseFlag('All',False,True)
    SapModel.Analyze.SetRunCaseFlag(Load_Case, True)
    # Assign preliminary cross-sectional areas
    # Get deck area
    Deck_area = SapModel.PropFrame.GetSectProps('Deck_2.5m')[0]
    # Deck self-weight (N/mm)
    Deck_SW = Deck_area*w_c
    # Permanent loads
    Deck_per = Deck_SW + q_ballast + q_rail + q_equip
    
    # Get preliminary tension force in the cables
    Cables_Ti = [] # Initialize cable preliminary tension forces
    for i in range(Cable_names[0]):
        Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][i])
        if Cables_assignments[0] in Edge_cables:
            Ti = (Deck_per*s_cables_e)/(math.sin(Cable_angles[i]*math.pi/180))*0.5
        else:
            Ti = (Deck_per*s_cables)/(math.sin(Cable_angles[i]*math.pi/180))*0.5
        Cables_Ti.append(Ti)
    
    # Initial cross-sectional areas of the cables   
    A_cables = [] # Intialize cable areas
    for i in range(Cable_names[0]):
        A_cables.append(Cables_Ti[i]/(Cable_si_max*f_u_cables))
     
    # Assign initial cable cross-sectional areas
    setCableAreas(SapModel,Cable_names,A_cables,'Cables')
                 
    # Assign initial tension in the cables
    setCableInitialForces(SapModel,Cable_names,Cables_Ti)

    # Iterate on initial cross-sectional areas to obtain stress ratios within the limits
    while True: 
        # Run analysis
        ret = SapModel.Analyze.RunAnalysis()
         
        # Deselect results for all cases
        ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
        # Select desired load case
        ret = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
         
        # Track axial force in the cables due to permanent load
        Cables_Fo = getCableAxialForces(SapModel,Cable_names)
        
        # Stress ratios in the cables   
        Cables_S = np.array(Cables_Fo)/np.array(A_cables)/f_u_cables
        
        print('Stress ratios:')
        print(Cables_S)  
          
        # Unlock model
        SapModel.SetModelIsLocked(0)
        
        counter_a = 0
        # Assign cable cross-sectional areas
        for i in range(Cable_names[0]):  
            Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][i])
            if (Cables_S[i] < Cable_si_min) and Cables_S[i] > 0:
                F_A = Cables_S[i]/Cable_si_min
                counter_a = counter_a + 1
            elif (Cables_S[i] > Cable_si_max):
                F_A = Cables_S[i]/Cable_si_max
                counter_a = counter_a + 1
            else:
                F_A = 1
            A_cables[i]= A_cables[i]*F_A   
            SapModel.PropCable.SetProp(Cables_assignments[0], 'Cables', A_cables[i]*F_A)
        # Break from loop once stress ratios are within the limits
        if counter_a == 0:
            print('Preliminary cable stress ratios within the limits*')
            break
    
    
    """
    Track Displacements at Cable Joints Connected to Deck, Stress Ratios and Re-assign Cable Area Sections
    """  
    Cable_Parameters = [Cable_names,A_cables,Cables_Ti,Cables_S]
    Cable_Properties = ['Cables',f_u_cables,A_strands,A_strands_min,A_strands_max,Cable_si_min,Cable_si_max]
    Iteration_Parameters = [Deck_v_allow_v,max_iter,1]
    if l == 0:
        [A_cables_S1F, Cables_Ti_S1F, Cables_S_S1F,Deck_v_allow_S1F] = iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters)
    else:
        [A_cables_S2F, Cables_Ti_S2F, Cables_S_S2F,Deck_v_allow_S2F] = iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters)
        print('*First iteration set for ' + Load_Case + ' completed*')
    
    
    """
    Round and Re-assign Cable Area Sections
    """    
    # Round with number of strands
    A_cables_f = []
    if l==0:
        A_cables_S = A_cables_S1F
    else:
        A_cables_S = A_cables_S2F
        
    for i in range(len(A_cables_S)):
        Area_rounded = round(A_cables_S[i]/A_strands)*A_strands
        A_cables_f.append(Area_rounded)
    
    setCableAreas(SapModel,Cable_names,A_cables_f,'Cables')
    print('*Cable cross-sectional areas for ' + Load_Case + ' rounded*')   
       
              
    """
    Make Cable Areas Symmetric (if required)
    """ 
    if Make_Symm == 1 and SYMM[l] == 1:
        if l == 0:
            Cables_S = Cables_S_S1F
        else:
            Cables_S = Cables_S_S2F
        # Check difference between actual and allowable stress ratios    
        for i in range(len(Symm_Cables)):
            abs_diff_1 = max(abs(Cable_si_min - Cables_S[Symm_Cables[i][0]]),abs(Cable_si_max - Cables_S[Symm_Cables[i][0]]))
            abs_diff_2 = max(abs(Cable_si_min - Cables_S[Symm_Cables[i][1]]),abs(Cable_si_max - Cables_S[Symm_Cables[i][1]]))
            if abs_diff_1 <= abs_diff_2:
                Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][Symm_Cables[i][0]])
            else:
                Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][Symm_Cables[i][1]])   
            A_temp = SapModel.PropCable.GetProp(Cables_assignments[0])[1]
            for n in range(len(Symm_Cables[i])):   
                Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][Symm_Cables[i][n]])
                SapModel.PropCable.SetProp(Cables_assignments[0], 'Cables', A_temp)
        print('*Cable cross-sectional areas for symmetric cables of ' + Load_Case + ' made equal*')  
        A_cables_f = getCableAreas(SapModel,Cable_names,'Cables')
     
        
    """
    Get Final Cable Cross-sectional Areas 
    """ 
    if l==0:
        A_cables_S1F = getCableAreas(SapModel,Cable_names,'Cables')
    else:
        A_cables_S2F = getCableAreas(SapModel,Cable_names,'Cables')
    print('*Final cable cross-sectional areas of ' + Load_Case + ' obtained*')  
      
                     
    """
    Re-iterate on the Tensile Force in the Cables Only
    """ 
    # Run analysis
    ret = SapModel.Analyze.RunAnalysis()
    
    # Get maximum displacement
    Deck_Anchor_V_Disp = []            # Initialize vertical displacements in at the deck anchor points
    for i in range(Cable_names[0]): 
        Deck_Cable_Joints_Disp = SapModel.Results.JointDispl(Deck_Cable_Joints[i],0)
        Deck_Anchor_V_Disp.append(Deck_Cable_Joints_Disp[8][0])

    # Unlock modell
    SapModel.SetModelIsLocked(0)  
    
    # Modify vector of allowable displacements
    Deck_v_allow_max = round(max(abs(np.array(Deck_Anchor_V_Disp))),0)   
    Deck_v_allow_min = Deck_v_allow_v[len(Deck_v_allow_v)-1]
    Deck_v_allow_m = list(np.linspace(Deck_v_allow_max+1,Deck_v_allow_min,int(Deck_v_allow_max-Deck_v_allow_min+2)))
    Iteration_Parameters = [Deck_v_allow_m,max_iter,0]
    if l == 0:
        Cable_Parameters = [Cable_names,A_cables_S1F,Cables_Ti_S1F,Cables_S_S1F]
        [A_cables_S1F, Cables_Ti_S1F, Cables_S_S1F,Deck_v_allow_S1F] = iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters)
    else:
        Cable_Parameters = [Cable_names,A_cables_S2F,Cables_Ti_S2F,Cables_S_S2F]
        [A_cables_S2F, Cables_Ti_S2F, Cables_S_S2F,Deck_v_allow_S2F] = iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters)
    print('*Second iterations set for ' + Load_Case + ' completed*')           
    
    
    """
    Obtain Updated Stress Ratios
    """   
    ret = SapModel.Analyze.RunAnalysis()
     
    # Deselect results for all cases
    ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    # Select desired load case
    ret = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
     
    # Track axial force in the cables due to permanent load
    Cables_Fo = getCableAxialForces(SapModel,Cable_names)
    
    if l==0: 
        # Stress ratios in the cables   
        Cables_S_S1F = np.array(Cables_Fo)/np.array(A_cables_S1F)/f_u_cables
    else:
        Cables_S_S2F = np.array(Cables_Fo)/np.array(A_cables_S2F)/f_u_cables 
    print('*Updated cable stress ratios of ' + Load_Case + ' obtained*')  
    
    # Unlock model
    SapModel.SetModelIsLocked(0)  
    
    
    """
    Assign Cable Results to Each Load Case
    """ 
    # Assign to load case
    if l==0:    
        # Assign to first group 
        for i in range(len(Cable_names[1])):
            if Cables_S_S1F[i] > 0:
                A_cables_S1F[i] = A_cables_f[i]
                Cables_Ti_S1F[i] = Cables_Ti_S1F[i]
            else:
                A_cables_S1F[i] = 0
                Cables_Ti_S1F[i] = 0
    else:
        # Assign to second group 
        for i in range(len(Cable_names[1])):
            if Cables_S_S2F[i] > 0:
                A_cables_S2F[i] = A_cables_f[i]
                Cables_Ti_S2F[i] = Cables_Ti_S2F[i]
            else:
                A_cables_S2F[i] = 0
                Cables_Ti_S2F[i] = 0
    print('*Cable paramaters assigned to ' + Load_Case + '*')  
 
    
""" Assign Updated Cable Parameters""" 
A_cables_S12F = list(np.array(A_cables_S1F) + np.array(A_cables_S2F))
Cables_Ti_S12F = list(np.array(Cables_Ti_S1F) + np.array(Cables_Ti_S2F))
Cables_S_S12F = list(np.array(Cables_S_S1F) + np.array(Cables_S_S2F))

# Assign initial cable cross-sectional areas
setCableAreas(SapModel,Cable_names,A_cables_S12F,'Cables')
             
# Assign initial tension in the cables
setCableInitialForces(SapModel,Cable_names,Cables_Ti_S12F) 
print('*Updated cable parameters assigned to model*')      


""" Adjustment of Cable Forces in the Final State""" 
Load_Case = 'Staged_Construction-1-2F'
# Set load case to run
SapModel.Analyze.SetRunCaseFlag('All',False,True)
SapModel.Analyze.SetRunCaseFlag(Load_Case, True)
ret = SapModel.Analyze.RunAnalysis()
# Deselect results for all cases
ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
# Select desired load case
ret = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
# Get maximum displacement
Deck_Anchor_V_Disp = []            # Initialize vertical displacements in at the deck anchor points
for i in range(Cable_names[0]): 
    Deck_Cable_Joints_Disp = SapModel.Results.JointDispl(Deck_Cable_Joints[i],0)
    Deck_Anchor_V_Disp.append(Deck_Cable_Joints_Disp[8][0])

# Unlock modell
SapModel.SetModelIsLocked(0)  
    
Deck_v_allow_max = round(max(abs(np.array(Deck_Anchor_V_Disp))),0)   
Deck_v_allow_min = Deck_v_allow_v[len(Deck_v_allow_v)-1]
Deck_v_allow_f = list(np.linspace(Deck_v_allow_max+1,Deck_v_allow_min,int(Deck_v_allow_max-Deck_v_allow_min+2)))

# Iterate on the cable forces  
Iteration_Parameters = [Deck_v_allow_f,max_iter,0]
Cable_Parameters = [Cable_names,A_cables_S12F,Cables_Ti_S12F,Cables_S_S12F]
[A_cables_S12F, Cables_Ti_S12F, Cables_S_S12F,Deck_v_allow_S12F] = iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters)
print('*Cable paramaters updated for final state with permanent loads*')             

#####################################################################################################################################################
"""
Track Horizontal Reactions at Cable Joints Connected to Pylon, Assign Back Span Cable Forces, and Re-assign Area Sections for Back Span Cables
"""  
# Get Pylon horizontal reactions 
# Run analysis
ret = SapModel.Analyze.RunAnalysis()
 
# Deselect results for all cases
SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
 
# Select desired load case
SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
Pylon_Anchor_H_Rxn = []            # Initialize horizontal reactions in  the pylon anchor points
for i in range(len(Pylon_Cable_Joints)): 
    Pylon_Anchor_Rxn = SapModel.Results.JointReact(Pylon_Cable_Joints[i], 0)
    Pylon_Anchor_H_Rxn.append(Pylon_Anchor_Rxn[6][0])
print('*Pylon anchor points reactions for ' + Load_Case + ' obtained*')      
 
# Unlock model
SapModel.SetModelIsLocked(0)

# Get preliminary tension force in the backspan cables  
Cables_Ti_BS = [] # Initialize backspan cables preliminary tension forces 
for i in range(len(Pylon_Anchor_H_Rxn)):
    Ti_BS = Pylon_Anchor_H_Rxn[i]/(math.cos(Cable_angles_BS[i]*math.pi/180))*0.5
    Cables_Ti_BS.append(abs(Ti_BS))

# Initial cross-sectional areas of the cables   
A_cables_BS = [] # Intialize cable areas
for i in range(len(Pylon_Anchor_H_Rxn)):
    A_cables_BS.append(abs(Cables_Ti_BS[i]/(Cable_si_max*f_u_cables)))
    
# Assign initial cable cross-sectional areas
setCableAreas(SapModel,Cables_names_BS,[i for i in A_cables_BS if i != 0],'Cables')              
# Assign initial tension in the cables.
setCableInitialForces(SapModel,Cables_names_BS,[i for i in Cables_Ti_BS if i != 0])
 
# Iterate on backspan cables forces to minimize horizontal reaction (limit to 8 iterations)
for iter in range(8):
    # Run analysis
    ret = SapModel.Analyze.RunAnalysis()
   
    # Deselect results for all cases
    SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
   
    # Select desired load case
    SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
    Pylon_Anchor_H_Rxn_BS = []            # Initialize horizontal reactions in  the pylon anchor points (with backspan cables)
    for i in range(len(Pylon_Cable_Joints)): 
        Pylon_Anchor_Rxn = SapModel.Results.JointReact(Pylon_Cable_Joints[i], 0)
        Pylon_Anchor_H_Rxn_BS.append(Pylon_Anchor_Rxn[6][0])
   
    # Update reaction at pylon anchor points
    for i in range(len(Pylon_Anchor_H_Rxn)):
        Pylon_Anchor_H_Rxn[i] = Pylon_Anchor_H_Rxn[i] + Pylon_Anchor_H_Rxn_BS[i] 
       
    Cables_Ti_BS = [] # Initialize backspan cables preliminary tension forces 
    for i in range(len(Pylon_Anchor_H_Rxn)):
        Ti_BS = (Pylon_Anchor_H_Rxn[i])/(math.cos(Cable_angles_BS[i]*math.pi/180))*0.5
        Cables_Ti_BS.append(abs(Ti_BS))
   
    # Initial cross-sectional areas of the cables   
    A_cables_BS = [] # Intialize cable areas
    for i in range(len(Pylon_Anchor_H_Rxn)):
        A_cables_BS.append(abs(Cables_Ti_BS[i]/(Cable_si_max*f_u_cables)))
   
    # Unlock model
    SapModel.SetModelIsLocked(0)
           
    # Assign initial cable cross-sectional areas
    setCableAreas(SapModel,Cables_names_BS,[i for i in A_cables_BS if i != 0],'Cables')              
    # Assign initial tension in the cables.
    setCableInitialForces(SapModel,Cables_names_BS,[i for i in Cables_Ti_BS if i != 0])        
       
# Round with number of strands
A_cables_f = []
for i in range(len(A_cables_BS)):
    Area_rounded = round(A_cables_BS[i]/A_strands)*A_strands
    A_cables_f.append(Area_rounded)

A_cables_BS = A_cables_f

# Unlock model
SapModel.SetModelIsLocked(0)
 
# Assign cable cross-sectional areas
setCableAreas(SapModel,Cables_names_BS,[i for i in A_cables_BS if i != 0],'Cables')              
# Assign initial tension in the cables.
setCableInitialForces(SapModel,Cables_names_BS,[i for i in Cables_Ti_BS if i != 0])
print('* Initial forces/ cross-sectional areas in the backspan cables for assigned*')
 

""" Modify Boundary Conditions for the Final State""" 
# Remove horizontal restraint on the pylon
Pylon_Deck_Restraint = [False, False, False, False, False, False]  # Ux, Uy, Uz, Rx, Ry, Rz
for y in range(len(Pylon_Cable_Joints)):
    SapModel.PointObj.SetRestraint(Pylon_Cable_Joints[y], Pylon_Deck_Restraint)
# # Deck connection
# for z in range(len(Pylon_Deck_Joints)):
#     SapModel.PointObj.SetRestraint(Pylon_Deck_Joints[z], Pylon_Deck_Restraint)   
# # Temporary backspan supports    
# for t in range(len(Cables_Deck_Temporary_Restraint)):
#     SapModel.PointObj.SetRestraint(Cables_Deck_Temporary_Restraint[t], Pylon_Deck_Restraint)    
    
 
""" Tabulate Cable Results""" 
A_cables_S12F = getCableAreas(SapModel,Cable_names,'Cables')

ret = SapModel.Analyze.RunAnalysis()
 
# Deselect results for all cases
ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
# Select desired load case
ret = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
 
# Track axial force in the cables due to permanent load
Cables_Fo = getCableAxialForces(SapModel,Cable_names)

# Stress ratio in the cables
Cables_S_S12F = np.array(Cables_Fo)/np.array(A_cables_S12F)/f_u_cables
print('*Updated cable stress ratios of ' + Load_Case + ' obtained*')  


# Number of strands
N_strands_S12F =[]
for i in range(len(Cable_names[1])):
    N_strands_S12F.append(int(A_cables_S12F[i]/A_strands))

Cables_Results_Summary_Table = []
c = 1
i = 0
while True:
    # Create each row
    Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][i])
    if int(Cables_assignments[0].split('-')[1]) == c:
        row = ['C' + str(int(Cables_assignments[0].split('-')[1])),A_cables_S12F[i],N_strands_S12F[i],round(Cables_S_S12F[i],2)]
        c = c + 1
        Cables_Results_Summary_Table.append(row)
        if c > len(Cable_names[1])/2:
            break
    if i == len(Cable_names[1]) - 1:
        i = 0
    i = i + 1
    
col_names = ['Cable','Section [mm2]','Torons','s / fu']
print('**** Sections de câbles ****\n')
print(tabulate(Cables_Results_Summary_Table,headers=col_names,colalign=("center",)))

f = open("Cables_Summary.txt", "a")
f.write('****Sections de cables ****\n')
f.write("\n")
f.write(tabulate(Cables_Results_Summary_Table,headers=col_names,colalign=("center",)))
f.close()
print('*Final cable parameters printed to text file*')  