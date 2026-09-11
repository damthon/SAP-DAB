# -*- coding: utf-8 -*-
"""
This code assesses the vibrational behavior of the footbridge using the method in SETRA 
"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt
from expFit import expFit
import os
import glob

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['text.usetex'] = False
plt.rc('mathtext',fontset='stix')

save_plots = 1
initial_directory = os.getcwd()
g = 9.81     # Gravitational acceleration (m/s2)

""" Input""" 
Class = 'III' # Footbridge class: 'I', 'II', 'III', 'IV'
Comfort_level = 'Max' # Comfort level: 'Max', 'Avg', 'Min'
nat_freq = 2.25 # Natural frequency of the footbridge considered
Mode = 'V' # Mode 'V': vertical, Mode 'Lo': longitudinal, Mode 'La': lateral
Type = 'PC' # Footbridge type: 'RC'(reinforced concrete), 'PC' (prestressed concrete), 'CO' (composite), 'S' (steel), 'T' (timber)
A_deck = 225  # Area of the bridge deck [m2]
output_acc = 'SETRA_M3'

""" Load Models """ 
# Critical damping ratio
if Type == 'RC':
    eta = 0.013
elif Type == 'PC' or Type == 'T':
    eta = 0.01
elif Type == 'CO':
    eta = 0.006
elif Type == 'S':
    eta = 0.004

# Allowable acceleration range
# Vertical accelerations
if Comfort_level == 'Max':
    acc_ver_range = [0,0.5]
elif Comfort_level == 'Mean':
    acc_ver_range = [0.5,1]
else:
    acc_ver_range = [1,2.5]
# Horizontal acceleration
acc_hor_range = [0,0.1]

# Resonance risk 
if nat_freq <=2.1 and nat_freq>=1.7:
    risk_resonance = 1 # Maximum risk
elif (nat_freq <=2.6 and nat_freq>=2.1) or (nat_freq <1.7 and nat_freq>=1.0):
    risk_resonance = 2 # Medium risk
elif (nat_freq >2.6 and nat_freq<=5):
    risk_resonance = 3 # Low risk
else:
    risk_resonance = 4 # Negligible risk
 
# Dynamic load cases
LC = []
if (Class == 'II' or Class == 'III') and (risk_resonance == 1 or risk_resonance == 2):
    LC.append(1)
elif Class == 'I':
    LC.append(2)
if (Class == 'I' or Class == 'II'): # Second harmonic
    LC.append(3)

# Crowd density [pedestrian/m2] and equivalent number of pedestrians
Crowd_D = []
N_eq = []
if 1 in LC and Class == 'II':
    Crowd_D.append(0.8)
    n = 0.8*A_deck
    n_eq = 10.8*(eta*n)**0.5
    N_eq.append(n_eq)
elif 1 in LC and Class == 'III':
    Crowd_D.append(0.5)
    n = 0.5*A_deck
    n_eq = 10.8*(eta*n)**0.5
    N_eq.append(n_eq)
elif 2 in LC:
    Crowd_D.append(1.0)
    n = 1.0*A_deck
    n_eq = 1.85*(n)**0.5
    N_eq.append(n_eq)
# Second harmonic
if 3 in LC and Class == 'I':
    Crowd_D.append(1.0)
    n = 1.0*A_deck
    n_eq = 1.85*(n)**0.5
    N_eq.append(n_eq)
elif  3 in LC and Class == 'II':
    Crowd_D.append(0.8)
    n = 0.8*A_deck
    n_eq = 10.8*(eta*n)**0.5
    N_eq.append(n_eq)

# Reduction coefficients (accounts for probability that footfall frequency approaches critical range of natural frequencies)
if Mode == 'V' or Mode == 'Lo':
    # Vertical and longitudinal vibrations
    psi_ver = []
    if 1 in LC or 2 in LC:
        if nat_freq<=2.1 and nat_freq>=1.7:
            psi_ver_temp = 1.0
        elif nat_freq<1.7 and nat_freq>=1.0:
            psi_ver_temp = (nat_freq - 1.0)/0.7
        elif nat_freq>2.1 and nat_freq<=2.6:
            psi_ver_temp = (2.6 - nat_freq )/0.5
        else:
            psi_ver_temp = 0
        psi_ver.append(psi_ver_temp)
    if 3 in LC:
        if nat_freq<=4.2 and nat_freq>=3.4:
            psi_ver_temp = 1.0
        elif nat_freq<3.4 and nat_freq>=2.6:
            psi_ver_temp = (nat_freq - 2.6)/0.8
        elif nat_freq>4.2 and nat_freq<=5:
            psi_ver_temp = (5 - nat_freq )/0.8
        else:
            psi_ver_temp = 0
        psi_ver.append(psi_ver_temp)
else:
    # Lateral vibrations
    psi_lat = []
    if 1 in LC or 2 in LC:
        if nat_freq<=1.1 and nat_freq>=0.5:
            psi_lat_temp = 1.0
        elif nat_freq<0.5 and nat_freq>=0.3:
            psi_lat_temp = (nat_freq - 0.3)/0.2
        elif nat_freq>1.1 and nat_freq<=1.3:
            psi_lat_temp = (1.3 - nat_freq )/0.3
        else:
            psi_lat_temp = 0
        psi_lat.append(psi_lat_temp)
    if 3 in LC:
        if nat_freq<=2.1 and nat_freq>=1.7:
            psi_lat_temp = 1.0
        elif nat_freq<1.7 and nat_freq>=1.3:
            psi_lat_temp = (nat_freq - 1.3)/0.4
        elif nat_freq>2.1 and nat_freq<=2.5:
            psi_lat_temp = (2.5 - nat_freq )/0.4
        else:
            psi_lat_temp = 0
        psi_lat.append(psi_lat_temp)

# Load Case Models
# F = p_uni*cos*(2πtfv*t)
if Mode == 'V':
    P = 280 # Component due to single pedestrian [N]
    p_uni_V = []
    for i in range(len(LC)):
        if LC[i] == 3:
            P = 70
        p_uni_V.append(N_eq[i]*P*psi_ver[i]/A_deck)
elif Mode == 'Lo':
    P = 140 # Component due to single pedestrian [N]
    p_uni_Lo = []
    for i in range(len(LC)):
        if LC[i] == 3:
            P = 35
        p_uni_Lo.append(N_eq[i]*P*psi_ver[i]/A_deck)
elif Mode == 'La':
    P = 35 # Component due to single pedestrian [N]
    p_uni_La = []
    for i in range(len(LC)):
        if LC[i] == 3:
            P = 7
        p_uni_La.append(N_eq[i]*P*psi_lat[i]/A_deck)
        
    
    
# # Walking excitation
# m_w = 0           # Method to obtain the parameters for walking excitation (0 for Rainer, 1 for Willford)
# d_f_step_w = 0.01 # Intervals at which the step frequency is calculated
# type_w = 0        # 1 for marching, 0 for random walking 
# n_w = 10          # Number of walkers
# # Running excitation
# m_ru = 0         # Method to obtain the parameters for running excitation (0 for Rainer, 1 for Bachmann, 2 for ISO)
# NSteps_ru = 53   # Number of steps required to cross the span (calculated for an assumed stride length of 1.3 m)
# n_ru = 10          # Number of runners (for synchronized running)
# Q_ru = 0.8         # Bodyweight in kN (Table  1-1, AISC Design Guide 11)
# d_f_step_ru = 0.01 # Intervals at which the step frequency is calculated
# # Rythmic excitation (using jumping in this case)
# t_r = 3           # Type of rythmic excitation (0 for group dancing, 1 for concert, 2 for aerobics, 3 for normal jumping)
# m_f_step_r = 2    # Method for obtaing the step frequency (0: mimimum of the range, 1: average of the range, 2: maximum of the range)
# d_f_step_r = 0.01 # Intervals at which the step frequency is calculated

# """ Fourier Series Parameters """ 
# # Walking excitation Fourier series parameters
# f_step_w = 2.0    # Frequency of 1 step (walking) in Hz (Table  1-1, AISC Design Guide 11)
# beta_w = 0.02     # Viscous damping
# if Methods_walking[m_w] == 'Rainer':
#     Q_w = 0.7     # Bodyweight in kN (Table  1-1, AISC Design Guide 11)
#     f_step_w = [1.6,2.2]           # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
#     alpha_w = [0.5,0.2,0.1,0.05]   # Dynamic coefficients for the first i harmonics (Table  1-1, AISC Design Guide 11)
# else:  
#     Q_w = 0.75    # Bodyweight in kN (Table  1-1, AISC Design Guide 11)
#     f_step_w = [1.6,2.2]             # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
#     alpha_w = [0.4,0.07,0.06,0.05]   # Dynamic coefficients for the first i harmonics (Table  1-1, AISC Design Guide 11)
    
# # Running excitation Fourier series parameters
# beta_ru = 0.02       # Viscous damping
# if Methods_running[m_ru] == 'Rainer':
#     f_step_ru = [1.6,4.0]          # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
#     alpha_ru = [1.4,0.4,0.2,0.1]   # Dynamic coefficients for the f f_step_w = [1.6,2.2]   irst i harmonics (Table  1-1, AISC Design Guide 11)
# elif Methods_running[m_ru] == 'Bachmann':
#     f_step_ru = [2.0,3.0]      # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
#     alpha_ru = [1.6,0.7,0.2]   # Dynamic coefficients for the first i harmonics (Table  1-1, AISC Design Guide 11)
# else:
#     f_step_ru = [2.0,4.0]      # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
#     alpha_ru = [1.4,0.4,0.1]   # Dynamic coefficients for the first i harmonics (Table  1-1, AISC Design Guide 11)
 
# # Rythmic excitation Fourier series parameters
# if Types_rythmic[t_r] == 'Group Dancing':
#     wp_r = 0.6             # Unit weight of rythmic activity in kN/m2 (Table  1-2, AISC Design Guide 11)
#     f_step_r = [1.5,2.5]   # Step frequency range in Hz (Table  1-2, AISC Design Guide 11)
#     alpha_r = [0.5,0.05]   # Dynamic coefficients for the first i harmonics (Table  1-2, AISC Design Guide 11)
# elif Types_rythmic[t_r] == 'Concert':
#     wp_r = 1.              # Unit weight of rythmic activity in kN/m2 (Table  1-2, AISC Design Guide 11)
#     f_step_r = [1.5,2.5]   # Step frequency range in Hz (Table  1-2, AISC Design Guide 11)
#     alpha_r = [0.25,0.05]  # Dynamic coefficients for the first i harmonics (Table  1-2, AISC Design Guide 11)
# elif Types_rythmic[t_r] == 'Aerobics':
#      wp_r = 0.2               # Unit weight of rythmic activity in kN/m2 (Table  1-2, AISC Design Guide 11)
#      f_step_r = [1.5,2.5]     # Step frequency range in Hz (Table  1-2, AISC Design Guide 11)
#      alpha_r = [1.5,0.6,0.1]  # Dynamic coefficients for the first i harmonics (Table  1-2, AISC Design Guide 11)
# else:
#      wp_r = 0.19                 # Unit weight of rythmic activity in kN/m2 (Table  1-2, AISC Design Guide 11)
#      f_step_r = [1.5,2.5]        # Step frequency range in Hz (Table  1-2, AISC Design Guide 11)
#      alpha_r = [1.8,1.3,0.7,0.2] # Dynamic coefficients for the first i harmonics (Table  1-2, AISC Design Guide 11)
      
# """ Read Files for FRF Method (Applicable for regular and irregular framing) """ 
# # Walking/Running excitation
# r = open('FRF_Walking-Running.txt','r')
# FRF_freq_walk_run = [] # Initialize frequency (Hz)
# FRF_acc_walk_run = []  # Initialize acceleration (%g/kN)
# content_list = r.readlines()
# for j in range(1,len(content_list)):
#     FRF_freq_walk_run .append(float(content_list[j].split('\t')[0]))   
#     FRF_acc_walk_run.append(float(content_list[j].split('\t')[1].split('\n')[0]))
# FRF_freq_walk_run = np.array(FRF_freq_walk_run )
# FRF_acc_walk_run = np.array(FRF_acc_walk_run)/g*100

# # Rythmic excitation
# r = open('FRF_Rythmic.txt','r')
# FRF_freq_rythmic= [] # Initialize frequency (Hz)
# FRF_acc_rythmic = []  # Initialize acceleration (%g/(kN/m2))
# content_list = r.readlines()
# for j in range(1,len(content_list)):
#     FRF_freq_rythmic.append(float(content_list[j].split('\t')[0]))   
#     FRF_acc_rythmic.append(float(content_list[j].split('\t')[1].split('\n')[0]))
# FRF_freq_rythmic = np.array(FRF_freq_rythmic)
# FRF_acc_rythmic = np.array(FRF_acc_rythmic)/g*100

# """ Find the Resonance Frequencies """ 
# # Walking/Running excitation
# for i in range(len(FRF_freq_walk_run)):
#     if FRF_acc_walk_run[i] == max(FRF_acc_walk_run):
#         FRF_freq_walk_run_resonance = FRF_freq_walk_run[i]
# # Rythmic excitation
# for i in range(len(FRF_freq_rythmic)):
#     if FRF_acc_rythmic[i] == max(FRF_acc_rythmic):
#         FRF_freq_rythmic_resonance = FRF_freq_rythmic[i]
# # Find the harmonic number that causes resonance 
# range_running_harmonics = np.linspace(1,len(alpha_ru),len(alpha_ru))
# for l in range(len(alpha_ru)):     
#     if FRF_freq_walk_run_resonance >=  range_running_harmonics[l]*f_step_ru[0] and FRF_freq_walk_run_resonance <=  range_running_harmonics[l]*f_step_ru[1]:
#         h = l+1                     # Harmonic numbern
        
# """ Implement the FRF Method (Applicable for regular and irregular framing) """ 
# ########################## Walking excitation (low-frequency) ############################
# # Calculate the resonance build up factor, rho
# if beta_w < 0.01:
#     rho = 50*beta_w + 0.25
# elif beta_w >= 0.01 and beta_w <= 0.03:
#     rho = 12.5*beta_w + 0.625
# else:
#     rho = 1.0
# # Step frequency range
# f_step_w = np.linspace(f_step_w[0],f_step_w[1],int((f_step_w[1]-f_step_w[0])/d_f_step_w+1))    
# # Calculate the dynamic coefficients
# alpha_w_step = [[]]*len(f_step_w)        # Initialize the dynamic coefficient at each step
# f_n_w = [[]]*len(f_step_w)               # Intialize first harmonics for walking excitation
# for i in range(len(f_step_w)):     
#     f_n_w[i] = np.linspace(1,len(alpha_w),len(alpha_w))*f_step_w[i]  # First harmonics for walking excitation
#     # Calculate dynamic coefficients for low-frequency floors (less than 4th harmonic)  
#     a_w = expFit(f_n_w[i][1:len(alpha_w)],alpha_w[1:len(alpha_w)])[0]  # Coefficient a of the exponential fit from second harmonic onwards
#     b_w = expFit(f_n_w[i][1:len(alpha_w)],alpha_w[1:len(alpha_w)])[1]  # Coefficient b of the exponential fit from second harmonic onwards
#     temp = []
#     for j in range(len(FRF_freq_walk_run )):
#         if FRF_freq_walk_run [j] <= f_n_w[i][len(f_n_w[i])-1]:
#             temp.append(a_w*mt.exp(-b_w*FRF_freq_walk_run [j]))
#         else:
#             break
#         alpha_w_step[i] = temp
# # Calculate the peak accelerations
# a_p_w = [[]]*len(f_step_w)            # Intialize the accelerations (%g)
# a_p_w_peak = [[]]*len(f_step_w)       # Intialize the peak accelerations (%g) 
# # Amplification due to number of walkers
# if type_w == 0: # Random walking
#     n_w_amp = mt.sqrt(n_w) 
# else: # Marching
#     n_w_amp = n_w
# for i in range(len(f_step_w)):      
#     a_p_w[i] = FRF_acc_walk_run[0:len(alpha_w_step[i])]*alpha_w_step[i][0:len(alpha_w_step[i])]*Q_w*rho*n_w_amp
#     a_p_w_peak[i] = max(a_p_w[i])
# # Find step frequency that gives the maximum total peak acceleration 
# for m in range(len(f_step_w)): 
#     if a_p_w_peak[m] == max(a_p_w_peak):
#         a_p_w_max = a_p_w[m]              # Maximum peak total acceleration  
#         f_step_w_max = f_step_w[m]        # Step frequency that gives the maximum acceleration
#         f_n_w_max = f_n_w[m]              # First harmonics for the step frequency that gives the maximum acceleration
#         break
# ##########################################################################################   
 
# ################################## Running excitation ####################################
# NSteps_ru = min(10,NSteps_ru)
# # Step frequency range
# f_step_ru = np.linspace(f_step_ru[0],f_step_ru[1],int((f_step_ru[1]-f_step_ru[0])/d_f_step_ru+1))   
# # Calculate the dynamic coefficients
# alpha_ru_step = [[]]*len(f_step_ru)        # Initialize the dynamic coefficient at each step
# f_n_ru = [[]]*len(f_step_ru)               # Intialize first harmonics for running excitation
# for i in range(len(f_step_ru)):     
#     f_n_ru[i] = np.linspace(1,len(alpha_ru),len(alpha_ru))*f_step_ru[i]  # First harmonics for running excitation
#     # Calculate dynamic coefficients for running excitation 
#     a_ru = expFit(f_n_ru[i][1:len(alpha_ru)],alpha_ru[1:len(alpha_ru)])[0]  # Coefficient a of the exponential fit from second harmonic onwards
#     b_ru = expFit(f_n_ru[i][1:len(alpha_ru)],alpha_ru[1:len(alpha_ru)])[1]  # Coefficient b of the exponential fit from second harmonic onwards
#     temp = []
#     for j in range(len(FRF_freq_walk_run )):
#         if FRF_freq_walk_run [j] <= f_n_ru[i][len(f_n_ru[i])-1]:
#             temp.append(a_ru*mt.exp(-b_ru*FRF_freq_walk_run [j]))
#         else:
#             break
#         alpha_ru_step[i] = temp
# # Calculate the peak accelerations
# a_p_ru = [[]]*len(f_step_ru)            # Intialize the accelerations (%g)
# a_p_ru_peak = [[]]*len(f_step_ru)       # Intialize the peak accelerations (%g)   
# for i in range(len(f_step_ru)):  
#     rho_ru = (1-mt.exp(-2*mt.pi*beta_ru*h*NSteps_ru))
#     a_p_ru[i] = FRF_acc_walk_run[0:len(alpha_ru_step[i])]*alpha_ru_step[i][0:len(alpha_ru_step[i])]*Q_w*rho_ru*mt.sqrt(n_ru)
#     a_p_ru_peak[i] = max(a_p_ru[i])
# # Find step frequency that gives the maximum total peak acceleration 
# for m in range(len(f_step_ru)): 
#     if a_p_ru_peak[m] == max(a_p_ru_peak):
#         a_p_ru_max = a_p_ru[m]              # Maximum peak total acceleration  
#         f_step_ru_max = f_step_ru[m]        # Step frequency that gives the maximum acceleration
#         f_n_ru_max = f_n_ru[m]              # First harmonics for the step frequency that gives the maximum acceleration
#         break
# ##########################################################################################   
           
# ################################### Rythmic excitation ###################################
# # Step frequency range
# f_step_r = np.linspace(f_step_r[0],f_step_r[1],int((f_step_r[1]-f_step_r[0])/d_f_step_r+1))    
# # Frequency of the harmonics for each considered step frequency
# f_n_r = [[]]*len(f_step_r)               # Intialize first harmonics for rythmic excitation
# FRF_acc_rythmic_h = [[]]*len(f_step_r)   # Initiliaze FRF acceleration at each harmonic  (%g)
# a_p_r = [[]]*len(f_step_r)               # Intialize the peak accelerations (%g)
# a_p_r_total = [[]]*len(f_step_r)         # Intialize the peak accelerations (%g)
# for i in range(len(f_step_r)):
#     f_n_r[i] = np.linspace(1,len(alpha_r),len(alpha_r))*f_step_r[i]  # First harmonics for rythmic excitation
#     # Calculate the peak accelerations for each harmonic
#     FRF_acc_rythmic_h[i] = np.interp(f_n_r[i],FRF_freq_rythmic,FRF_acc_rythmic)  # FRF acceleration at each harmonic
#     a_p_r[i] = FRF_acc_rythmic_h[i]*alpha_r*wp_r  
#     # Calculate peak acceleration total response
#     a_p_r_total[i] = 0         # Intialize the total peak accelerations (%g)
#     for k in range(len(a_p_r[i])):
#             a_p_r_total[i] =  a_p_r[i][k]**1.5 + a_p_r_total[i]
#     a_p_r_total[i] = a_p_r_total[i]**(1/1.5)
# # Find step frequency that gives the maximum total peak acceleration 
# for m in range(len(f_step_r)): 
#     if a_p_r_total[m] == max(a_p_r_total):
#         a_p_r_total_max = max(a_p_r_total)            # Maximum peak total acceleration  
#         f_step_r_max = f_step_r[m]                    # Step frequency that gives the maximum acceleration
#         f_n_r_max = f_n_r[m]                          # FRF freqeuncy at each harmonic for the step frequency that gives the maximum acceleration
#         FRF_acc_rythmic_h_max = FRF_acc_rythmic_h[m]  # FRF acceleration at each harmonic for the step frequency that gives the maximum acceleration
#         break
# ##########################################################################################  

# """ Create Files with the Peak Acceleration for Each Scenario """ 
# acc_directory = os.path.join(initial_directory,'Max_Accelerations')
# os.chdir(acc_directory) # Go to directory with results
# Walking_filename = 'Walking-' + Methods_walking[m_w] + '.txt' 
# Running_filename = 'Running-' + Methods_running[m_ru] + '.txt' 
# Rythmic_filename = 'Rythmic-' + Types_rythmic[t_r] + '.txt' 
# f = open(Walking_filename, "a")
# f.truncate(0)
# f.write(str(round(max(a_p_w_max),2)))
# f.close()
# f = open(Running_filename, "a")
# f.truncate(0)
# f.write(str(round(max(a_p_ru_max),2)))
# f.close()
# f = open(Rythmic_filename, "a")
# f.truncate(0)
# f.write(str(round(a_p_r_total_max,2)))
# f.close()
# os.chdir(initial_directory) # Go to original directory

# """ Plots """ 
# ############################## Running/Walking excitation ################################
# # Create figure FRF - Walking/Running
# fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
# plt.xlim(0.0,20)
# plt.ylim(0,0.5)
# plt.xlabel('Fréquence [Hz]')
# plt.ylabel('FRF Acc. [%g / kN]')
# plt.plot(FRF_freq_walk_run ,FRF_acc_walk_run,'-',color = (0,0,0),linewidth = 1.0)
# # plt.legend(loc = 'lower right',fontsize = 11,edgecolor = 'inherit')
# if save_plots == 0:
#     plt.show()
# else:
#     plt.savefig('FRF_Walking-Running.svg')
# # Create figure peak accelerations - Walking/Running
# fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
# plt.xlim(0.0,20)
# plt.ylim(0,1.2)
# plt.xlabel('Fréquence [Hz]')
# plt.ylabel('Acc. Maximales [%g]')
# plt.plot(FRF_freq_walk_run [0:len(a_p_w_max)],a_p_w_max,'-',color = (0,0,0),linewidth = 1.0,label = 'Marcher')
# plt.plot(FRF_freq_walk_run [0:len(a_p_ru_max)],a_p_ru_max,'--',color = (1,0,0),linewidth = 1.0,label = 'Courir')
# plt.scatter(FRF_freq_walk_run_resonance,max(a_p_w_max),s=15,marker='o',edgecolor='k',color = (0.5,0.5,0.5),alpha=1,linewidth=1,zorder=10)
# plt.scatter(FRF_freq_walk_run_resonance,max(a_p_ru_max),s=15,marker='o',edgecolor='k',color = (1,0.,0.),alpha=1,linewidth=1,zorder=10)
# # Annotate
# Peak_acceleration_w = '$a_{max}$ (marcher) = '+ str(round(max(a_p_w_max),2)) + ' %g'
# Peak_acceleration_ru = '$a_{max}$ (couir) = '+ str(round(max(a_p_ru_max),2)) + ' %g'
# y_text = 0.45
# x_text = 7
# plt.annotate(Peak_acceleration_w,(x_text,y_text),textcoords="offset points",xytext=(0,0),ha='left',fontsize=10) 
# plt.annotate(Peak_acceleration_ru,(x_text,y_text-0.1),textcoords="offset points",xytext=(0,0),ha='left',fontsize=10) 
# plt.legend(loc = 'upper right',fontsize = 11,edgecolor = 'inherit')
# if save_plots == 0:
#     plt.show()
# else:
#     plt.savefig('Peak_Acc_Walking-Running.svg')
# # Create figure dynamic coefficient - Walking/Running
# # Walking exponential fit
# f_fit_w = np.linspace(0,10,100)
# alpha_fit_w = []
# for i in range(len(f_fit_w)):
#     alpha_fit_w.append(a_w*mt.exp(-b_w*f_fit_w[i]))
# # Running exponential fit
# f_fit_ru = np.linspace(0,20,100)
# alpha_fit_ru = []
# for i in range(len(f_fit_ru)):
#     alpha_fit_ru.append(a_ru*mt.exp(-b_ru*f_fit_ru[i]))
# # Plot fits
# fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
# plt.xlim(0.0,20)
# plt.ylim(0,0.5) 
# plt.xlabel('Fréquence [Hz]')
# plt.ylabel('Coefficient dynamique, ' + r'$\alpha$')
# #plt.ylabel('Coefficient dynamique, r$alpha$')
# plt.scatter(f_n_w_max[1:len(f_n_w_max)],alpha_w[1:len(f_n_w_max)],s=15,marker='o',edgecolor='k',color = (0.5,0.5,0.5),alpha=1,linewidth=1,zorder=10)
# plt.scatter(f_n_ru_max[1:len(f_n_ru_max)],alpha_ru[1:len(f_n_ru_max)],s=15,marker='o',edgecolor='k',color = (1,0.,0.),alpha=1,linewidth=1,zorder=10)
# plt.plot(f_fit_w,alpha_fit_w,'-',color = (0,0,0),linewidth = 1.0,label='Marcher')
# plt.plot(f_fit_ru,alpha_fit_ru,'--',color = (1,0,0),linewidth = 1.0,label='Courir')
# plt.legend(loc = 'upper right',fontsize = 11,edgecolor = 'inherit')
# if save_plots == 0:
#     plt.show()
# else:
#     plt.savefig('Alpha_Fit_Walking-Running.svg')
# ##########################################################################################  






""" Plots """ 
############################## Accelerations ################################
r = open(output_acc +'.txt','r')
time = [] # Initialize time (s)
acc_A = []  # Initialize acceleration at A [m/s2]
acc_B = []  # Initialize acceleration at B [m/s2]
content_list = r.readlines()
for j in range(2,len(content_list)):
    time.append(float(content_list[j].split('\t')[0]))   
    acc_A.append(float(content_list[j].split('\t')[1].split('\n')[0]))
    acc_B.append(float(content_list[j].split('\t')[2].split('\n')[0]))

# Create figure peak accelerations
fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
plt.xlim(0.0,5)
plt.ylim(-0.5,0.5)
plt.xlabel('Temps [s]')
plt.ylabel('Acc. Maximales [m/$s^2$]')
plt.plot(time,acc_A,'-',color = (0,0,0),linewidth = 1.0,label = 'A')
plt.plot(time,acc_B,'--',color = (1,0,0),linewidth = 1.0,label = 'B')

# Annotate
Peak_acceleration_A = '$a_{max}$ (A) = '+ str(round(max(acc_A),2))
Peak_acceleration_B = '$a_{max}$ (B) = '+ str(round(max(acc_B),2))
y_text = 0.4
x_text = 0.2
plt.annotate(Peak_acceleration_A,(x_text,y_text),textcoords="offset points",xytext=(0,0),ha='left',fontsize=10) 
plt.annotate(Peak_acceleration_B,(x_text,y_text-0.1),textcoords="offset points",xytext=(0,0),ha='left',fontsize=10) 
plt.legend(loc = 'upper right',fontsize = 11,edgecolor = 'inherit')
if save_plots == 0:
    plt.show()
else:
    plt.savefig('Peak_Acc_Walking_' + output_acc + '.svg')