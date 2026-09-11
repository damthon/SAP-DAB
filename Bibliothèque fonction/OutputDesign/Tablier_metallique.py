# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:54:21 2024

@author: hammad.eljisr
"""

from shapely import Polygon
from shapely import affinity
import math
from sectionproperties.pre import Geometry, CompoundGeometry
from sectionproperties.analysis import Section
import matplotlib.pyplot as plt



plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['text.usetex'] = False
plt.rc('mathtext',fontset='stix')

save_plots = 1

# Deck geometry
w = 5.0 # Deck width [m]
w_b = 3  # Box section width [m]
h1_b = 0.9 # Maximum depth of the box section [m]
h2_b = 0.4 # Minimum depth of the box section [m]
t_f_top = 0.03 # Flange thickness [m]
t_f_bott = 0.03 # Flange thickness [m]
t_w1 = 0.04 # Web thickness [m]
t_w2 = 0.015 # Web thickness [m]§
# Stiffeners
n_stiff = 4  # Number of stiffeners 
t_stiff = 0.015 # Stiffener thickness [m]
l_stiff = 0.15   # Stiffener height [m]


# Create section geometry
e_b = w-w_b
# Top flange
A = (0,0)
B = (-w,0)
C = (-w,-t_f_top)
D = (0,-t_f_top)
top_flange = Polygon([A,B,C,D])

# Web (max depth)
E = (-w+t_w1,-t_f_top)
F = (-w+t_w1,-h1_b)
G = (-w,-h1_b)
web_1 = Polygon([C,E,F,G])

# Bottom flange
H = (-w+t_w1,-h1_b+t_f_bott)
I = (-e_b-t_w2,-h2_b)
J = (-e_b-t_w2,-h2_b+t_f_bott)
bott_flange = Polygon([H,F,I,J])

# Web (min depth)
K = (-e_b,-h2_b+t_f_bott)
L = (-e_b,-t_f_top)
M = (-e_b-t_w2,-t_f_top)
web_2 = Polygon([J,K,L,M])

# Create top flange stiffeners
s_stiff_t = (w_b- t_w1 - t_w2)/(n_stiff+1) # Spacing
a_t = [[] for _ in range(n_stiff)]
top_flange_stiff = [[] for _ in range(n_stiff)]
geom_top_flange_stiff = [[] for _ in range(n_stiff)]
for i in range(len(a_t)):
    a_t[i].append((-e_b - t_w2 - s_stiff_t*(i+1) + t_stiff/2,-t_f_top))
    a_t[i].append((-e_b - t_w2 - s_stiff_t*(i+1) - t_stiff/2,-t_f_top))
    a_t[i].append((-e_b - t_w2 - s_stiff_t*(i+1) - t_stiff/2,-t_f_top-l_stiff))
    a_t[i].append((-e_b - t_w2 - s_stiff_t*(i+1) + t_stiff/2,-t_f_top-l_stiff))
for i in range(len(top_flange_stiff)):
    top_flange_stiff[i] = Polygon(a_t[i])

# Create bottom flange stiffeners
l_bott_flange = (((h1_b-t_f_bott)-(h2_b-t_f_bott))**2 + (w_b-t_w1-t_w2)**2)**0.5
angle_bott_flange = math.atan((h1_b-h2_b)/l_bott_flange)
s_stiff_b = l_bott_flange/(n_stiff+1) # Spacing
a_b = [[] for _ in range(n_stiff)]
bott_flange_stiff = [[] for _ in range(n_stiff)]
geom_bott_flange_stiff = [[] for _ in range(n_stiff)]
for i in range(len(a_b)):
    a_b[i].append((-e_b - t_w2 - s_stiff_b*(i+1) + t_stiff/2,-h2_b+t_f_bott))
    a_b[i].append((-e_b - t_w2 - s_stiff_b*(i+1) - t_stiff/2,-h2_b+t_f_bott))
    a_b[i].append((-e_b - t_w2 - s_stiff_b*(i+1) - t_stiff/2,-h2_b+t_f_bott+l_stiff))
    a_b[i].append((-e_b - t_w2 - s_stiff_b*(i+1) + t_stiff/2,-h2_b+t_f_bott+l_stiff))
for i in range(len(top_flange_stiff)):
    bott_flange_stiff[i] = Polygon(a_b[i])
    bott_flange_stiff[i] = affinity.rotate(bott_flange_stiff[i], angle_bott_flange, origin=(-e_b-t_w2,-h2_b+t_f_bott),use_radians=True)

# Create deck section
geom_top_flange = Geometry(geom=top_flange)
geom_web_1 = Geometry(geom=web_1)
geom_bott_flange = Geometry(geom=bott_flange)
geom_web_2 = Geometry(geom=web_2)
for i in range(n_stiff):
    geom_top_flange_stiff[i] = Geometry(geom=top_flange_stiff[i])
    geom_bott_flange_stiff[i] = Geometry(geom=bott_flange_stiff[i])
    
# List of elements
list_geom = [geom_top_flange, geom_web_1,geom_bott_flange,geom_web_2] 
for i in range(n_stiff):
    list_geom.append(geom_top_flange_stiff[i])
    list_geom.append(geom_bott_flange_stiff[i])
geom = CompoundGeometry(geoms=list_geom)
geom.plot_geometry()

# Create mesh
geom = geom.create_mesh(mesh_sizes=[0.001])

sec = Section(geometry=geom)
sec.calculate_geometric_properties()
sec.calculate_plastic_properties()
shear_center = sec.calculate_warping_properties()
sec.plot_centroids()

# Section properties
c_section = sec.get_c()
sc_section = sec.get_sc()
area_section = sec.get_area()
phi= sec.get_phi()
ixx_c = sec.get_ic()[0]
iyy_c = sec.get_ic()[1]
ixy_c = sec.get_ic()[2]
w_pl_xx = sec.get_s()[0]
w_pl_yy = sec.get_s()[1]
print('Deck width = ' + str(w) + 'm')
print('Centroid at ' + str(round(c_section[0],2)) + ' m from free edge')
print('Shear centre at ' + str(round(sc_section[0],2)) + ' m from free edge')
print('Area of the section = ' + str(round(area_section,3)) + ' m2')
print('Ixx = ' + str(round(ixx_c,3)) + ' m4')
print('Iyy = ' + str(round(iyy_c,3)) + ' m4')
print('Ixy = ' + str(round(ixy_c,3)) + ' m4')
print('W_pl,xx = ' + str(round(w_pl_xx,3)) + ' m3')
print('W_pl,yy = ' + str(round(w_pl_yy,3)) + ' m3')

# Plot Section
fig = plt.figure(facecolor='white',figsize=(10,10),tight_layout=True)
plt.axis('scaled')
plt.xlim(-w,0)
plt.ylim(-h1_b,0)
plt.plot([A[0],B[0],C[0],D[0],A[0]],[A[1],B[1],C[1],D[1],A[1]],'k',label='$\it{t}$' + ' = ' + str(t_f_top*1000)+' mm') # Top flange
plt.plot([C[0],E[0],F[0],G[0],C[0]],[C[1],E[1],F[1],G[1],C[1]],'g',label='$\it{t}$' + ' = ' + str(t_w1*1000)+' mm') # Web 1
plt.plot([H[0],F[0],I[0],J[0],H[0]],[H[1],F[1],I[1],J[1],H[1]],'r',label='$\it{t}$' + ' = ' + str(t_f_bott*1000)+' mm') # Bottom flange
plt.plot([J[0],K[0],L[0],M[0],J[0]],[J[1],K[1],L[1],M[1],J[1]],'b',label='$\it{t}$' + ' = ' + str(t_w2*1000)+' mm') # Web 2
for i in range(len(a_t)):
    plt.plot(*top_flange_stiff[i].exterior.xy,color=(0.5,0.5,0.5)) # Top flange stiffeners
for i in range(len(a_t)):
    plt.plot(*bott_flange_stiff[i].exterior.xy,color=(0.5,0.5,0.5)) # Bottom flange stiffeners
plt.scatter(c_section[0],c_section[1],s=50,color='w',edgecolor='r',marker='o',label='Centre de gravité')
plt.scatter(sc_section[0],sc_section[1],s=70,color='r', marker='+',label='Centre de torsion')
plt.legend(loc = 'upper right',fontsize=10,edgecolor = 'inherit',bbox_to_anchor=(0, 2))
if save_plots == 0:
    plt.show()
else:
    plt.savefig('Deck_section.svg')

