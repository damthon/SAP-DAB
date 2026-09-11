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
from getCableInitialForces import getCableInitialForces
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

# Steel (S355)
w_s = 7.85e-5      # Weight of steel per unit volume (N/mm3)

# Cables properties
E_s = 195000   # Modulus of elasiticy
nu_s = 0.3     # Poisson ratio
alpha_s = 1.0e-5   # Coefficient of thermal expansion of concrete 
f_u_cables = 1860  # Ultimate strength of the cables
A_strands = 150    # Area of 1 cable strand 
Cable_si_max = 0.3   # Maximum allowable cable tension as a fraction of the ultimate strength of the cables
Cable_si_min = 0.25   # Minimum allowable cable tension as a fraction of the ultimate strength of the cables
A_strands_max = 91  # Maximum allowable number of strands per cable
A_strands_min = 12   # Minimum allowable number of strands per cable

# Cables horizontal spacing / edge cables
N_cable_sections = 36     # Number of cable sections
s_cables = 12000    # Horizontal distance between deck anchor points in the main span
s_cables_e = 12000   # Main span edge cables tributary length
s_cables_BS1 = 7300  # Backspan 1 cables deck tributary length 
s_cables_BS2 = 7300  # Backspan 2 cables deck tributary length 
Edge_cables = []
BS1_cables = ['Cables-1','Cables-2','Cables-3','Cables-4','Cables-5','Cables-6','Cables-7','Cables-8','Cables-9','Cables-10','Cables-11','Cables-12','Cables-13','Cables-14','Cables-15','Cables-16','Cables-17','Cables-18'] # Backspan 1cables
BS2_cables =[] # Backspan 2 cables
BS_cables = BS1_cables + BS2_cables
Deck_Temporary_Restraint = ['132','131','130','120','118','115','111','107','103','99','95','93','91','89','87','85','83','316'] #'316'

# Deck Sections
Concrete_Deck_Filled = 'Deck_2.5m_F'  # Filled concrete deck for the backstays
Concrete_Deck_O = 'Deck_2.5m' # Open concrete deck for the mainspan

# Loads
q_ballast = 50.76 # Ballast
q_rail = 4.5 # Rail
q_equip = 4.0 # Equipment

# Iteration parameters 
#Deck_v_allow_v = [800,700,600,500,400,300,250,200,150,120,100,95,90,85,80,75,70] + list(np.linspace(69,10,60))
Deck_v_allow_v = [500,400,300,200,150,120,100,80,70,65,60,55,50,45,40,35,30] + list(np.linspace(29,5,25))

max_iter = 300 # Maximum number of allowable iterations


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
ret = SapModel.PropFrame.SetSDSection(Concrete_Deck_Filled, 'Concrete')

# Steel material assignment
ret = SapModel.PropFrame.SetSDSection(Concrete_Deck_O, 'Concrete')

# Cable material
for i in range(N_cable_sections):
    SapModel.PropCable.SetProp('Cables-'+str(i+1), 'Cables', 1)
print('*Material properties assigned*')


"""
Modify Deck Section (Section Designer)
"""  
# Get SD section properties
Deck_SD = SapModel.PropFrame.GetSDSection(Concrete_Deck_Filled)
# Get Shape name
Deck_SD_Shape_Name = Deck_SD[2][0]
# Get polygon parameters: x,y coordinates
Deck_SD_Parameters = SapModel.PropFrame.SDShape.GetPolygon(Concrete_Deck_Filled,Deck_SD_Shape_Name)
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
ret = SapModel.PropFrame.SDShape.SetPolygon(Concrete_Deck_Filled,Deck_SD_Shape_Name, Deck_SD_Parameters[0] , Deck_SD_Parameters[1], Deck_SD_Parameters[2], Deck_SD_x, 
                                            Deck_SD_y,Deck_SD_Parameters[5],Deck_SD_Parameters[6])
   
"""
Modify Pier/Pylons Section
"""      


"""
Get Cables Names,Angles, Stage and Corresponding Joints Connected to Deck
""" 
Cable_names = SapModel.CableObj.GetNameList()  # Number of cable objects: Cable_names[0], Cable names: Cable_names[1]  
Cables = []  # Initialize cable names
Cables_BS1 = []  # Backspan 1 cable names
Cables_BS2 = []  # Backspan 2 cable names
Cables_BS = []   # All backspan cable names
Cable_angles = [] # Initialize cable angles 
Cables_Stage = [] # Intialize stage for each cable
Deck_Cable_Joints = []  # Initial cable-deck anchor joints
Pylon_Cable_Joints = [] # Initial cable-pylon anchor joints
# List of cables, stage and anchor point for each cable
for i in range(Cable_names[0]):
    Cables.append(Cable_names[1][i])
    if SapModel.CableObj.GetProperty(Cable_names[1][i])[0] in BS1_cables:
        Cables_BS1.append(Cable_names[1][i])
    if SapModel.CableObj.GetProperty(Cable_names[1][i])[0] in BS2_cables:   
        Cables_BS2.append(Cable_names[1][i])
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
        Pylon_Cable_Joints.append(Cable_Points[1])
    else:
        Deck_Cable_Joints.append(Cable_Points[1])
        Pylon_Cable_Joints.append(Cable_Points[0])
Cables_names_BS1 = [len(Cables_BS1),Cables_BS1,0]
Cables_names_BS2 = [len(Cables_BS2),Cables_BS2,0]
Cables_names_BS = [len(Cables_BS2),Cables_BS2,0]
Cables_names_BS = [len(Cables_BS),Cables_BS,0]

print('*Geometrical properties of the cables obtained*')
       

"""
Assign Cross-sectional Area / Tension to Mainspan Cables
"""
Load_Case_o = 'Staged_Construction-1F'
# Main span cables only included 
Load_Case = Load_Case_o + '_MS'
# Set load case to run
# SapModel.Analyze.SetRunCaseFlag('All',False,True)
# SapModel.Analyze.SetRunCaseFlag(Load_Case, True)
     
# Assign horizontal restraint to pylon anchor points
Pylon_Restraint = [True, True, False, False, False, False]  # Ux, Uy, Uz, Rx, Ry, Rz
for y in range(len(Pylon_Cable_Joints)):
    SapModel.PointObj.SetRestraint(Pylon_Cable_Joints[y], Pylon_Restraint)
# Assign pinned restraint to backstay cables anchor points and pylon
Deck_Restraint  = [True, True, True, False, False, False]  # Ux, Uy, Uz, Rx, Ry, Rz
for y in range(len(Deck_Temporary_Restraint)):
    SapModel.PointObj.SetRestraint(Deck_Temporary_Restraint[y], Deck_Restraint)
    
# Assign preliminary cross-sectional areas
# Get deck area in the mianspan
Deck_area = SapModel.PropFrame.GetSectProps(Concrete_Deck_O)[0]

# Deck self-weight (N/mm)
Deck_SW = Deck_area*w_c
# Permanent loads
Deck_per = Deck_SW + q_ballast + q_rail + q_equip
    
# Get preliminary tension force in the cables based on tributary length 
Cables_Ti = [] # Initialize cable preliminary tension forces
for i in range(Cable_names[0]):
    Cables_assignments = SapModel.CableObj.GetProperty(Cable_names[1][i])
    if Cables_assignments[0] in BS1_cables:
        Ti = (Deck_per*s_cables_BS1)/(math.sin(Cable_angles[i]*math.pi/180))*0.5
    elif Cables_assignments[0] in BS2_cables:
            Ti = (Deck_per*s_cables_BS2)/(math.sin(Cable_angles[i]*math.pi/180))*0.5
    elif Cables_assignments[0] in Edge_cables:
        Ti = (Deck_per*s_cables_e)/(math.sin(Cable_angles[i]*math.pi/180))*0.5
    else:
        Ti = (Deck_per*s_cables)/(math.sin(Cable_angles[i]*math.pi/180))*0.5
    Cables_Ti.append(Ti)
    
# Initial cross-sectional areas of the cables based on tributary length 
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
Cable_Parameters= [Cable_names,A_cables,Cables_Ti,Cables_S]
Cable_Properties = ['Cables',f_u_cables,A_strands,A_strands_min,A_strands_max,Cable_si_min,Cable_si_max]
Iteration_Parameters = [Deck_v_allow_v,max_iter,1]

[A_cables_SF_MS, Cables_Ti_SF_MS, Cables_S_SF_MS,Deck_v_allow_SF_MS] = iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters)
print('*First iteration set for ' + Load_Case + ' (main span) completed*')
    
    
"""
Round and Re-assign Cable Area Sections
"""    
# Round with number of strands
A_cables_f = []
A_cables_S = A_cables_SF_MS   
for i in range(len(A_cables_S)):
    Area_rounded = round(A_cables_S[i]/A_strands)*A_strands
    A_cables_f.append(Area_rounded)

setCableAreas(SapModel,Cable_names,A_cables_f,'Cables')
print('*Cable cross-sectional areas for ' + Load_Case + ' (main span) rounded*')   

    
"""
Get Final Cable Cross-sectional Areas 
""" 
A_cables_SF_MS = getCableAreas(SapModel,Cable_names,'Cables')
print('*Final cable cross-sectional areas of ' + Load_Case + ' (main span) obtained*')  
  
                     
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

Cable_Parameters = [Cable_names,A_cables_SF_MS,Cables_Ti_SF_MS,Cables_S_SF_MS]
[A_cables_SF_MS, Cables_Ti_SF_MS, Cables_S_SF_MS,Deck_v_allow_SF] = iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters)
print('*Second iterations set for ' + Load_Case + ' (main span) completed*')      
    

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

for i in range(len(Cable_names[1])):
    if Cables[i] in Cables_BS:
        Ti_BS = Pylon_Anchor_H_Rxn[i]/(math.cos(Cable_angles[i]*math.pi/180))*0.5
    else:
        Ti_BS = 0
    Cables_Ti_BS.append(abs(Ti_BS))

# Initial cross-sectional areas of the cables   
A_cables_BS = [] # Intialize cable areas
for i in range(len(Cable_names[1])):
    if Cables[i] in Cables_BS:
        A_cables_BS.append(abs(Cables_Ti_BS[i]/(Cable_si_max*f_u_cables)))
    else:
        A_cables_BS.append(0)

# Assign initial cable cross-sectional areas
setCableAreas(SapModel,Cables_names_BS,[i for i in A_cables_BS if i != 0],'Cables')              
# Assign initial tension in the cables.
setCableInitialForces(SapModel,Cables_names_BS,[i for i in Cables_Ti_BS if i != 0])
    
# Iterate on backspan cables forces to minimize horizontal reaction (limit to 4 iterations)
Load_Case = Load_Case_o + '_BS'  
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
        if Cables[i] in Cables_BS:
            Ti_BS = (Pylon_Anchor_H_Rxn[i])/(math.cos(Cable_angles[i]*math.pi/180))*0.5
        else:
            Ti_BS = 0
        Cables_Ti_BS.append(abs(Ti_BS))
    
    # Initial cross-sectional areas of the cables   
    A_cables_BS = [] # Intialize cable areas
    for i in range(len(Cable_names[1])):
        if Cables[i] in Cables_BS:
            A_cables_BS.append(abs(Cables_Ti_BS[i]/(Cable_si_max*f_u_cables)))
        else:
            A_cables_BS.append(0)
    
    # Unlock model
    SapModel.SetModelIsLocked(0)
    
    # Round with number of strands
    A_cables_f = []
    for i in range(len(A_cables_BS)):
        Area_rounded = round(A_cables_BS[i]/A_strands)*A_strands
        A_cables_f.append(Area_rounded)

    A_cables_BS = A_cables_f
        
    # Assign initial cable cross-sectional areas
    setCableAreas(SapModel,Cables_names_BS,[i for i in A_cables_BS if i != 0],'Cables')              
    # Assign initial tension in the cables.
    setCableInitialForces(SapModel,Cables_names_BS,[i for i in Cables_Ti_BS if i != 0])        

#####################################   
print('* Initial forces/ cross-sectional areas in the backspan cables for ' + Load_Case + ' assigned*')        

"""
Obtain Updated Stress Ratios
"""  
# Get updated cable areas
A_cables_SF = getCableAreas(SapModel,Cable_names,'Cables')
  
# Get updated cable initial forces
Cables_Ti_SF = getCableInitialForces(SapModel,Cable_names)

# Load case 
Load_Case = Load_Case_o + '_BS'

# Run analysis
ret = SapModel.Analyze.RunAnalysis()
 
# Deselect results for all cases
ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
# Select desired load case
ret = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
 
# Track axial force in the cables due to permanent load
Cables_Fo = getCableAxialForces(SapModel,Cable_names)

# Stress ratios in the cables   
Cables_S_SF = np.array(Cables_Fo)/np.array(A_cables_SF)/f_u_cables
print('*Updated cable stress ratios of ' + Load_Case + ' obtained*')  

# Unlock modell
SapModel.SetModelIsLocked(0)  
    
# """
# Assign Cable Results to Each Load Case
# """ 
# # Assign to load case
  
#     # Assign to first group 
#     for i in range(len(Cable_names[1])):
#         if Cables_S_S1F[i] > 0:
#             A_cables_S1F[i] = A_cables_S1F[i]
#             Cables_Ti_S1F[i] = Cables_Ti_S1F[i]
#         else:
#             A_cables_S1F[i] = 0
#             Cables_Ti_S1F[i] = 0

# print('*Cable paramaters assigned to ' + Load_Cases[l] + '*')  
 
    
# """ Assign Updated Cable Parameters""" 
# A_cables_S12F = list(np.array(A_cables_S1F) + np.array(A_cables_S2F))
# Cables_Ti_S12F = list(np.array(Cables_Ti_S1F) + np.array(Cables_Ti_S2F))
# Cables_S_S12F = list(np.array(Cables_S_S1F) + np.array(Cables_S_S2F))

# # Assign initial cable cross-sectional areas
# setCableAreas(SapModel,Cable_names,A_cables_S12F,'Cables')
             
# # Assign initial tension in the cables
# setCableInitialForces(SapModel,Cable_names,Cables_Ti_S12F) 
# print('*Updated cable parameters assigned to model*')      

""" Modify Boundary Conditions for the Final State""" 
# Remove horizontal restraint on the pylon
Pylon_Deck_Restraint = [False, False, False, False, False, False]  # Ux, Uy, Uz, Rx, Ry, Rz
for y in range(len(Pylon_Cable_Joints)):
    SapModel.PointObj.SetRestraint(Pylon_Cable_Joints[y], Pylon_Deck_Restraint)
# Remove pinned restraint on the deck
Deck_Restraint  = [False, False, False, False, False, False]  # Ux, Uy, Uz, Rx, Ry, Rz
for y in range(len(Deck_Temporary_Restraint)):
    SapModel.PointObj.SetRestraint(Deck_Temporary_Restraint[y], Deck_Restraint)
    
    
""" Adjustment of Cable Forces in the Final State""" 
ret = SapModel.Analyze.RunAnalysis()
Load_Case = Load_Case_o + '_BS'
# Deselect results for all cases
ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
# Select desired load case
ret = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_Case)
# Get maximum displacement
Deck_Anchor_V_Disp = []            # Initialize vertical displacements in at the deck anchor points
for i in range(Cables_names_BS[0]): 
    Deck_Cable_Joints_Disp = SapModel.Results.JointDispl(Deck_Cable_Joints[i],0)
    Deck_Anchor_V_Disp.append(Deck_Cable_Joints_Disp[8][0])

# Unlock modell
SapModel.SetModelIsLocked(0)  
    
Deck_v_allow_max = round(max(abs(np.array(Deck_Anchor_V_Disp))),0)   
Deck_v_allow_min = Deck_v_allow_v[len(Deck_v_allow_v)-1]
Deck_v_allow_f = list(np.linspace(Deck_v_allow_max+1,Deck_v_allow_min,int(Deck_v_allow_max-Deck_v_allow_min+2)))

# Iterate on the cable forces  
Iteration_Parameters = [Deck_v_allow_f,max_iter,0]
Cable_Parameters = [Cable_names,A_cables_SF,Cables_Ti_SF,Cables_S_SF]
[A_cables_S12F, Cables_Ti_S12F, Cables_S_S12F,Deck_v_allow_S12F] = iterateCableAreasForces(SapModel,Load_Case,Cable_Parameters,Cable_Properties,Deck_Cable_Joints,Iteration_Parameters)
print('*Cable paramaters updated for final state with permanent loads*')             

""" Tabulate Cable Results""" 
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
