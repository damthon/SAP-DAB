# -*- coding: utf-8 -*-
"""
Created on Tue Apr  22 15:56:54 2025

@author: hammad.eljisr
"""
 
from math import nan

def getPlateEffectiveWidth(psi,element_type,b,t,fy):
    """
    This function calculates the effective width of UNSTIFFENED plate elements (without longitudinal stiffeners): Clause 4.4, EN 1993-1-5
    Input:
        psi: Stress ratio
        element_type: 0 for internal element, 1 for outstand element with maximum stress at free end, 2 for outstand element with maximum stress at fixed end
        b: Element width (see Table 5.2, EN 1993-1)
        t: Element thickness
        fy: Characteristic yield strength

    Output:
        rho: Reduction factor for plate buckling
        b_eff: Effective width of the element
        b_e1, b_e2: Effective width distribution for internal elements only
    """
    
    eps = (235/fy)**0.5
    
    if element_type == 0: 
        # Internal compression element # Table 4.1, EN 1993-1-5
        if psi == 1:
            k_sigma = 4.0
        elif (psi > 0) and (psi < 1.0):
            k_sigma = 8.2/(1.05 + psi)
        elif psi == 0:
            k_sigma = 7.81
        elif (psi < 0) and (psi > -1.0):
            k_sigma = 7.81 - 6.29*psi + 9.78*psi**2
        elif psi == -1:
            k_sigma = 23.9
        elif (psi < -1) and (psi > -3.0):
            k_sigma = 5.98*(1-psi)**2
        else:
            k_sigma = 95.68 # Limit for psi = -3   
        lambda_p = (b/t)/(28.4*eps*(k_sigma)**0.5) 
        if  psi > 1.0: # psi > 1.0 means tension only
            rho = 1.0
        elif (lambda_p <= 0.5 + (0.085 - 0.055*psi)**0.5):
            rho = 1.0
        else:
            rho = min((lambda_p - 0.055*(3 + psi))/(lambda_p**2),1.0)
    
    elif element_type == 1:
        # Outstand compression element # Table 4.2, EN 1993-1-5
        if psi == 1:
            k_sigma = 0.43
        elif psi == 0:
            k_sigma = 0.57
        elif psi == -1:
            k_sigma = 0.85
        elif (psi <= 1.0) and (psi > -3.0):
            k_sigma = 0.57 - 0.21*psi + 0.07*psi**2
        else:
            k_sigma = 1.83 # Limit for psi = -3
        lambda_p = (b/t)/(28.4*eps*(k_sigma)**0.5) 
        if lambda_p <= 0.748 or psi > 1.0: # psi > 1.0 means tension only
            rho = 1.0
        else:
            rho = min((lambda_p - 0.188)/(lambda_p**2),1.0)
    
    elif element_type == 2:
        # Outstand compression element # Table 4.2, EN 1993-1-5
        if psi == 1:
            k_sigma = 0.43
        elif (psi > 0) and (psi < 1.0):
            k_sigma = 0.578/(psi + 0.34)
        elif psi == 0:
            k_sigma = 1.7
        elif (psi < 0) and (psi > -1.0):
            k_sigma = 1.7 - 5*psi + 17.1*psi**2
        else:
            k_sigma = 23.8 # Limit for psi = -1
        lambda_p = (b/t)/(28.4*eps*(k_sigma)**0.5) 
        if lambda_p <= 0.748 or psi > 1.0: # psi > 1.0 means tension only
            rho = 1.0
        else:
            rho = min((lambda_p - 0.188)/(lambda_p**2),1.0)
            
    # Get effective width, Table 4.1, EN 1993-1-5
    if element_type == 0: 
        if psi == 1:
            b_eff = rho*b 
            b_e1 = 0.5*b_eff
            b_e2 = 0.5*b_eff
        elif psi < 1.0 and psi >= 0:
            b_eff = rho*b 
            b_e1 = 2/(5-psi)*b_eff
            b_e2 = b_eff - b_e1
        else:
            b_eff = rho*b/(1-psi) 
            b_e1 = 0.4*b_eff
            b_e2 = 0.6*b_eff
    elif element_type == 1 or element_type == 2: 
        if (psi <= 1.0) and (psi >= 0):  
            b_eff = rho*b
        else:
            b_eff = rho*b/(1-psi) 
        b_e1 = nan
        b_e2 = nan
    
    return rho, b_eff, b_e1, b_e2
