# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 15:48:20 2025

@author: hammad.eljisr
"""

import numpy as np
import scipy

class Catenary:
    def __init__(self,parameters):
        """
        This function intializes the object of the Catenary class
        
        parameters = [h,v,L,w] -->
        h: Horizontal distance between the anchor points
        v: Vertical distance between the anchor points
        L: Length of the catenary 
        w: Applied load per unit length along the catenary
        """
        self.parameters = parameters # parameters: list [h,v,L,w] 
        
    # Get the catenary constant
    def get_a(self):
        """
        This function gets the catenary constant of the catenary object
        """
        h = self.parameters[0]
        v = self.parameters[1]
        L = self.parameters[2]
        # Objective function
        def get_a_obj(a):  # Get the catenary constant given the length
            a = a[0]
            f1 = (L**2 - v**2)**0.5/h # Left-hand side of the transcendental equation
            f2 = 2*a/h*np.sinh(h/(2*a)) # Right-hand side of the transcendental equation
            return abs(f1 - f2)
        denom = (L**2 - v**2)**0.5 - h
        if np.isclose(denom, 0) or denom < 0:
            a_0 = h / 700  # Safe small value to avoid overflow
        else:
            temp = h/((L**2 - v**2)**0.5-h)
            a_0 = h/(24)**0.5*np.sqrt(temp) # Initial estimate of a
        # Bounds: a > 0
        bounds = [(h/700, None)]  # (lower_bound, upper_bound)
        a = scipy.optimize.minimize(get_a_obj,a_0,method = 'L-BFGS-B',bounds = bounds).x[0] # Solve the transcendental equation
        
        return a
    
    def get_y(self,x):
        """
        This function outputs the y coordinate of the catenary at a given x coordinate
        
        Input:
        x: x coordinate,, vertex (lowest point) is the origin
        """
        a = self.get_a()
        
        return a*np.cosh(x/a) 
    
    def get_s(self,x): 
        """
        This function outputs the arc length of the catenary measured from the vertex at a given x coordinate 
        
        Input:
        x: x coordinate,, vertex (lowest point) is the origin
        """
        a = self.get_a()
        
        return a*np.sinh(x/a) 
    
    def get_dmax(self):
        """
        This function gets the maximum sag measured with respect the the chord connecting the two anchor points
        """
        h = self.parameters[0]
        v = self.parameters[1]
        L = self.parameters[2]  
        a = self.get_a() 
        x_H = h/2 + a*np.arctanh(v/L) # x coordinate from the vertex of the highest anchor point
        x_L = x_H - h # x coordinate from the vertex of the lowest anchor point
        y_H = self.get_y(x_H) # y coordinate from the vertex of the highest anchor point
        y_L = self.get_y(x_L) # y coordinate from the vertex of the lowest anchor point
        # Objective function
        def get_dmax_obj(x_dmax): # To find location at maximum sag
            x_dmax = x_dmax[0]
            y_dmax = self.get_y(x_dmax) # y coordinate of the catenary at maxium sag
            y_chord = np.interp(x_dmax,[x_L,x_H],[y_L,y_H]) # y coordinate of the chord at maximum sag
            d = (y_chord - y_dmax)*-1 # Sag measured from the chord (negative value)
            return d
        bounds = [(0, None)]  # (lower_bound, upper_bound)
        x_dmax = scipy.optimize.minimize(get_dmax_obj,0,method = 'L-BFGS-B',bounds = bounds).x[0] # Solve the equation
        y_dmax = self.get_y(x_dmax) 
        y_chord = np.interp(x_dmax,[x_L,x_H],[y_L,y_H])
        d_max = (y_chord - y_dmax) 
        return d_max
    
    def get_To(self):
        """
        This function gets the constant horizontal force in the catenary
        
        Input:
        w: Applied load per unit length of the cantenary
        """
        w = self.parameters[3]  
        a = self.get_a()
        T_o = w*a # Constant horizontal force
      
        return T_o
    
    def get_Tv(self,x):
        """
        This function gets the vertical force in the catenary at a given x coordinate 
        
        Input:
        x: x coordinate,, vertex (lowest point) is the origin
        w: Applied load per unit length of the cantenary
        """
        w = self.parameters[3]  
        s = self.get_s(x) # Arc length of the catenary measured from the vertex at a given x coordinate 
        T_v = w*s # Vertical force at an x coordinate
      
        return T_v
    
    def update_Catenary_To(self,T_u):
        """
        This function updates the catenary parameters (length, L) for a target constant horizontal force. The updated length L is output.
        
        Input:
        T_u: Target horizontal force
        
        Output:
        L_u: Updated length of the catenary
        """
        # Objective function
        h = self.parameters[0]
        v = self.parameters[1]
        L = self.parameters[2]  
        def update_Catenary_To_obj(L_u):
            L_u = L_u[0]
            h, v, _, w = self.parameters  # Do not mutate original catenary in the objective function
            temp_cat = Catenary([h, v, L_u, w])
            T_calc = temp_cat.get_To()
            return abs(T_calc - T_u)
        L_min = np.sqrt(h**2 + v**2)
        bounds = [(L_min, None)]  # (lower_bound, upper_bound)
        # Get new length of the catenary
        L_u = scipy.optimize.minimize(update_Catenary_To_obj,L,method = 'L-BFGS-B',bounds = bounds).x[0] # Solve the transcendental equation
        # Update catenary parameters
        self.parameters[2] = L_u
        
        return L_u
   
    def update_Catenary_dmax(self,dmax_u):
        """
        This function updates the catenary parameters (length, L) for a target maximum sag. The updated length L is output.
        
        Input:
        dmax_u: Target maximum sag measured with respect the the chord connecting the two anchor points
        
        Output:
        L_u: Updated length of the catenary
        """
        # Objective function
        h = self.parameters[0]
        v = self.parameters[1]
        L = self.parameters[2]  
        def update_Catenary_dmax_obj(L_u):
            L_u = L_u[0]
            h, v, _, w = self.parameters  # Do not mutate original catenary in the objective function
            temp_cat = Catenary([h, v, L_u, w])
            dmax_calc = temp_cat.get_dmax()
            return abs(dmax_calc - dmax_u)
        L_min = np.sqrt(h**2 + v**2)
        bounds = [(L_min, None)]  # (lower_bound, upper_bound)
        # Get new length of the catenary
        L_u = scipy.optimize.minimize(update_Catenary_dmax_obj,L,method = 'L-BFGS-B',bounds = bounds).x[0] # Solve the transcendental equation
        # Update catenary parameters
        self.parameters[2] = L_u
        
        return L_u
    