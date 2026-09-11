# -*- coding: utf-8 -*-
"""
Created on Tue Apr  22 15:56:54 2025

@author: hammad.eljisr
"""

from shapely import Polygon
from sectionproperties.pre import Geometry, CompoundGeometry, Material
import copy

def IsectionGeometry(h,b_tf,t_tf,t_w,b_bf,t_bf,E,fy,fsk,fck,gamma,composite_slab,doubler_pos,doubler_neg,additional_elements):
    """
    This function creates a built up I-section using the 'sectionproperties' library. An option for a composite section is available.
    Input:
        h: Beam depth
        b_tf: Top flange width
        t_tf: Top flange thickness
        t_w: Web thickness
        b_bf: Bottom flange width
        t_bf: Bottom flange thickness
        E: Elastic modulus of steel,concrete [Es,Ec]
        fy: Characteristic yield strength of the web and flanges [fyw,fyf]
        fsk: Characteristic yield strength of the reinforcement
        fck: Characteristic strength of concrete
        gamma: Partial safety factors  for steel, reinforcement and concrete [gamma_M0,gamma_M1,gamma_c]        
        composite_slab: 0 no slab
                        1 if sagging bending, slab coordinates measured from top flange (y) and web centerline (x), [1,(x0,y0),(x1,y1),(x2,y2)...(xn,yn)]
                        -1 if  hogging bending, reinforcement coordinates measured from top flange (y) and web centerline (x), [1,(x0,y0),(x1,y1),(x2,y2)...(xn,yn)]
                          area of equivalent reinforcement in the slab
        doubler_pos: Thickness of doubler plate on the positive bending side of the web
        doubler_neg: Thickness of doubler plate on the positive negative side of the web
        additional_elements: List of coordinates of additional elements [[(x10,y10),(x11,y11),(x12,y12)...(x1n,y1n)],[(x20,y20),(x21,y21),(x22,y22)...(x2n,y2n)]...]
    Output:
        geom: Section geometry ('sectionproperties' library)
    """
    
    # Material properties and partial safety factors
    fyw = fy[0]
    fyf = fy[1]
    Es = E[0]
    Ec = E[1]
    gamma_M0 = gamma[0]
    gamma_M1 = gamma[1]
    gamma_c = gamma[2]
    steel_flanges = Material(name="Steel_Flanges",elastic_modulus=Es,poissons_ratio=0.3,density=0,yield_strength=fyf/gamma_M0,color="red")
    steel_web = Material(name="Steel_Web",elastic_modulus=Es,poissons_ratio=0.3,density=0,yield_strength=fyw/gamma_M0,color="red")
    steel_reinforcement = Material(name="Rebars",elastic_modulus=Es,poissons_ratio=0.3,density=0,yield_strength=fsk/gamma_M1,color="blue")
    concrete_slab = Material(name="Concrete_Slab",elastic_modulus=Ec,poissons_ratio=0.2,density=0,yield_strength=0.85*fck/gamma_c,color="grey")
    
    # Top flange L
    A = (-b_tf/2,h)
    B = (0,h)
    C = (0,h-t_tf)
    D = (-b_tf/2,h-t_tf)
    top_flange_L = Polygon([A,B,C,D])
    
    # Top flange R
    M = (0,h)
    N = (b_tf/2,h)
    O = (b_tf/2,h-t_tf)
    P = (0,h-t_tf)
    top_flange_R = Polygon([M,N,O,P])
    
    # Web T
    E = (-t_w/2-doubler_neg,h-t_tf)
    F = (t_w/2+doubler_pos,h-t_tf)
    G = (t_w/2+doubler_pos,+(h-t_tf-t_bf)/2+t_bf)
    H = (-t_w/2-doubler_neg,(h-t_tf-t_bf)/2+t_bf)
    web_T = Polygon([E,F,G,H])
    
    # Web B
    Q = (-t_w/2-doubler_neg,(h-t_tf-t_bf)/2+t_bf)
    R = (t_w/2+doubler_pos,(h-t_tf-t_bf)/2+t_bf)
    S = (t_w/2+doubler_pos,t_bf)
    T = (-t_w/2-doubler_neg,t_bf)
    web_B = Polygon([Q,R,S,T])
    
    # Bottom flange L
    I = (-b_bf/2,0)
    J = (0,0)
    K = (0,t_bf)
    L = (-b_bf/2,t_bf)
    bott_flange_L = Polygon([I,J,K,L])
    
    # Bottom flange R
    U = (0,0)
    V = (b_bf/2,0)
    W = (b_bf/2,t_bf)
    X = (0,t_bf)
    bott_flange_R = Polygon([U,V,W,X])
    
    # Slab if composite section
    composite = copy.deepcopy(composite_slab)
    if composite_slab[0] != 0:
        for p in range(1,len(composite)):
            composite[p] = list(composite[p])
            composite[p][1] = composite[p][1] + h
            composite[p] = tuple(composite[p])
        slab = Polygon(composite[1:len(composite)])
    
    # Additional elements
    add_polygons = [[] for _ in range(len(additional_elements))]
    for i in range(len(additional_elements)): 
        add_polygons[i] = Polygon(additional_elements[i])
    
    # Create deck section
    geom_top_flange_L = Geometry(geom=top_flange_L,material=steel_flanges)
    geom_top_flange_R = Geometry(geom=top_flange_R,material=steel_flanges)
    geom_web_T = Geometry(geom=web_T,material=steel_web)
    geom_web_B = Geometry(geom=web_B,material=steel_web)
    geom_bott_flange_L = Geometry(geom=bott_flange_L,material=steel_flanges)
    geom_bott_flange_R = Geometry(geom=bott_flange_R,material=steel_flanges)
    if composite_slab[0] == 1:
        geom_slab = Geometry(geom=slab,material=concrete_slab)
        list_geom = [geom_top_flange_L,geom_top_flange_R,geom_web_T,geom_web_B,geom_bott_flange_L,geom_bott_flange_R,geom_slab] 
    elif composite_slab[0] == -1:
        geom_slab = Geometry(geom=slab,material=steel_reinforcement)
        list_geom = [geom_top_flange_L,geom_top_flange_R,geom_web_T,geom_web_B,geom_bott_flange_L,geom_bott_flange_R,geom_slab] 
    else:
        list_geom = [geom_top_flange_L,geom_top_flange_R,geom_web_T,geom_web_B,geom_bott_flange_L,geom_bott_flange_R] 
        
    # Additional elements
    add_geom = [[] for _ in range(len(additional_elements))]
    for i in range(len(additional_elements)): 
        add_geom[i] = Geometry(geom=add_polygons[i],material=steel_flanges)
        
    list_geom = list_geom + add_geom
    
    geom = CompoundGeometry(geoms=list_geom)
    
    return geom

