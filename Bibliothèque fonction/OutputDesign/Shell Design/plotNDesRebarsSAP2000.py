# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:20:43 2024

@author: hammad.eljisr
"""
import numpy as np
import math
import os
from plotContourValues import plotContourValues
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.cm import ScalarMappable
from getGroupPointObjSAP2000 import getGroupPointObjSAP2000

def plotNDesRebarsSAP2000(SapModel,shell_forces,NDes,ticks,lines,
                          clb_levels,clb_min,fix_contour_limits,contour_continous,
                          scale_font,figure_dimensions,figure_save):
    """
    This function converts x,y,z coordinates into X,Y,Z arrays for input in countour plots
    Input:
        - SapModel: SAP Model object
        - shell_forces: Shell design forces obtained from getShellDesignSAP2000
        - NDes: Output design forces
             0 = Design force in the top layer (1 direction)
             1 = Design force in the bottom layer (1 direction)
             2 = Design force in the top layer (2 direction)
             3 =  Design force in the bottom layer (2 direction)
        - ticks: List of lists containing additional x and y ticks [x_ticks,y_ticks]. The min and max ticks are added regardless
        - lines: Additional plotted lines, dictionary with keys corresponding to the linetype. Each key has lines corresponding to a list of tuples, last element is the color 
        e.g. {'--': [[(x0,x1),(y0,y1)],[(x2,x3),(y2,y3)],'r'],'-': [[(x4,x5),(y4,y5)],[(x6,x7),(y6,y7)],'w']} 
        - clb_levels: Contour plot levels
        - clb_min: Minimum value of the color bar
        - fix_contour_limits: Fix contour limits (e.g [0,200,328,'max']) if 'max' is added at the end maximum value is also displayed, 0 if automatically obtained
        - contour_continous: Boolean 1 for continous contours, 0 for discrete contours
        - scale_font: Font scale factor 1.0 for default font size of 14
        - figure_dimensions: tuple (length,width). If 0 is used instead of tuple use default values (6,6) for size
        - figure_save: [save_plot,figure_name,figure_directory] , save_plot = 0 or 1, figure_name = the name of the figure saved, figure_directory = directory in which the figure is saved
    
    Input:
        - fig: Output figure
    """
    
    # Font size
    plt.rcParams['font.size'] = float(14*scale_font)
    
    # Figure data
    save_plot = figure_save[0]
    figure_name = figure_save[1]
    figure_directory = figure_save[2] 
 
    # NDesign 
    eq_forces = shell_forces[NDes]
    joints = shell_forces[4]
    if max(eq_forces) == 0:
        print('Equivalent design forces = 0 kN (compressive forces)')
    else:
        # Get joint coordinates
        X_joints = []
        Y_joints = []
        for j in range(len(joints)):
            X_joints.append(SapModel.PointObj.GetCoordCartesian(joints[j])[0])
            Y_joints.append(SapModel.PointObj.GetCoordCartesian(joints[j])[1])
            
        # Figure dimensions
        if figure_dimensions != 0:
            fig_size = figure_dimensions
        else:
            ratio_fig_x = 10/abs(max(X_joints)-min(X_joints)) # Limit x to 10
            ratio_fig_y = 5/abs(max(Y_joints)-min(Y_joints)) # Limit y to 5
            ratio_fig = min(ratio_fig_x,ratio_fig_y) # Minimum ratio between the two
            fig_size = (abs(max(X_joints)-min(X_joints))*ratio_fig,abs(max(Y_joints)-min(Y_joints))*ratio_fig)
      
        # Countour plots ND11 top
        [X,Y,Z] = plotContourValues(X_joints,Y_joints,eq_forces,resolution=1000,contour_method='linear')
          
        # Maximum value of grid
        z = Z[~np.isnan(Z)]
        max_value = np.amax(z) 
        
    # Get levels
    # Top and bottom values
    if len(fix_contour_limits) > 0:
        clb_min = fix_contour_limits[0]
    if clb_min >= math.floor(max_value):
        clb_min = math.floor(max_value/1.1) # 10% lower than maximum value     
    if len(fix_contour_limits) > 0:
        if fix_contour_limits[-1] != 'max':
            clb_max = fix_contour_limits[-1]
        else:
            clb_max = math.ceil(max_value)
    if len(fix_contour_limits) > 0: 
        #plt.clim(vmin=clb_min,vmax=clb_max)
        spacing = math.floor((clb_max - clb_min)/clb_levels) # Color bar spacing
        if fix_contour_limits[-1] == 'max':
            ticks_range = list(np.sort(list(range(clb_min, fix_contour_limits[-2], spacing)) + fix_contour_limits[0:-1] + [clb_max]))
        else:
            ticks_range = list(np.sort(list(range(clb_min, fix_contour_limits[-1], spacing)) + fix_contour_limits))
        # Remove adjacent labels
        ticks_range = np.sort(list(set(ticks_range))) # Unique ticks
        ticks_range_spaced = []
        for ti in range(len(ticks_range)-1):
            if ticks_range[ti+1] - ticks_range[ti] >= spacing:
                ticks_range_spaced.append(ticks_range[ti]) 
            elif ticks_range[ti] in fix_contour_limits:
                    ticks_range_spaced.append(ticks_range[ti]) 
            elif ticks_range[ti+1] in fix_contour_limits:
                    ticks_range_spaced.append(ticks_range[ti+1]) 
        ticks_range_spaced.append(ticks_range[-1])
        levels = np.sort(list(set(ticks_range_spaced)))        
        
    # Plot contours and lines
    fig = plt.figure(facecolor='white', figsize=fig_size, tight_layout=True)
    plt.xlim(round(min(X_joints),1),round(max(X_joints),1))
    plt.ylim(round(min(Y_joints),1),round(max(Y_joints),1))
    x_ticks = [round(min(X_joints),1)] + ticks[0] + [round(max(X_joints),1)]
    y_ticks = [round(min(Y_joints),1)] + ticks[1] + [round(max(Y_joints),1)]
    plt.xticks(x_ticks,fontsize=14)
    plt.yticks(y_ticks,fontsize=14) 
    plt.box(False) # Removes the frame but keeps ticks
    my_cmap = cm.jet
    my_cmap.set_over('lightgrey') # Values exceeding max in grey
    CS = plt.contourf(X,Y,Z,levels=levels, cmap=my_cmap,alpha=1,antialiased = 'True',extend="max")
    # Add additional lines
    line_types = list(lines.keys())
    for t in line_types:
        lines_lt = lines[t]
        for l in range(len(lines_lt)-1):
            plt.plot(lines_lt[l][0],lines_lt[l][1],t,color=lines_lt[-1],linewidth=1.5)


    # Plot colorbar      
    if contour_continous == 0:
        clb = plt.colorbar(ScalarMappable(norm=CS.norm, cmap=CS.cmap),ticks=levels,boundaries=levels,ax=plt.gca())
    else:
        clb = plt.colorbar(ScalarMappable(norm=CS.norm, cmap=CS.cmap),ticks=levels,ax=plt.gca())
            
    if NDes == 0:
        clb.ax.set_title(r'$n_{R,x,sup}$' + ' [kN/m]',fontsize=14) 
    elif NDes == 1:
        clb.ax.set_title(r'$n_{R,x,inf}$' + ' [kN/m]',fontsize=14) 
    elif NDes == 2:
        clb.ax.set_title(r'$n_{R,y,sup}$' + ' [kN/m]',fontsize=14) 
    else:
        clb.ax.set_title(r'$n_{R,y,inf}$' + ' [kN/m]',fontsize=14) 
    if save_plot == 0:
        plt.show()
    else:
        os.chdir(figure_directory)
        plt.savefig(figure_name + '.svg')  
        plt.close()  
                
    return fig

def linesfromGroupSAP2000(SapModel,lines_group,sort_dir):
    """
    This function obtaines the lines to be used in the contour plot from a group of points in SAP2000
    Input:
        - SapModel: SAP Model object
        - lines_group: Group containing points 
        - sort_dir: Direction in which the points are sorted: 1 for x, 2 for y
    
    Output:
        - fig: Output figure
    """
    # Lines
    p_s = getGroupPointObjSAP2000(SapModel,lines_group) # Points for top cantilever
    # Sort increasing x
    x_s = []
    for i in range(len(p_s)):
        x_s.append(SapModel.PointObj.GetCoordCartesian(p_s[i])[0])
    I_x_s = np.argsort(x_s)
    p_s = np.array(p_s)[I_x_s]
    lines_s = [[] for _ in range(len(p_s)-1)]  # Lines for top cantilever
    for i in range(len(lines_s)):
        lines_s[i] =[(SapModel.PointObj.GetCoordCartesian(p_s[i])[0],SapModel.PointObj.GetCoordCartesian(p_s[i+1])[0]),
         (SapModel.PointObj.GetCoordCartesian(p_s[i])[1],SapModel.PointObj.GetCoordCartesian(p_s[i+1])[1])]
        
    return lines_s