# -*- coding: utf-8 -*-
"""
Created on Fri Apr  25 15:56:54 2025

@author: hammad.eljisr
"""

import copy
from sectionproperties.pre import CompoundGeometry
from getIsectionNormalStresses import getIsectionNormalStresses
from getplasticNeutralAxisBareIsection import getplasticNeutralAxisBareIsection

def classificationIsection(P,Mxx,Myy,I_sec,gamma_M0):
    """
    This function outputs the class of a steel I-section under a load combination. The classification is done according to EN 1993-1-1, Tables 5.1 and 5.2.
    The shift in the location of the plastic neutral axis (PNA) is accounted for if the section is composite
    Input:
        P: Applied axial force in the steel beam (NOT composite section). Tension positive
        Mxx: Applied bending moment in the steel beam (NOT composite section). Sagging positive
        I_sec: Section geometry ('sectionproperties' library)
        gamma_M0: Partial safety factor for the steel section
        
    Output:
        class_section: Section class
        class_web: Web class
        class_tf: Top flange class 
        class_bf: Bottom flange class
    """
   
    # Check if section is composite and get bare section for the cross section classification
    if len(I_sec.geoms) == 6:
        I_sec_bare = copy.deepcopy(I_sec)
    else:
        list_geom = [I_sec.geoms[0],I_sec.geoms[1],I_sec.geoms[2],I_sec.geoms[3],I_sec.geoms[4],I_sec.geoms[5]] 
        list_geom_bare = copy.deepcopy(list_geom)
        I_sec_bare = CompoundGeometry(geoms=list_geom_bare)
        
    def getKsigma(element_type,psi):
        # Function that calculates K_sigma, # Table 4.2, EN 1993-1-5
        # Input 1: element_type = 1 for outstand element with maximum compressive stress at free end, 2 for outstand element with maximum compressive stress at fixed end
        # Input 2: psi = stress ratio
        if element_type == 1:
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
            
        return k_sigma 
    
    # Steel material yield strength
    fyw = I_sec_bare.geoms[2].material.yield_strength*gamma_M0
    fyf = I_sec_bare.geoms[0].material.yield_strength*gamma_M0
    
    # Constants
    eps_w = (235/fyw)**0.5
    eps_f = (235/fyf)**0.5
    
    # I-section regions (flanges + web)
    top_flange_L = I_sec_bare.geoms[0] # Top flange left region
    top_flange_R = I_sec_bare.geoms[1] # Top flange right region
    bottom_flange_L = I_sec_bare.geoms[4] # Bottom flange left region
    bottom_flange_R = I_sec_bare.geoms[5] # Bottom flange right region
    web_T = I_sec_bare.geoms[2] # Web top region
    web_B = I_sec_bare.geoms[3] # Web bottom region
    
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
    
    # Plastic analysis to get plastic neutral axis
    y_pl = getplasticNeutralAxisBareIsection(P,Mxx,I_sec) # Plastic neutral axis
    
    # Get psi and K_sigma (for flanges)
    # Elastic stress distribution
    [Top_Flange_L,Top_Flange_R,Bottom_Flange_L,Bottom_Flange_R,Web_T,Web_B,Slab_Stress] = getIsectionNormalStresses(P,Mxx,Myy,I_sec_bare) 
    # Web
    psi_w = max(Web_T[4],Web_B[5])/min(Web_T[4],Web_B[5])
    # Top flange L
    psi_tf_L = max(Top_Flange_L[4],Top_Flange_L[5])/min(Top_Flange_L[4],Top_Flange_L[5])
    if Top_Flange_L[4] < Top_Flange_L[5]:
        el_Top_Flange_L = 1
    else:
        el_Top_Flange_L = 2
    K_sigma_tf_L = getKsigma(el_Top_Flange_L,psi_tf_L)
    # Top flange R
    psi_tf_R = max(Top_Flange_R[4],Top_Flange_R[5])/min(Top_Flange_R[4],Top_Flange_R[5])
    if Top_Flange_R[5] < Top_Flange_R[4]:
        el_Top_Flange_R = 1
    else:
        el_Top_Flange_R = 2
    K_sigma_tf_R = getKsigma(el_Top_Flange_R,psi_tf_R)
    # Bottom flange L
    psi_bf_L = max(Bottom_Flange_L[4],Bottom_Flange_L[5])/min(Bottom_Flange_L[4],Bottom_Flange_L[5])
    if Bottom_Flange_L[4] < Bottom_Flange_L[5]:
        el_Bottom_Flange_L = 1
    else:
        el_Bottom_Flange_L = 2
    K_sigma_bf_L = getKsigma(el_Bottom_Flange_L,psi_bf_L)
    # Bottom flange R
    psi_bf_R = max(Bottom_Flange_R[4],Bottom_Flange_R[5])/min(Bottom_Flange_R[4],Bottom_Flange_R[5])   
    if Bottom_Flange_R[5] < Bottom_Flange_R[4]:
        el_Bottom_Flange_R = 1
    else:
        el_Bottom_Flange_R = 2
    K_sigma_bf_R = getKsigma(el_Bottom_Flange_R,psi_bf_R)
    
    # Get alpha for web (to check if Class 1 or 2)
    # Web region in compression
    if Mxx > 0:
        a_w = max(0,min(h_w,h_w - (y_pl - 0.5*(t_f_bottom_flange_R+t_f_bottom_flange_R)))) # From top flange
    else:
        a_w = max(0,min(h_w,(y_pl - 0.5*(t_f_bottom_flange_R+t_f_bottom_flange_R)))) # From bottom flange
    alpha_w = a_w/h_w  
    
    # Internal element (web) classification
    cw_tw = h_w/t_w 
    
    if (Web_T[4] < 0 or Web_B[5] < 0): # Element fully of partially under compression
        # Class 3 slenderness limit
        if psi_w > -1:
            cw_tw_limit_3 = (42/(0.67+0.33*psi_w))*eps_w
        else:
            cw_tw_limit_3 = (62*(1-psi_w)*(-psi_w)**0.5)*eps_w
        if cw_tw > cw_tw_limit_3:
            class_web = 4
        else: # Check if Class 1, 2 or 3
            if alpha_w > 0.5:
                cw_tw_limit_2 = (456/(13*alpha_w-1))*eps_w
                cw_tw_limit_1 = (396/(13*alpha_w-1))*eps_w
            elif alpha_w != 0:
                cw_tw_limit_2 = (41.5/alpha_w)*eps_w
                cw_tw_limit_1 = (36/alpha_w)*eps_w
            else:
                cw_tw_limit_1 =1e6 # alpha = 0 (Tension)
                cw_tw_limit_2 =1e6 # alpha = 0 (Tension)
            if cw_tw > cw_tw_limit_2:
                class_web = 3
            elif cw_tw > cw_tw_limit_1:
                class_web = 2
            else: 
                class_web = 1
    else: # Element under pure tension
        class_web = 1
     
        
    # Outstand elements (flange) classification
    # Top flange 
    c_tf_L = b_f_top_flange_L - t_w/2
    t_tf_L = t_f_top_flange_L
    c_tf_L_tf = c_tf_L/t_tf_L # Top flange left slenderness
    c_tf_R = b_f_top_flange_R - t_w/2
    t_tf_R = t_f_top_flange_R
    c_tf_R_tf = c_tf_R/t_tf_R # Top flange right slenderness
    
    # Top flange left slenderness
    if (Top_Flange_L[4] < 0 or Top_Flange_L[5] < 0): # Element fully or partially under compression
        # Slenderness limits 
        if (Top_Flange_L[4] < 0 and Top_Flange_L[5] < 0): # Case partially under compression considered for Class 3 only (elastic distribution)
            c_tf_L_limit_3 = 14*eps_f # Class 3
        else:
            c_tf_L_limit_3 = (21*(K_sigma_tf_L)**0.5)*eps_f 
        c_tf_L_limit_2 = 10*eps_f # Class 2
        c_tf_L_limit_1 = 9*eps_f # Class 1
        if c_tf_L_tf > c_tf_L_limit_3:
            class_tf_L = 4
        elif c_tf_L_tf > c_tf_L_limit_2:
            class_tf_L = 3
        elif c_tf_L_tf > c_tf_L_limit_1:
            class_tf_L = 2
        else:
            class_tf_L = 1
    else:
        class_tf_L = 1
            
    # Top flange right slenderness
    if (Top_Flange_R[4] < 0 or Top_Flange_R[5] < 0): # Element fully or partially under compression
        # Slenderness limits 
        if (Top_Flange_R[4] < 0 and Top_Flange_R[5] < 0): # Case partially under compression considered for Class 3 only (elastic distribution)
            c_tf_R_limit_3 = 14*eps_f # Class 3
        else:
            c_tf_R_limit_3 = (21*(K_sigma_tf_R)**0.5)*eps_f 
        c_tf_R_limit_2 = 10*eps_f # Class 2
        c_tf_R_limit_1 = 9*eps_f # Class 1
        if c_tf_R_tf > c_tf_R_limit_3:
            class_tf_R = 4
        elif c_tf_R_tf > c_tf_R_limit_2:
            class_tf_R = 3
        elif c_tf_R_tf > c_tf_R_limit_1:
            class_tf_R = 2
        else:
            class_tf_R = 1
    else:
        class_tf_R = 1
    
    class_tf = max(class_tf_L,class_tf_R)  
     
    # Bottom flange
    c_bf_L = b_f_bottom_flange_L - t_w/2
    t_bf_L = t_f_bottom_flange_L
    c_bf_L_tf = c_bf_L/t_bf_L # Bottom flange left slenderness
    c_bf_R = b_f_bottom_flange_R - t_w/2
    t_bf_R = t_f_bottom_flange_R
    c_bf_R_tf = c_bf_R/t_bf_R # Bottom flange right slenderness
    
    # Top flange left slenderness
    if (Bottom_Flange_L[4] < 0 or Bottom_Flange_L[5] < 0): # Element fully or partially under compression
        # Slenderness limits 
        if (Bottom_Flange_L[4] < 0 and Bottom_Flange_L[5] < 0): # Case partially under compression considered for Class 3 only (elastic distribution)
            c_bf_L_limit_3 = 14*eps_f # Class 3
        else:
            c_bf_L_limit_3 = (21*(K_sigma_bf_L)**0.5)*eps_f 
        c_bf_L_limit_2 = 10*eps_f # Class 2
        c_bf_L_limit_1 = 9*eps_f # Class 1
        if c_bf_L_tf > c_bf_L_limit_3:
            class_bf_L = 4
        elif c_bf_L_tf > c_bf_L_limit_2:
            class_bf_L = 3
        elif c_bf_L_tf > c_bf_L_limit_1:
            class_bf_L = 2
        else:
            class_bf_L = 1
    else:
        class_bf_L = 1
            
    # Bottom flange right slenderness
    if (Bottom_Flange_R[4] < 0 or Bottom_Flange_R[5] < 0): # Element fully or partially under compression
        # Slenderness limits 
        if (Bottom_Flange_R[4] < 0 and Bottom_Flange_R[5] < 0): # Case partially under compression considered for Class 3 only (elastic distribution)
            c_bf_R_limit_3 = 14*eps_f # Class 3
        else:
            c_bf_R_limit_3 = (21*(K_sigma_bf_R)**0.5)*eps_f 
        c_bf_R_limit_2 = 10*eps_f # Class 2
        c_bf_R_limit_1 = 9*eps_f # Class 1
        if c_bf_R_tf > c_bf_R_limit_3:
            class_bf_R = 4
        elif c_bf_R_tf > c_bf_R_limit_2:
            class_bf_R = 3
        elif c_bf_R_tf > c_bf_R_limit_1:
            class_bf_R = 2
        else:
            class_bf_R = 1
    else:
        class_bf_R = 1
    
    class_bf = max(class_bf_L,class_bf_R)  
    
    # Cross-section class
    class_section= max(class_web,class_tf,class_bf)
    
    return class_section, class_web, class_tf, class_bf

def classificationIsection_SIA269_3(P,Mxx,Myy,I_sec,Ek,gamma_M1_act):
    """
    This function outputs the class of a steel I-section under a load combination. The classification is done according to EN 1993-1-1, Tables 5.1 and 5.2.
    The safety factors and epsilon are calculated according to SIA269/3 for existing structures
    The shift in the location of the plastic neutral axis (PNA) is accounted for if the section is composite
    Input:
        P: Applied axial force in the steel beam (NOT composite section). Tension positive
        Mxx: Applied bending moment in the steel beam (NOT composite section). Sagging positive
        I_sec: Section geometry ('sectionproperties' library)
        Ek: Modulus of elasticity of the steel beam in MPa
        gamma_M1_act: Partial safety factor for the steel section
        
    Output:
        class_section: Section class
        class_web: Web class
        class_tf: Top flange class 
        class_bf: Bottom flange class
    """
   
    # Check if section is composite and get bare section for the cross section classification
    if len(I_sec.geoms) == 6:
        I_sec_bare = copy.deepcopy(I_sec)
    else:
        list_geom = [I_sec.geoms[0],I_sec.geoms[1],I_sec.geoms[2],I_sec.geoms[3],I_sec.geoms[4],I_sec.geoms[5]] 
        list_geom_bare = copy.deepcopy(list_geom)
        I_sec_bare = CompoundGeometry(geoms=list_geom_bare)
        
    def getKsigma(element_type,psi):
        # Function that calculates K_sigma, # Table 4.2, EN 1993-1-5
        # Input 1: element_type = 1 for outstand element with maximum compressive stress at free end, 2 for outstand element with maximum compressive stress at fixed end
        # Input 2: psi = stress ratio
        if element_type == 1:
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
            
        return k_sigma 
    
    # Steel material yield strength
    fyw = I_sec_bare.geoms[2].material.yield_strength*gamma_M1_act
    fyf = I_sec_bare.geoms[0].material.yield_strength*gamma_M1_act
    
    # Constants
    eps_w = (Ek/210000*235/fyw*gamma_M1_act/1.05)**0.5
    eps_f = (Ek/210000*235/fyf*gamma_M1_act/1.05)**0.5
    
    # I-section regions (flanges + web)
    top_flange_L = I_sec_bare.geoms[0] # Top flange left region
    top_flange_R = I_sec_bare.geoms[1] # Top flange right region
    bottom_flange_L = I_sec_bare.geoms[4] # Bottom flange left region
    bottom_flange_R = I_sec_bare.geoms[5] # Bottom flange right region
    web_T = I_sec_bare.geoms[2] # Web top region
    web_B = I_sec_bare.geoms[3] # Web bottom region
    
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
    
    # Plastic analysis to get plastic neutral axis
    y_pl = getplasticNeutralAxisBareIsection(P,Mxx,I_sec) # Plastic neutral axis
    
    # Get psi and K_sigma (for flanges)
    # Elastic stress distribution
    [Top_Flange_L,Top_Flange_R,Bottom_Flange_L,Bottom_Flange_R,Web_T,Web_B,Slab_Stress] = getIsectionNormalStresses(P,Mxx,Myy,I_sec_bare) 
    # Web
    psi_w = max(Web_T[4],Web_B[5])/min(Web_T[4],Web_B[5])
    # Top flange L
    psi_tf_L = max(Top_Flange_L[4],Top_Flange_L[5])/min(Top_Flange_L[4],Top_Flange_L[5])
    if Top_Flange_L[4] < Top_Flange_L[5]:
        el_Top_Flange_L = 1
    else:
        el_Top_Flange_L = 2
    K_sigma_tf_L = getKsigma(el_Top_Flange_L,psi_tf_L)
    # Top flange R
    psi_tf_R = max(Top_Flange_R[4],Top_Flange_R[5])/min(Top_Flange_R[4],Top_Flange_R[5])
    if Top_Flange_R[5] < Top_Flange_R[4]:
        el_Top_Flange_R = 1
    else:
        el_Top_Flange_R = 2
    K_sigma_tf_R = getKsigma(el_Top_Flange_R,psi_tf_R)
    # Bottom flange L
    psi_bf_L = max(Bottom_Flange_L[4],Bottom_Flange_L[5])/min(Bottom_Flange_L[4],Bottom_Flange_L[5])
    if Bottom_Flange_L[4] < Bottom_Flange_L[5]:
        el_Bottom_Flange_L = 1
    else:
        el_Bottom_Flange_L = 2
    K_sigma_bf_L = getKsigma(el_Bottom_Flange_L,psi_bf_L)
    # Bottom flange R
    psi_bf_R = max(Bottom_Flange_R[4],Bottom_Flange_R[5])/min(Bottom_Flange_R[4],Bottom_Flange_R[5])   
    if Bottom_Flange_R[5] < Bottom_Flange_R[4]:
        el_Bottom_Flange_R = 1
    else:
        el_Bottom_Flange_R = 2
    K_sigma_bf_R = getKsigma(el_Bottom_Flange_R,psi_bf_R)
    
    # Get alpha for web (to check if Class 1 or 2)
    # Web region in compression
    if Mxx > 0:
        a_w = max(0,min(h_w,h_w - (y_pl - 0.5*(t_f_bottom_flange_R+t_f_bottom_flange_R)))) # From top flange
    else:
        a_w = max(0,min(h_w,(y_pl - 0.5*(t_f_bottom_flange_R+t_f_bottom_flange_R)))) # From bottom flange
    alpha_w = a_w/h_w  
    
    # Internal element (web) classification
    cw_tw = h_w/t_w 
    
    if (Web_T[4] < 0 or Web_B[5] < 0): # Element fully of partially under compression
        # Class 3 slenderness limit
        if psi_w > -1:
            cw_tw_limit_3 = (42/(0.67+0.33*psi_w))*eps_w
        else:
            cw_tw_limit_3 = (62*(1-psi_w)*(-psi_w)**0.5)*eps_w
        if cw_tw > cw_tw_limit_3:
            class_web = 4
        else: # Check if Class 1, 2 or 3
            if alpha_w > 0.5:
                cw_tw_limit_2 = (456/(13*alpha_w-1))*eps_w
                cw_tw_limit_1 = (396/(13*alpha_w-1))*eps_w
            elif alpha_w != 0:
                cw_tw_limit_2 = (41.5/alpha_w)*eps_w
                cw_tw_limit_1 = (36/alpha_w)*eps_w
            else:
                cw_tw_limit_1 =1e6 # alpha = 0 (Tension)
                cw_tw_limit_2 =1e6 # alpha = 0 (Tension)
            if cw_tw > cw_tw_limit_2:
                class_web = 3
            elif cw_tw > cw_tw_limit_1:
                class_web = 2
            else: 
                class_web = 1
    else: # Element under pure tension
        class_web = 1
     
        
    # Outstand elements (flange) classification
    # Top flange 
    c_tf_L = b_f_top_flange_L - t_w/2
    t_tf_L = t_f_top_flange_L
    c_tf_L_tf = c_tf_L/t_tf_L # Top flange left slenderness
    c_tf_R = b_f_top_flange_R - t_w/2
    t_tf_R = t_f_top_flange_R
    c_tf_R_tf = c_tf_R/t_tf_R # Top flange right slenderness
    
    # Top flange left slenderness
    if (Top_Flange_L[4] < 0 or Top_Flange_L[5] < 0): # Element fully or partially under compression
        # Slenderness limits 
        if (Top_Flange_L[4] < 0 and Top_Flange_L[5] < 0): # Case partially under compression considered for Class 3 only (elastic distribution)
            c_tf_L_limit_3 = 14*eps_f # Class 3
        else:
            c_tf_L_limit_3 = (21*(K_sigma_tf_L)**0.5)*eps_f 
        c_tf_L_limit_2 = 10*eps_f # Class 2
        c_tf_L_limit_1 = 9*eps_f # Class 1
        if c_tf_L_tf > c_tf_L_limit_3:
            class_tf_L = 4
        elif c_tf_L_tf > c_tf_L_limit_2:
            class_tf_L = 3
        elif c_tf_L_tf > c_tf_L_limit_1:
            class_tf_L = 2
        else:
            class_tf_L = 1
    else:
        class_tf_L = 1
            
    # Top flange right slenderness
    if (Top_Flange_R[4] < 0 or Top_Flange_R[5] < 0): # Element fully or partially under compression
        # Slenderness limits 
        if (Top_Flange_R[4] < 0 and Top_Flange_R[5] < 0): # Case partially under compression considered for Class 3 only (elastic distribution)
            c_tf_R_limit_3 = 14*eps_f # Class 3
        else:
            c_tf_R_limit_3 = (21*(K_sigma_tf_R)**0.5)*eps_f 
        c_tf_R_limit_2 = 10*eps_f # Class 2
        c_tf_R_limit_1 = 9*eps_f # Class 1
        if c_tf_R_tf > c_tf_R_limit_3:
            class_tf_R = 4
        elif c_tf_R_tf > c_tf_R_limit_2:
            class_tf_R = 3
        elif c_tf_R_tf > c_tf_R_limit_1:
            class_tf_R = 2
        else:
            class_tf_R = 1
    else:
        class_tf_R = 1
    
    class_tf = max(class_tf_L,class_tf_R)  
     
    # Bottom flange
    c_bf_L = b_f_bottom_flange_L - t_w/2
    t_bf_L = t_f_bottom_flange_L
    c_bf_L_tf = c_bf_L/t_bf_L # Bottom flange left slenderness
    c_bf_R = b_f_bottom_flange_R - t_w/2
    t_bf_R = t_f_bottom_flange_R
    c_bf_R_tf = c_bf_R/t_bf_R # Bottom flange right slenderness
    
    # Top flange left slenderness
    if (Bottom_Flange_L[4] < 0 or Bottom_Flange_L[5] < 0): # Element fully or partially under compression
        # Slenderness limits 
        if (Bottom_Flange_L[4] < 0 and Bottom_Flange_L[5] < 0): # Case partially under compression considered for Class 3 only (elastic distribution)
            c_bf_L_limit_3 = 14*eps_f # Class 3
        else:
            c_bf_L_limit_3 = (21*(K_sigma_bf_L)**0.5)*eps_f 
        c_bf_L_limit_2 = 10*eps_f # Class 2
        c_bf_L_limit_1 = 9*eps_f # Class 1
        if c_bf_L_tf > c_bf_L_limit_3:
            class_bf_L = 4
        elif c_bf_L_tf > c_bf_L_limit_2:
            class_bf_L = 3
        elif c_bf_L_tf > c_bf_L_limit_1:
            class_bf_L = 2
        else:
            class_bf_L = 1
    else:
        class_bf_L = 1
            
    # Bottom flange right slenderness
    if (Bottom_Flange_R[4] < 0 or Bottom_Flange_R[5] < 0): # Element fully or partially under compression
        # Slenderness limits 
        if (Bottom_Flange_R[4] < 0 and Bottom_Flange_R[5] < 0): # Case partially under compression considered for Class 3 only (elastic distribution)
            c_bf_R_limit_3 = 14*eps_f # Class 3
        else:
            c_bf_R_limit_3 = (21*(K_sigma_bf_R)**0.5)*eps_f 
        c_bf_R_limit_2 = 10*eps_f # Class 2
        c_bf_R_limit_1 = 9*eps_f # Class 1
        if c_bf_R_tf > c_bf_R_limit_3:
            class_bf_R = 4
        elif c_bf_R_tf > c_bf_R_limit_2:
            class_bf_R = 3
        elif c_bf_R_tf > c_bf_R_limit_1:
            class_bf_R = 2
        else:
            class_bf_R = 1
    else:
        class_bf_R = 1
    
    class_bf = max(class_bf_L,class_bf_R)  
    
    # Cross-section class
    class_section= max(class_web,class_tf,class_bf)
    
    return class_section, class_web, class_tf, class_bf