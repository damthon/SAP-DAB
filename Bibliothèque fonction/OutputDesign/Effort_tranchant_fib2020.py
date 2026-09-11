# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 14:14:48 2025

@author: hammad.eljisr
"""


import os
import sys
import comtypes.client
from shapely import Polygon
import pandas
from sectionproperties.pre import Geometry
from sectionproperties.analysis import Section
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import math
from fib2020_V_Level_II import fib2020_V_Level_II
from outputTorsionalStressTSection import outputTorsionalStressTSection
from getGroupTendonObjSAP2000 import getGroupTendonObjSAP2000

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['text.usetex'] = False
plt.rc('mathtext', fontset='stix')

save_plot = 1

# """
# Link to Running Instance of SAP2000 
# """  
# #%%             
# # Set the following flag to True to attach to an existing instance of the program 
# # otherwise a new instance of the program will be started
# AttachToInstance = True

# # Full path to the model
# # Set it to the desired path of your model
# APIPath = 'D:\API_Test'

# if not os.path.exists(APIPath):
#         try:
#             os.makedirs(APIPath)
#         except OSError:
#             pass

# # Create API helper object
# helper = comtypes.client.CreateObject('SAP2000v1.Helper')
# helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)

# if AttachToInstance:
#     #Attach to a running instance of SAP2000
#     try:
#         # Get the active SapObject
#         mySapObject = helper.GetObject("CSI.SAP2000.API.SapObject") 
#     except (OSError, comtypes.COMError):
#         print("No running instance of the program found or failed to attach")
#         sys.exit(-1)

# # Create SapModel object
# SapModel = mySapObject.SapModel
#%% 

"""
Input
""" 
# T-section polygon points (DD)
A = (-6.09,-0.15)
B = (-0.64,-0.02)
C = (-0.64,-0.23)
D = (-2.56,-0.27)
E = (-3.06,-0.39)
F = (-3.1,-0.49)
G = (-3.5,-0.57)
H = (-3.5,-1.94)
I = (-3.29,-2.01)
J = (-3.29,-2.15)
K = (-3.91,-2.15)
L = (-3.91,-2.01)
M = (-3.7,-1.94)
N = (-3.7,-0.57)
O = (-4.1,-0.49)
P = (-4.1,-0.41)
Q = (-4.14,-0.41)
R = (-4.64,-0.33)
S = (-6.07,-0.36)
T = (-6.09,-0.15)
Or = (-3.6,-2.15) # Origin to be set to (0,0)
b_2 = 0.1 # Half the web width (distance from the origin to the edge of the web)
d_appuis = 2.1 # Distance from center of support at which polygon (DD) section starts (from model: conservative assumption, 2.6 m in the drawings)
h_sec = 2.05 # Section depth in m
d_pos = [2.0,2.0] # d for positive bending P1-2, P5-6 respectively
d_neg = [1.88,1.88] # d for negative bending P1-2, P5-6 respectively
bw = 0.16 # Beam width accounting for the prestressing ducts
initial_directory = os.getcwd()

# Pier x-locations
x_piers = [0,30.93,61.876,92.826,123.776,154.726,185.677,216.629]
d_ent = 0.5 # Distance from face of the entretoise to pier location (piers B, C, D, E)

# Beam reinforcement
Asw_sw = 1.81e-3 # Shear reinforcement in the beam (2 legs)
As = 6365e-6 # Main longitudinal reinforcement in the tension chord
De = 0.6 

# Effective depth calculation
# prestress_zv = 'Prestress_zv' # Prestress group for calculating the effective shear depth zv at each location
# zs = 1.92 # Depth of the centroid of the main reinforcement measured from the compression chord

# Material properties
fsk = 477000 
fck = 55000 # C55/67 
gamma_s = 1.15
gamma_c = 1.5
Es = 205e6 

# Forces directory
forces_folder = 'Output'
forces_file = 'Tablier_1_ELU Type II - ENV_V_centroid.xlsx' # Excel file name
forces_file_sheets = ['P12_DD appuis_V_R','P56_DD appuis_V_R'] # Sheet names
forces_directory = initial_directory + '\\' + forces_folder

# Output figure
figure_name = 'tau_y_avg'
output_folder = 'Shear stresses'
# Output figure directory
figure_directory = initial_directory + '\\' + output_folder

"""
Extract Vertical Shear and Torsional Forces
""" 
os.chdir(forces_directory)
file_path = forces_directory + '\\' + forces_file
table_sheets = [] # List of tables (converted to list) in each sheet
for i in range(len(forces_file_sheets)):
    df = pandas.read_excel(file_path,forces_file_sheets[i])
    headers = df.columns.tolist()
    table = df.values.tolist()
    table_sheets.append(list(map(list, zip(*table))))  


"""
Get Total Equivalent Shear, V_Eq (includes V_Ed + T_Ed) in Sections DD
""" 
i_V_Ed = headers.index('Vz [kN]')
i_T_Ed = headers.index('Tx [kNm]')
i_N_Ed = headers.index('Nx [kN]') 
i_M_Ed =  headers.index('My [kNm]')
V_Ed =  [[] for _ in range(len(table_sheets))] 
T_Ed =  [[] for _ in range(len(table_sheets))] 
N_Ed =  [[] for _ in range(len(table_sheets))] 
M_Ed =  [[] for _ in range(len(table_sheets))] 
for i in range(len(table_sheets)):
    V_Ed[i] = list(abs(np.array(table_sheets[i][i_V_Ed]))) # Absolute value of the vertical shear forces
    T_Ed[i] = list(abs(np.array(table_sheets[i][i_T_Ed]))) # Absolute value of the torsional forces
    N_Ed[i] = list(np.array(table_sheets[i][i_N_Ed])) # Normal forces
    M_Ed[i] = list(np.array(table_sheets[i][i_M_Ed])) # Moment 
    
# Section DD
Section_points = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T]

# Get weighted average of the shear stresses due to torsion
# Discretize web (10 lines from origin to edge)
x_pts = list(np.linspace(0,b_2,11))
tau_yz_avg = [[] for _ in range(len(table_sheets))]  # Intialize average shear stress due to torsion
V_T_Ed = [[] for _ in range(len(table_sheets))]  # Intialize shear force due to torsion
for i in range(len(tau_yz_avg)):
    tau_yz_avg[i] = [[] for _ in range(len(T_Ed[i]))] 
    V_T_Ed[i] = [[] for _ in range(len(T_Ed[i]))] 

# Weighted average  for T_Ed = 100 kNm
[fig,tau_yz,tau_yz_avg_100,y_points] = outputTorsionalStressTSection(Section_points,Or,x_pts,100,0,figure_name,figure_directory) # Calculate the shear stress due to torsion in the half web fot T = 100 kNm
V_T_Ed_100 = scipy.integrate.trapezoid(np.array(tau_yz_avg_100)*1000,y_points,dx=0.1)*b_2 # Calculate the shear force due to torsion in the half web fot T = 100 kNm
for i in range(len(T_Ed)):  
    for s in range(len(T_Ed[i])):
        V_T_Ed[i][s] = V_T_Ed_100*T_Ed[i][s]/100 # Calculate the shear force due to torsion in the half web
        print(str(s) + ' = ' + str(V_T_Ed[i][s]))
        
# Equivalent total shear half-web
V_Eq = [[] for _ in range(len(table_sheets))] 
for i in range(len(T_Ed)):
    for s in range(len(T_Ed[i])):
        V_Eq[i].append(abs(V_T_Ed[i][s]) + V_Ed[i][s]/2)


"""
Get zv in each section
""" 
# Tendon locations
# def calculate_zp_Ap(x,prestress_zv):
#     """
#     This functions outputs the area, Ap, and depth from compression chord, zp, of the tendons used for calculating the effective shear depth from SAP2000
#     Input:
#         - x: List of global x coordinates at which Ap and zp are calculated
#         - prestress_zv: Group of the tendons considered
#     Output:
#         - tendons_zv: Tendon labels
#         - Ap: Area of the tendon
#         - zp: Depth from the compression chord at the specified x-coordinates
#     """  
#     SapModel.SetPresentUnits(6)   # kNm units 
    
#     # Get beam tendons in the specified group
#     tendons_zv = getGroupTendonObjSAP2000(SapModel,prestress_zv)
    
#     X_zv = [[] for _ in range(len(tendons_zv))] # Intialize global x coordinate
#     y_zv = [[] for _ in range(len(tendons_zv))] # Intialize local y coordinate (from slab mid-depth, i.e. compressive chord)
#     Ap = [[] for _ in range(len(tendons_zv))] # Intialize tendon area
#     zp = [[] for _ in range(len(tendons_zv))] # Intialize tendon area
#     # Get tendon global x-coordinates and local y-coordinates
#     for  i in range(len(tendons_zv)):
#         X_zv[i] = SapModel.TendonObj.GetTendonGeometry(tendons_zv[i],3,[],[],[],"Global")[1] # Global x coordinate
#         y_zv[i] = SapModel.TendonObj.GetTendonGeometry(tendons_zv[i],3,[],[],[],"Local")[2] # Local y coordinate (from slab mid-depth, i.e. compressive chord)
    
#     # Get tendon cross-sectional area, Ap of each tendon
#     for  i in range(len(tendons_zv)):
#         tp = SapModel.TendonObj.GetProperty(tendons_zv[i])[0] # Tendon property
#         Ap[i] = SapModel.PropTendon.GetProp(tp)[2] # Tendon area in mm2
    
#     # Get tendon zp at specified global x   
#     for i in range(len(tendons_zv)):
#         for j in range(len(x)):
#             if x[j] >= X_zv[i][0] and x[j] <= X_zv[i][len(X_zv[i])-1]:
#                 zp[i].append(np.interp(x[j],X_zv[i],y_zv[i]))
#             else:
#                 zp[i].append(0)
            
#     return tendons_zv,Ap,zp


# # Calculate zv for each section
# zv = [[] for _ in range(len(table_sheets))]
# # Calculate zp and Ap for each tendon
# for i in range(len(table_sheets)):
#     stations = table_sheets[i][1]
#     tendons_zv = calculate_zp_Ap(stations,prestress_zv)[0]
#     Ap = calculate_zp_Ap(stations,prestress_zv)[1]
#     zp = calculate_zp_Ap(stations,prestress_zv)[2]

#     # zv
#     for t in range(len(tendons_zv)):
#         zp_2_Ap = 0
#         zp_Ap = 0
#         zv_s = []
#         for s in range(len(stations)):
#             zp_2_Ap = zp_2_Ap + abs(zp[t][s]**2*Ap[t])
#             zp_Ap = zp_Ap + zp[t][s]*Ap[t]
#             zv_s.append(max(((zs**2)*As + zp_2_Ap)/(zs*As + zp_Ap),0.72*h_sec))
#     zv[i] = zv_s

# Calculate as zv = 0.9d (fib MC 2020 simplification)
zv = [[] for _ in range(len(table_sheets))]
for i in range(len(table_sheets)):
    for m in range(len(M_Ed[i])):
        if M_Ed[i][m] > 0:
            zv[i].append(d_pos[i]*0.9)
        else:
            zv[i].append(d_neg[i]*0.9)
    
"""
Calculate VRd and Degrees of Compliance using Level II fib MC 2020
""" 
Materials = [[fsk,Es,'A'],fck]
Gamma = [gamma_s,gamma_c]

V_Rd = [[] for _ in range(len(V_Eq))]  # Shear resistance
theta = [[] for _ in range(len(V_Eq))] # Strut angle
Level_approx = [[] for _ in range(len(V_Eq))] # Approximation level that yields the highest resistance
degree_compliance_V = [[] for _ in range(len(V_Eq))] # Degree of compliance
for i in range(len(V_Eq)):
    V_Rd[i] = [[] for _ in range(len(V_Eq[i]))] 
    theta[i] = [[] for _ in range(len(V_Eq[i]))] 
    Level_approx[i] = [[] for _ in range(len(V_Eq[i]))] 
    degree_compliance_V[i] = [[] for _ in range(len(V_Eq[i]))] 
for i in range(len(V_Eq)):
    for s in range(len(V_Eq[i])):
        Forces = [N_Ed[i][s],M_Ed[i][s],V_Eq[i][s]*2]
        Sec_geom = [bw,zv[i][s],De,Asw_sw,As]
        [V_Rd_IIa,theta_IIa] =  fib2020_V_Level_II(Forces,Sec_geom,Materials,Gamma,'IIa',0) # Level IIa
        [V_Rd_IIb,theta_IIb] =  fib2020_V_Level_II(Forces,Sec_geom,Materials,Gamma,'IIb',0) # Level IIb
        if V_Rd_IIa > V_Rd_IIb: # Choose higher value
            V_Rd[i][s] = V_Rd_IIa
            theta[i][s] = theta_IIa
            Level_approx[i][s] = 'IIa'
        else:
            V_Rd[i][s] = V_Rd_IIb
            theta[i][s] = theta_IIb
            Level_approx[i][s] = 'IIb'
        degree_compliance_V[i][s] = V_Rd[i][s]/(V_Eq[i][s]*2)

# Remove all values within zcot(theta)
for i in range(len(V_Ed)):
    x_stations = table_sheets[i][1] 
    for s in range(len(x_stations)):
        z_cot_theta = zv[i][s]*1/math.tan(math.radians(theta[i][s]))
        closest_x_pier = min(x_piers, key=lambda x:abs(x-x_stations[s])) # x coordinate of the closest pier
        if (x_stations[s] < closest_x_pier + z_cot_theta + d_ent) and (x_stations[s] > closest_x_pier - z_cot_theta - d_ent): # Check if station is within zcot(theta) from face of closest entretoise
            degree_compliance_V[i][s] = 1e5
            V_Rd[i][s] = None
        

"""
Plot Torsional Stresses in the Critical Sections and Degrees of Compliance
""" 
# Get minimum degrees of compliance
min_degree = [[] for _ in range(len(degree_compliance_V))]  # Degree of compliance 
index_min_degree = [[] for _ in range(len(degree_compliance_V))]  # Index of the minimum degree of compliance 
for i in range(len(degree_compliance_V)):
    min_temp = 1e5
    for d in range(len(degree_compliance_V[i])):
        min_temp = min(min_temp,degree_compliance_V[i][d]) 
        if min_temp == degree_compliance_V[i][d]:
            index_min_degree[i] = d
    min_degree[i] = min_temp
    
# Plot torsional stress for the critical cases
for i in range(len(degree_compliance_V)):
    figure_name_cr = figure_name + '_' + str(table_sheets[i][1][index_min_degree[i]])
    [fig,tau_yz,tau_yz_avg_100,y_points] = outputTorsionalStressTSection(Section_points,Or,x_pts,T_Ed[i][index_min_degree[i]],save_plot,figure_name_cr,figure_directory)
    
# Plot degrees of compliance
stations_deg = []
deg_plot = []
for i in range(len(degree_compliance_V)):
    for s in range(len(table_sheets[i][1])):
        if degree_compliance_V[i][s] < 2:
            print(degree_compliance_V[i][s])
            deg_plot.append(degree_compliance_V[i][s])
            stations_deg.append(table_sheets[i][1][s])

fig = plt.figure(facecolor='white', figsize=(8,3), tight_layout=True)
plt.grid(color=[0.25,0.25,0.25], linestyle=':', linewidth=0.25)
# Plot limits
plt.xlim(0,max(stations_deg)*1.05)
plt.ylim(0.5,max(deg_plot))   
plt.ylabel(r'$\eta_V$',fontsize = 16)
plt.xlabel(r'$s$ [m]',fontsize = 16)
plt.yticks([0.5,1,1.25,1.5,2,2.5], ['',1,1.25,1.5,2,2.5])
#int_MNV_critical = np.array(int_MNV)*(np.array(int_MNV)>1.0)
plt.scatter(stations_deg,deg_plot,s=12,marker='o',linewidths=0.5,color=(1,0,0),edgecolors=(0.5,0,0))
plt.plot([0,max(stations_deg)*1.05],[1,1],'--',color=(1.0,0,0),linewidth=1)
#plt.legend(loc='upper right', fontsize=11, edgecolor='inherit')
if save_plot == 0:
    plt.show()
else:
    plt.savefig('Degree_V' + '.svg')       

