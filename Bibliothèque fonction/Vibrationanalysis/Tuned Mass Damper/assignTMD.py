# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:00:26 2026

@author: hammad.eljisr
"""


import numpy as np

def calculateTMD(mode):
    """
    This function calculates the required tuned mass damper properties for a given mode.
    Input:
        - mode: Mode to be damped
        

def assignTimeHistoryLoadsSETRASAP2000(SapModel,SETRA_pattern,scale_factor,target_frequency,analysis_type,solution_type,stiffness_o,time_step_size,damping_ratio,n_cycles):
    """
    This function assign the time history load to the created SETRA load pattern.
    Input:
       - SapModel: SAP model object
       - SETRA_pattern: SETRA load pattern
       - scale_factor: Scale factor for the loads applied in the shape of the mode
       - target_frequency: Frequency of the targeted mode
       - analysis_type: 0 for linear analysis, 1 for nonlinear analysis with p-delta and 2 for nonlinear analysis with p-delta and large displacements
       - Solution_Type: 0 for modal solution type, 1 for direct integration type
       - stiffness_o: Load pattern corresponding to the initial conditions (loads are not included if linear analysis is conducted)
       - time_step_size: Time step size (negative power of 10)
       - damping_ratio: Critical damping ratio
       - n_cycles: Number of cycles to run (until steady state is achieved)
        
    Output:
       - modes_SETRA: Modes to which SETRA loads shapes are applied
       - frequencies_SETRA: Frequencies of the modes to which the SETRA loads are applied
       - SETRA_pattern_TH: Names of the created SETRA time history load cases
    """     
    
    # Load case name
    SETRA_pattern_TH = SETRA_pattern + '_TH'
    # Create sine function
    sin_fn_name = 'sin(' + str(int(n_cycles + 10)) + ' cycles)'
    SapModel.Func.FuncTH.SetSine(sin_fn_name,1,100,n_cycles+10,1) # Cycles to achieve steady state + 10
    # Time steps
    time_factor = 1/target_frequency
    number_steps = int(round(time_factor/time_step_size,0))*n_cycles
    # Frequency limits for viscous proportional damping (Direct integration solution type).
    f1 = target_frequency
    f2 = target_frequency + 0.05 # Choose second frequency to be close to obtain a constant damping ratio
    # Create load case
    if solution_type == 0 and analysis_type == 0:
        SapModel.LoadCases.ModHistLinear.SetCase(SETRA_pattern_TH) # Modal solution type, linear
        SapModel.LoadCases.ModHistLinear.SetTimeStep(SETRA_pattern_TH,number_steps,time_step_size) # Time steps
        SapModel.LoadCases.ModHistLinear.SetLoads(SETRA_pattern_TH,1,['Load'],[SETRA_pattern],[sin_fn_name],[scale_factor],[time_factor],[0],['GLOBAL'],[0]) # Loads
        SapModel.LoadCases.ModHistLinear.SetDampConstant(SETRA_pattern_TH,damping_ratio) # Constant damping
    elif solution_type == 0 and analysis_type == 1:
        SapModel.LoadCases.ModHistNonlinear.SetCase(SETRA_pattern_TH) # Modal solution type, nonlinear
        SapModel.LoadCases.ModHistNonlinear.SetTimeStep(SETRA_pattern_TH,number_steps,time_step_size)  # Time steps
        SapModel.LoadCases.ModHistNonlinear.SetLoads(SETRA_pattern_TH,1,['Load'],[SETRA_pattern],[sin_fn_name],[scale_factor],[time_factor],[0],['GLOBAL'],[0]) # Loads
        SapModel.LoadCases.ModHistNonlinear.SetDampConstant(SETRA_pattern_TH,damping_ratio) # Constant damping
    elif solution_type == 1 and analysis_type == 0:
        SapModel.LoadCases.DirHistLinear.SetCase(SETRA_pattern_TH) # Direct integration solution type, linear
        SapModel.LoadCases.DirHistLinear.SetTimeStep(SETRA_pattern_TH,number_steps,time_step_size) # Time steps
        SapModel.LoadCases.DirHistLinear.SetLoads(SETRA_pattern_TH,1,['Load'],[SETRA_pattern],[sin_fn_name],[scale_factor],[time_factor],[0],['GLOBAL'],[0]) # Loads
        SapModel.LoadCases.DirHistLinear.SetDampProportional(SETRA_pattern_TH,3,0,0,f1,f2,damping_ratio,damping_ratio) # Viscous proportional damping
    else:
        SapModel.LoadCases.DirHistNonlinear.SetCase(SETRA_pattern_TH) # Direct integration solution type, nonlinear
        SapModel.LoadCases.DirHistNonlinear.SetGeometricNonlinearity(SETRA_pattern_TH,analysis_type) # With p-delta
        SapModel.LoadCases.DirHistNonlinear.SetTimeStep(SETRA_pattern_TH,number_steps,time_step_size)  # Time steps
        SapModel.LoadCases.DirHistNonlinear.SetLoads(SETRA_pattern_TH,1,['Load'],[SETRA_pattern],[sin_fn_name],[scale_factor],[time_factor],[0],['GLOBAL'],[0]) # Loads
        SapModel.LoadCases.DirHistNonlinear.SetDampProportional(SETRA_pattern_TH,3,0,0,f1,f2,damping_ratio,damping_ratio) # Viscous proportional damping
        
    # Initial conditions
    if solution_type == 1 and analysis_type == 0: # Linear analysis (loads in initial case not included)
        SapModel.LoadCases.DirHistLinear.SetInitialCase(SETRA_pattern_TH,stiffness_o)
    elif solution_type == 1 and analysis_type == 1: # Nonlinear analysis (loads in initial case included)
        SapModel.LoadCases.DirHistNonlinear.SetInitialCase(SETRA_pattern_TH,stiffness_o)
    else: 
        print('Initial stiffness cannot be assigned from a load case. Solution type should be changed to Direct Integration')
        
    return SETRA_pattern_TH
        
def assignSteadyStateLoadsSETRASAP2000(SapModel,SETRA_pattern,scale_factor,target_frequency,stiffness_o,damping_ratio):
    """
    This function assign the steady state function to the created SETRA load pattern.
    Input:
        - SapModel: SAP model object
        - SETRA_pattern: SETRA load pattern
        - scale_factor: Scale factor for the loads applied in the shape of the mode
        - target_frequency: Frequency of the targeted mode
        - stiffness_o: Load pattern corresponding to the initial conditions (loads are not included if linear analysis is conducted)
        - damping_ratio: Critical damping ratio
        
    Output:
       - SETRA_pattern_S: Names of the created SETRA steady state load cases
    """     
    
    # Load case name
    SETRA_pattern_S = SETRA_pattern + '_SS'
    
    # Create FRF function
    f_min = max(target_frequency - 0.5,0)
    f_max = target_frequency + 0.5
    FRF_sine = 'FRF_sine'
    freq_step = int((f_max - f_min)/0.01)
    freq_FRF = list(np.linspace(f_min,f_max,freq_step))
    values_FRF = list(np.ones(len(freq_FRF)))
    SapModel.Func.FuncSS.SetUser(FRF_sine,len(freq_FRF),freq_FRF,values_FRF)
        
    # Create load case
    SapModel.LoadCases.SteadyState.SetCase(SETRA_pattern_S) # Load case
    SapModel.LoadCases.SteadyState.SetInitialCase(SETRA_pattern_S,stiffness_o) # Linear analysis (loads in initial case not included)
    SapModel.LoadCases.SteadyState.SetDampConstant(SETRA_pattern_S,0,damping_ratio*2) # Hysteretic damping (constant damping = 2*damping ratio)
    # Frequency step data
    f1 = target_frequency - 0.05
    f2 = target_frequency + 0.05
    SapModel.LoadCases.SteadyState.SetFreqData(SETRA_pattern_S,f1,f2,100,True,True,False,"MODAL",2,[-0.005,0.005],0,[]) # Frequency step data
    # Steady state load
    SapModel.LoadCases.SteadyState.SetLoads(SETRA_pattern_S,1,['Load'],[SETRA_pattern],[FRF_sine],[scale_factor],[0],['GLOBAL'],[0])
    
    return SETRA_pattern_S
        
        
    
    
    
    
