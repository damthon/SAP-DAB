# -*- coding: utf-8 -*-
"""
Created on Tue Apr  22 15:56:54 2025

@author: hammad.eljisr
"""

import copy
from sectionproperties.analysis import Section
from sectionproperties.pre import CompoundGeometry

def getplasticNeutralAxisBareIsection(P,Mxx,I_sec):
    """
    This function outputs the plastic neutral axis (PNA) of a steel I-section subject to an axial force used for cross section classification.
    If the PNA is outside the section, it is output as 0 (if below) or h_section (if above the section). If a slab is present, the axial force in the slab is
    accounted for to check the location of the PNA inside or outside the section
    Input:
        P: Applied axial force. Tension positive
        Mxx: Applied bending moment. Sagging positive
        I_sec: Section geometry ('sectionproperties'  library)
        
    Output:
        y_pl_shifted: Shifted plastic neutral axis position from the bottom flange
    """
    
    # Check if section is composite
    if len(I_sec.geoms) == 6:
        composite = 0
        I_sec_bare = copy.deepcopy(I_sec)
    else:
        composite = 1
        list_geom = [I_sec.geoms[0],I_sec.geoms[1],I_sec.geoms[2],I_sec.geoms[3],I_sec.geoms[4],I_sec.geoms[5]] 
        list_geom_bare = copy.deepcopy(list_geom)
        I_sec_bare = CompoundGeometry(geoms=list_geom_bare)
     
    # Steel material yield strength
    fyw = I_sec_bare.geoms[2].material.yield_strength
    fyf = I_sec_bare.geoms[0].material.yield_strength
    if composite == 1:
        f_slab = I_sec.geoms[6].material.yield_strength # fcd for concrete or fsd for rebars
        F_slab = I_sec.geoms[6].calculate_area()*f_slab # Force in the slab if it plastifies (concrete or rebars)
     
    # Add force contribution from the slab assuming if fully plastifies. Note that if the slab partially plastifies, the PNA is in the slab and not in the section
    if composite == 1:
        if Mxx > 0:
            P = P + F_slab
        else:
            P = P - F_slab
            
    # I-section regions
    top_flange_L = I_sec_bare.geoms[0].points # Top flange left region
    top_flange_R = I_sec_bare.geoms[1].points # Top flange right region
    web_T = I_sec_bare.geoms[2].points # Web top region
    web_B = I_sec_bare.geoms[3].points # Web bottom region
    bottom_flange_L = I_sec_bare.geoms[4].points # Bottom flange left region
    bottom_flange_R = I_sec_bare.geoms[5].points # Bottom flange right region
    
    # I_section dimensions
    # Top flange (on each side of the web)
    b_f_top_flange_L = abs((top_flange_L[0][0]-top_flange_L[1][0]))
    b_f_top_flange_R = abs((top_flange_R[0][0]-top_flange_R[1][0]))
    b_f_top_flange = b_f_top_flange_L + b_f_top_flange_R
    # Bottom flange (on each side of the web)
    b_f_bottom_flange_L = abs((bottom_flange_L[0][0]-bottom_flange_L[1][0]))
    b_f_bottom_flange_R = abs((bottom_flange_R[0][0]-bottom_flange_R[1][0]))
    b_f_bottom_flange = b_f_bottom_flange_L + b_f_bottom_flange_R
    # Web
    t_w = abs((web_T[0][0] + web_T[0][0])/2 - (web_T[1][0] + web_B[1][0])/2)
    
    # Web and flange limits
    y_limits = [0.5*(bottom_flange_R[1][1]+bottom_flange_L[1][1]),
                0.5*(bottom_flange_R[2][1]+bottom_flange_L[3][1]),
                0.5*(top_flange_R[2][1]+top_flange_L[2][1]),
                0.5*(top_flange_R[1][1]+top_flange_L[1][1])]

    # Mesh
    t_web = min(web_T[1][0]-web_T[0][0],web_B[1][0]-web_B[0][0]) # Minimum dimension (web thickness)
    sec_geom = I_sec_bare.create_mesh(mesh_sizes=[t_web**2]) # Mesh size = area of minimum dimension squared
    
    # Plastic centroid position (pure bending)
    sec = Section(geometry=sec_geom)
    sec.calculate_geometric_properties()
    sec.calculate_plastic_properties()
    y_pl = sec.get_pc()[1]
    
    # Shift in neutral axis script for sagging bending, tension in the bottom. For hogging bending the same rules apply but P is multiplied by -1
    if Mxx < 0: 
        P = P*-1
    if y_pl < y_limits[1]: # Centroid in the bottom flange
        if P > 0: # Tension axial force
            pl_bf = (y_limits[1] - y_pl)*b_f_bottom_flange*fyf*2
            if abs(P/pl_bf) < 1.0: # PNA in bottom flange
               y_pl_shift = P/(b_f_bottom_flange*fyf*2) # Shift upwards in bottom flange
            else:
               y_pl_shift = (y_limits[1]  - y_pl) + (P - pl_bf)/(t_w*fyw*2) # Shift upwards in web
               if y_pl_shift > y_limits[2] - y_pl: # Shift in top flange
                   pl_w = (y_limits[2] - y_limits[1])*t_w*fyw*2
                   y_pl_shift = min((y_limits[2] - y_pl) + (P - pl_bf - pl_w)/(b_f_top_flange*fyf*2),(y_limits[3] - y_pl))
        else: # Compression axial load
            pl_bf = (y_limits[0]-y_pl)*b_f_bottom_flange*fyf*2
            if abs(P/pl_bf) < 1.0: # PNA in bottom flange
               y_pl_shift = P/(b_f_bottom_flange*fyf*2) # Shift downwards in bottom flange
            else:
               y_pl_shift = -y_pl # PNA below section, section plastic capacity in compression reached
    elif y_pl < y_limits[2]: # Centroid in the web 
        if P > 0: # Tension axial force
            pl_w = (y_limits[2] - y_pl)*t_w*fyw*2
            if abs(P/pl_w) < 1.0: # PNA in web
               y_pl_shift = P/(t_w*fyw*2) # Shift upwards in web
            else:
               y_pl_shift = min((y_limits[2]  - y_pl) + (P - pl_w)/(b_f_top_flange*fyf*2),(y_limits[3]  - y_pl)) # Shift upwards in top flange. If capacity reaches top fiber, section plastic capacity is reached in tension
        else: # Compression axial load
            pl_w = (y_limits[1] - y_pl)*t_w*fyw*2
            if abs(P/pl_w)  < 1.0: # PNA in web
               y_pl_shift = P/(t_w*fyw*2) # Shift downwards in web
            else:
               y_pl_shift = max(-y_pl,(y_limits[1] - y_pl) + (P - pl_w)/(b_f_bottom_flange*fyf*2)) # Shift downwards in bottom flange, bottom flange if PNA below section, section capacity is reached in compression
    elif y_pl < y_limits[3]: # Centroid in the top flange
        if P > 0: # Tension axial force
            pl_tf = (y_limits[3] - y_pl)*b_f_top_flange*fyf*2
            if abs(P/pl_tf) < 1.0: # PNA in top flange
              y_pl_shift = P/(b_f_top_flange*fyf*2) # Shift upwards in bottom flange
            else:
               y_pl_shift = y_limits[3] - y_pl # PNA above section, secion plasticy capacity in tension reached
        else: # Compression axial load
            pl_tf = (y_limits[2]-y_pl)*b_f_top_flange*fyf*2
            if abs(P/pl_tf) < 1.0:
                y_pl_shift = P/(b_f_top_flange*fyf*2) # Shift downwards in top flange
            else:
                y_pl_shift = (y_limits[2]  - y_pl) + (P - pl_tf)/(t_w*fyw*2) # Shift downwards in web
                if y_pl_shift < y_limits[1] - y_pl: # Shift in bottom flange
                    pl_w = (y_limits[1] - y_limits[2])*t_w*fyw*2
                    y_pl_shift = max((y_limits[1] - y_pl) + (P - pl_tf - pl_w)/(b_f_bottom_flange*fyf*2),(y_limits[0] - y_pl))                
    
    y_pl_shifted = y_pl + y_pl_shift
                   
    return y_pl_shifted
