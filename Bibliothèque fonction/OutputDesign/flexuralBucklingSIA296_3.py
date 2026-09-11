# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 14:25:47 2026

@author: hammad.eljisr
"""

import math

def flexuralBucklingSIA296_3(lk,I,A,ak,fy,E,gamma_M1):
    """
    This function calculates the axial resistance to flexural buckling  of a steel member according to SIA 263, §4.5.1
    Input:
        lk: Buckling lengh of the member
        I: Moment of inertia of the member cross-section
        A: Cross-sectional area of the member
        ak: Imperfection factor
        fy: Steel yield strength
        E: Steel modulus of elasticity
        gamma_M1: Partial safety factor


    Output:
        Nk_Rd: Member flexural buckling resistance
    """
     
    # Flexural buckling according to SIA 263, §4.5.1
    # Slenderness
    s_cr_k = (math.pi**2)*E*I/(A*lk**2)
    lambda_k = (fy/s_cr_k)**0.5
    
    # Reduction factor
    Phi_k = 0.5*(1 + ak*(lambda_k-0.2) + lambda_k**2)
    Xi_k = min(1/(Phi_k + (Phi_k**2 - lambda_k**2)**0.5),1)
    
    # Axial resistance to flexural buckling
    Nk_Rd = Xi_k*fy*A/gamma_M1

    
    return Nk_Rd
    
    