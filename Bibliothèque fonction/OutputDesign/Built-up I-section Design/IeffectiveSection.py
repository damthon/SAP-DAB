# -*- coding: utf-8 -*-
"""
Created on Wed Apr  23 15:56:54 2025

@author: hammad.eljisr
"""

from getIsectionNormalStresses import getIsectionNormalStresses
from getPlateEffectiveWidth import getPlateEffectiveWidth
from shapely import Polygon
from sectionproperties.pre import Geometry, CompoundGeometry

def IeffectiveSection(P,Mxx,Myy,I_sec,web_bw_i,gamma_M0,tol,iterations):
    """
    This function calculates the effective built-up I-section with no stiffeners using EN 1993-1-5. An option for a composite section is available.
    An iterative procedure is applied to obtain the final stress state
    Input:
        P: Applied axial force. Tension positive 
        Mxx: Applied strong axis bending moment. Sagging bending positive  (M3 in SAP2000)
        Myy: Applied weak axis bending moment. y-axis positive (M2 in SAP2000)
        I_sec: Initial section geometry ('sectionproperties'  library)
        web_bw_i: Ignored portions of the web for calculating bw [i_Web_T,i_Web_B], [0,0] if all web is considered. E.g. used to decrease bw for riveted beams (Figure 3, SIA 296/3)
        gamma_M0: Partial safety factor for MN
        tol: Section convergence tolerance in %
        iterations: Maximum number of iterations

    Output:
        I_sec_final: Final section geometry ('sectionproperties' library)
        Top_Flange_L and Top_Flange_R: [x_1,x_2,y_1,y_2,stress_1,stress_2] # Coordinates and stresses at centerline of I-section top flange (left and right portions)
        Bottom_flange_L and Bottom_flange_R: [x_1,x_2,y_1,y_2,stress_1,stress_2] # Coordinates and stresses at centerline of I-section bottom flange (left and right portions)
        Web_T and Web_B: [x_1,x_2,y_1,y_2,stress_1,stress_2] # Coordinates and stresses at centerline of I-section web (top and bottom portions)
        Slab_stress: Minimum and maximum elastic normal stress in the slab (if composite) [s_min,s_max]
    """
    
    #%% 
    # Check if section is composite
    try: 
        if I_sec.geoms[6].material.name != 'Concrete':
            composite = 0
        else:
            composite = 1
    except:
        composite = 0
        
    # Section initial regions and materials (to be updated)
    top_flange_L_points = I_sec.geoms[0].points # Top flange left region
    top_flange_R_points = I_sec.geoms[1].points # Top flange right region
    steel_flanges = I_sec.geoms[0].material # Steel flanges material
    web_T_points = I_sec.geoms[2].points # Web top region
    web_B_points = I_sec.geoms[3].points # Web bottom region
    steel_web = I_sec.geoms[2].material # Steel web material
    bottom_flange_L_points = I_sec.geoms[4].points # Bottom flange left region
    bottom_flange_R_points = I_sec.geoms[5].points # Bottom flange right region
    if composite == 1:
        slab = I_sec.geoms[6] # Slab region
        # Angles
        angles_geom = I_sec.geoms[7:]
    else:
        # Angles
        angles_geom = I_sec.geoms[6:]

    # Steel material yield strength
    fyw = I_sec.geoms[2].material.yield_strength*gamma_M0
    fyf = I_sec.geoms[0].material.yield_strength*gamma_M0
    
    # Web dimensions (internal compression element initial dimensions maintained throughout the iterations)
    b_w = web_T_points[0][1] - web_B_points[2][1]
    t_w = abs(web_T_points[0][0] - web_T_points[1][0])  
    web_center = (web_T_points[2][1] + web_B_points[1][1])/2
        
    # Initial normal stresses   
    [Top_Flange_L,Top_Flange_R,Bottom_Flange_L,Bottom_Flange_R,Web_T,Web_B,Slab_Stress] = getIsectionNormalStresses(P,Mxx,Myy,I_sec)    
    #%% 
    for iteration in range(iterations):
        if iteration == 0:
            I_sec_updated = I_sec # First iteration, use initial section
        # Top flange L effective width
        b_L_tf = abs(top_flange_L_points[0][0] - top_flange_L_points[1][0]) - abs(web_T_points[0][0]-web_T_points[1][0])/2
        t_L_tf = abs(top_flange_L_points[0][1]-top_flange_L_points[2][1])
        stress_fixity_L = Top_Flange_L[5] # Stress at fixity
        psi_L_tf = max(Top_Flange_L[4],stress_fixity_L)/min(Top_Flange_L[4],stress_fixity_L)
        # Maximum compressive stress at free end or fixity
        if stress_fixity_L > Top_Flange_L[4]: # Maximum stress at free end
            element_type = 1
        else:
            element_type = 2      
        [rho_L_tf,b_L_eff_tf,b_e1_L_tf,b_e2_L_tf] = getPlateEffectiveWidth(psi_L_tf,element_type,b_L_tf,t_L_tf,fyf) 
        # Get removed portions of the flange and update points
        if rho_L_tf < 1.0:
            if psi_L_tf > 0:
                b_removed = max(b_L_tf - b_L_eff_tf,0)
            else:
                b_c = b_L_tf/(1-psi_L_tf)
                b_removed = max(b_c - b_L_eff_tf,0)
            top_flange_L_points[0] = list(top_flange_L_points[0])
            top_flange_L_points[0][0] = top_flange_L_points[0][0] + b_removed
            top_flange_L_points[3] = list(top_flange_L_points[3])
            top_flange_L_points[3][0] = top_flange_L_points[3][0] + b_removed
            top_flange_L_points[0] = tuple(top_flange_L_points[0])
            top_flange_L_points[3] = tuple(top_flange_L_points[3]) 
        
        # Top flange R effective width
        b_R_tf = abs(top_flange_R_points[0][0] - top_flange_R_points[1][0]) - abs(web_T_points[0][0]-web_T_points[1][0])/2
        t_R_tf = abs(top_flange_R_points[0][1]-top_flange_R_points[2][1])
        stress_fixity_R = Top_Flange_R[4] # Stress at fixity
        psi_R_tf = max(Top_Flange_R[5],stress_fixity_R)/min(Top_Flange_R[5],stress_fixity_R)
        
        # Maximum compressive stress at free end or fixity
        if stress_fixity_R > Top_Flange_R[5]: # Maximum stress at free end
            element_type = 1
        else:
            element_type = 2      
        [rho_R_tf,b_R_eff_tf,b_e1_R_tf,b_e2_R_tf] = getPlateEffectiveWidth(psi_R_tf,element_type,b_R_tf,t_R_tf,fyf) 
        # Get removed portions of the flange and update points
        if rho_R_tf < 1.0:
            if psi_R_tf > 0:
                b_removed = max(b_R_tf - b_R_eff_tf,0)
            else:
                b_c = b_R_tf/(1-psi_R_tf)
                b_removed = b_c - b_R_eff_tf
            top_flange_R_points[1] = list(top_flange_R_points[1])
            top_flange_R_points[1][0] = top_flange_R_points[1][0] - b_removed
            top_flange_R_points[2] = list(top_flange_R_points[2])
            top_flange_R_points[2][0] = top_flange_R_points[2][0] - b_removed
            top_flange_R_points[1] = tuple(top_flange_R_points[1])
            top_flange_R_points[2] = tuple(top_flange_R_points[2])
    #%%             
        # Bottom flange L effective width
        b_L_bf = abs(bottom_flange_L_points[0][0] - bottom_flange_L_points[1][0]) - abs(web_B_points[0][0]-web_B_points[1][0])/2
        t_L_bf = abs(bottom_flange_L_points[0][1]-bottom_flange_L_points[2][1])
        stress_fixity_L = Bottom_Flange_L[5] # Stress at fixity
        psi_L_bf = max(Bottom_Flange_L[4],stress_fixity_L)/min(Bottom_Flange_L[4],stress_fixity_L)
        # Maximum compressive stress at free end or fixity
        if stress_fixity_L > Bottom_Flange_L[4]: # Maximum stress at free end
            element_type = 1
        else:
            element_type = 2      
        [rho_L_bf,b_L_eff_bf,b_e1_L_bf,b_e2_L_bf] = getPlateEffectiveWidth(psi_L_bf,element_type,b_L_bf,t_L_bf,fyf) 
        # Get removed portions of the flange and update points
        if rho_L_bf < 1.0:
            if psi_L_bf > 0:
                b_removed = max(b_L_bf - b_L_eff_bf,0)
            else:
                b_c = b_L_bf/(1-psi_L_bf)
                b_removed = max(b_c - b_L_eff_bf,0)
            bottom_flange_L_points[0] = list(bottom_flange_L_points[0])
            bottom_flange_L_points[0][0] = bottom_flange_L_points[0][0] + b_removed
            bottom_flange_L_points[3] = list(bottom_flange_L_points[3])
            bottom_flange_L_points[3][0] = bottom_flange_L_points[3][0] + b_removed
            bottom_flange_L_points[0] = tuple(bottom_flange_L_points[0])
            bottom_flange_L_points[3] = tuple(bottom_flange_L_points[3])
            
        # Bottom flange R effective width
        b_R_bf = abs(bottom_flange_R_points[0][0] - bottom_flange_R_points[1][0]) - abs(web_B_points[0][0]-web_B_points[1][0])/2
        t_R_bf = abs(bottom_flange_R_points[0][1]-bottom_flange_R_points[2][1])
        stress_fixity_R = Bottom_Flange_R[4] # Stress at fixity
        psi_R_bf = max(Bottom_Flange_R[5],stress_fixity_R)/min(Bottom_Flange_R[5],stress_fixity_R)
        # Maximum compressive stress at free end or fixity
        if stress_fixity_R > Bottom_Flange_R[5]: # Maximum stress at free end
            element_type = 1
        else:
            element_type = 2      
        [rho_R_bf,b_R_eff_bf,b_e1_R_bf,b_e2_R_bf] = getPlateEffectiveWidth(psi_R_bf,element_type,b_R_bf,t_R_bf,fyf) 
        # Get removed portions of the flange and update points
        if rho_R_bf < 1.0:
            if psi_R_bf > 0:
                b_removed = max(b_R_bf - b_R_eff_bf,0)
            else:
                b_c = b_R_bf/(1-psi_R_bf)
                b_removed = max(b_c - b_R_eff_bf,0)
            bottom_flange_R_points[1] = list(bottom_flange_R_points[1])
            bottom_flange_R_points[1][0] = bottom_flange_R_points[1][0] - b_removed
            bottom_flange_R_points[2] = list(bottom_flange_R_points[2])
            bottom_flange_R_points[2][0] = bottom_flange_R_points[2][0] - b_removed
            bottom_flange_R_points[1] = tuple(bottom_flange_R_points[1])
            bottom_flange_R_points[2] = tuple(bottom_flange_R_points[2])
               
        # Update section with reduced flanges in compression
        top_flange_L_eff = Polygon(top_flange_L_points)
        top_flange_R_eff = Polygon(top_flange_R_points) 
        bottom_flange_L_eff = Polygon(bottom_flange_L_points)
        bottom_flange_R_eff = Polygon(bottom_flange_R_points)
        
        geom_top_flange_L = Geometry(geom=top_flange_L_eff,material=steel_flanges)
        geom_top_flange_R = Geometry(geom=top_flange_R_eff,material=steel_flanges)
        geom_web_T = I_sec_updated.geoms[2]
        geom_web_B = I_sec_updated.geoms[3]
        geom_bott_flange_L = Geometry(geom=bottom_flange_L_eff,material=steel_flanges)
        geom_bott_flange_R = Geometry(geom=bottom_flange_R_eff,material=steel_flanges)
        
        if composite == 1:
            list_geom = [geom_top_flange_L,geom_top_flange_R,geom_web_T,geom_web_B,geom_bott_flange_L,geom_bott_flange_R,slab] 
        else:
            list_geom = [geom_top_flange_L,geom_top_flange_R,geom_web_T,geom_web_B,geom_bott_flange_L,geom_bott_flange_R] 
        I_sec_updated = CompoundGeometry(geoms=list_geom+angles_geom)
        
        # Updated section normal stresses with reduced beam flanges 
        [Top_Flange_L,Top_Flange_R,Bottom_Flange_L,Bottom_Flange_R,Web_T,Web_B,Slab_Stress] = getIsectionNormalStresses(P,Mxx,Myy,I_sec_updated)
        
        # Web
        s_w_T = (Web_T[4]-Web_T[5])/(Web_T[2]-Web_T[3])*(Web_T[2]-Web_T[3]-web_bw_i[0]) + Web_T[5] # Stress in the top considered part of the web
        s_w_B = (Web_B[5]-Web_B[4])/(Web_B[3]-Web_B[2])*(Web_B[3]-Web_B[2]+web_bw_i[1]) + Web_B[4] # Stress in the bottom considered part of the web
        psi_w = max(s_w_T,s_w_B)/min(s_w_T,s_w_B)
        b_w = b_w - web_bw_i[0] - web_bw_i[1]
        [rho_w,b_eff_w,b_e1_w,b_e2_w] = getPlateEffectiveWidth(psi_w,0,b_w,t_w,fyw) 
        # Update section with reduced web in compression (get removed portions of the web)
        if rho_w < 1.0:
            if psi_w > 0:
                if Web_T[4] < Web_B[5]: # Higher compression in top region of web 
                    b_T_removed = max(b_w/2-b_e1_w,0)
                    b_B_removed = max(b_w/2-b_e2_w,0)
                else: # Higher compression in bottom region of web
                    b_T_removed = max(b_w/2-b_e2_w,0)
                    b_B_removed = max(b_w/2-b_e1_w,0)
            elif Web_T[4]<0: # Compression in top region of web only
                b_T_removed = b_w/2-b_e1_w
                b_t = b_w - b_w/(1-psi_w)
                b_B_removed = max(b_w/2 - (b_t + b_e2_w),0)
            else: # Compression in bottom region of web only
                b_B_removed = b_w/2-b_e1_w
                b_t = b_w - b_w/(1-psi_w)
                b_T_removed = max(b_w/2 - (b_t + b_e2_w),0)
            
            # Update top web portion     
            web_T_points[2] = list(web_T_points[2])
            web_T_points[3] = list(web_T_points[3])
            web_T_points[2][1] = web_center + b_T_removed
            web_T_points[3][1] = web_center + b_T_removed
            web_T_points[2] = tuple(web_T_points[2])
            web_T_points[3] = tuple(web_T_points[3])
            # Update bottom web portion 
            web_B_points[0] = list(web_B_points[0])
            web_B_points[1] = list(web_B_points[1])
            web_B_points[0][1] = web_center - b_B_removed
            web_B_points[1][1] = web_center - b_B_removed
            web_B_points[0] = tuple(web_B_points[0])
            web_B_points[1] = tuple(web_B_points[1])     
                
        # Update section with reduced web
        web_T_eff = Polygon(web_T_points)
        web_B_eff = Polygon(web_B_points)
        
        geom_top_flange_L = I_sec_updated.geoms[0]
        geom_top_flange_R = I_sec_updated.geoms[1]
        geom_web_T = Geometry(geom=web_T_eff,material=steel_web)
        geom_web_B = Geometry(geom=web_B_eff,material=steel_web)
        geom_bott_flange_L = I_sec_updated.geoms[4]
        geom_bott_flange_R = I_sec_updated.geoms[5]
        
        if composite == 1:
            list_geom = [geom_top_flange_L,geom_top_flange_R,geom_web_T,geom_web_B,geom_bott_flange_L,geom_bott_flange_R,slab] 
        else:
            list_geom = [geom_top_flange_L,geom_top_flange_R,geom_web_T,geom_web_B,geom_bott_flange_L,geom_bott_flange_R] 
        I_sec_updated = CompoundGeometry(geoms=list_geom+angles_geom)
        
        # Top and bottom stresses before updating section
        top_stress = (Top_Flange_L[4] + Top_Flange_L[5] + Top_Flange_R[4] + Top_Flange_R[5])/4
        bottom_stress = (Top_Flange_L[4] + Top_Flange_L[5] + Top_Flange_R[4] + Top_Flange_R[5])/4
        
        # Updated section normal stresses with reduced web
        [Top_Flange_L,Top_Flange_R,Bottom_Flange_L,Bottom_Flange_R,Web_T,Web_B,Slab_stress] = getIsectionNormalStresses(P,Mxx,Myy,I_sec_updated)
        
        # Break if difference in top and bottom centerline stresses is less than tolerance
        if iteration>0:
            top_stress_final = (Top_Flange_L[4] + Top_Flange_L[5] + Top_Flange_R[4] + Top_Flange_R[5])/4
            bottom_stress_final = (Top_Flange_L[4] + Top_Flange_L[5] + Top_Flange_R[4] + Top_Flange_R[5])/4
            if abs((top_stress_final - top_stress)/top_stress)*100.0 < tol and abs((bottom_stress_final - bottom_stress)/bottom_stress)*100.0 < tol :
                if iterations == 1:
                    print(str(iteration) + ' iteration required to converge to final section')
                else:
                    print(str(iteration) + ' iterations required to converge to final section')
                break     
    
    return I_sec_updated,Top_Flange_L,Top_Flange_R,Bottom_Flange_L,Bottom_Flange_R,Web_T,Web_B,Slab_stress
