# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 08:30:03 2022

@author: hammad.eljisr
"""

def momentResistanceRect(Beam_Dim,A_s,Material_Prop,Factors):
    # SIA 262 4.2
    # Beam dimensions
    h = Beam_Dim[0] # Beam depth
    b = Beam_Dim[1] # Beam width
    c = Beam_Dim[2] # Reinforcemen cover   
    
    # Material properties
    f_ck = Material_Prop[0]  # Concrete characteristic compressive strength
    e_c2d = Material_Prop[1] # Concrete ultimate crushing strain
    f_sk = Material_Prop[2] # Rebar characteristic yield strength
    e_ud = Material_Prop[3] # Ultimate strain in the rebars (design value)
    E_s = Material_Prop[4]  # Rebar modulus of elasticity
    
    # Resistance factors
    gamma_c = Factors[0]
    gamma_sk = Factors[1]
    eta_t = Factors[2] 
    
    # Design compressive strength of concrete
    eta_fc = min(1,(30/f_ck)**(1/3)) # SIA 262 4.2.1.2
    f_cd = eta_fc*eta_t*f_ck/gamma_c
    
    # Design yield strength of the rebars
    f_sd = f_sk/gamma_sk
    
    # Depth of the stress block
    x = A_s*f_sd/(0.8*b*f_cd)
    
    # Lever arm 
    d = h - c
    z = d - 0.4*x
    
    # Rebar yield strain
    e_sy = f_sd/E_s
    
    # Rebar strain
    e_s = e_c2d*(d - x)/x
    
    if e_s < e_sy:
        print('Non-ductile beam: Decrease tensile reinforcement or add compression reinforcement')
    elif e_s > e_ud:
        print('Rebar failure: Increase tensile reinforcement')
        
    # Moment resistance of the concrete beam
    M_Rd = A_s*f_sd*z
    
    return M_Rd, x, z  

