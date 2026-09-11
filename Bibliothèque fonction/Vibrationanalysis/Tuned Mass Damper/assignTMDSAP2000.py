# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:00:26 2026

@author: hammad.eljisr
"""


import numpy as np
import scipy


def sizingTMDSAP2000(SapModel,mode,Point_TMD,Direction,eta,mu):
    """
    This function calculates the properties of a tuned mass damper (TMD) properties for a given mode and a target bandwidth.
    Input:
        - SapModel: SAP model object
        - mode: Mode to be damped (eg. 3)
        - Point_TMD: Point label corresponding the the location at which the TMD is attached (e.g. '707')
        - Direction: Dominant direction of the mode to be damped 'U1', 'U2' or 'U3' corresponding to the local axis of the Point_TMD (e.g. 'U2')
        - eta: Critical damping ratio
        - mu: Mass ratio of the TMD (ideally between 0.005 to 0.05)

    Output: 
        - mass_TMD: TMD mass in kg
        - k_TMD: TMD stiffness in N/m
        - eta_opt: OptimalTMD damping 
        - alpha_opt: Ratio of TMD frequency to resonance frequency
        - reduction_acc: Percentage reduction of the pseudo-acceleration
        - op_bandwidth: Operational bandwidth (delta frequency between peaks)
    """
    
    SapModel.SetPresentUnits(6) # kN-m-s units
    
    # Get resonance frequency in Hz
    # Run modal analysis only
    SapModel.SetModelIsLocked(False) # Unlock model
    SapModel.Analyze.SetRunCaseFlag("MODAL",False,'All')
    SapModel.Analyze.SetRunCaseFlag("MODAL",True)
    SapModel.Analyze.RunAnalysis()
    # Get modal frequencies
    Modal_analysis = SapModel.Results.ModalPeriod(1,'MODAL','Mode')
    modes = Modal_analysis[3] # Mode numbers
    frequencies = Modal_analysis[5] # Modal frequencies
    index_mode = modes.index(mode) # index of the damped mode
    f_res = frequencies[index_mode] # F
    
    # Get the effective mass
    modal_mass = SapModel.Results.ModalParticipationFactors()[-3][index_mode]*1000 # # Generalized modal mass in kg
    index_disp = int(Direction[-1]) - 8
    SapModel.Results.Setup.SetCaseSelectedForOutput('MODAL')
    modal_disp = SapModel.Results.JointDispl(Point_TMD,0,LoadCase='MODAL')[index_disp][index_mode] # Displacement at the TMD location
    effective_mass = modal_mass/(modal_disp**2)  # Effective mass in kg
    
    # Calculate the optimal damping ratio for the mass ratio
    eta_opt_0 = (mu*(1 + 0.75*mu)/(4*(1 + mu)*(1 + mu/2)))**0.5  # Optimal damping ratio of the TMD if the primary mass has zero damping according to Warburton (SETRA Eq.3.18)
    eta_opt = eta_opt_0 + (0.13 + 0.12*mu + 0.4*mu**2)*eta - (0.01 + 0.9*mu + 3*mu**2)*eta**2 # Optimal damping ratio of the TMD if the primary mass has natural damping (SETRA Eq.3.19)
    
    # Get optimal frequence of the TMD
    alpha_opt_0 = (1 + mu/2)**0.5/(1 + mu)  # Optimal frequency ratio of the TMD if the primary mass has zero damping according to Warburton (SETRA Eq.3.17)
    alpha_opt = alpha_opt_0 - (0.241 + 1.7*mu - 2.6*mu**2)*eta - (1.0 - 1.9*mu + mu**2)*eta**2 
    
    # Calculate dynamic amplification factors and % reduction in accelerations
    A_noTMD = 1/(2*eta) # Dynamic amplification factor at resonance: no TMD
    A_TMD = (1 + 2/mu)**0.5  # Dynamic amplification factor with TMD according to Den Hartog (SETRA Eq.3.14)
    reduction_acc = (A_noTMD - A_TMD)/A_noTMD*100 # Percentage reduction in pseudo-accelerations (proportional to A)
    
    # Calculate mass and stiffness of the TMD
    mass_TMD = mu*effective_mass # Mass of the tuned mass damper in kg
    f_TMD = alpha_opt*f_res # Frequency of the TMD 
    k_TMD = mass_TMD*(2*np.pi*f_TMD)**2 # Stiffness of the TMD in N/m
   
    # Calculate operational bandwidth, applicable if mu_opt is at the bounds
    op_bandwidth = f_res*(mu)**0.5
    
    return mass_TMD,k_TMD,eta_opt,alpha_opt,reduction_acc,op_bandwidth
    

def createTMDSAP2000(SapModel,mass_TMD,k_TMD,eta_TMD,attachment_point,direction):
    """
    This function creates and assigns the properties of the tuned mass damper. 
    Input:
        - SapModel: SAP model object
        - mass_TMD: TMD mass in kg
        - k_TMD: TMD stiffness in N/m
        - eta_TMD: TMD damping 
        - attachment_point: Label of the point attached to the TMD
        - direction: Vector in global coordinates e.g. [0,0,0.5]

    Output: 
        - link_TMD: TMD link element
    """
    
    SapModel.SetModelIsLocked(False) # Unlock model
    SapModel.SetPresentUnits(10) # N-m-s units   
    
    # Create TMD link property
    cv = 2*eta_TMD*(k_TMD*mass_TMD)**0.5 # Damping coefficient
    SapModel.PropLink.SetLinear('TMD',[1,1,1,1,1,1],[0,True,True,True,True,True],[k_TMD,0,0,0,0,0],[cv,0,0,0,0,0],0,0) # Local 1 axis along link
    
    # Get coordinates of attachment point
    x = SapModel.PointObj.GetCoordCartesian(attachment_point)[0]
    y = SapModel.PointObj.GetCoordCartesian(attachment_point)[1]
    z = SapModel.PointObj.GetCoordCartesian(attachment_point)[2]
    
    # Create TMD link end point to which mass is assigned
    mass_point = SapModel.PointObj.AddCartesian(x+direction[0],y+direction[1],z+direction[2])[0]
    link_TMD = SapModel.LinkObj.AddByPoint(attachment_point,mass_point,IsSingleJoint=0,PropName='TMD')[0]
    
    # Assign mass to mass point
    SapModel.PointObj.SetMass(mass_point,[0,0,mass_TMD,0,0,0],0,False)
    
    return link_TMD


def TMDSteadyStateLoadsSETRASAP2000(SapModel,SETRA_pattern,target_frequency):
    """
    This function adjusts the frequeny range for steady state analysis using SETRA loads
    Input:
        - SapModel: SAP model object
        - SETRA_pattern: SETRA load pattern
        - target_frequency: Frequency of the targeted mode
    """
    # Load case name
    SETRA_pattern_S = SETRA_pattern + '_SS'
    
    # Run modal analysis 
    SapModel.SetModelIsLocked(False) # Unlock model
    SapModel.Analyze.SetRunCaseFlag("MODAL",False,'All')
    SapModel.Analyze.SetRunCaseFlag("MODAL",True)
    SapModel.Analyze.RunAnalysis()
   
    # Get modal frequencies
    Modal_analysis = SapModel.Results.ModalPeriod(1,'MODAL','Mode')
    n_modes = Modal_analysis[0] # Number of modes
    frequencies = Modal_analysis[5] # Modal frequencies
    
    # Get f1and f2
    SapModel.SetModelIsLocked(False) # Unlock model
    f1_modal = frequencies[sum(np.ones(len(frequencies))*target_frequency > frequencies)-1]
    f2_modal = frequencies[sum(np.ones(len(frequencies))*target_frequency > frequencies)]
    f1 = f1_modal - 0.05
    f2 = f2_modal + 0.05
    SapModel.LoadCases.SteadyState.SetFreqData(SETRA_pattern_S,f1,f2,100,True,True,False,"MODAL",2,[-0.005,0.005],0,[]) # Frequency step data
    
    return 