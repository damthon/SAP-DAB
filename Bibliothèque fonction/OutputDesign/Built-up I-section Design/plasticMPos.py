# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 19:46:02 2026

@author: hammad.eljisr
"""

import numpy as np
from scipy.optimize import brentq

def plasticMPos(I_sec_c,fyd,fcd,N_ext,y_N,t):
    """
    This function calculates the sagging plastic moment resistance of a fully composite beam for a given axial force
    Input:
        - I_sec_c: Section geometry ('sectionproperties' library)
        - fyd: Steel design yield strength
        - fcd: Concrete design compressive strength
        - N_ext: External axial force applied to the section
        - y_N: y-coordinate of the point of application of the external axial force
        - t: Fiber thickness used for discretization
    Output:
        - M_pl_Rd_c: Sagging plastu moment resistance of the composite section
        - y_PNA: Plastic neutral axis y-coordinate
    """
    
    # Polygons and assigned material
    all_polygons = I_sec_c.geoms
    polygon = []
    for i in range(len(all_polygons)):
        polygon.append({"geom": all_polygons[i].points,"material": I_sec_c.geoms[i].material.name})

    M_pl_Rd_t = 0.0
    
    # Get all  fibers
    fibers = []
    for i in range(len(polygon)):
        if "Concrete" in polygon[i]["material"]:
            fibers = fibers + getFibers(polygon[i]["geom"], t, "concrete")
        else:
            fibers = fibers + getFibers(polygon[i]["geom"], t, "steel")
        
    # Get plastic neutral axis
    y_pna = getPNA(fibers,fyd,fcd,N_ext)
    
    if y_pna != None:
        for f in fibers:
            z = f["y"] - y_pna # Lever arm of each fiber measured from PNA
    
            if f["material"] == "steel":
                if z<0: # Below neutral axis
                    stress = fyd   # Tensile stress in the steel
                else:
                    stress = -fyd  # Compressive stress in the steel
            else: # Concrete
                if z > 0: # Above neutral axis
                    stress = -0.85*fcd # Compressive stress in the concrete
                else:
                    continue
            M_pl_Rd_t = M_pl_Rd_t + stress*f["area"]*z
        M_pl_Rd_c =  M_pl_Rd_t - N_ext*(y_N-y_pna)
    
    else:
        M_pl_Rd_c = 0
        
    return abs(M_pl_Rd_c), y_pna


def getFibers(polygon,t,material):
    """
    This function discretizes a polygon into fiber of a specified thickness
    Input:
        - polygon: List of (x, y) points 
        - t: Fiber thickness
        - material: 'steel' or 'concrete'
    
    Output:
        - fibers: List of dictionary containing the y-coordinate, the area, and the material of the fiber
    """    
    # Get y-coordinates of the polygon
    ys = [p[1] for p in polygon]
    
    y_min, y_max = min(ys), max(ys)

    fibers = []
    y = y_min # Start from bottom
    
    xs_previous = []
    while y < y_max:
        y_mid = y + t/2 # Fiber midpoint

        # Find intersections with horizontal line
        xs = []
        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)] # Wraps around first vertex

            if (y1 - y_mid)*(y2 - y_mid) <= 0 and y1 != y2:
                x = x1 + (y_mid - y1)/(y2 - y1)*(x2 - x1)
                xs.append(x)
            xs.sort()
        
        if round(len(xs)/2,0) != len(xs)/2: # Odd number meaning intersection at interface
            xs = xs_previous # Use previous xs
            
        # Assign area and material to each fiber
        for i in range(0, len(xs), 2):
            width = xs[i + 1] - xs[i]
            area = width*t
            fibers.append({
                "y": y_mid,
                "area": area,
                "material": material})
        
        y = y + t
        
        xs_previous = xs # Previous interesections with horizontal line
       
    return fibers


def getPNA(fibers,fyd,fcd,N_ext):
    """
    This function obtaines the location of the plastic neutral axis of a composite section subjected to an axial force
    Input:
        - fibers: Discretized fibers of the composite section
        - fyd: Steel design yield strength
        - fcd: Concrete design compressive strength
        - N_ext: External axial force applied to the section
    
    Output:
        - y_pna: y-coordinate of the plastic neutral axis
    """
    ys = [f["y"] for f in fibers]
    
    # Limit plastic neutral axis to section
    y_min = min(ys)
    y_max = max(ys)
    
    
    def equilibrium(y_pna):
        N = 0.0
        for f in fibers:
            if f["material"] == "steel":
                if f["y"] < y_pna: # Below neutral axis
                    stress = fyd 
                else: # Above neutral axis
                    stress = -fyd
            else:  # concrete
                if f["y"] > y_pna: # Above neutral axis
                    stress = -0.85*fcd
                else:
                    stress = 0.0  # Concrete in tension
            N = N + stress*f["area"]
            
        return N - N_ext
    
    # Axial plastic resistance
    N_pl_Rd_pos = sum(fyd*f["area"] for f in fibers if f["material"] == "steel")
    N_pl_Rd_neg = (sum(-fyd*f["area"] for f in fibers if f["material"] == "steel")
    + sum(-0.85*fcd*f["area"] for f in fibers if f["material"] == "concrete"))
    
    if N_ext > N_pl_Rd_pos :
        print(f"Axial force {N_ext} is beyond section capacity " + str(N_pl_Rd_pos))      
        y_pna = None
    elif N_ext < N_pl_Rd_neg:
        print(f"Axial force {N_ext} is beyond section capacity " +str(N_pl_Rd_neg))
        y_pna = None
    else:
        y_pna = brentq(equilibrium, y_min, y_max)    
    
    return y_pna



# fyd = 190        # MPa
# fcd = 13.6       # MPa
# t = 5.0          # mm
# N_ext = 0

# # I_sec = 0

# Mpl = plasticMPos(I_sec_c,fyd,fcd,N_ext,0,0.1)[0]

# # #print(f"PNA at y = {y_pna:.1f} mm")
# print(f"M_pl,Rd = {Mpl / 1e6:.1f} kNm")

# # M = []
# # N = list(np.linspace(-8e6,10e6,100))
# # for n in N:
# #     M.append(plasticMPos(I_sec, fyd, fcd, float(n), t)[0])
# #     #print(f"N = {N/1e6:+.1f} MN | M = {M/1e6:.1f} kNm | PNA = {y:.1f}")

