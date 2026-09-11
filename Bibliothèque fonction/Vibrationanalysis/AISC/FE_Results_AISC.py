# -*- coding: utf-8 -*-
"""
This code reads the FRFs and calculates the predicted maximum accelerations for the pedestrian bridge using AISC Guide 11
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
Methods_walking = ['Rainer','Willford']  # Methods to obtain the Fourier series parameters for walking excitation (Table  1-1, AISC Design Guide 11)
Methods_running = ['Rainer','Bachmann','ISO'] # Methods to obtain the Fourier series parameters for running excitation (Table  1-1, AISC Design Guide 11)
Types_rythmic = ['Group Dancing','Concert','Aerobics','Normal Jumping'] # Types of group rythmic activity
walking_exc = 1 # Include walking excitation (1 or 0)
running_exc = 1 # Include running excitation (1 or 0)
rythmic_exc = 0 # Include rythmic excitation (1 or 0)

""" Input""" 
# Walking excitation
m_w = 1           # Method to obtain the parameters for walking excitation (0 for Rainer, 1 for Willford)
d_f_step_w = 0.01 # Intervals at which the step frequency is calculated
type_w = 0        # 1 for marching, 0 for random walking 
n_w = 47          # Number of walkers (calculated assuming a pedestrian density = 0.2 ped/m2)
red_ped = 0.7     # Reduction factor for pedestrian bridges (section 4.2, AISC Design Guide 11)
# Running excitation
m_ru = 2         # Method to obtain the parameters for running excitation (0 for Rainer, 1 for Bachmann, 2 for ISO)
NSteps_ru = 58   # Number of steps required to cross the span (calculated for an assumed stride length of 1.3 m)
n_ru = 10          # Number of runners (for synchronized running)
Q_ru = 0.8         # Bodyweight in kN (Table  1-1, AISC Design Guide 11)
d_f_step_ru = 0.01 # Intervals at which the step frequency is calculated
# Rythmic excitation (using jumping in this case)
t_r = 3           # Type of rythmic excitation (0 for group dancing, 1 for concert, 2 for aerobics, 3 for normal jumping)
m_f_step_r = 2    # Method for obtaing the step frequency (0: mimimum of the range, 1: average of the range, 2: maximum of the range)
d_f_step_r = 0.01 # Intervals at which the step frequency is calculated

""" Fourier Series Parameters """ 
if walking_exc == 1:
    # Walking excitation Fourier series parameters
    f_step_w = 2.0    # Frequency of 1 step (walking) in Hz (Table  1-1, AISC Design Guide 11)
    beta_w = 0.01     # Viscous damping
    if Methods_walking[m_w] == 'Rainer':
        Q_w = 0.7     # Bodyweight in kN (Table  1-1, AISC Design Guide 11)
        f_step_w = [1.6,2.2]           # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
        alpha_w = [0.5,0.2,0.1,0.05]   # Dynamic coefficients for the first i harmonics (Table  1-1, AISC Design Guide 11)
    else:  
        Q_w = 0.75    # Bodyweight in kN (Table  1-1, AISC Design Guide 11)
        f_step_w = [1.6,2.2]             # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
        alpha_w = [0.4,0.07,0.06,0.05]   # Dynamic coefficients for the first i harmonics (Table  1-1, AISC Design Guide 11)

if running_exc == 1:        
    # Running excitation Fourier series parameters
    beta_ru = 0.01       # Viscous damping
    if Methods_running[m_ru] == 'Rainer':
        f_step_ru = [1.6,4.0]          # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
        alpha_ru = [1.4,0.4,0.2,0.1]   # Dynamic coefficients for the f f_step_w = [1.6,2.2] for the first i harmonics (Table  1-1, AISC Design Guide 11)
    elif Methods_running[m_ru] == 'Bachmann':
        f_step_ru = [2.0,3.0]      # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
        alpha_ru = [1.6,0.7,0.2]   # Dynamic coefficients for the first i harmonics (Table  1-1, AISC Design Guide 11)
    else:
        f_step_ru = [2.0,4.0]      # Step frequency range in Hz (Table  1-1, AISC Design Guide 11)
        alpha_ru = [1.4,0.4,0.1]   # Dynamic coefficients for the first i harmonics (Table  1-1, AISC Design Guide 11)
        
if rythmic_exc == 1:   
    # Rythmic excitation Fourier series parameters
    if Types_rythmic[t_r] == 'Group Dancing':
        wp_r = 0.6             # Unit weight of rythmic activity in kN/m2 (Table  1-2, AISC Design Guide 11)
        f_step_r = [1.5,2.5]   # Step frequency range in Hz (Table  1-2, AISC Design Guide 11)
        alpha_r = [0.5,0.05]   # Dynamic coefficients for the first i harmonics (Table  1-2, AISC Design Guide 11)
    elif Types_rythmic[t_r] == 'Concert':
        wp_r = 1.              # Unit weight of rythmic activity in kN/m2 (Table  1-2, AISC Design Guide 11)
        f_step_r = [1.5,2.5]   # Step frequency range in Hz (Table  1-2, AISC Design Guide 11)
        alpha_r = [0.25,0.05]  # Dynamic coefficients for the first i harmonics (Table  1-2, AISC Design Guide 11)
    elif Types_rythmic[t_r] == 'Aerobics':
         wp_r = 0.2               # Unit weight of rythmic activity in kN/m2 (Table  1-2, AISC Design Guide 11)
         f_step_r = [1.5,2.5]     # Step frequency range in Hz (Table  1-2, AISC Design Guide 11)
         alpha_r = [1.5,0.6,0.1]  # Dynamic coefficients for the first i harmonics (Table  1-2, AISC Design Guide 11)
    else:
         wp_r = 0.19                 # Unit weight of rythmic activity in kN/m2 (Table  1-2, AISC Design Guide 11)
         f_step_r = [1.5,2.5]        # Step frequency range in Hz (Table  1-2, AISC Design Guide 11)
         alpha_r = [1.8,1.3,0.7,0.2] # Dynamic coefficients for the first i harmonics (Table  1-2, AISC Design Guide 11)
      
""" Read Files for FRF Method (Applicable for regular and irregular framing) """ 
if walking_exc == 1 or running_exc == 1:
    # Walking/Running excitation
    r = open('FRF_C2_Walking-Running.txt','r')
    FRF_freq_walk_run = [] # Initialize frequency (Hz)
    FRF_acc_walk_run = []  # Initialize acceleration (%g/kN)
    content_list = r.readlines()
    for j in range(1,len(content_list)):
        FRF_freq_walk_run .append(float(content_list[j].split('\t')[0]))   
        FRF_acc_walk_run.append(float(content_list[j].split('\t')[1].split('\n')[0]))
    FRF_freq_walk_run = np.array(FRF_freq_walk_run )
    FRF_acc_walk_run = np.array(FRF_acc_walk_run)/g*100

if rythmic_exc == 1:
    # Rythmic excitation
    r = open('FRF_Rythmic.txt','r')
    FRF_freq_rythmic= [] # Initialize frequency (Hz)
    FRF_acc_rythmic = []  # Initialize acceleration (%g/(kN/m2))
    content_list = r.readlines()
    for j in range(1,len(content_list)):
        FRF_freq_rythmic.append(float(content_list[j].split('\t')[0]))   
        FRF_acc_rythmic.append(float(content_list[j].split('\t')[1].split('\n')[0]))
    FRF_freq_rythmic = np.array(FRF_freq_rythmic)
    FRF_acc_rythmic = np.array(FRF_acc_rythmic)/g*100

""" Find the Resonance Frequencies """ 
if walking_exc == 1 or running_exc == 1:
    # Walking/Running excitation
    for i in range(len(FRF_freq_walk_run)):
        if FRF_acc_walk_run[i] == max(FRF_acc_walk_run):
            FRF_freq_walk_run_resonance = FRF_freq_walk_run[i]
            
if rythmic_exc == 1:
    # Rythmic excitation
    for i in range(len(FRF_freq_rythmic)):
        if FRF_acc_rythmic[i] == max(FRF_acc_rythmic):
            FRF_freq_rythmic_resonance = FRF_freq_rythmic[i]
        
# Find the harmonic number that causes resonance 
range_running_harmonics = np.linspace(1,len(alpha_ru),len(alpha_ru))
for l in range(len(alpha_ru)):     
    if FRF_freq_walk_run_resonance >=  range_running_harmonics[l]*f_step_ru[0] and FRF_freq_walk_run_resonance <=  range_running_harmonics[l]*f_step_ru[1]:
        h = l+1                     # Harmonic numbern
        
""" Implement the FRF Method (Applicable for regular and irregular framing) """ 
########################## Walking excitation (low-frequency) ############################
if walking_exc == 1:
# Calculate the resonance build up factor, rho
    if beta_w < 0.01:
        rho = 50*beta_w + 0.25
    elif beta_w >= 0.01 and beta_w <= 0.03:
        rho = 12.5*beta_w + 0.625
    else:
        rho = 1.0
    # Step frequency range
    f_step_w = np.linspace(f_step_w[0],f_step_w[1],int((f_step_w[1]-f_step_w[0])/d_f_step_w+1))    
    # Calculate the dynamic coefficients
    alpha_w_step = [[]]*len(f_step_w)        # Initialize the dynamic coefficient at each step
    f_n_w = [[]]*len(f_step_w)               # Intialize first harmonics for walking excitation
    for i in range(len(f_step_w)):     
        f_n_w[i] = np.linspace(1,len(alpha_w),len(alpha_w))*f_step_w[i]  # First harmonics for walking excitation
        # Calculate dynamic coefficients for low-frequency floors (less than 4th harmonic)  
        a_w = expFit(f_n_w[i][1:len(alpha_w)],alpha_w[1:len(alpha_w)])[0]  # Coefficient a of the exponential fit from second harmonic onwards
        b_w = expFit(f_n_w[i][1:len(alpha_w)],alpha_w[1:len(alpha_w)])[1]  # Coefficient b of the exponential fit from second harmonic onwards
        temp = []
        for j in range(len(FRF_freq_walk_run )):
            if FRF_freq_walk_run [j] <= f_n_w[i][len(f_n_w[i])-1]:
                temp.append(a_w*mt.exp(-b_w*FRF_freq_walk_run [j]))
            else:
                break
            alpha_w_step[i] = temp
    # Calculate the peak accelerations
    a_p_w = [[]]*len(f_step_w)            # Intialize the accelerations (%g)
    a_p_w_peak = [[]]*len(f_step_w)       # Intialize the peak accelerations (%g) 
    # Amplification due to number of walkers
    if type_w == 0: # Random walking
        n_w_amp = mt.sqrt(n_w) 
    else: # Marching
        n_w_amp = n_w
    for i in range(len(f_step_w)):      
        a_p_w[i] = FRF_acc_walk_run[0:len(alpha_w_step[i])]*alpha_w_step[i][0:len(alpha_w_step[i])]*Q_w*red_ped*rho*n_w_amp
        a_p_w_peak[i] = max(a_p_w[i])
    # Find step frequency that gives the maximum total peak acceleration 
    for m in range(len(f_step_w)):
        if a_p_w_peak[m] == max(a_p_w_peak):
            a_p_w_max = a_p_w[m]              # Maximum peak total acceleration  
            f_step_w_max = f_step_w[m]        # Step frequency that gives the maximum acceleration
            f_n_w_max = f_n_w[m]              # First harmonics for the step frequency that gives the maximum acceleration
            break
##########################################################################################   
 
################################## Running excitation ####################################
if running_exc == 1:
    NSteps_ru = min(10,NSteps_ru)
    # Step frequency range
    f_step_ru = np.linspace(f_step_ru[0],f_step_ru[1],int((f_step_ru[1]-f_step_ru[0])/d_f_step_ru+1))   
    # Calculate the dynamic coefficients
    alpha_ru_step = [[]]*len(f_step_ru)        # Initialize the dynamic coefficient at each step
    f_n_ru = [[]]*len(f_step_ru)               # Intialize first harmonics for running excitation
    for i in range(len(f_step_ru)):     
        f_n_ru[i] = np.linspace(1,len(alpha_ru),len(alpha_ru))*f_step_ru[i]  # First harmonics for running excitation
        # Calculate dynamic coefficients for running excitation 
        a_ru = expFit(f_n_ru[i][1:len(alpha_ru)],alpha_ru[1:len(alpha_ru)])[0]  # Coefficient a of the exponential fit from second harmonic onwards
        b_ru = expFit(f_n_ru[i][1:len(alpha_ru)],alpha_ru[1:len(alpha_ru)])[1]  # Coefficient b of the exponential fit from second harmonic onwards
        temp = []
        for j in range(len(FRF_freq_walk_run )):
            if FRF_freq_walk_run [j] <= f_n_ru[i][len(f_n_ru[i])-1]:
                temp.append(a_ru*mt.exp(-b_ru*FRF_freq_walk_run [j]))
            else:
                break
            alpha_ru_step[i] = temp
    # Calculate the peak accelerations
    a_p_ru = [[]]*len(f_step_ru)            # Intialize the accelerations (%g)
    a_p_ru_peak = [[]]*len(f_step_ru)       # Intialize the peak accelerations (%g)   
    for i in range(len(f_step_ru)):  
        rho_ru = (1-mt.exp(-2*mt.pi*beta_ru*h*NSteps_ru))
        a_p_ru[i] = FRF_acc_walk_run[0:len(alpha_ru_step[i])]*alpha_ru_step[i][0:len(alpha_ru_step[i])]*Q_w*rho_ru*mt.sqrt(n_ru)
        a_p_ru_peak[i] = max(a_p_ru[i])
    # Find step frequency that gives the maximum total peak acceleration 
    for m in range(len(f_step_ru)): 
        if a_p_ru_peak[m] == max(a_p_ru_peak):
            a_p_ru_max = a_p_ru[m]              # Maximum peak total acceleration  
            f_step_ru_max = f_step_ru[m]        # Step frequency that gives the maximum acceleration
            f_n_ru_max = f_n_ru[m]              # First harmonics for the step frequency that gives the maximum acceleration
            break
##########################################################################################   
           
################################### Rythmic excitation ###################################
if rythmic_exc == 1:
    # Step frequency range
    f_step_r = np.linspace(f_step_r[0],f_step_r[1],int((f_step_r[1]-f_step_r[0])/d_f_step_r+1))    
    # Frequency of the harmonics for each considered step frequency
    f_n_r = [[]]*len(f_step_r)               # Intialize first harmonics for rythmic excitation
    FRF_acc_rythmic_h = [[]]*len(f_step_r)   # Initiliaze FRF acceleration at each harmonic  (%g)
    a_p_r = [[]]*len(f_step_r)               # Intialize the peak accelerations (%g)
    a_p_r_total = [[]]*len(f_step_r)         # Intialize the peak accelerations (%g)
    for i in range(len(f_step_r)):
        f_n_r[i] = np.linspace(1,len(alpha_r),len(alpha_r))*f_step_r[i]  # First harmonics for rythmic excitation
        # Calculate the peak accelerations for each harmonic
        FRF_acc_rythmic_h[i] = np.interp(f_n_r[i],FRF_freq_rythmic,FRF_acc_rythmic)  # FRF acceleration at each harmonic
        a_p_r[i] = FRF_acc_rythmic_h[i]*alpha_r*wp_r  
        # Calculate peak acceleration total response
        a_p_r_total[i] = 0         # Intialize the total peak accelerations (%g)
        for k in range(len(a_p_r[i])):
                a_p_r_total[i] =  a_p_r[i][k]**1.5 + a_p_r_total[i]
        a_p_r_total[i] = a_p_r_total[i]**(1/1.5)
    # Find step frequency that gives the maximum total peak acceleration 
    for m in range(len(f_step_r)): 
        if a_p_r_total[m] == max(a_p_r_total):
            a_p_r_total_max = max(a_p_r_total)            # Maximum peak total acceleration  
            f_step_r_max = f_step_r[m]                    # Step frequency that gives the maximum acceleration
            f_n_r_max = f_n_r[m]                          # FRF freqeuncy at each harmonic for the step frequency that gives the maximum acceleration
            FRF_acc_rythmic_h_max = FRF_acc_rythmic_h[m]  # FRF acceleration at each harmonic for the step frequency that gives the maximum acceleration
            break
##########################################################################################  

""" Create Files with the Peak Acceleration for Each Scenario """ 
acc_directory = os.path.join(initial_directory,'Max_Accelerations')
os.chdir(acc_directory) # Go to directory with results
if walking_exc == 1:
    Walking_filename = 'Walking-' + Methods_walking[m_w] + '.txt' 
    f = open(Walking_filename, "a")
    f.truncate(0)
    f.write(str(round(max(a_p_w_max),2)))
    f.close()
if running_exc == 1:
    Running_filename = 'Running-' + Methods_running[m_ru] + '.txt' 
    f = open(Running_filename, "a")
    f.truncate(0)
    f.write(str(round(max(a_p_ru_max),2)))
    f.close()
if rythmic_exc == 1:
    Rythmic_filename = 'Rythmic-' + Types_rythmic[t_r] + '.txt' 
    f = open(Rythmic_filename, "a")
    f.truncate(0)
    f.write(str(round(a_p_r_total_max,2)))
    f.close()

os.chdir(initial_directory) # Go to original directory

""" Plots """ 
############################## Running/Walking excitation ################################
# Create figure FRF - Walking/Running
if walking_exc == 1 or running_exc == 1:
    fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
    plt.xlim(0.0,10)
    # plt.ylim(0,0.5)
    plt.xlabel('Fréquence [Hz]')
    plt.ylabel('FRF Acc. [%g / kN]')
    plt.plot(FRF_freq_walk_run ,FRF_acc_walk_run,'-',color = (0,0,0),linewidth = 1.0)
    # plt.legend(loc = 'lower right',fontsize = 11,edgecolor = 'inherit')
    if save_plots == 0:
        plt.show()
    else:
        plt.savefig('FRF_Walking-Running.svg')
    # Create figure peak accelerations - Walking/Running
    fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
    plt.xlim(0.0,10)
    #plt.ylim(0,1.2)
    plt.xlabel('Fréquence [Hz]')
    plt.ylabel('Acc. Maximales [%g]')
    plt.plot(FRF_freq_walk_run [0:len(a_p_w_max)],a_p_w_max,'-',color = (0,0,0),linewidth = 1.0,label = 'Marcher')
    plt.plot(FRF_freq_walk_run [0:len(a_p_ru_max)],a_p_ru_max,'--',color = (1,0,0),linewidth = 1.0,label = 'Courir')
    plt.scatter(FRF_freq_walk_run_resonance,max(a_p_w_max),s=15,marker='o',edgecolor='k',color = (0.5,0.5,0.5),alpha=1,linewidth=1,zorder=10)
    plt.scatter(FRF_freq_walk_run_resonance,max(a_p_ru_max),s=15,marker='o',edgecolor='k',color = (1,0.,0.),alpha=1,linewidth=1,zorder=10)
    # Annotate
    Peak_acceleration_w = '$a_{max}$ (marcher) = '+ str(round(max(a_p_w_max),2)) + ' %g'
    Peak_acceleration_ru = '$a_{max}$ (couir) = '+ str(round(max(a_p_ru_max),2)) + ' %g'
    y_text = 4
    x_text = 4
    plt.annotate(Peak_acceleration_w,(x_text,y_text),textcoords="offset points",xytext=(0,0),ha='left',fontsize=10) 
    plt.annotate(Peak_acceleration_ru,(x_text,y_text-0.45),textcoords="offset points",xytext=(0,0),ha='left',fontsize=10) 
    plt.legend(loc = 'upper right',fontsize = 11,edgecolor = 'inherit')
    if save_plots == 0:
        plt.show()
    else:
        plt.savefig('Peak_Acc_Walking-Running.svg')
    # Create figure dynamic coefficient - Walking/Running
    # Walking exponential fit
    f_fit_w = np.linspace(0,10,100)
    alpha_fit_w = []
    for i in range(len(f_fit_w)):
        alpha_fit_w.append(a_w*mt.exp(-b_w*f_fit_w[i]))
    # Running exponential fit
    f_fit_ru = np.linspace(0,20,100)
    alpha_fit_ru = []
    for i in range(len(f_fit_ru)):
        alpha_fit_ru.append(a_ru*mt.exp(-b_ru*f_fit_ru[i]))
    # Plot fits
    fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
    plt.xlim(0.0,20)
    plt.ylim(0,0.5) 
    plt.xlabel('Fréquence [Hz]')
    plt.ylabel('Coefficient dynamique, ' + r'$\alpha$')
    #plt.ylabel('Coefficient dynamique, r$alpha$')
    plt.scatter(f_n_w_max[1:len(f_n_w_max)],alpha_w[1:len(f_n_w_max)],s=15,marker='o',edgecolor='k',color = (0.5,0.5,0.5),alpha=1,linewidth=1,zorder=10)
    plt.scatter(f_n_ru_max[1:len(f_n_ru_max)],alpha_ru[1:len(f_n_ru_max)],s=15,marker='o',edgecolor='k',color = (1,0.,0.),alpha=1,linewidth=1,zorder=10)
    plt.plot(f_fit_w,alpha_fit_w,'-',color = (0,0,0),linewidth = 1.0,label='Marcher')
    plt.plot(f_fit_ru,alpha_fit_ru,'--',color = (1,0,0),linewidth = 1.0,label='Courir')
    plt.legend(loc = 'upper right',fontsize = 11,edgecolor = 'inherit')
    if save_plots == 0:
        plt.show()
    else:
        plt.savefig('Alpha_Fit_Walking-Running.svg')
##########################################################################################  

################################### Rythmic excitation ###################################    
if rythmic_exc == 1:
    # Create figure FRF - Rythmic Activity
    fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
    plt.xlim(0.0,10)
    plt.ylim(0,15)
    plt.xlabel('Fréquence [Hz]')
    plt.ylabel('FRF Acc. [%g / kN/m$^2$]')
    plt.plot(FRF_freq_rythmic,FRF_acc_rythmic,'-',color = (0,0,0),linewidth = 1.0)
    plt.scatter(f_n_r_max,FRF_acc_rythmic_h_max,s=15,marker='o',edgecolor='k',color = (0.5,0.5,0.5),alpha=1,linewidth=1,zorder=10)
    # Annotate
    Critical_step_freq_ru = '$f_{pas,cr}$ = ' + str(f_step_r_max) +' Hz'
    Peak_acceleration_r = '$a_{max}$ = '+ str(round(a_p_r_total_max,2)) + ' %g'
    y_text = 13.5
    x_text = 1
    plt.annotate(Critical_step_freq_ru,(x_text,y_text),textcoords="offset points",xytext=(0,0),ha='left',fontsize=10) 
    plt.annotate(Peak_acceleration_r,(x_text,y_text-1.5),textcoords="offset points",xytext=(0,0),ha='left',fontsize=10) 
    if save_plots == 0:
        plt.show()
    else:
        plt.savefig('FRF_Rythmic-'+ Types_rythmic[t_r] +'.svg')
    
    # Create figure rythmic activity peak acceleration vs. step frequency
    fig = plt.figure(facecolor='white',figsize=(3.5,3),tight_layout=True)
    plt.xlim(f_step_r[0],f_step_r[(len(f_step_r)-1)])
    plt.ylim(0,4)
    plt.xlabel('Fréquence de pas [Hz]')
    plt.ylabel('$a_{max}$ [%g]')
    plt.plot(f_step_r,a_p_r_total,'-',color = (0,0,0),linewidth = 1.0)
    if save_plots == 0:
        plt.show()
    else:
        plt.savefig('FRF_Rythmic-'+ Types_rythmic[t_r] +'_amax_step.svg')
##########################################################################################  

# ################################ Summary of Accelerations ################################     
# Create bargraph with peak accelerations
# Read peak acceleration results
os.chdir(acc_directory) # Go to directory with acceleration results
result_files_acc = [f for f in glob.glob("*.txt")]
acc_max = []
result_name = []
for i in range(len(result_files_acc)):
    result_name.append(result_files_acc[i].split('.txt')[0])
    r = open(result_files_acc[i],'r')
    acc_max.append(float(r.readlines()[0]))

# Divide peak acceleration results into the 3 categories
result_walking = []
result_running = []
result_rythmic= []
acc_max_walking = []
acc_max_running = []
#acc_max_rythmic = []
for i in range(len(result_name)):
    if result_name[i].find('Walking') != -1:
        result_walking.append(result_name[i])
        acc_max_walking.append(acc_max[i])
    elif result_name[i].find('Running') != -1: 
        result_running.append(result_name[i])
        acc_max_running.append(acc_max[i])
   # else:
   #      if result_name[i] != 'Rythmic-Concert':    # Exclude concert
   #          result_rythmic.append(result_name[i])
   #          acc_max_rythmic.append(acc_max[i])      

# Plot 
fig = plt.figure(facecolor='white',figsize=(4.0,3),tight_layout=False)
plt.rcParams['font.size'] = 18
fig.subplots_adjust(left=0.0, bottom=0.0, right=1, top=1.0)
ax = fig.add_subplot(111)
bar_width = 0.25
plt.xlim(0.0,2.0)
#plt.ylim(0,3)
x_labels = ['Rainer','Willford','Bachmann','ISO','Rainer']#,'Aérobie','Danser','Sauter']
plt.ylabel('$a_{max}$ [%g]')
X1 = (np.arange(len(result_walking)))*bar_width
X2 = (np.arange(len(result_running)) + 2*len(result_walking))*bar_width
X3 = (np.arange(len(result_rythmic)) + 2*len(result_walking) + 2*len(result_running))*bar_width
#ax = fig.add_axes([0,0,1,1])
ax.set_xticks(np.concatenate((X1+0.25,X2+0.25,X3+0.25)))
ax.set_xticklabels(x_labels,rotation = 90)
ax.bar(X1+0.25, acc_max_walking, color = (0.25,0.25,0.25), width = bar_width,edgecolor='k',hatch = '....',label='Marcher')
ax.bar(X2+0.25, acc_max_running, color = (0.5,0.5,0.5), width = bar_width,edgecolor='k',hatch = '/////',label='Courir')
#ax.bar(X3+0.25, acc_max_rythmic, color = (0.75,0.75,0.75), width = bar_width,edgecolor='k',hatch = 'xxxx',label='Activité rythmique')
plt.legend(loc = 'upper left',fontsize = 14,edgecolor = 'inherit')
if save_plots == 0:
    plt.show()
else:
    plt.savefig('Acceleration_Summary.svg',bbox_inches='tight')
    
print('Walking a_max = ' + str(round(max(a_p_w_max),2))+'%g')
print('Running a_max = ' +  str(round(max(a_p_ru_max),2))+'%g')
#print('Rythmic, ' + Types_rythmic[t_r] + ' a_max = ' + str(round(a_p_r_total_max,2))+'%g')
