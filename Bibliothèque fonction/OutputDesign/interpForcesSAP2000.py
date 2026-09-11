# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:29:33 2024

@author: hammad.eljisr
"""

from scipy import interpolate
import numpy as np

def interpForces(output_type,stations,forces,stations_interp,combine): 
    """
    This function interpolates of the output forces at specified stations
    Input:
        output_type: List containing the output type for every force (e.g. 'Min M2', 'Max M3' ...). If 1 type exists, use a list of equal values 
        stations: List of unique stations at which the forces are specified
        forces: Force to be interpolated
        stations_interp: Stations at which the forces are interpolated 
        combine: Boolean (1 or 0) to combine the interpolated forces at the specified stations
        
    Output:
        output_type_combined: Output type at the interpolated stations
        stations_combined: Stations
        forces_combined : Interpolated forces (array of lists of 1 list depending on combine boolean)
    """ 
   
    # List of unique output types
    unique_types = list(set(output_type))
    
    # Filter stations/forces based on output type
    filtered_stations = [[] for _ in range(len(unique_types))]
    filtered_forces = [[] for _ in range(len(unique_types))]
    for u in range(len(unique_types)):
        filtered_stations[u] = [stations[i] for i in range(len(stations)) if output_type[i] == unique_types[u]]
        filtered_forces[u] = [forces[i] for i in range(len(forces)) if output_type[i] == unique_types[u]]
    
    forces_interp = [[] for _ in range(len(unique_types))]
    f = [[] for _ in range(len(unique_types))]
    for u in range(len(unique_types)):
        f = interpolate.interp1d(filtered_stations[u],filtered_forces[u],bounds_error=False,kind='linear',fill_value="extrapolate") # Interpolation function, linear extrapolation if value outside range
        forces_interp[u] = f(stations_interp) # Interpolated forces
    
    # Combine forces/stations
    if combine == 1:
        forces_combined = []
        stations_combined = []
        output_type_combined = []
        for u in range(len(unique_types)):
            forces_combined = forces_combined + list(forces_interp[u])
            stations_combined = stations_combined + stations_interp
            output_type_combined = output_type_combined + [unique_types[u]]*len(stations_interp)
        # Sort stations in ascending order   
        s_indices = np.argsort(stations_combined)
        stations_combined = np.array(stations_combined)[s_indices]
        forces_combined = np.array(forces_combined)[s_indices]
        output_type_combined = np.array(output_type_combined)[s_indices]
    else:
        forces_combined = forces_interp
        stations_combined = stations_interp
        output_type_combined = output_type[0]*len(forces_combined)
        
    return  stations_combined, output_type_combined, forces_combined