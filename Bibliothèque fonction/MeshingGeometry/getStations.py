# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:48:50 2026

@author: hammad.eljisr
"""

def getStations(points_coord):
    """ This function obtains stations at points coordinates
    Input:
        - points_coord: List of centerline points coordinates of the deck [(x1,y1,z1),(x2,y2,z2)...]. Add points to ensure meshing at certain locations
    Output:
        - stations: Stations
    """ 
    stations = [0]
    for i in range(1,len(points_coord)):
        l_temp =  ((points_coord[i][0] - points_coord[i-1][0])**2  + (points_coord[i][1] - points_coord[i-1][1])**2)**0.5
        stations.append(l_temp + stations[i-1])
    
    return stations