# -*- coding: utf-8 -*-
"""
Created on Mon Nov  27 11:02:54 2023

@author: hammad.eljisr
"""


def otherPTLosses(P,E,A,e_sh,phi_cr,rel):
    """
    This function calculates the other prestress losses in SAP2000
    Input:
        - P: Prestress force in the beam; P[0] is the initial force, P[1] is the average prestress force in the beam after initial losses due to friction and anchorage slip
        - E: Modulii of elasticity; E[0] concrete, E[1] tendons
        - A: Areas; A[0] concrete section, A[1] tendon section (total of all tendons in the section)
        - e_sh: Shrinkage strain
        - phi_cr: Creep coefficient
        - rel: Percentage of relaxation in the tendons (e.g. 0.05)
    """
    
    Po = P[0]
    P_init = P[1]
    Ec = E[0]
    Ep = E[1]
    Ac = A[0]
    Ap = A[1]

    # Elastic shortening loss
    e_el = Po/(Ac*Ec) # Elastic shortening strain
    s_el = e_el*Ep   # Elastic shortening loss
    
    # Shrinkage loss
    s_sh = Ep*e_sh # Shrinkage loss
    
    # Creep loss 
    sc_init = P_init/Ac # Average stress in the concrete after initial losses
    ec_avg = sc_init/Ec # Average strain in the concrete after initial losses
    e_cr = phi_cr*ec_avg # Creep strain
    s_cr = Ep*e_cr # Creep loss
    
    # Relaxation losses
    s_avg_rel = P_init/Ap - (s_cr + s_sh)/2 # Average stress in the tendons at an average time (hence the /2)
    s_rel = s_avg_rel*rel
    
    
    return s_el, s_sh, s_cr, s_rel





    

      