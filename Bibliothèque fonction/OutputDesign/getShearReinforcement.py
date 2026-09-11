# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:48:06 2022

@author: hammad.eljisr
"""

import math
import numpy as np

def getShearReinforcement(V_max,material_properties,z,bw,alpha,n_stirrups,spacing):
    """
    This function calculates the required shear reinforcement (area per unit spacing) in accordance with SIA 262
    Input:
        - V_max: Maximum shear force in the beam
        - material_properties: Material properties (f_sk,f_sd,f_ck,f_cd)
        - z: Lever arm
        - bw: Width of the rectangular section (or web of T-beam)
        - alpha: Angle of inclination of the compressive strut (in degrees)
        - n_stirrups: Number of stirrups
        - spacing: Spacing between stirrups
    Output:
        - A_sw_s: Required shear reinforcement area
        - A_sw_s_min: Minimum required shear reinforcement area
        - D_sw: Bar diameter
    """
    
    f_sk = material_properties[0]
    f_sd = material_properties[1]
    f_ck = material_properties[2]
    f_cd = material_properties[3]
    
    
    # Reinforcement SIA 262 - 4.3.3.4.3
    cot_alpha = 1/math.tan(math.radians(alpha))
    A_sw_s = V_max/(z*f_sd*cot_alpha)
    
    # Check compression strut
    k_c = 0.8 # Coefficient taking into accoun state of stress in the compression strut (SIA 262 4.2.1.7 )
    V_Rdc = bw*z*k_c*f_cd*math.sin(math.radians(alpha))*math.cos(math.radians(alpha)) 
    if V_Rdc < V_max:
        print('Increase alpha')
      
    # Get minimum reinforcement (SIA 262 5.5.2.2)
    rho_w_min = 0.001*math.sqrt(f_ck/30)*500/f_sk
    A_sw_s_min = rho_w_min*bw
    
    if A_sw_s < A_sw_s_min:
        print('Required shear reinforcement less than the minimum value')
        A_sw_s = A_sw_s_min
    
    D_rebars = [8,10,12,14,16,20,25,30] # Rebar dimensions
    D_sw = D_rebars[sum(math.sqrt(4*(A_sw_s*spacing/(2*n_stirrups))/math.pi) > np.array(D_rebars))]
    
    return A_sw_s, A_sw_s_min, D_sw