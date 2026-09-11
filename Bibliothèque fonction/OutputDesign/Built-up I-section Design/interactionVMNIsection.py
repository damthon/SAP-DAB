# -*- coding: utf-8 -*-
"""
Created on Tue Apr  22 15:56:54 2025

@author: hammad.eljisr
"""

from sectionproperties.analysis import Section
from sectionproperties.pre import Geometry, CompoundGeometry
from getIsectionNormalStresses import getIsectionNormalStresses
from shapely import Polygon

def interactionVMNIsection(N_Ed,M_Ed,V_Ed,I_sec,V_bw_Rd,eta_1_MN,gamma_M0):
    """
    This function checks the interaction between the shear force, bending moment and axial force: Clause 7.1, EN 1993-1-5
    Input:
        N_Ed: Applied axial load
        M_Ed: Applied strong axis moment
        V_Ed: Applied shear force
        I_sec: Effective I-section
        V_bw_Rd: Web contribution to the total shear resistance of the steel beam
        eta_1_MN: Verification of axial force and uniaxial bending: Clause 4.6, EN 1993-1-5
        gamma_M0: Partial safety factor for MN

    Output:
        Interaction_check: Interaction check, satisfied if < 1.0 (if 0 no check is required), not satisfied otherwise
    """
    
    # I-section regions (flanges + web)
    top_flange_L = I_sec.geoms[0] # Top flange left region
    top_flange_R = I_sec.geoms[1] # Top flange right region
    bottom_flange_L = I_sec.geoms[4] # Bottom flange left region
    bottom_flange_R = I_sec.geoms[5] # Bottom flange right region
    web_T = I_sec.geoms[2] # Web top region
    web_B = I_sec.geoms[3] # Web bottom region
    
    # Web dimensions
    h_w = abs(web_T.points[0][1] - web_B.points[3][1])
    t_w = abs((web_T.points[0][0] + web_T.points[0][0])/2 - (web_T.points[1][0] + web_B.points[1][0])/2)
    
    # Steel  material
    steel_web = I_sec.geoms[2].material
    steel_flanges = I_sec.geoms[0].material
    fyw = steel_web.yield_strength*gamma_M0
    fyf = steel_flanges.yield_strength*gamma_M0
    
    # Get web stress state
    [Top_Flange_L,Top_Flange_R,Bottom_Flange_L,Bottom_Flange_R,Web_T, Web_B,Slab_stress] = getIsectionNormalStresses(N_Ed,M_Ed,0,I_sec)
    if max(Web_T[4:6]) < 0 and max(Web_B[4:6]) < 0: # Web is in fully in compression 
        web_compression = 1 
    else:
        web_compression = 0
        
    # Get Mf_Rd: Design plastic resistance of the section consisiting of the effective area of the flanges
    if web_compression == 0:
        I_sec_f = CompoundGeometry(geoms=[top_flange_L,top_flange_R,bottom_flange_L,bottom_flange_R])  
        I_sec_f.create_mesh(mesh_sizes=[t_w**2])
        sec_f = Section(geometry=I_sec_f)
        sec_f.calculate_geometric_properties()
        sec_f.calculate_plastic_properties()
        W_pl_f = sec_f.get_mp()[0]/fyf # Plastic modulus of the effective flanges about strong axis
        N_f_Rd = sec_f.get_area()*fyf/gamma_M0 # Axial resistance of cross section consisting of the effective area of the flanges
        M_f_Rd = (1-abs(N_Ed)/N_f_Rd)*W_pl_f*fyf/gamma_M0 # Moment resistance of cross section consisting of the effective area of the flanges
    else:
        M_f_Rd = 0
   
    # Get M_pl_Rd: Design plastic resistance of the section consisiting of the effective area of the flanges and full web irrespective of its section class
    if web_compression == 0:
        full_web = Polygon([web_T.points[0],web_T.points[1],web_B.points[2],web_B.points[3]])
        geom_full_web = Geometry(geom=full_web,material=steel_web)
        I_sec_pl = CompoundGeometry(geoms=[top_flange_L,top_flange_R,bottom_flange_L,bottom_flange_R,geom_full_web])  
        I_sec_pl.create_mesh(mesh_sizes=[t_w**2])
        sec_pl = Section(geometry=I_sec_pl)
        sec_pl.calculate_geometric_properties()
        sec_pl.calculate_plastic_properties()
        M_pl_Rd_0 = sec_pl.get_mp()[0] # Plastic moment resistance of the section with effective flanges, full web, no reduction due to axial force
        # Axial resistance of the section with effective flanges, full web
        N_pl_Rd = fyf/gamma_M0*(I_sec_pl.geoms[0].calculate_area() + I_sec_pl.geoms[1].calculate_area() + I_sec_pl.geoms[2].calculate_area() + I_sec_pl.geoms[3].calculate_area())+fyw/gamma_M0*(I_sec_pl.geoms[4].calculate_area())
        # Reduced M_pl_Rd according to Clause 6.2.9, EN 1993-1-1 
        n = abs(N_Ed/N_pl_Rd)
        a = min(0.5,(I_sec_pl.calculate_area() - h_w*t_w)/I_sec_pl.calculate_area())
        M_pl_Rd = min((1-n)/(1-0.5*a)*M_pl_Rd_0,M_pl_Rd_0) # Moment resistance of the section with effective flanges, full web, linear reduction (linear interaction) due to axial force
        eta_1 = abs(M_Ed/M_pl_Rd)
        eta_3 = abs(V_Ed/V_bw_Rd)
        # Interaction (< 1 satisifactory)
        if eta_3 <= 0.5:
            print('Design resistance to bending moment and axial force need not be reduced, no interaction check required')
            Interaction_check = 0 # Satisfied
        else:
            Interaction_check = eta_1 + (1-M_f_Rd/M_pl_Rd)*(2*eta_3-1)**2 
    else:
        eta_1 = eta_1_MN
        eta_3 = abs(V_Ed/V_bw_Rd)
        # Interaction (< 1 satisifactory)
        if eta_3 <= 0.5:
            print('Design resistance to bending moment and axial force need not be reduced, no interaction check required')
            Interaction_check = 0 # Satisfied
        else:
            Interaction_check = eta_1 + (2*eta_3-1)**2

    return Interaction_check
