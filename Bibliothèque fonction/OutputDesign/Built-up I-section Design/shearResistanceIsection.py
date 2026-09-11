# -*- coding: utf-8 -*-
"""
Created on Tue Apr  22 15:56:54 2025

@author: hammad.eljisr
"""

import math 
from sectionproperties.analysis import Section
from sectionproperties.pre import CompoundGeometry

def shearResistanceIsection(N_Ed,M_Ed,I_sec,a,rigid_end_post,E,post_buckling,gamma_M):
    """
    This function calculates the shear resistance of an I-section without web longitudinal stiffeners: Clause 5, EN 1993-1-5
    Input:
        N_Ed: Applied axial load
        M_Ed: Applied strong axis moment
        I_sec: Effective I-section
        a: Panel width (distance between rigid transverse stiffeners). For an unstiffened web use a = 1e10
        rigid_end_post: 0 non-rigid end post, 1 rigid end post
        E: Steel elastic modulus
        post_buckling: 0 if post-buckling behavior is not considered, 1 otherwise
        gamma_M: [gamma_M0,gamma_M1], partial safety factors

    Output:
        V_b_Rd: Total shear resistance of the steel beam (including flange contribution if present)
        V_bw_Rd: Web contribution to the total shear resistance of the steel beam
        V_bf_Rd: Flange contribution to the total shear resistance of the steel beam 
    """
    
    # I-section regions (flanges + web)
    top_flange_L = I_sec.geoms[0] # Top flange left region
    top_flange_R = I_sec.geoms[1] # Top flange right region
    bottom_flange_L = I_sec.geoms[4] # Bottom flange left region
    bottom_flange_R = I_sec.geoms[5] # Bottom flange right region
    web_T = I_sec.geoms[2] # Web top region
    web_B = I_sec.geoms[3] # Web bottom region
    
    # Section dimensions
    # Top flange (on each side of the web)
    b_f_top_flange_L = abs((top_flange_L.points[0][0]-top_flange_L.points[1][0]))
    t_f_top_flange_L = abs((top_flange_L.points[0][1]-top_flange_L.points[2][1]))
    b_f_top_flange_R = abs((top_flange_R.points[0][0]-top_flange_R.points[1][0]))
    t_f_top_flange_R = abs((top_flange_R.points[0][1]-top_flange_R.points[2][1]))
    # Bottom flange (on each side of the web)
    b_f_bottom_flange_L = abs((bottom_flange_L.points[0][0]-bottom_flange_L.points[1][0]))
    t_f_bottom_flange_L = abs((bottom_flange_L.points[0][1]-bottom_flange_L.points[2][1]))
    b_f_bottom_flange_R = abs((bottom_flange_R.points[0][0]-bottom_flange_R.points[1][0]))
    t_f_bottom_flange_R = abs((bottom_flange_R.points[0][1]-bottom_flange_R.points[2][1]))    
    # Web
    h_w = abs(web_T.points[0][1] - web_B.points[3][1])
    t_w = abs((web_T.points[0][0] + web_T.points[0][0])/2 - (web_T.points[1][0] + web_B.points[1][0])/2)
    
    # Partial factors
    gamma_M0 = gamma_M[0]
    gamma_M1 = gamma_M[1]
    
    # Steel material yield strength
    fyw = I_sec.geoms[2].material.yield_strength*gamma_M0
    fyf = I_sec.geoms[0].material.yield_strength*gamma_M0
    
    # Constants
    eps = (235/fyw)**0.5
    if fyw <= 460: # Clause 5.1, EN 1993-1-5
        eta = 1.2
    else:
        eta = 1.0 
        
    # Shear buckling coefficient, Annex A.3, EN 1993-1-5
    if a/h_w >= 1.0:
        k_tau = 5.34 + 4*(h_w/a)**2
    else:
        k_tau = 4 + 5.34*(h_w/a)**2
    
    # Resistance to shear buckling
    if h_w/t_w <= (31/eta)*eps*(k_tau)**0.5:
        print('Shear buckling not critical')
   
    # Critical plate buckling stress, Annex A.1 EN 1993-1-5
    nu = 0.3 # Poisson ratio
    sigma_E = ((math.pi**2)*E)/(12*(1-nu**2))*(t_w/h_w)**2
    # Critical shear buckling stress, Clause 5.3, EN 1993-1-5
    tau_cr = k_tau*sigma_E 
    
    # Design resistance 
    if post_buckling == 1:
        # Web contribution
        # Modified slenderness, Clause 5.3, EN 1993-1-5
        lambda_w = 0.76*(fyw/tau_cr)**0.5
        if lambda_w < 0.83/eta:
            Xi_w = eta
        elif lambda_w < 1.08 or rigid_end_post == 0:
            Xi_w = 0.83/lambda_w
        else:
            Xi_w = 1.37/(0.7 + lambda_w) 
        
        V_bw_Rd = (Xi_w*fyw*h_w*t_w)/(3**0.5*gamma_M1)
        
        # Flange contribution (effective area) Clause 5.4, EN 1993-1-5
        # Area of each flange (axial resistance)
        area_top_flange = b_f_top_flange_L*t_f_top_flange_L + b_f_top_flange_R*t_f_top_flange_R
        area_bottom_flange = b_f_bottom_flange_L*t_f_bottom_flange_L + b_f_bottom_flange_R*t_f_bottom_flange_R
        
        if area_top_flange < area_bottom_flange:
            t_f = min(t_f_top_flange_L,t_f_top_flange_R)
            b_f = min(b_f_top_flange_L,15*eps*t_f_top_flange_L) + min(b_f_top_flange_R,15*eps*t_f_top_flange_R)
        else:
            t_f = min(t_f_bottom_flange_L,t_f_bottom_flange_R)
            b_f = min(b_f_bottom_flange_L,15*eps*t_f_bottom_flange_L) + min(b_f_bottom_flange_R,15*eps*t_f_bottom_flange_R)
        
        c = a*(0.25 + (1.6*b_f*t_f**2*fyf)/(t_w*h_w**2*fyw))
        # Get plastic resistance of section with effective area of the flanges only  
        I_sec_f = CompoundGeometry(geoms=[top_flange_L,top_flange_R,bottom_flange_L,bottom_flange_R])  
        I_sec_f.create_mesh(mesh_sizes=[t_w**2])
        sec = Section(geometry=I_sec_f)
        sec.calculate_geometric_properties()
        sec.calculate_plastic_properties()
        W_pl_sec_f = sec.get_mp()[1]/fyf # Plastic modulus of the effective flanges about strong axis
        N_f_Rd = sec.get_area()*fyf/gamma_M0 # Axial resistance of cross section consisting of the effective area of the flanges
        M_f_Rd = (1-abs(N_Ed)/N_f_Rd)*W_pl_sec_f*fyf/gamma_M0 # Moment resistance of cross section consisting of the effective area of the flanges
        
        if abs(M_Ed) < M_f_Rd:
            V_bf_Rd = (b_f*t_f**2*fyf)/(c*gamma_M1)*(1-(M_Ed/M_f_Rd)**2)
        else:
            V_bf_Rd = 0
        
        # Design resistance to shear
        V_b_Rd = min(V_bw_Rd + V_bf_Rd,(eta*fyw*h_w*t_w)/(3**0.5*gamma_M1))
   
    else: # Elastic resistance
        V_b_Rd = (min(tau_cr,fyw/(3**0.5))*h_w*t_w)/(gamma_M1)
        print(tau_cr)
        print(h_w)
        V_bw_Rd = V_b_Rd
        V_bf_Rd = 0
       
    return V_b_Rd, V_bw_Rd, V_bf_Rd,tau_cr
