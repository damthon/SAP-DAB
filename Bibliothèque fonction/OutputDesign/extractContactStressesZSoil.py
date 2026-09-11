# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:30:16 2023

@author: hammad.eljisr
"""

import os
import pandas as pd
import numpy as np
from scipy import interpolate

def extractContactStressesZSoil(file_directory,file_name,Parameters):
    """
    This function extracts the contact stresses from the CSV file imported from a 2D ZSoil model
    Input:
        - file_directory = Directory of folder with the CSV file
        - file_name = Name of the CSV file
        - Parameters = List containing the parameters [time,di,global_direction]
               - time: Time at which the contact stresses are extracted
               - di: Length intervals at which the contact stresses are extracted
               - global_direction: Global direction in ZSoil along which the locations are sorted (X: 0, Y: 1)
    Output (in order):
       - X: X coordinates along which the contact stresses are extracted
       - Y: Y coordinates along which the contact stresses are extracted
       - normal_stress: Normal contact stresses
       - tangent_stress: Tangent contact stresses
       
    *NOTE*: First row consist of the headers, second row of the data imported from ZSoil (contact: effective/total stresses)
    """
    
    time = Parameters[0]
    di = Parameters[1] 
    global_direction = Parameters[2] 

    # List .txt files in directory
    os.chdir(file_directory)  # Go to directory with the input file
    
    
    # Create data array (Time, X, Y, Normal stress, Tangent stress)
    df = pd.read_csv(file_name + '.csv',delimiter = ';')
    headers = df.columns.tolist()
    data_filtered = df.filter(items = [headers[0],headers[10],headers[11],headers[19],headers[20]])
    data_array = pd.DataFrame.to_numpy(data_filtered)
    
    # Get coordinates, normal stress and tangent stress
    X = []
    Y = []
    normal_stress = []
    tangent_stress = []
    for i in range(0,len(data_array)):
        if float(data_array[i][0]) == time:
            X.append(float(data_array[i][1]))
            Y.append(float(data_array[i][2]))
            normal_stress.append(float(data_array[i][3]))
            tangent_stress.append(float(data_array[i][4]))
    
    # Sort in ascending order of the specified global direction
    if global_direction == 0:
        I = np.argsort(X) # Sort indices
    else:
        I = np.argsort(Y) # Sort indices
    
    X = np.array(X)[I]
    Y = np.array(Y)[I]
    normal_stress = np.array(normal_stress)[I]
    tangent_stress = np.array(tangent_stress)[I]
    
    # Interpolate at discretized size
    if global_direction == 0:
        n_spacing = int(round((X[len(X)-1] - X[0])/di,0))
        intervals = np.linspace(X[0],X[len(X)-1],n_spacing)

        # Interpolation functions
        interp_f_Y = interpolate.interp1d(X,Y)
        interp_f_normal_stress = interpolate.interp1d(X,normal_stress)
        interp_f_tangent_stress = interpolate.interp1d(X,tangent_stress)
        
        # Get interpoolated valuzes
        X = intervals
        Y = interp_f_Y(X)
        normal_stress = interp_f_normal_stress(X)
        tangent_stress = interp_f_tangent_stress(X)
        
    else:
        n_spacing = int(round((Y[len(Y)-1] - Y[0])/di,0))
        intervals = np.linspace(Y[0],Y[len(Y)-1],n_spacing)

        # Interpolation functions
        interp_f_X = interpolate.interp1d(Y,X)
        interp_f_normal_stress = interpolate.interp1d(Y,normal_stress)
        interp_f_tangent_stress = interpolate.interp1d(Y,tangent_stress)
        
        # Get interpoolated valuzes
        Y = intervals
        X = interp_f_X(Y)
        normal_stress = interp_f_normal_stress(Y)
        tangent_stress = interp_f_tangent_stress(Y)
    
   
    return X,Y,normal_stress,tangent_stress


