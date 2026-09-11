# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 10:08:01 2025

@author: hammad.eljisr

""" 

import scipy
import math

def fib2020_V_Level_II(Forces,Sec_geom,Materials,Gamma,Level,Cracked):
    """
    This functions calculates the shear resistance of a reinforced section using the Level II approximation of fib Model Code 2020. 
    UNIT SYSTEM: kN-m
    Input:
        - Forces: Design forces in the beam section, list [N_Ed,M_Ed,V_Ed] where N_Ed is the axial force, M_Ed is the moment, and V_Ed is shear force
        - Sec_geom: Section geometry and reinforcement, list [bw,zv,De,Asw_sw,As] where bw is the beam width, zv is the effective shear depth, De is the 
        distance from the centroid of the section (or location of normal force) to the middle of the effective shear depth (positive direction towards tensile chord), Asw_sw is the shear reinforcement per m,
        and As is the main longitudinal reinforcement in the tension chord
        - Materials: Material properties list [[fsk, Es,Duct],fck] where fsk is the characteristic strength of the steel reinforcement, Es is the Young's modulus
        of the steel reinforcement, Duct is the ductility class of the reinforcement ('A','B','C' or 'D'), and fck is the characteristic concrete compressive 
        strength
        - Gamma: Partial safety factors [gamma_s, gamma_c]
        - Level: Approximation level 'IIa' or 'IIb'
        - Cracked: 1 if section is fully cracking (no compressive zone due to the moment), 0 otherwise
    Output:
        - V_Rd: Shear resistance
        - theta: Compressive strut angle
    """   
    
    # Forces in the beam section
    N_Ed = Forces[0] # Applied axial force at the section to be verified
    M_Ed = abs(Forces[1]) # Applied moment at the section to be verified
    V_Ed = abs(Forces[2]) # Applied shear force at the section to be verified
    
    # Beam geometry
    bw = Sec_geom[0] # Width
    zv = Sec_geom[1] # Effective shear depth
    De = Sec_geom[2] # Distance from centroid to the middle of the effective shear depth
    Asw_sw = Sec_geom[3] # Area of shear reinforcement per length
    As = Sec_geom[4] # Area of main longitudinal reinforcement in the tension chord
    
    # Material properties
    fsk = Materials[0][0] # Characteristic yield stress of the rebars
    Es = Materials[0][1] # Elastic modulus of the rebars
    ductility = Materials[0][2] # Reinforcement ductility class
    fck = Materials[1] # Characteristic compressive strength of concrete

    # Partial safety factors 
    gamma_s = Gamma[0] # Partial safety factor the beam reinforcement
    gamma_c = Gamma[1] # Partial safety factor for concrete
    
    # Design compressive strength
    eta_fc = min(1,(40000/fck)**(1/3))
    fcd = fck*eta_fc/gamma_c  
    
    if Level == 'IIa':
        # Level IIa
        # Optimize theta for level IIa
        def optimizeThetaIIa(theta):  
            cot_theta = 1/math.tan(math.radians(theta))
            e_x = min(max((1/(2*Es*As))*(M_Ed/zv + (V_Ed/2)*cot_theta + N_Ed*(0.5 - De/zv)),0),0.003)*(Cracked+1) # Clause 30.1-10
            e_1 = e_x + (e_x + 0.001)*cot_theta**2 # Clause 30.1-44
            ke = min(1/(1.2+60*e_1),1) # Clause 30.1-43
            V_Rdmax = (ke*fcd*bw*zv)/(cot_theta + 1/cot_theta)  # Clause 30.1-25
            V_Rds = Asw_sw*zv*fsk/gamma_s*cot_theta
            return abs(V_Rdmax - V_Rds)
        theta_opt = scipy.optimize.minimize(optimizeThetaIIa,20,method = 'Nelder-Mead').x[0] # Optimized theta such that V_Rds = V_Rdmax
        
        # Get minimum theta
        cot_theta = 1/math.tan(math.radians(theta_opt))
        e_x = min(max((1/(2*Es*As))*(M_Ed/zv + (V_Ed/2)*cot_theta + N_Ed*(0.5 - De/zv)),0),0.003)*(Cracked+1) # Clause 30.1-10
        
        if ductility == 'C' or ductility == 'D':
            cot_theta_min = 1/math.tan(math.radians(13+2500*e_x))
        elif ductility == 'B':
            cot_theta_min = 1/math.tan(math.radians(15+3000*e_x))
        else:
            cot_theta_min = 1/math.tan(math.radians(20+4000*e_x))
        theta_min = math.degrees(math.atan(1/cot_theta_min))  

        # Use theta to compute V_Rd
        theta = max(theta_opt,theta_min)
        cot_theta = 1/math.tan(math.radians(theta))
        e_1 = e_x + (e_x + 0.001)*cot_theta**2 # Clause 30.1-44
        ke = min(1/(1.2+60*e_1),1) # Clause 30.1-43
        V_Rdmax = (ke*fcd*bw*zv)/(cot_theta + 1/cot_theta)  # Clause 30.1-25
        V_Rds = Asw_sw*zv*fsk/gamma_s*cot_theta # Clause 30.1-24
        V_Rd = min(V_Rds,V_Rdmax)
    
    elif Level == 'IIb':
        # Level IIb 
        # Optimize theta for level IIb
        def optimizeThetaIIb(theta):  
            cot_theta = 1/math.tan(math.radians(theta))
            e_x = min(max((1/(2*Es*As))*(M_Ed/zv + (V_Ed/2)*cot_theta + N_Ed*(0.5 - De/zv)),0),0.003)*(Cracked+1) # Clause 30.1-10
            cot_theta_2 = 1/math.tan(math.radians(29+7000*e_x))
            return abs(cot_theta - cot_theta_2)
        theta = scipy.optimize.minimize(optimizeThetaIIb,20,method = 'Nelder-Mead').x[0] # Optimized theta to converge to e_x
        
        # Use theta to compute V_Rd = V_Rds + V_Rdc
        cot_theta = 1/math.tan(math.radians(theta))
        e_x = min(max((1/(2*Es*As))*(M_Ed/zv + (V_Ed/2)*cot_theta + N_Ed*(0.5 - De/zv)),0),0.003)*(Cracked+1) # Clause 30.1-10
        kv = 0.4/(1+1500*e_x) # Clause 30.1-47
        e_1 = e_x + (e_x + 0.001)*cot_theta**2 # Clause 30.1-44
        ke = min(1/(1.2+60*e_1),1) # Clause 30.1-43
        # Design shear resistance of concrete  
        if zv > 800:
            fck_v = min(8,math.sqrt(fck/1000))
        else:
            fck_v = math.sqrt(fck/1000)
        V_Rdc = kv*fck_v*bw*zv/gamma_c*1000 # Clause 30.1-23
        V_Rds = Asw_sw*zv*fsk/gamma_s*cot_theta # Clause 30.1-24
        V_Rdmax = (ke*fcd*bw*zv)/(cot_theta + 1/cot_theta)
        V_Rd = min(V_Rdc + V_Rds,V_Rdmax)
        if V_Rdc + V_Rds > V_Rd:
            print('Use level IIa approxamiation to optimize the shear resistance')
    else:
        print('Approximation level should be either IIa or IIb')
    
    return V_Rd,theta,e_x
