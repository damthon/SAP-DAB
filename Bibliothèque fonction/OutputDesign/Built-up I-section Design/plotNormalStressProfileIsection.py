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

def plotNormalStressProfileIsection(P,Mxx,Myy,I_sec,fy,stress_profile,scale_font,figure_dimensions,figure_save):
    """
    This function plots the elastic normal stress profile in an I-section 
    Input:
        P: Applied axial force. Tension positive 
        Mxx: Applied strong axis bending moment. Sagging bending positive  (M3 in SAP2000)
        Myy: Applied weak axis bending moment. y-axis positive (M2 in SAP2000)
        I_sec: Initial section geometry ('sectionproperties'  library)
        fy: Characteristic yield strength of the web and flanges [fyw,fyf]
        stress_profile: Use provided stress profile instead of forces [1,[stress,y_stress]], first element 1 if stress profile to be used and 0 otherwise; second list of stress,y_stress profile
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
        fig_size = (6,6)
    if figure_dimensions[1] != 0:
        fig_width_ratio = figure_dimensions[1]
    else:
        fig_width_ratio = (1,1)
    
    # Maximum yield stress of web and flanges
    fy_max = max(fy)
        
    # Top flange coordinates
    Top_Flange_coord = [I_sec.geoms[0].points[0],I_sec.geoms[1].points[1],I_sec.geoms[1].points[2],I_sec.geoms[0].points[3]]
    x_tf, y_tf = Polygon(Top_Flange_coord).exterior.xy
    # Bottom flange coordinates
    Bottom_Flange_coord = [I_sec.geoms[4].points[0],I_sec.geoms[5].points[1],I_sec.geoms[5].points[2],I_sec.geoms[4].points[3]]
    x_bf, y_bf = Polygon(Bottom_Flange_coord).exterior.xy
    # Web top region coordinates
    Web_T_coord = I_sec.geoms[2].points
    x_wt, y_wt = Polygon(Web_T_coord).exterior.xy
    # Web bottom region coordinates
    Web_B_coord = I_sec.geoms[3].points
    x_wb, y_wb = Polygon(Web_B_coord).exterior.xy
    if y_wt[2] == y_wb[0]:
       Web = Polygon(Web_T_coord).union(Polygon(Web_B_coord))
       x_w, y_w = Web.exterior.xy
    
    # Angles
    angles_geom = I_sec.geoms[6:]
    Angles_coord = [[] for _ in range(len(angles_geom))]
    x_a = [[] for _ in range(len(angles_geom))]
    y_a = [[] for _ in range(len(angles_geom))]
    for i in range(len(angles_geom)):
        for j in range(len(angles_geom[i].points)):
            Angles_coord[i].append(angles_geom[i].points[j])
        x_a[i], y_a[i] = Polygon(Angles_coord[i]).exterior.xy
        
    # Section limits
    y_limits_sec = [min(y_bf),max(y_tf)] # y-coordinates limits
    x_limits_sec = [min(min(x_bf),min(x_tf)),max(max(x_bf),max(x_tf))] # x-coordinates limits
    
    # Get normal stresses along web centerline and corresponding centerline coordinates
    if stress_profile[0] == 1:
        s_profile = stress_profile[1][0]
        y_profile = stress_profile[1][1]
    else:
        [Top_Flange_L, Top_Flange_R, Bottom_Flange_L, Bottom_Flange_R, Web_T, Web_B, Slab_stress] = getIsectionNormalStresses(P,Mxx,Myy,I_sec)
        # y-vertical
        s_0 = (Top_Flange_L[4] + Top_Flange_L[5] + Top_Flange_R[4] + Top_Flange_R[5])/4 # Top stress
        y_0 = (Top_Flange_L[2] + Top_Flange_L[3] + Top_Flange_R[2] + Top_Flange_R[3])/4 # Top flange centerline coordinate
        s_1 = Web_T[5] # Web top region bottom stress
        y_1 = Web_T[3] # Web top region bottom coordinate
        s_2 = Web_B[4] # Web bottom region top stress
        y_2 = Web_B[2] # Web bottom region top coordinate
        s_3 = (Bottom_Flange_L[4] + Bottom_Flange_L[5] + Bottom_Flange_R[4] + Bottom_Flange_R[5])/4 # Bottom stress
        y_3 = (Bottom_Flange_L[2] + Bottom_Flange_L[3] + Bottom_Flange_R[2] + Bottom_Flange_R[3])/4 # Bottom flange centerline coordinate
        # Stress and center
        if y_1 != y_2:
            s = [s_0,s_1,s_2,s_3]
            y = [y_0,y_1,y_2,y_3]
        else:
            s = [s_0,s_1,s_3]
            y = [y_0,y_1,y_3]
        
        # Extrapolate stress profile over beam depth and add the top and bottom stresses
        f_s = interpolate.interp1d(y,s,'linear',fill_value='extrapolate')
        s_limits = f_s(y_limits_sec) # Stress at the bottom and top limits
        s.insert(0,s_limits[1])
        s.append(s_limits[0])
        y.insert(0,y_limits_sec[1])
        y.append(y_limits_sec[0])
    
    # Split profile if discontinous (e.g. if reinforcement is present)
    discontinuity = 0
    if stress_profile[0] == 1:
        for k in range(len(y_profile)-1):
            if y_profile[k+1] == y_profile[k]:
                discontinuity = 1
                y = y_profile[0:k+1] # First part
                s = s_profile[0:k+1]
                y_profile_2 = y_profile[k+1:len(y_profile)] # Second part
                s_profile_2 = s_profile[k+1:len(s_profile)]
                break
    
    # Get elastic neutral axis position and add it
    try:
        f_NA = interpolate.interp1d(s,y,'linear')
        y_NA = float(f_NA(0))
        for i in range(len(s)-1):
            if np.sign(s[i])*np.sign(s[i+1]) < 0: # Change in stress state
                i_NA = i+1
                break
        if y_NA>=y_1 or y_NA<=y_2:
            s.insert(i_NA, 0)
            y.insert(i_NA,y_NA)
    except:
        y_NA = y[0]
        print('Neutral axis not in the section')
 
    # Plot
    fig = plt.figure(facecolor='white', figsize=fig_size, tight_layout=True)
    gs = fig.add_gridspec(1,2, wspace=0,width_ratios=fig_width_ratio)
    (ax1, ax2) = gs.subplots(sharey=True,sharex=False)
    
    # Plot limits
    plt.ylim(y_limits_sec[0],y_limits_sec[1])
    ax1.set_xlim(x_limits_sec[0],x_limits_sec[1]) 
    ax2.set_xlim(-fy_max*1.5,fy_max*1.5) # +-50% fy
    # y-ticks
    if y_wt[2] != y_wb[0]:
        y_ticks_boundaries = list(set(list(y_wt)+list(y_wb)+list(y_tf)+list(y_bf)+[y_NA]))
    else:
        y_w_ticks = [y_w[0],y_w[2],y_w[3],y_w[5],y_w[6]]
        y_ticks_boundaries = list(set(list(y_w_ticks)+list(y_tf)+list(y_bf)+[y_NA]))
    plt.yticks(y_ticks_boundaries)
    # x-ticks
    ax1.set_xticks([x_limits_sec[0],0,x_limits_sec[1]])
    ax2.set_xticks([-fy_max,0,fy_max])
    # Labels
    ax1.set_xlabel('[mm]',fontsize = 16)
    ax2.set_xlabel('[MPa]',fontsize = 16)
    # Top flange
    ax1.plot(x_tf, y_tf,'-', color=(0, 0, 0), linewidth=1.0) 
    ax1.fill(x_tf,y_tf,c=(0.5,0.5,0.5),alpha=.3)
    # Bottom flange
    ax1.plot(x_bf, y_bf,'-', color=(0, 0, 0), linewidth=1.0) # Top flange
    ax1.fill(x_bf,y_bf,c=(0.5,0.5,0.5),alpha=.3)
    # Angles
    for l in range(len(x_a)):
        ax1.plot(x_a[l], y_a[l],'-', color=(1, 0, 0), linewidth=1.0) 
        ax1.fill(x_a[l],y_a[l],c=(0.5,0.0,0.0),alpha=.3) # Web
    # Discontinuity (reinforcement)
    if discontinuity == 1:
        ax1.plot(x_bf,[0,0,y_profile_2[0],y_profile_2[0],0],'-', color=(0, 0, 0), linewidth=1.0) # Top flange
        ax1.fill(x_bf,[0,0,y_profile_2[0],y_profile_2[0],0],c=(1,1,0),alpha=.3)
    # Centerline
    ax1.plot([0,0],y_limits_sec,'--', color=(0., 0., 0.), linewidth=0.75) 
    # Neutral axis
    ax1.plot(x_limits_sec,[y_NA,y_NA],'-.', color=(0., 0., 0.), linewidth=0.75) 
    if y_wt[2] != y_wb[0]: # Discontinous web
        # Web top
        ax1.plot(x_wt,y_wt, color=(0, 0, 0), linewidth=1.0)
        ax1.fill(x_wt,y_wt,c=(0.5,0.5,0.5),alpha=.3)
        # Web bottom
        ax1.plot(x_wb, y_wb, color=(0, 0, 0), linewidth=1.0)
        ax1.fill(x_wb,y_wb,c=(0.5,0.5,0.5),alpha=.3)
    else:
        # Web 
        ax1.plot(x_w, y_w, color=(0, 0, 0), linewidth=1.0)
        ax1.fill(x_w,y_w,c=(0.5,0.5,0.5),alpha=.3)
        
    # Plot stress profile
    ax2.grid(color=[0.5,0.5,0.5], linestyle=':', linewidth=0.25)
    # Split into positive and negative normal stresses
    s_pos = list(np.array(s)[np.array([sp>=0 for sp in s])])
    y_pos = list(np.array(y)[np.array([sp>=0 for sp in s])])
    s_neg = list(np.array(s)[np.array([sp<=0 for sp in s])])
    y_neg = list(np.array(y)[np.array([sp<=0 for sp in s])])
    if y_wt[2] != y_wb[0]: # Discontinous web  
        try: # Compression below NA
            try: 
                i_t = y_neg.index(y_wt[2])
            except: 
                i_t = 0 # First element
            i_b = y_neg.index(y_wb[0])
            ax2.plot(s_neg[0:i_t+1], y_neg[0:i_t+1],'-', color=(1.0, 0, 0), linewidth=1.5)
            ax2.plot([s_neg[i_t],0], [y_neg[i_t],y_neg[i_t]],'--', color=(1.0, 0, 0), linewidth=1.5)
            ax2.plot(s_neg[i_b:len(y)], y_neg[i_b:len(y)],'-', color=(1.0, 0, 0), linewidth=1.5)
            ax2.plot([s_neg[i_b],0], [y_neg[i_b],y_neg[i_b]],'--', color=(1.0, 0, 0), linewidth=1.5)
            ax2.plot(s_pos, y_pos,'-', color=(0, 0.5, 0), linewidth=1.5)
        except: # Tension below NA
            i_t = y_pos.index(y_wt[2])
            i_b = y_pos.index(y_wb[0])  
            ax2.plot(s_pos[0:i_t+1], y_pos[0:i_t+1],'-', color=(0.0, 0.5, 0), linewidth=1.5)
            ax2.plot([s_pos[i_t],0], [y_pos[i_t],y_pos[i_t]],'--', color=(0, 0.5, 0), linewidth=1.5)
            ax2.plot(s_pos[i_b:len(y)], y_pos[i_b:len(y)],'-', color=(0, 0.5, 0), linewidth=1.5)
            ax2.plot([s_pos[i_b],0], [y_pos[i_b],y_pos[i_b]],'--', color=(0, 0.5, 0), linewidth=1.5)
            ax2.plot(s_neg, y_neg,'-', color=(1.0, 0, 0), linewidth=1.5)
    else: # Continous web
        ax2.plot(s_neg, y_neg,'-', color=(1.0, 0, 0), linewidth=1.5)
        ax2.plot(s_pos, y_pos,'-', color=(0, 0.5, 0), linewidth=1.5)
    # Centerline
    ax2.plot([0,0],y_limits_sec,'--', color=(0., 0., 0.), linewidth=0.75) 
    # Neutral axis
    ax2.plot([-fy_max*1.5,fy_max*1.5],[y_NA,y_NA],'-.', color=(0., 0., 0.), linewidth=0.75) 
    
    if discontinuity == 1:
        if max(s_profile_2) < 0: # Compression in second part
            ax2.plot(s_profile_2, y_profile_2,'-', color=(1.0, 0, 0), linewidth=1.5)
        elif min(s_profile_2) > 0: # Tension in second part
            ax2.plot(s_profile_2, y_profile_2,'-', color=(0, 0.5, 0), linewidth=1.5)
        else:
            print("Current code does not account for different stress state in the second part!")
        
    # Fill Tension/Compression
    fill_zeros = np.zeros(len(s))
    if y_wt[2] != y_wb[0]: # Discontinous web
        try:
            plt.fill_betweenx(y_neg[0:i_t+1],s_neg[0:i_t+1],fill_zeros[0:i_t+1],where=s_neg[0:i_t+1]<=fill_zeros[0:i_t+1],color=(1, 0, 0),alpha=0.25) # Compression   
            plt.fill_betweenx(y_neg[i_b:len(y)],s_neg[i_b:len(y)],np.zeros(len(y_neg[i_b:len(y)])),where=s_neg[i_b:len(y)]<=np.zeros(len(y_neg[i_b:len(y)])),color=(1, 0, 0),alpha=0.25) # Compression
        except:
            plt.fill_betweenx(y_pos[0:i_t+1],s_pos[0:i_t+1],fill_zeros[0:i_t+1],where=s_pos[0:i_t+1]>=fill_zeros[0:i_t+1],color=(0, 1, 0),alpha=0.25) # Tension   
            plt.fill_betweenx(y_pos[i_b:len(y)],s_pos[i_b:len(y)],np.zeros(len(y_pos[i_b:len(y)])),where=s_pos[i_b:len(y)]>=np.zeros(len(y_pos[i_b:len(y)])),color=(0, 1, 0),alpha=0.25) # Tension 
    else: # Continous web
        try:
            plt.fill_betweenx(y,s,fill_zeros,where=s<=fill_zeros,color=(1, 0, 0),alpha=0.25) # Compression
        except:
            plt.fill_betweenx(y,s,fill_zeros,where=s>=fill_zeros,color=(0, 1, 0),alpha=0.25) # Tension
    try:
        plt.fill_betweenx(y,s,fill_zeros,where=s>=fill_zeros,color=(0, 1, 0),alpha=0.25) # Tension
    except:
        plt.fill_betweenx(y,s,fill_zeros,where=s<=fill_zeros,color=(1, 0, 0),alpha=0.25) # Compression
    
    if discontinuity == 1:
        if max(s_profile_2) < 0: # Compression in second part
            plt.fill_betweenx(y_profile_2,s_profile_2, np.zeros(len(s_profile_2)),color=(1, 0, 0),alpha=0.25) # Compression   
        elif min(s_profile_2) > 0: # Tension in second part
            plt.fill_betweenx(y_profile_2,s_profile_2, np.zeros(len(s_profile_2)),color=(0, 0.5, 0),alpha=0.25) # Tension   
        else:
            print("Current code does not account for different stress state in the second part!")
            
    # Annotate stresses
    # Point 1
    annotation_pt_0 = (s[0],y[0])
    if annotation_pt_0[0] > 0:
        ha_orient = 'left'
    else:
        ha_orient = 'right'
    ax2.annotate('%.0f' % annotation_pt_0[0], xy=annotation_pt_0, xytext=(annotation_pt_0[0]*1.1,annotation_pt_0[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
    # Point 2
    if y_wt[2] != y_wb[0]: # Discontinous web
        try:
            annotation_pt_1 = (s_neg[i_t],y_neg[i_t])
        except:
            annotation_pt_1 = (s_pos[i_t],y_pos[i_t])
        if annotation_pt_1[0] > 0:
            ha_orient = 'left'
        else:
            ha_orient = 'right'
        ax2.annotate('%.0f' % annotation_pt_1[0], xy=annotation_pt_1, xytext=(annotation_pt_1[0]*1.1,annotation_pt_1[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
    # Point 3
    if y_wt[2] != y_wb[0]:
        try:
            annotation_pt_2 = (s_neg[i_b],y_neg[i_b])
        except:
            annotation_pt_2 = (s_pos[i_b],y_pos[i_b])
        if annotation_pt_2[0] > 0:
            ha_orient = 'left'
        else:
            ha_orient = 'right'
        ax2.annotate('%.0f' % annotation_pt_2[0], xy=annotation_pt_2, xytext=(annotation_pt_2[0]*1.1,annotation_pt_2[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
    # Point 4
    annotation_pt_3 = (s[len(s)-1],y[len(s)-1])
    if annotation_pt_3[0] > 0:
        ha_orient = 'left'
    else:
        ha_orient = 'right'
    ax2.annotate('%.0f' % annotation_pt_3[0], xy=annotation_pt_3, xytext=(annotation_pt_3[0]*1.1,annotation_pt_3[1]*0.97),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
    
    if discontinuity == 1:
        # Point 5
        annotation_pt_4 = (s_profile_2[len(s_profile_2)-1],y_profile_2[len(y_profile_2)-1])
        if annotation_pt_4[0] > 0:
            ha_orient = 'left'
        else:
            ha_orient = 'right'
        ax2.annotate('%.0f' % annotation_pt_4[0], xy=annotation_pt_4, xytext=(annotation_pt_4[0]*1.1,-annotation_pt_3[1]*1.1),ha=ha_orient,fontsize=13*scale_font,color=(0, 0, 0))
        
    if save_plot == 0:
        plt.show()
    else:
        os.chdir(figure_directory)
        plt.savefig(figure_name + '.svg')  
        plt.close()  
        
    return fig
