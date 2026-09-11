# -*- coding: utf-8 -*-
"""
Created on Tue Apr  22 15:56:54 2025

@author: hammad.eljisr
"""

from math import nan
from sectionproperties.analysis import Section
import numpy as np
 
def getIsectionNormalStresses(P,Mxx,Myy,I_sec):
    """
    This function outputs the normal stresses in each element of the I-section. An option for a composite section is available.
    Input:
        P: Applied axial force. Tension positive
        Mxx: Applied strong axis bending moment. 
        Myy: Applied weak axis bending moment. y-axis positive (M2 in SAP2000)
        I_sec: Section geometry ('sectionproperties'  library)
        
    Output:
        Top_Flange_L and Top_Flange_R: [x_1,x_2,y_1,y_2,stress_1,stress_2] # Coordinates and stresses at centerline of I-section top flange (left and right portions)
        Bottom_flange_L and Bottom_flange_R: [x_1,x_2,y_1,y_2,stress_1,stress_2] # Coordinates and stresses at centerline of I-section bottom flange (left and right portions)
        Web_T and Web_B: [x_1,x_2,y_1,y_2,stress_1,stress_2] # Coordinates and stresses at centerline of I-section web (top and bottom portions)
        Slab_stress: Minimum and maximum elastic normal stress in the slab (if composite) [s_min,s_max]
    """
    
    # Moment convention: sagging bending positive
    Mxx = -Mxx
    
    # Check if section is composite
    try: 
        if I_sec.geoms[6].material.name != 'Concrete':
            composite = 0
        else:
            composite = 1
    except:
        composite = 0
        
    # Applied load
    load_case = {"n": P, "mxx": Mxx, "myy": Myy} # Applied bending moments and axial force

    # I-section regions
    top_flange_L = I_sec.geoms[0].points # Top flange left region
    top_flange_R = I_sec.geoms[1].points # Top flange right region
    web_T = I_sec.geoms[2].points # Web top region
    web_B = I_sec.geoms[3].points # Web bottom region
    bottom_flange_L = I_sec.geoms[4].points # Bottom flange left region
    bottom_flange_R = I_sec.geoms[5].points # Bottom flange right region
    if composite == 1:
        slab = I_sec.geoms[6].points # Slab region
        
    # Mesh
    t_web = min(web_T[1][0]-web_T[0][0],web_B[1][0]-web_B[0][0]) # Minimum dimension (web thickness)
    if composite == 1:
        mesh_sizes = list(np.ones(len(I_sec.geoms))*t_web**2)
        mesh_sizes[6] = (5*t_web)**2
        sec_geom = I_sec.create_mesh(mesh_sizes=mesh_sizes) # Mesh size = area of minimum dimension squared
    else:
        sec_geom = I_sec.create_mesh(mesh_sizes=[t_web**2]) # Mesh size = area of minimum dimension squared
    
    # Stress calculation
    sec = Section(geometry=sec_geom)
    sec.calculate_geometric_properties()

    # Top flange L stress
    x_L1_tf = (top_flange_L[0][0] + top_flange_L[3][0])/2
    y_L1_tf = (top_flange_L[0][1] + top_flange_L[2][1])/2
    s_L1_tf = sec.get_stress_at_points(pts=[(x_L1_tf,y_L1_tf)], **load_case)[0][0]
    x_L2_tf = (top_flange_L[1][0] + top_flange_L[2][0])/2 - t_web/2
    y_L2_tf = (top_flange_L[1][1] + top_flange_L[3][1])/2
    s_L2_tf = sec.get_stress_at_points(pts=[(x_L2_tf,y_L2_tf)], **load_case)[0][0]
    
    # Top flange R stress
    x_R1_tf = (top_flange_R[0][0] + top_flange_R[3][0])/2 + t_web/2
    y_R1_tf = (top_flange_R[0][1] + top_flange_R[2][1])/2
    s_R1_tf = sec.get_stress_at_points(pts=[(x_R1_tf,y_R1_tf)], **load_case)[0][0]
    x_R2_tf = (top_flange_R[1][0] + top_flange_R[2][0])/2 
    y_R2_tf = (top_flange_R[1][1] + top_flange_R[3][1])/2
    s_R2_tf = sec.get_stress_at_points(pts=[(x_R2_tf,y_R2_tf)], **load_case)[0][0]
    
    # Web T stress
    x_T1_w = (web_T[0][0] + web_T[1][0])/2
    y_T1_w = (web_T[0][1] + web_T[1][1])/2 
    s_T1_w = sec.get_stress_at_points(pts=[(x_T1_w,y_T1_w)], **load_case)[0][0]
    x_T2_w = (web_T[2][0] + web_T[3][0])/2
    y_T2_w = (web_T[2][1] + web_T[3][1])/2 
    s_T2_w = sec.get_stress_at_points(pts=[(x_T2_w,y_T2_w)], **load_case)[0][0]
    
    # Web B stress
    x_B1_w = (web_B[0][0] + web_B[1][0])/2
    y_B1_w = (web_B[0][1] + web_B[1][1])/2 
    s_B1_w = sec.get_stress_at_points(pts=[(x_B1_w,y_B1_w)], **load_case)[0][0]
    x_B2_w = (web_B[2][0] + web_B[3][0])/2
    y_B2_w = (web_B[2][1] + web_B[3][1])/2 
    s_B2_w = sec.get_stress_at_points(pts=[(x_B2_w,y_B2_w)], **load_case)[0][0]
    
    # Bottom flange L stress
    x_L1_bf = (bottom_flange_L[0][0] + bottom_flange_L[3][0])/2
    y_L1_bf = (bottom_flange_L[0][1] + bottom_flange_L[2][1])/2
    s_L1_bf = sec.get_stress_at_points(pts=[(x_L1_bf,y_L1_bf)], **load_case)[0][0]
    x_L2_bf = (bottom_flange_L[1][0] + bottom_flange_L[2][0])/2 - t_web/2
    y_L2_bf = (bottom_flange_L[1][1] + bottom_flange_L[3][1])/2
    s_L2_bf = sec.get_stress_at_points(pts=[(x_L2_bf,y_L2_bf)], **load_case)[0][0]
    
    # Bottom flange R stress
    x_R1_bf = (bottom_flange_R[0][0] + bottom_flange_R[3][0])/2 + t_web/2
    y_R1_bf = (bottom_flange_R[0][1] + bottom_flange_R[2][1])/2
    s_R1_bf = sec.get_stress_at_points(pts=[(x_R1_bf,y_R1_bf)], **load_case)[0][0]
    x_R2_bf = (bottom_flange_R[1][0] + bottom_flange_R[2][0])/2
    y_R2_bf = (bottom_flange_R[1][1] + bottom_flange_R[3][1])/2
    s_R2_bf = sec.get_stress_at_points(pts=[(x_R2_bf,y_R2_bf)], **load_case)[0][0]
    
    # Slab stress
    if composite == 1:
        s_sl_0 = 0
        for j in range(len(slab)):
            s_sl = sec.get_stress_at_points(pts=[slab[j]],**load_case)[0][0]
            s_sl_min = min(s_sl,s_sl_0)
            s_sl_max = max(s_sl,s_sl_0)
        
    Top_Flange_L = [x_L1_tf,x_L2_tf,y_L1_tf,y_L2_tf,s_L1_tf,s_L2_tf]
    Top_Flange_R = [x_R1_tf,x_R2_tf,y_R1_tf,y_R2_tf,s_R1_tf,s_R2_tf]
    
    Bottom_Flange_L = [x_L1_bf,x_L2_bf,y_L1_bf,y_L2_bf,s_L1_bf,s_L2_bf]
    Bottom_Flange_R = [x_R1_bf,x_R2_bf,y_R1_bf,y_R2_bf,s_R1_bf,s_R2_bf]
    
    Web_T = [x_T1_w,x_T2_w,y_T1_w,y_T2_w,s_T1_w,s_T2_w]
    Web_B = [x_B1_w,x_B2_w,y_B1_w,y_B2_w,s_B1_w,s_B2_w]
    
    if composite == 1:
        Slab_stress = [s_sl_min,s_sl_max]
    else:
        Slab_stress = [nan,nan]
    
    return Top_Flange_L, Top_Flange_R, Bottom_Flange_L, Bottom_Flange_R, Web_T, Web_B, Slab_stress
