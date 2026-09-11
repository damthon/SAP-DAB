# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:04:08 2024

@author: hammad.eljisr
"""

import math
import numpy as np
import scipy

def parabola_vertex_form(p1, p2, p3):
    """
    This function find the vertex form y = a(x - h)^2 + k of a parabola through three points.
    Input:
        p1, p2, p3 (tuples): Three points (x, y)

    Output:
        (a, h, k): Coefficients of the vertex form
    """

    # Extract x and y values
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Solve system of equations for a, b, c in y = ax^2 + bx + c
    A = np.array([
        [x1**2, x1, 1],
        [x2**2, x2, 1],
        [x3**2, x3, 1]])
    
    B = np.array([y1, y2, y3])

    a, b, c = np.linalg.solve(A, B)

    # Convert to vertex form
    h = -b / (2 * a)
    k = a * h**2 + b * h + c

    return a, h, k

def mainCableSAP2000(SapModel,nodes_m,f_m,h_p,s_h,theta_long,theta_trans):
    """
    This function creates the main span parabola with break points at the hanger locations. If inclined pylons are used, variably inclined hangers are implemented.
    Input:
        SapModel: SAP model object
        nodes_m: Pylon nodes connecting the main span parabola
        f_m: Main span sag at midpoint
        h_p: Pylon height from deck
        s_h: Hanger spacing (closer to pylons if span is not divisible by the spacing)
        theta_long: Pylon longitudinal inclination in degrees at the start and end pylons, list [theta_s,theta_f] e.g. [0,10] if first pylon is vertical and second is inclined +10 degrees
        theta_trans: Pylon transverse inclination in degrees, corresponding to the pylon nodes
    Output:
        x, y, z: Coordinates of points at which the hangers are connected in the main cable
        x_deck: x-coordinate of the points at which the hangers are connected in the deck
        m_s_cables: Cable segments
    """     
    
    # Average pylon height
    h_p0 = 0.5*(h_p[0][0] + h_p[0][1]) # Average pylon height
    # Get coordinates of the connecting points
    x_o = []
    y_o = []
    z_o = []
    x_o.append(SapModel.PointObj.GetCoordCartesian(nodes_m[0])[0])
    x_o.append(SapModel.PointObj.GetCoordCartesian(nodes_m[1])[0])
    y_o.append(SapModel.PointObj.GetCoordCartesian(nodes_m[0])[1])
    y_o.append(SapModel.PointObj.GetCoordCartesian(nodes_m[1])[1])
    z_o.append(SapModel.PointObj.GetCoordCartesian(nodes_m[0])[2])
    z_o.append(SapModel.PointObj.GetCoordCartesian(nodes_m[1])[2])
    
    # Sort coordinates in ascending x
    I = list(np.argsort(x_o)) # Sort array
    x_o = list(np.array(x_o)[I])
    y_o = list(np.array(y_o)[I])
    z_o = list(np.array(z_o)[I])
    
    # Main span length between pylon
    l_m  = x_o[1] - x_o[0]
    l_m0 = l_m - abs(math.tan(theta_long[0]*math.pi/180)*h_p[0][0]) - abs(math.tan(theta_long[1]*math.pi/180)*h_p[0][1])
    
    # Get parabola midpoint 
    x_mid = (x_o[0] + x_o[1])/2
    z_mid = h_p0 - f_m
    
    # Parabolic equation z = a(x-xmo)^2 + k corresponds to the minimum y of the parabola
    [a,x_mo,k] = parabola_vertex_form((x_o[0],z_o[0]),(x_o[1],z_o[1]),(x_mid,z_mid))

    # Get x at break points in the deck
    s_hm = s_h # Hanger spacing in the middle
    n_shm = int((round(l_m0/s_h,0)-2)) # Number of division with s_hm spacing
    s_he = (l_m0-n_shm*s_h)/2 # Hanger spacing near the pylon (2 hangers)
    x = [x_o[0] + abs(math.tan(theta_long[0]*math.pi/180)*h_p[0][0])]
    x_deck = x
    x.append(s_he+ x[0])
    for i in range(1,n_shm+1):
        x.append(s_hm + x[i])
    x.append(x[0] + l_m0)
    
    # Get hanger inclinations at the x locations
    theta_hangers = np.interp(x,[x[0],x[len(x)-1]],theta_long)
    
    # Get x to include inclination of the hangers
    # Objective function to solve the equation
    def getx_hangers_obj(x_h):
        lhs = a*(x_h-x_mo)**2 + k # Left-hand side of the equation
        slope = np.tan((90-theta_hanger)*math.pi/180) # Slope of the hanger straight line
        rhs = slope*(x_h-x[i]) # Right-hand side of the equation
        return abs(lhs - rhs)
    x_h = []
    for i in range(len(x)):
        theta_hanger = theta_hangers[i]
        if x[i] < x_mo:
            bounds = [(x_o[0],x_mo)]
        else:
            bounds = [(x_mo,x_o[1])]
        x_h.append(scipy.optimize.minimize(getx_hangers_obj,x[i],method = 'L-BFGS-B',bounds = bounds,tol = 1e-6).x[0]) # Solve the equation 
    
    x = x_h
    
    # Coodinates at break points
    z = []
    for i in range(len(x)):
        z.append(a*(x[i]-x_mo)**2 + k)

    # Transverse coordinates in plane between pylons 
    # Parabolic equation z = a(x-xmo)^2 + k corresponds to the minimum y of the parabola
    theta_plane = (theta_trans[0] + theta_trans[1])/2 # Average inclination of the main cable plane
    y_mid = (y_o[0] + y_o[1])/2 - (h_p0 - z_mid)*math.tan(theta_plane*math.pi/180) # y-coordinate of the midpoint 
    [a_y,x_mo_y,k_y] = parabola_vertex_form((x_o[0],y_o[0]),(x_o[1],y_o[1]),(x_mid,y_mid))
    # Coodinates at break points
    y = []
    for i in range(len(x)):
        y.append(a_y*(x[i]-x_mo_y)**2 + k_y)
    #y = list(np.interp(x,x_o,y_o)) # Linear interpolation between pylons
    #y_avg = (y_o[0] + y_o[1])/2
    #y = list(y_avg - (h_p0 - np.array(z))*math.tan(theta_plane*math.pi/180))

    # Construct cable
    ms_cables = []
    for i in range(len(x)-1):
        s = SapModel.CableObj.AddByCoord(x[i],y[i],z[i],x[i+1],y[i+1],z[i+1])
        SapModel.CableObj.SetCableData(s[0], 8, 1, 0, 0, 0, 0)
        # Set cable layout
        ms_cables.append(s[0])
    
    return x, y, z, ms_cables, x_deck