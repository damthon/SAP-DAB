# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:33:14 2023

@author: hammad.eljisr
"""

import numpy as np

class Plane:
    def __init__(self,equation):
        self.equation = equation # equation: list [A,B,C,D] --> Ax + By + Cz + D = 0
        

    def getPerpPlane(vector,point):
        """
        This function gets the equation of a plane perpendicular to a vector and passing
        through a point
        Input:
            - vector: Vector to which plane is perpendicular [x_v,y_v,z_v]
            - point: Point through which plane passes [x_p,y_p,z_p]
            
        Output:
            plane: Plane
        """
    
      
        A = vector[0]
        B = vector[1]
        C = vector[2]
        D = -(vector[0]*point[0] + vector[1]*point[1] + vector[2]*point[2])
        
        plane = Plane([A,B,C,D])
    
        return plane
    
    def get3PointsPlane(point_1,point_2,point_3):
        """
        This function gets the equation of a plane passing through three non-colinear points
        
        Input:
            - point_1, point_2, point_3: Three points through which the plane passes [x_p,y_p,z_p] for each point
            
        Output:
            plane: Plane
            v_perp: Vector perpendicular to the plane passing through point_1
        """
    
        # Normalized vector
        v1 = np.array(point_1) - np.array(point_2)
        norm = np.linalg.norm(v1)
        v1 = v1/norm
        
        v2 = np.array(point_1) - np.array(point_3)
        norm = np.linalg.norm(v2)
        v2 = v2/norm
        
        v_perp = np.cross(v1,v2)
        norm = np.linalg.norm(v_perp)
        v_perp = v_perp/norm 
        
        A = v_perp[0]
        B = v_perp[1]
        C = v_perp[2]
        D = -(v_perp[0]*point_1[0] + v_perp[1]*point_1[1] + v_perp[2]*point_1[2])
        
        plane = Plane([A,B,C,D])
    
        return plane,list(v_perp)
    
    def getIntPoint(self,P1,P2):
        """
        This function gets the intersection point of the plane with 2 other planes
        Input:
            - P1, P2: Planes
            
        Output:
            point: List of the point coordinates, [] if no single point is found
        """
        # Plane coefficients
        A_0 = self.equation[0]
        B_0 = self.equation[1]
        C_0 = self.equation[2]
        D_0 = self.equation[3]
        
        # Intersection planes coefficients
        # P1
        A_1 = P1.equation[0]
        B_1 = P1.equation[1]
        C_1 = P1.equation[2]
        D_1 = P1.equation[3]
        # P2
        A_2 = P2.equation[0]
        B_2 = P2.equation[1]
        C_2 = P2.equation[2]
        D_2 = P2.equation[3]
        
        # Get intersection
        try:
            a = np.array([[A_0,B_0,C_0],[A_1,B_1,C_1],[A_2,B_2,C_2]])
            b = np.array([-D_0,-D_1,-D_2])
            point = np.linalg.solve(a, b)
        except: # If singular
            point = []
                
        return list(point)
            
