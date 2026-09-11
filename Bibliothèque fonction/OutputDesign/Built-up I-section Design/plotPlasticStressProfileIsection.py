# -*- coding: utf-8 -*-
"""
Created on Wed Apr  23 15:56:54 2025

@author: hammad.eljisr
"""

import numpy as np
from scipy import interpolate
import os
from getIsectionNormalStresses import getIsectionNormalStresses
from shapely import Polygon
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = False
plt.rc('mathtext', fontset='stix')

def plotPlasticStressProfileIsection(I_sec_comp,fyd,fcd,y_pna,scale_font,figure_dimensions,figure_save):
    """
    This function plots the plastic normal stress profile in a composite I-section subjected to positive (sagging) bending
    Input:
        I_sec_comp: Initial composite section geometry ('sectionproperties'  library)
        fyd: Design yield strength
        fcd: Concrete 
        y_pna: Plastic neutral axis y-coordinate
        scale_font: Font scale factor 1.0 for default font size of 14
        figure_dimensions: [(l,w),(1,r2)], first tuple: (length,width), second tuple: (1,width ratio). If 0 is used instead of tuple use default values (6,6) for size and (1,1) for width ratio
        figure_save: [save_plot,figure_name,figure_directory] , save_plot = 0 or 1, figure_name = the name of the figure saved, figure_directory = directory in which the figure is saved

    Output:
        fig: Figure
    """
    
    # Font size
    plt.rcParams['font.size'] = float(14*scale_font)
    
    # Figure data
    save_plot = figure_save[0]
    figure_name = figure_save[1]
    figure_directory = figure_save[2] 
    
    # Figure dimensions
    if figure_dimensions[0] != 0:
        fig_size = figure_dimensions[0]
    else:
        fig_size = (21.4,6)
    if figure_dimensions[1] != 0:
        fig_width_ratio = figure_dimensions[1]
    else:
        fig_width_ratio = (1,1)
      
    # Top flange coordinates
    Top_Flange_coord = [I_sec_comp.geoms[0].points[0],I_sec_comp.geoms[1].points[1],I_sec_comp.geoms[1].points[2],I_sec_comp.geoms[0].points[3]]
    x_tf, y_tf = Polygon(Top_Flange_coord).exterior.xy
    # Bottom flange coordinates
    Bottom_Flange_coord = [I_sec_comp.geoms[4].points[0],I_sec_comp.geoms[5].points[1],I_sec_comp.geoms[5].points[2],I_sec_comp.geoms[4].points[3]]
    x_bf, y_bf = Polygon(Bottom_Flange_coord).exterior.xy
    # Web top region coordinates
    Web_T_coord = I_sec_comp.geoms[2].points
    x_wt, y_wt = Polygon(Web_T_coord).exterior.xy
    # Web bottom region coordinates
    Web_B_coord = I_sec_comp.geoms[3].points
    x_wb, y_wb = Polygon(Web_B_coord).exterior.xy
    # Slab coordinates
    Slab_coord = I_sec_comp.geoms[6].points
    x_s, y_s = Polygon(Slab_coord).exterior.xy
    if y_wt[2] == y_wb[0]:
       Web = Polygon(Web_T_coord).union(Polygon(Web_B_coord))
       x_w, y_w = Web.exterior.xy
       
    # Angles
    angles_geom = I_sec_comp.geoms[7:]
    Angles_coord = [[] for _ in range(len(angles_geom))]
    x_a = [[] for _ in range(len(angles_geom))]
    y_a = [[] for _ in range(len(angles_geom))]
    for i in range(len(angles_geom)):
        for j in range(len(angles_geom[i].points)):
            Angles_coord[i].append(angles_geom[i].points[j])
        x_a[i], y_a[i] = Polygon(Angles_coord[i]).exterior.xy
               
    # Section limits
    y_limits_sec = [min(y_bf),max(max(y_tf),max(y_s))] # y-coordinates limits
    x_limits_sec = [min(min(x_bf),min(x_tf),min(x_s)),max(max(x_bf),max(x_tf),max(x_s))] # x-coordinates limits
    
    # Get normal stresses along web centerline and corresponding polygon coordinates
    if y_pna >= max(y_tf): # Neutral axis in slab
        y_comp = [max(y_s),y_pna,y_pna,max(y_s)] # Compressed region
        s_comp = [-0.85*fcd,-0.85*fcd,0,0] # Compressive stresses
        y_ten = [min(max(y_tf),y_pna),min(y_bf),min(y_bf),min(max(y_tf),y_pna)] # Regions in tension, concrete ignored
        s_ten = [fyd,fyd,0,0] # Tensile stresse
    else: # Neutral axis in steel beam 
        y_comp = [max(y_s),max(y_tf),max(y_tf),y_pna,y_pna,max(y_s)] # Compressed regions
        s_comp = [-0.85*fcd,-0.85*fcd,-fyd,-fyd,0,0] # Compressive stresses
        y_ten = [y_pna,min(y_bf),min(y_bf),y_pna] # Regions in tension, concrete ignored
        s_ten = [fyd,fyd,0,0] # Tensile stresses
    
    # Plot
    fig = plt.figure(facecolor='white', figsize=fig_size, tight_layout=True)
    gs = fig.add_gridspec(1,2, wspace=0,width_ratios=fig_width_ratio)
    (ax1, ax2) = gs.subplots(sharey=True,sharex=False)
    # Plot limits
    plt.ylim(y_limits_sec[0],y_limits_sec[1])
    ax1.set_xlim(x_limits_sec[0],x_limits_sec[1]) 
    ax2.set_xlim(-fyd*1.5,fyd*1.5) # +-10% fyd
    # y-ticks
    y_w_ticks = [y_w[0],y_w[2],y_w[3],y_w[5],y_w[6]]
    y_ticks_boundaries = list(set(list(y_w_ticks)+list(y_tf)+list(y_bf)+[y_pna]+[max(y_s),min(y_s)]))
    plt.yticks(y_ticks_boundaries)
    # x-ticks
    ax1.set_xticks([x_limits_sec[0],0,x_limits_sec[1]])
    ax2.set_xticks([-fyd,0,fyd])
    # Labels
    ax1.set_xlabel('[mm]',fontsize = 16)
    ax2.set_xlabel('[MPa]',fontsize = 16)
    # Top flange
    ax1.plot(x_tf, y_tf,'-', color=(0, 0, 0), linewidth=1.0) 
    ax1.fill(x_tf,y_tf,c=(0.5,0.5,0.5),alpha=.3)
    # Bottom flange
    ax1.plot(x_bf, y_bf,'-', color=(0, 0, 0), linewidth=1.0) # Top flange
    ax1.fill(x_bf,y_bf,c=(0.5,0.5,0.5),alpha=.3)
    # Web
    ax1.plot(x_w, y_w,'-', color=(0, 0, 0), linewidth=1.0) 
    ax1.fill(x_w,y_w,c=(0.5,0.5,0.5),alpha=.3) # Web
    # Slab 
    ax1.plot(x_s, y_s,'-', color=(0, 0, 0), linewidth=1.0) # Top flange
    ax1.fill(x_s,y_s,c=(0.5,0.5,0.5),alpha=.7)
    # Angles
    for l in range(len(x_a)):
        ax1.plot(x_a[l], y_a[l],'-', color=(1, 0, 0), linewidth=1.0) 
        ax1.fill(x_a[l],y_a[l],c=(0.5,0.,0.),alpha=.3) # Web
    # Centerline
    ax1.plot([0,0],y_limits_sec,'--', color=(0., 0., 0.), linewidth=0.75) 
    # Neutral axis
    ax1.plot(x_limits_sec,[y_pna,y_pna],'-.', color=(0., 0., 0.), linewidth=0.75) 
  
    # Plot stress profile
    ax2.grid(color=[0.5,0.5,0.5], linestyle=':', linewidth=0.25)
        
    # Centerline
    ax2.plot([0,0],y_limits_sec,'--', color=(0., 0., 0.), linewidth=0.75) 
    # Neutral axis
    ax2.plot([-fyd*1.5,fyd*1.5],[y_pna,y_pna],'-.', color=(0., 0., 0.), linewidth=0.75) 
      
    # Fill Tension/Compression
    # Compression zone
    ax2.fill(s_comp,y_comp,c=(1,0,0),alpha=.25)
    ax2.plot(s_comp[0:-2],y_comp[0:-2],'-', color=(1., 0., 0.), linewidth=1.5)
    ax2.plot([min(s_comp),max(s_comp)],[y_pna,y_pna],'--', color=(1., 0.0, 0.), linewidth=1.5)
    
    # Tension zone
    ax2.fill(s_ten,y_ten,c=(0,1,0),alpha=.25)
    ax2.plot(s_ten[0:-2],y_ten[0:-2],'-', color=(0., 0.5, 0.), linewidth=1.5)
    ax2.plot([min(s_ten),max(s_ten)],[max(y_ten),max(y_ten)],'--', color=(0., 0.5, 0.), linewidth=1.5)
            
    # Annotate stresses
    if y_pna >= max(y_tf): # Neutral axis in slab
        # Point 1
        annotation_pt_0 = (min(s_comp),max(y_comp)/2 + min(y_comp)/2)
        ha_orient = 'right'
        ax2.annotate('%.1f' % annotation_pt_0[0], xy=annotation_pt_0, xytext=(annotation_pt_0[0]*1.1,annotation_pt_0[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
    
        # Point 2
        annotation_pt_1 = (max(s_ten),max(y_ten)/2 + min(y_ten)/2)
        ha_orient = 'left'
        ax2.annotate('%.0f' % annotation_pt_1[0], xy=annotation_pt_1, xytext=(annotation_pt_1[0]*1.0,annotation_pt_1[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
    
    else: # Neutral axis in steel beam
        y_c = np.sort(list(set(y_comp)))
        # Point 1
        annotation_pt_0 = (min(s_comp),y_c[0]/2 + y_c[1]/2)
        ha_orient = 'right'
        ax2.annotate('%.0f' % annotation_pt_0[0], xy=annotation_pt_0, xytext=(annotation_pt_0[0]*1.1,annotation_pt_0[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
        
        # Point 2
        annotation_pt_1 = (max(s_ten),max(y_ten)/2 + min(y_ten)/2)
        ha_orient = 'left'
        ax2.annotate('%.0f' % annotation_pt_1[0], xy=annotation_pt_1, xytext=(annotation_pt_1[0]*1.0,annotation_pt_1[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
        
        # Point 3
        annotation_pt_2 = (max(s_comp[0:-2]),y_c[1]/2 + y_c[2]/2)
        ha_orient = 'right'
        ax2.annotate('%.1f' % annotation_pt_2[0], xy=annotation_pt_2, xytext=(annotation_pt_2[0]*1.1,annotation_pt_2[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
        
        
    if save_plot == 0:
        plt.show()
    else:
        os.chdir(figure_directory)
        plt.savefig(figure_name + '.svg')  
        plt.close()  
        
    return fig

# r_plot = 1
# figure_dimensions = [(6*r_plot,6),(0.2,1)]

# plotNormalStressProfileIsection(I_sec_comp,fyd,fcd,y_pna,scale_font,figure_dimensions,figure_save)