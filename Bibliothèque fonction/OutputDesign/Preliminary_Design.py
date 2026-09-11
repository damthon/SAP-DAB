# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:21:35 2022

@author: hammad.eljisr

This script performs a preliminary check of the deck, pylon and pier sections. The M-P interaction surfaces are imported and the longitudinal reinforcement is verified.
The required shear reinforcement is also provided
"""

import os
import sys
import comtypes.client
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt 
from getFrameSectionLabels import getFrameSectionLabels
from frameSectionForces import frameSectionForces
from getShearReinforcement import getShearReinforcement

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['text.usetex'] = False
plt.rc('mathtext',fontset='stix')

save_plots = 1

"""
Input
"""
Unit_sytem = 'N_mm_C'  # INPUT FORMAT: Force_displacement_Temperature  (Force = lb, Kip, KN, Kgf, N, Tonf; Distance = ft, in, mm, m, cm, Temperature = F,C)

# Deck dimensions
h_deck = 2500    # Deck section depth
b_deck = 2500    # Assumed width of the deck (middle part ignored)

# Pylon dimensions 
h_pylon_base = 5000  # Pylon base depth
b_pylon_base = 5000  # Pylon base width

h_pylon_middle = 5000  # Pylon middle section depth
b_pylon_middle = 2200  # Pylon middle section width

h_pylon_top = 5000  # Pylon middle section depth
b_pylon_top = 2200  # Pylon middle section width

# Pier dimensions 
h_pier = 1500 # Pier section depth
b_pier = 5000 # Pier section width

f_sk = 500    # Characteristic yield of the rebars
f_sd = 435    # Design yield strength of the rebars
f_ck = 50     # Characteristic compressive strength of concrete
f_cd = 28     # Design compressive strength of the concrete

s_s = 150     # Longitudinal rebar spacing
s_sw = 150    # Shear stirrups spacing
c_c = 25      # Clear cover in mm

D_rebars = [8,10,12,14,16,20,25,30] # Rebar dimensions





"""
Import M-P interaction curves
"""
# Read interaction surfaces from excel file
# Deck
M_P_Deck = pd.read_excel('Interaction_Surfaces.xlsx',sheet_name = 'Deck-2N25_s=150',skiprows = 1, header = None)
M_P_Deck = np.array(M_P_Deck)
# Pylon
M_P_Pylon_Base = pd.read_excel('Interaction_Surfaces.xlsx',sheet_name = 'Pylon Base-2N30_s=150',skiprows = 1, header = None)
M_P_Pylon_Base = np.array(M_P_Pylon_Base)
M_P_Pylon_Middle = pd.read_excel('Interaction_Surfaces.xlsx',sheet_name = 'Pylon Middle-N30_s=150',skiprows = 1, header = None)
M_P_Pylon_Middle = np.array(M_P_Pylon_Middle)
M_P_Pylon_Top = pd.read_excel('Interaction_Surfaces.xlsx',sheet_name = 'Pylon Top-N30_s=150',skiprows = 1, header = None)
M_P_Pylon_Top = np.array(M_P_Pylon_Top)
# Pier
M_P_Pier = pd.read_excel('Interaction_Surfaces.xlsx',sheet_name = 'Pier-N30_s=150',skiprows = 1, header = None)
M_P_Pier = np.array(M_P_Pier)

# Plot material properties (EN 1992-1-1, SIA 262)
# Generate stress-strain diagram for the rebars (SIA 262 - 4.2.2)
Type = 'B500A'
E_s = 205000 # Modulus of elasticity of the rebars in MPa
if Type == 'B500A':
    f_sd = 435 # Yield stress in MPa
    k_s = 1.05 # Strain hardening ratio
    e_ud = 0.02 # Strain at ultimate stress
elif Type == 'B500B':
    f_sd = 435 # Yield stress in MPa
    k_s = 1.08 # Strain hardening ratio
    e_ud = 0.045 # Strain at ultimate stress
elif Type == 'B500C':
    f_sd = 435 # Yield stress in MPa
    k_s = 1.15 # Strain hardening ratio
    e_ud = 0.065 # Strain at ultimate stress
elif Type == 'B700B':
    f_sd = 610 # Yield stress in MPa
    k_s = 1.08 # Strain hardening ratio
    e_ud = 0.045 # Strain at ultimate stress

# Rebar stress-strain
e_st = [0,f_sd/E_s,e_ud]
s_st = [0,f_sd,f_sd*k_s]

# Plot rebar stress-strain
fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
plt.xlim(0,3)
plt.ylim(0,500)
plt.grid(color = (0.75,0.75,0.75), linestyle = ':', linewidth = 1)
plt.xlabel('$\epsilon_s$ [%]')
plt.ylabel('$\sigma_s$ [MPa]')
plt.plot(np.array(e_st)*100,s_st,'-',color = (0,0,0),linewidth = 1.0,label = Type)  
plt.legend(loc='lower right', fontsize=10, edgecolor='inherit')   
if save_plots == 0:
    plt.show()
else:
    plt.savefig('Stress_Strain_Rebar.svg')
    

# Generate stress-strain diagram for the concrete (EN-1992-1 - 3.1.7, SIA 262 - S4.2.1.4)
f_cd = 28
e_c1d = 0.002
e_c2d = 0.003
n = 2

e_c = list(np.linspace(0,e_c1d,11))
s_c = []
for i in range(len(e_c)):
    s_c.append(f_cd*(1-(1-e_c[i]/e_c1d)**n))

# Concrete stress-strain
e_c.append(e_c2d)
s_c.append(f_cd)

# Plot concrete stress-strain
fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
plt.xlim(0,0.4)
plt.ylim(0,35)
plt.grid(color = (0.75,0.75,0.75), linestyle = ':', linewidth = 1)
plt.xlabel('$\epsilon_c$ [%]')
plt.ylabel('$\sigma_c$ [MPa]')
plt.plot(np.array(e_c)*100,s_c,'-',color = (0,0,0),linewidth = 1.0,label = 'C50/60')  
plt.legend(loc='lower right', fontsize=10, edgecolor='inherit')   
if save_plots == 0:
    plt.show()
else:
    plt.savefig('Stress_Strain_Concrete.svg')

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


# Run analysis
ret = SapModel.Analyze.RunAnalysis()
Load_Combo = 'ELU 2-ENV (Type 2)'

"""
Check Deck Section
"""
# Unlock model
SapModel.SetModelIsLocked(0)

# Minimum required reinforcement
Deck_area = SapModel.PropFrame.GetSectProps('Deck_2.5m')[0]
As_min_deck = 0.06*Deck_area  # SIA 5.5.4.2

# Deck reinforcement
D_s_deck = 25   # Rebar diameter in mm
D_s_layers = 2  # Number of layers
A_eq_s_deck = D_s_layers*math.pi*D_s_deck**2/4
D_eq_s_deck = math.sqrt(A_eq_s_deck*4/math.pi)

if D_s_layers < 2:
    D_s_deck_name = 'N' + str(int(D_s_deck))  # Rebar name
else:
    D_s_deck_name = str(int(D_s_layers)) + 'N' + str(int(D_s_deck))

# Add reinforcement bar size if more than 1 layer is input
if D_s_layers > 1:
    SapModel.PropRebar.SetProp(D_s_deck_name, A_eq_s_deck, D_eq_s_deck)
    # Equivalent clear cover (assuming stirrup diameter = 20 mm)
    cover_s_deck = c_c + 20 + D_s_deck - D_eq_s_deck/2 
else:
    cover_s_deck = c_c + 20


# Get Shape name
Deck_SD = SapModel.PropFrame.GetSDSection('Deck_2.5m')
Deck_SD_Shape_Name = Deck_SD[2][0]
# Edge reinforcement
SapModel.PropFrame.SDShape.SetReinfEdge('Deck_2.5m',Deck_SD_Shape_Name,1,D_s_deck_name,s_s,cover_s_deck,True)
SapModel.PropFrame.SDShape.SetReinfCorner('Deck_2.5m',Deck_SD_Shape_Name,1,D_s_deck_name,True)

# Deck section labels
Deck_section_labels = getFrameSectionLabels(SapModel,'Deck_2.5m')

# Get deck forces
ret = SapModel.Analyze.RunAnalysis()
P_deck = frameSectionForces(SapModel,Deck_section_labels,Load_Combo)[0]
M_deck = frameSectionForces(SapModel,Deck_section_labels,Load_Combo)[1]
V_deck = frameSectionForces(SapModel,Deck_section_labels,Load_Combo)[2]

# Plot M-P interaction (with 25% amplification of deck moments to account for second-order effects and imperfections)
fig = plt.figure(facecolor='white',figsize=(5,3),tight_layout=True)
plt.grid(color = (0.75,0.75,0.75), linestyle = ':', linewidth = 1)
plt.xlabel('Force Axiale, $\itP$ [kN]')
plt.ylabel('Moment, $\itM_{xx}$ [kNm]')
plt.plot(M_P_Deck[:,0]/1000,M_P_Deck[:,1]/1000000,'-',color = (0,0,0),linewidth = 1.0,label = 'Surface de M-P')
for i in range(len(Deck_section_labels)):
    if i == 0:
        plt.scatter(np.array(P_deck[i])/1000,np.array(M_deck[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k',label = 'Forces du modèle')
    else:
        plt.scatter(np.array(P_deck[i])/1000,np.array(M_deck[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k')    
plt.legend(loc='lower left', fontsize=10, edgecolor='inherit')   
if save_plots == 0:
    plt.show()
else:
    plt.savefig('M_P_Deck.svg')

# Get shear reinforcement
# Maximum shear force
V_max_deck = []
for i in range(len(Deck_section_labels)):
    V_max_deck.append(max(abs(max(V_deck[i])),abs(min(V_deck[i]))))
V_max_abs_deck = max(V_max_deck)

# Deck shear reinforcement
material_properties = [f_sk,f_sd,f_ck,f_cd] 
n_stirrups_deck = 2
A_sw_s_deck = getShearReinforcement(V_max_abs_deck,material_properties,0.9*h_deck,b_deck,22,n_stirrups_deck,s_sw)[0]
D_sw_deck = getShearReinforcement(V_max_abs_deck,material_properties,0.9*h_deck,b_deck,22,n_stirrups_deck,s_sw)[2]
print('Deck Stirrups: ' + str(int(n_stirrups_deck)) + ' stirrups,' + ' D' + str(int(D_sw_deck)) + ' at s = ' + str(int(s_sw)) + ' mm')    


"""
Check Pylon Base Section
"""
# Unlock model
SapModel.SetModelIsLocked(0)

# Minimum required reinforcement
Pylon_base_area = h_pylon_base*b_pylon_base
As_min_pylon_base = 0.06*Pylon_base_area    # SIA 5.5.4.2

# Deck reinforcement
D_s_pylon_base = 30 # Rebar diameter in mm
D_s_layers = 2  # Number of layers
A_eq_s_pylon_base = D_s_layers*math.pi*D_s_pylon_base**2/4
D_eq_s_pylon_base = math.sqrt(A_eq_s_pylon_base*4/math.pi)

if D_s_layers < 2:
    D_s_pylon_base_name = 'N' + str(int(D_s_pylon_base))  # Rebar name
else:
    D_s_pylon_base_name = str(int(D_s_layers)) + 'N' + str(int(D_s_pylon_base))

# Add reinforcement bar size if more than 1 layer is input
if D_s_layers > 1:
    SapModel.PropRebar.SetProp(D_s_pylon_base_name, A_eq_s_pylon_base, D_eq_s_pylon_base)
    # Equivalent clear cover (assuming stirrup diameter = 20 mm)
    cover_s_pylon_base = c_c + 20 + D_s_pylon_base - D_eq_s_pylon_base/2 
else:
    cover_s_pylon_base = c_c + 20 

# Get Shape name
Pylon_Base_SD = SapModel.PropFrame.GetSDSection('Pylon_Base_SD')
Pylon_Base_SD_Shape_Name = Pylon_Base_SD[2][0]
# Edge reinforcement
SapModel.PropFrame.SDShape.SetReinfEdge('Pylon_Base_SD',Pylon_Base_SD_Shape_Name,1,D_s_pylon_base_name,s_s,cover_s_pylon_base,True)
SapModel.PropFrame.SDShape.SetReinfCorner('Pylon_Base_SD',Pylon_Base_SD_Shape_Name,1,D_s_pylon_base_name,True)

# Pylon section labels
Pylon_base_section_labels = getFrameSectionLabels(SapModel,'Pylon 5.0x5.0')

# Get pylon base forces
ret = SapModel.Analyze.RunAnalysis()
P_pylon_base = frameSectionForces(SapModel,Pylon_base_section_labels,Load_Combo)[0]
M_pylon_base = frameSectionForces(SapModel,Pylon_base_section_labels,Load_Combo)[1]
V_pylon_base = frameSectionForces(SapModel,Pylon_base_section_labels,Load_Combo)[2]

# Plot M-P interaction
fig = plt.figure(facecolor='white',figsize=(5,3),tight_layout=True)
plt.grid(color = (0.75,0.75,0.75), linestyle = ':', linewidth = 1)
plt.xlabel('Force Axiale, $\itP$ [kN]')
plt.ylabel('Moment, $\itM_{xx}$ [kNm]')
plt.plot(M_P_Pylon_Base[:,0]/1000,M_P_Pylon_Base[:,1]/1000000,'-',color = (0,0,0),linewidth = 1.0,label = 'Surface de M-P')
for i in range(len(Pylon_base_section_labels)):
    if i == 0:
        plt.scatter(np.array(P_pylon_base[i])/1000,np.array(M_pylon_base[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k',label = 'Forces du modèle')
    else:
        plt.scatter(np.array(P_pylon_base[i])/1000,np.array(M_pylon_base[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k')    
plt.legend(loc='lower left', fontsize=10, edgecolor='inherit')   
if save_plots == 0:
    plt.show()
else:
    plt.savefig('M_P_Pylon_Base.svg')

# Get shear reinforcement
# Maximum shear force
V_max_pylon_base = []
for i in range(len(Pylon_base_section_labels)):
    V_max_pylon_base.append(max(abs(max(V_pylon_base[i])),abs(min(V_pylon_base[i]))))
V_max_abs_pylon_base = max(V_max_pylon_base)

# Pylon shear reinforcement
material_properties = [f_sk,f_sd,f_ck,f_cd] 
n_stirrups_pylon_base = 2
A_sw_s_pylon_base = getShearReinforcement(V_max_abs_pylon_base,material_properties,0.9*h_pylon_base,b_pylon_base,22,n_stirrups_pylon_base,s_sw)[0]
D_sw_pylon_base = getShearReinforcement(V_max_abs_pylon_base,material_properties,0.9*h_pylon_base,b_pylon_base,22,n_stirrups_pylon_base,s_sw)[2]
print('Pylon Base Stirrups: ' + str(int(n_stirrups_deck)) + ' stirrups,' + ' D' + str(int(D_sw_deck)) + ' at s = ' + str(int(s_sw)) + ' mm')    


"""
Check Pylon Middle Section
"""
# Unlock model
SapModel.SetModelIsLocked(0)

# Minimum required reinforcement
Pylon_middle_area = h_pylon_middle*b_pylon_middle
As_min_pylon_middle = 0.06*Pylon_middle_area    # SIA 5.5.4.2

# Deck reinforcement
D_s_pylon_middle = 30 # Rebar diameter in mm
D_s_layers = 1  # Number of layers
A_eq_s_pylon_middle = D_s_layers*math.pi*D_s_pylon_middle**2/4
D_eq_s_pylon_middle = math.sqrt(A_eq_s_pylon_middle*4/math.pi)

if D_s_layers < 2:
    D_s_pylon_middle_name = 'N' + str(int(D_s_pylon_middle))  # Rebar name
else:
    D_s_pylon_middle_name = str(int(D_s_layers)) + 'N' + str(int(D_s_pylon_middle))

# Add reinforcement bar size if more than 1 layer is input
if D_s_layers > 1:
    SapModel.PropRebar.SetProp(D_s_pylon_middle_name, A_eq_s_pylon_middle, D_eq_s_pylon_middle)
    # Equivalent clear cover (assuming stirrup diameter = 20 mm)
    cover_s_pylon_middle = c_c + 20 + D_s_pylon_middle - D_eq_s_pylon_middle/2
else:
    cover_s_pylon_middle = c_c + 20

# Get Shape name
Pylon_Middle_SD = SapModel.PropFrame.GetSDSection('Pylon_Middle_SD')
Pylon_Middle_SD_Shape_Name = Pylon_Middle_SD[2][0]
# Edge reinforcement
SapModel.PropFrame.SDShape.SetReinfEdge('Pylon_Middle_SD',Pylon_Middle_SD_Shape_Name,1,D_s_pylon_middle_name,s_s,cover_s_pylon_middle,True)
SapModel.PropFrame.SDShape.SetReinfCorner('Pylon_Middle_SD',Pylon_Middle_SD_Shape_Name,1,D_s_pylon_middle_name,True)

# Pylon section labels
Pylon_middle_section_labels_1 = getFrameSectionLabels(SapModel,'Pylon-P1a')
Pylon_middle_section_labels_2 = getFrameSectionLabels(SapModel,'Pylon-P2a')
Pylon_middle_section_labels_3 = getFrameSectionLabels(SapModel,'Pylon-P1b')
Pylon_middle_section_labels_4 = getFrameSectionLabels(SapModel,'Pylon-P2b')

Pylon_middle_section_labels = Pylon_middle_section_labels_1 + Pylon_middle_section_labels_2 + Pylon_middle_section_labels_3 + Pylon_middle_section_labels_4

# Get pylon base forces
ret = SapModel.Analyze.RunAnalysis()
P_pylon_middle = frameSectionForces(SapModel,Pylon_middle_section_labels,Load_Combo)[0]
M_pylon_middle = frameSectionForces(SapModel,Pylon_middle_section_labels,Load_Combo)[1]
V_pylon_middle = frameSectionForces(SapModel,Pylon_middle_section_labels,Load_Combo)[2]

# Plot M-P interaction
fig = plt.figure(facecolor='white',figsize=(5,3),tight_layout=True)
plt.grid(color = (0.75,0.75,0.75), linestyle = ':', linewidth = 1)
plt.xlabel('Force Axiale, $\itP$ [kN]')
plt.ylabel('Moment, $\itM_{xx}$ [kNm]')
plt.plot(M_P_Pylon_Middle[:,0]/1000,M_P_Pylon_Middle[:,1]/1000000,'-',color = (0,0,0),linewidth = 1.0,label = 'Surface de M-P')
for i in range(len(Pylon_middle_section_labels)):
    if i == 0:
        plt.scatter(np.array(P_pylon_middle[i])/1000,np.array(M_pylon_middle[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k',label = 'Forces du modèle')
    else:
        plt.scatter(np.array(P_pylon_middle[i])/1000,np.array(M_pylon_middle[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k')    
plt.legend(loc='lower left', fontsize=10, edgecolor='inherit')   
if save_plots == 0:
    plt.show()
else:
    plt.savefig('M_P_Pylon_Middle.svg')

# Get shear reinforcement
# Maximum shear force
V_max_pylon_middle = []
for i in range(len(Pylon_middle_section_labels)):
    V_max_pylon_middle.append(max(abs(max(V_pylon_middle[i])),abs(min(V_pylon_middle[i]))))
V_max_abs_pylon_middle = max(V_max_pylon_middle)

# Pylon shear reinforcement
material_properties = [f_sk,f_sd,f_ck,f_cd] 
n_stirrups_pylon_middle = 1
A_sw_s_pylon_middle = getShearReinforcement(V_max_abs_pylon_middle,material_properties,0.9*h_pylon_middle,b_pylon_middle,22,n_stirrups_pylon_middle,s_sw)[0]
D_sw_pylon_middle = getShearReinforcement(V_max_abs_pylon_middle,material_properties,0.9*h_pylon_middle,b_pylon_middle,22,n_stirrups_pylon_middle,s_sw)[2]
print('Pylon Middle Section Stirrups: ' + str(int(n_stirrups_pylon_middle)) + ' stirrups,' + ' D' + str(int(D_sw_pylon_middle)) + ' at s = ' + str(int(s_sw)) + ' mm')  

"""
Check Pylon Top Section
"""
# Unlock model
SapModel.SetModelIsLocked(0)

# Minimum required reinforcement
Pylon_top_area = h_pylon_top*b_pylon_top
As_min_pylon_top = 0.06*Pylon_top_area    # SIA 5.5.4.2

# Deck reinforcement
D_s_pylon_top = 30 # Rebar diameter in mm
D_s_layers = 1  # Number of layers
A_eq_s_pylon_top = D_s_layers*math.pi*D_s_pylon_top**2/4
D_eq_s_pylon_top = math.sqrt(A_eq_s_pylon_top*4/math.pi)

if D_s_layers < 2:
    D_s_pylon_top_name = 'N' + str(int(D_s_pylon_top))  # Rebar name
else:
    D_s_pylon_top_name = str(int(D_s_layers)) + 'N' + str(int(D_s_pylon_top))

# Add reinforcement bar size if more than 1 layer is input
if D_s_layers > 1:
    SapModel.PropRebar.SetProp(D_s_pylon_top_name, A_eq_s_pylon_top, D_eq_s_pylon_top)
    # Equivalent clear cover (assuming stirrup diameter = 20 mm)
    cover_s_pylon_top = c_c + 20 + D_s_pylon_top - D_eq_s_pylon_top/2
else:
    cover_s_pylon_top = c_c + 20

# Get Shape name
Pylon_Top_SD = SapModel.PropFrame.GetSDSection('Pylon_Top_SD')
Pylon_Top_SD_Shape_Name = Pylon_Top_SD[2][0]
# Edge reinforcement
SapModel.PropFrame.SDShape.SetReinfEdge('Pylon_Top_SD',Pylon_Top_SD_Shape_Name,1,D_s_pylon_top_name,s_s,cover_s_pylon_top,True)
SapModel.PropFrame.SDShape.SetReinfCorner('Pylon_Top_SD',Pylon_Top_SD_Shape_Name,1,D_s_pylon_top_name,True)

# Pylon section labels
Pylon_top_section_labels_1 = getFrameSectionLabels(SapModel,'Pylon-P3a')
Pylon_top_section_labels_2 = getFrameSectionLabels(SapModel,'Pylon-P3b')


Pylon_top_section_labels = Pylon_top_section_labels_1 + Pylon_top_section_labels_2

# Get pylon base forces
ret = SapModel.Analyze.RunAnalysis()
P_pylon_top = frameSectionForces(SapModel,Pylon_top_section_labels,Load_Combo)[0]
M_pylon_top = frameSectionForces(SapModel,Pylon_top_section_labels,Load_Combo)[1]
V_pylon_top = frameSectionForces(SapModel,Pylon_top_section_labels,Load_Combo)[2]

# Plot M-P interaction
fig = plt.figure(facecolor='white',figsize=(5,3),tight_layout=True)
plt.grid(color = (0.75,0.75,0.75), linestyle = ':', linewidth = 1)
plt.xlabel('Force Axiale, $\itP$ [kN]')
plt.ylabel('Moment, $\itM_{xx}$ [kNm]')
plt.plot(M_P_Pylon_Top[:,0]/1000,M_P_Pylon_Top[:,1]/1000000,'-',color = (0,0,0),linewidth = 1.0,label = 'Surface de M-P')
for i in range(len(Pylon_top_section_labels)):
    if i == 0:
        plt.scatter(np.array(P_pylon_top[i])/1000,np.array(M_pylon_top[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k',label = 'Forces du modèle')
    else:
        plt.scatter(np.array(P_pylon_top[i])/1000,np.array(M_pylon_top[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k')      
plt.legend(loc='lower left', fontsize=10, edgecolor='inherit')   
if save_plots == 0:
    plt.show()
else:
    plt.savefig('M_P_Pylon_Top.svg')

# Get shear reinforcement
# Maximum shear force
V_max_pylon_top = []
for i in range(len(Pylon_top_section_labels)):
    V_max_pylon_top.append(max(abs(max(V_pylon_top[i])),abs(min(V_pylon_top[i]))))
V_max_abs_pylon_top = max(V_max_pylon_top)

# Pylon shear reinforcement
material_properties = [f_sk,f_sd,f_ck,f_cd] 
n_stirrups_pylon_top = 1
A_sw_s_pylon_top = getShearReinforcement(V_max_abs_pylon_top,material_properties,0.9*h_pylon_top,b_pylon_top,22,n_stirrups_pylon_top,s_sw)[0]
D_sw_pylon_top = getShearReinforcement(V_max_abs_pylon_top,material_properties,0.9*h_pylon_top,b_pylon_top,22,n_stirrups_pylon_top,s_sw)[2]
print('Pylon Top Section Stirrups: ' + str(int(n_stirrups_pylon_top)) + ' stirrups,' + ' D' + str(int(D_sw_pylon_top)) + ' at s = ' + str(int(s_sw)) + ' mm')      


"""
Check Piers
"""
# Unlock model
SapModel.SetModelIsLocked(0)

# Minimum required reinforcement
Pier_area = h_pier*b_pier
As_min_pier = 0.06*Pier_area    # SIA 5.5.4.2

# Deck reinforcement
D_s_pier = 30 # Rebar diameter in mm
D_s_layers = 1  # Number of layers
A_eq_s_pier = D_s_layers*math.pi*D_s_pier**2/4
D_eq_s_pier = math.sqrt(A_eq_s_pier*4/math.pi)

if D_s_layers < 2:
    D_s_pier_name = 'N' + str(int(D_s_pier))  # Rebar name
else:
    D_s_pier_name = str(int(D_s_layers)) + 'N' + str(int(D_s_pier))

# Add reinforcement bar size if more than 1 layer is input
if D_s_layers > 1:
    SapModel.PropRebar.SetProp(D_s_pier_name, A_eq_s_pier, D_eq_s_pier)
    # Equivalent clear cover (assuming stirrup diameter = 20 mm)
    cover_s_pier = c_c + 20 + D_s_pier - D_eq_s_pier/2
else:
    cover_s_pier = c_c + 20

# Get Shape name
Pier_SD = SapModel.PropFrame.GetSDSection('Pier_SD')
Pier_SD_Shape_Name = Pier_SD[2][0]
# Edge reinforcement
SapModel.PropFrame.SDShape.SetReinfEdge('Pier_SD',Pier_SD_Shape_Name,1,D_s_pier_name,s_s,cover_s_pier,True)
SapModel.PropFrame.SDShape.SetReinfCorner('Pier_SD',Pier_SD_Shape_Name,1,D_s_pier_name,True)

# Pier section labels
Pier_section_labels = getFrameSectionLabels(SapModel,'Pier 1.5x5.73')


# Get pier base forces
ret = SapModel.Analyze.RunAnalysis()
P_pier = frameSectionForces(SapModel,Pier_section_labels,Load_Combo)[0]
M_pier = frameSectionForces(SapModel,Pier_section_labels,Load_Combo)[1]
V_pier = frameSectionForces(SapModel,Pier_section_labels,Load_Combo)[2]

# Plot M-P interaction
fig = plt.figure(facecolor='white',figsize=(5,3),tight_layout=True)
plt.grid(color = (0.75,0.75,0.75), linestyle = ':', linewidth = 1)
plt.xlabel('Force Axiale, $\itP$ [kN]')
plt.ylabel('Moment, $\itM_{xx}$ [kNm]')
plt.plot(M_P_Pier[:,0]/1000,M_P_Pier[:,1]/1000000,'-',color = (0,0,0),linewidth = 1.0,label = 'Surface de M-P')
for i in range(len(Pier_section_labels)):
    if i == 0:
        plt.scatter(np.array(P_pier[i])/1000,np.array(M_pier[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k',label = 'Forces du modèle')
    else:
        plt.scatter(np.array(P_pier[i])/1000,np.array(M_pier[i])*1.25/1000000, s = 3, marker = 'o', color = 'r',linewidths=0.5,edgecolors='k')      
plt.legend(loc='lower left', fontsize=10, edgecolor='inherit')   
if save_plots == 0:
    plt.show()
else:
    plt.savefig('M_P_Pier.svg')

# Get shear reinforcement
# Maximum shear force
V_max_pier = []
for i in range(len(Pier_section_labels)):
    V_max_pier.append(max(abs(max(V_pier[i])),abs(min(V_pier[i]))))
V_max_abs_pier = max(V_max_pier)

# Pylon shear reinforcement
material_properties = [f_sk,f_sd,f_ck,f_cd] 
n_stirrups_pier = 1
A_sw_s_pier = getShearReinforcement(V_max_abs_pier,material_properties,0.9*h_pier,b_pylon_top,22,n_stirrups_pier,s_sw)[0]
D_sw_pier = getShearReinforcement(V_max_abs_pier,material_properties,0.9*h_pier,b_pylon_top,22,n_stirrups_pier,s_sw)[2]
print('Pier Section Stirrups: ' + str(int(n_stirrups_pier)) + ' stirrups,' + ' D' + str(int(D_sw_pier)) + ' at s = ' + str(int(s_sw)) + ' mm')     