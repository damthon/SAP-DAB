# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 13:57:31 2025

@author: hammad.eljisr
"""

import numpy as np

sec = 'P_RV_Proto_1m / 20mm'

def sectionTopFlange_O(SapModel,sec):
    """
    This function shifts the beam section origin point O(0,0) to the bottom center of the top flange plates
    Input: 
        SapModel: SAP Model object 
        sec: Deck section
    """  
    # Get polygons the deck section
    polygons_sec = SapModel.PropFrame.GetSDSection(sec)[2]
    
    # Flange and web coordinates of the prototype section
    index_tf = polygons_sec.index('Top_Plates')
    top_flanges = SapModel.PropFrame.SDShape.GetPolygon(sec,SapModel.PropFrame.GetSDSection(sec)[2][index_tf])[3:5]
    x_coord_tf = top_flanges[0]
    y_coord_tf = top_flanges[1]
    
    # Sort y-coordinates of the top flange
    I = np.argsort(y_coord_tf)
    x_coord_tf = np.array(x_coord_tf)[I]
    y_coord_tf = np.array(y_coord_tf)[I]
    
    x_O = (x_coord_tf[0] + x_coord_tf[1])/2
    y_O = (y_coord_tf[0] + y_coord_tf[1])/2
    
    # Get all polygon coordinates
    x_poly = [[] for _ in range(len(polygons_sec))]
    y_poly = [[] for _ in range(len(polygons_sec))]
    for i in range(len(polygons_sec)):
        poly = SapModel.PropFrame.SDShape.GetPolygon(sec,SapModel.PropFrame.GetSDSection(sec)[2][i])[3:5]
        x_poly[i].append(poly[0])
        y_poly[i].append(poly[1])
    
    # Create new shifted polygon coordinates 
    x_poly_new = [[] for _ in range(len(polygons_sec))]
    y_poly_new = [[] for _ in range(len(polygons_sec))]
    for i in range(len(polygons_sec)):
        x_poly_new[i] = tuple(np.array(x_poly[i][0]) - x_O)
        y_poly_new[i] = tuple(np.array(y_poly[i][0]) - y_O)
    
    # Create section polygons
    for i in range(len(polygons_sec)):
        print(i)
        SapModel.PropFrame.SDShape.SetPolygon(sec,polygons_sec[i],'Acier Puddlé','Default',len(x_poly_new[i]), x_poly_new[i], 
                                                 y_poly_new[i],tuple(np.zeros(len(x_poly_new))),65280,False)
    
    return
    
def createBeamSection_CH(SapModel,proto_sec,H,tf,bf,sec_name):
    """
    This function creates the Charratières beam sections
    Input: 
        SapModel: SAP Model object 
        proto_sec: Prototype section (height = 1 m, 20 mm flanges)
        H: Section height
        tf: Section top flange thickness (of all plates)
        bf: Section bototm flange thickness (of all plates)
        sec_name: Section name

    Output: Output SD section in the SAP2000 model
    """  
    
    # Get polygons the prototype deck section
    polygons_proto_sec = SapModel.PropFrame.GetSDSection(proto_sec)[2]
    
    # Flange, web and angles coordinates of the prototype section
    index_tf = polygons_proto_sec.index('Top_Plates')
    index_bf = polygons_proto_sec.index('Bottom_Plates')
    index_web = polygons_proto_sec.index('Âme')
    index_angle_BL = polygons_proto_sec.index('L120.80.10_BL')
    index_angle_BR = polygons_proto_sec.index('L120.80.10_BR')
    index_angle_TL = polygons_proto_sec.index('L120.80.10_TL')
    index_angle_TR = polygons_proto_sec.index('L120.80.10_TR')
    index_angle_iL = polygons_proto_sec.index('L70.70.9_L')
    index_angle_iR = polygons_proto_sec.index('L70.70.9_R')
    
    top_flanges_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_tf])[3:5]
    bottom_flanges_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_bf])[3:5]
    web_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_web])[3:5]
    angle_TL_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_TL])[3:5]
    angle_TR_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_TR])[3:5]
    angle_BL_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_BL])[3:5]
    angle_BR_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_BR])[3:5]
    angle_iL_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_iL])[3:5]
    angle_iR_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_iR])[3:5]
    
    # Top flange
    x_coord_tf_proto = list(top_flanges_proto[0])
    y_coord_tf_proto = list(top_flanges_proto[1])
    x_coord_bf_proto = list(bottom_flanges_proto[0])
    y_coord_bf_proto = list(bottom_flanges_proto[1])
    x_coord_w_proto = list(web_proto[0])
    y_coord_w_proto = list(web_proto[1])
    # Angles
    x_coord_a_BL_proto = list(angle_BL_proto[0])
    y_coord_a_BL_proto = list(angle_BL_proto[1])
    x_coord_a_BR_proto = list(angle_BR_proto[0])
    y_coord_a_BR_proto = list(angle_BR_proto[1])
    x_coord_a_TL_proto = list(angle_TL_proto[0])
    y_coord_a_TL_proto = list(angle_TL_proto[1])
    x_coord_a_TR_proto = list(angle_TR_proto[0])
    y_coord_a_TR_proto = list(angle_TR_proto[1])
    # Intermediate angles
    x_coord_a_iL_proto = list(angle_iL_proto[0])
    y_coord_a_iL_proto = list(angle_iL_proto[1])
    x_coord_a_iR_proto = list(angle_iR_proto[0])
    y_coord_a_iR_proto = list(angle_iR_proto[1])
   
    # Round to the nearest 3rd digit (prototype section)
    for i in range(len(x_coord_tf_proto)):
        x_coord_tf_proto[i] = round(x_coord_tf_proto[i],3)
        y_coord_tf_proto[i] = round(y_coord_tf_proto[i],3)
    for i in range(len(x_coord_bf_proto)):
        x_coord_bf_proto[i] = round(x_coord_bf_proto[i],3)
        y_coord_bf_proto[i] = round(y_coord_bf_proto[i],3)  
    for i in range(len(x_coord_w_proto)):
        x_coord_w_proto[i] = round(x_coord_w_proto[i],3)
        y_coord_w_proto[i] = round(y_coord_w_proto[i],3)  
    for i in range(len(x_coord_a_BL_proto)):
        x_coord_a_BL_proto[i] = round(x_coord_a_BL_proto[i],3)
        y_coord_a_BL_proto[i] = round(y_coord_a_BL_proto[i],3) 
    for i in range(len(y_coord_a_BL_proto)):
        x_coord_a_BR_proto[i] = round(x_coord_a_BR_proto[i],3)
        y_coord_a_BR_proto[i] = round(y_coord_a_BR_proto[i],3) 
    for i in range(len(x_coord_a_TL_proto)):
        x_coord_a_TL_proto[i] = round(x_coord_a_TL_proto[i],3)
        y_coord_a_TL_proto[i] = round(y_coord_a_TL_proto[i],3) 
    for i in range(len(x_coord_a_TR_proto)):
        x_coord_a_TR_proto[i] = round(x_coord_a_TR_proto[i],3)
        y_coord_a_TR_proto[i] = round(y_coord_a_TR_proto[i],3) 
    for i in range(len(x_coord_a_iL_proto)):
        x_coord_a_iL_proto[i] = round(x_coord_a_iL_proto[i],3)
        y_coord_a_iL_proto[i] = round(y_coord_a_iL_proto[i],3) 
    for i in range(len(x_coord_a_iR_proto)):
        x_coord_a_iR_proto[i] = round(x_coord_a_iR_proto[i],3)
        y_coord_a_iR_proto[i] = round(y_coord_a_iR_proto[i],3) 
            
    # Modify top flange coordinates
    tf_proto = max(y_coord_tf_proto) - min(y_coord_tf_proto)
    x_coord_tf_new = x_coord_tf_proto
    y_coord_tf_new = []
    for i in range(len(y_coord_bf_proto)):
        if y_coord_tf_proto[i] == max(y_coord_tf_proto):
            y_coord_tf_new.append(y_coord_tf_proto[i] + (tf - tf_proto))
        else:
            y_coord_tf_new.append(y_coord_tf_proto[i])
    
    # Modify bottom flange coordinates
    x_coord_bf_new = x_coord_bf_proto
    y_bf_min = max(y_coord_tf_new) - H
    y_bf_max = max(y_coord_tf_new) - H + bf
    y_coord_bf_new = []
    for i in range(len(y_coord_bf_proto)):
        if y_coord_bf_proto[i] == min(y_coord_bf_proto):
            y_coord_bf_new.append(y_bf_min)
        else:
            y_coord_bf_new.append(y_bf_max)
    
    # Modify web  coordinates
    x_coord_w_new = x_coord_w_proto
    y_coord_w_new = []
    for i in range(len(y_coord_w_proto)):
        if y_coord_w_proto[i] == min(y_coord_w_proto):
            y_coord_w_new.append(max(y_coord_bf_new))
        else:
            y_coord_w_new.append(y_coord_w_proto[i])

    # Shift bottom angles
    x_coord_a_BL_new = x_coord_a_BL_proto
    x_coord_a_BR_new = x_coord_a_BR_proto
    delta_y_angle = min(y_coord_w_new) - min(y_coord_a_BL_proto)
    y_coord_a_BL_new = np.array(y_coord_a_BL_proto) + delta_y_angle
    y_coord_a_BR_new = np.array(y_coord_a_BR_proto) + delta_y_angle   

    # Round to the nearest 3rd digit (new section)
    for i in range(len(x_coord_tf_new)):
        x_coord_tf_new[i] = round(x_coord_tf_new[i],3)
        y_coord_tf_new[i] = round(y_coord_tf_new[i],3)
    for i in range(len(x_coord_bf_proto)):
        x_coord_bf_new[i] = round(x_coord_bf_new[i],3)
        y_coord_bf_new[i] = round(y_coord_bf_new[i],3)  
    for i in range(len(x_coord_w_new)):
        x_coord_w_new[i] = round(x_coord_w_new[i],3)
        y_coord_w_new[i] = round(y_coord_w_new[i],3)  
    for i in range(len(x_coord_a_BL_new)):
        x_coord_a_BL_new[i] = round(x_coord_a_BL_new[i],3)
        y_coord_a_BL_new[i] = round(y_coord_a_BL_new[i],3) 
    for i in range(len(y_coord_a_BL_new)):
        x_coord_a_BR_new[i] = round(x_coord_a_BR_new[i],3)
        y_coord_a_BR_new[i] = round(y_coord_a_BR_new[i],3)

    # Create section
    SapModel.PropFrame.SetSDSection(sec_name,'Acier Puddlé',0,255)
    # Top flange
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'Top_Plates','Acier Puddlé','Default',len(x_coord_tf_new),tuple(x_coord_tf_new),
                                                 tuple(y_coord_tf_new),tuple(np.zeros(len(x_coord_tf_new))),65280,False)
    # Bottom flange
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'Bottom_Plates','Acier Puddlé','Default',len(x_coord_bf_new),tuple(x_coord_bf_new),
                                                 tuple(y_coord_bf_new),tuple(np.zeros(len(x_coord_bf_new))),65280,False)
    # Web 
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'Âme','Acier Puddlé','Default',len(x_coord_w_new),tuple(x_coord_w_new),
                                                 tuple(y_coord_w_new),tuple(np.zeros(len(x_coord_w_new))),65280,False)
    # Top angles
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L120.80.10_TL','Acier Puddlé','Default',len(x_coord_a_TL_proto),tuple(x_coord_a_TL_proto),
                                                 tuple(y_coord_a_TL_proto),tuple(np.zeros(len(x_coord_a_TL_proto))),65280,False)
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L120.80.10_TR','Acier Puddlé','Default',len(x_coord_a_TR_proto),tuple(x_coord_a_TR_proto),
                                                 tuple(y_coord_a_TR_proto),tuple(np.zeros(len(x_coord_a_TR_proto))),65280,False)
    # Bottom angles
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L120.80.10_BL','Acier Puddlé','Default',len(x_coord_a_BL_new),tuple(x_coord_a_BL_new),
                                                 tuple(y_coord_a_BL_new),tuple(np.zeros(len(x_coord_a_BL_new))),65280,False)
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L120.80.10_BR','Acier Puddlé','Default',len(x_coord_a_BR_new),tuple(x_coord_a_BR_new),
                                                 tuple(y_coord_a_BR_new),tuple(np.zeros(len(x_coord_a_BR_new))),65280,False)
    # Intermediate angles
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L70.70.9_L','Acier Puddlé','Default',len(x_coord_a_iL_proto),tuple(x_coord_a_iL_proto),
                                                 tuple(y_coord_a_iL_proto),tuple(np.zeros(len(x_coord_a_iL_proto))),65280,False)
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L70.70.9_R','Acier Puddlé','Default',len(x_coord_a_iR_proto),tuple(x_coord_a_iR_proto),
                                                 tuple(y_coord_a_iR_proto),tuple(np.zeros(len(x_coord_a_iR_proto))),65280,False)
    return 

def createBeamSection_RV(SapModel,proto_sec,H,tf,bf,sec_name):
    """
    This function creates the Rive beam sections
    Input: 
        SapModel: SAP Model object 
        proto_sec: Prototype section (height = 1 m, 20 mm flanges)
        H: Section height
        tf: Section top flange thickness (of all plates)
        bf: Section bottom flange thickness (of all plates)
        sec_name: Section name

    Output: Output SD section in the SAP2000 model
    """  
    
    # Get polygons the prototype deck section
    polygons_proto_sec = SapModel.PropFrame.GetSDSection(proto_sec)[2]
    
    # Flange, web and angles coordinates of the prototype section
    index_tf = polygons_proto_sec.index('Top_Plates')
    index_bf = polygons_proto_sec.index('Bottom_Plates')
    index_web = polygons_proto_sec.index('Âme')
    index_angle_BL = polygons_proto_sec.index('L120.80.10_BL')
    index_angle_BR = polygons_proto_sec.index('L120.80.10_BR')
    index_angle_TL = polygons_proto_sec.index('L120.80.10_TL')
    #index_angle_TR = polygons_proto_sec.index('L120.80.10_TR')
    index_angle_iL = polygons_proto_sec.index('L70.70.9_L')
    #index_angle_iR = polygons_proto_sec.index('L70.70.9_R')
    index_angle_e = polygons_proto_sec.index('L80.80.10')
    
    top_flanges_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_tf])[3:5]
    bottom_flanges_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_bf])[3:5]
    web_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_web])[3:5]
    angle_TL_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_TL])[3:5]
    #angle_TR_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_TR])[3:5]
    angle_BL_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_BL])[3:5]
    angle_BR_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_BR])[3:5]
    angle_iL_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_iL])[3:5]
    #angle_iR_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_iR])[3:5]
    angle_e_proto = SapModel.PropFrame.SDShape.GetPolygon(proto_sec,SapModel.PropFrame.GetSDSection(proto_sec)[2][index_angle_e])[3:5]
    
    # Top flange
    x_coord_tf_proto = list(top_flanges_proto[0])
    y_coord_tf_proto = list(top_flanges_proto[1])
    x_coord_bf_proto = list(bottom_flanges_proto[0])
    y_coord_bf_proto = list(bottom_flanges_proto[1])
    x_coord_w_proto = list(web_proto[0])
    y_coord_w_proto = list(web_proto[1])
    # Angles
    x_coord_a_BL_proto = list(angle_BL_proto[0])
    y_coord_a_BL_proto = list(angle_BL_proto[1])
    x_coord_a_BR_proto = list(angle_BR_proto[0])
    y_coord_a_BR_proto = list(angle_BR_proto[1])
    x_coord_a_TL_proto = list(angle_TL_proto[0])
    y_coord_a_TL_proto = list(angle_TL_proto[1])
    #x_coord_a_TR_proto = list(angle_TR_proto[0])
    #y_coord_a_TR_proto = list(angle_TR_proto[1])
    # Intermediate angles
    x_coord_a_iL_proto = list(angle_iL_proto[0])
    y_coord_a_iL_proto = list(angle_iL_proto[1])
    #x_coord_a_iR_proto = list(angle_iR_proto[0])
    #y_coord_a_iR_proto = list(angle_iR_proto[1])
    # Extra edge beam angle
    x_coord_a_e_proto = list(angle_e_proto[0])
    y_coord_a_e_proto = list(angle_e_proto[1])
    
    # Round to the nearest 3rd digit (prototype section)
    for i in range(len(x_coord_tf_proto)):
        x_coord_tf_proto[i] = round(x_coord_tf_proto[i],3)
        y_coord_tf_proto[i] = round(y_coord_tf_proto[i],3)
    for i in range(len(x_coord_bf_proto)):
        x_coord_bf_proto[i] = round(x_coord_bf_proto[i],3)
        y_coord_bf_proto[i] = round(y_coord_bf_proto[i],3)  
    for i in range(len(x_coord_w_proto)):
        x_coord_w_proto[i] = round(x_coord_w_proto[i],3)
        y_coord_w_proto[i] = round(y_coord_w_proto[i],3)  
    for i in range(len(x_coord_a_BL_proto)):
        x_coord_a_BL_proto[i] = round(x_coord_a_BL_proto[i],3)
        y_coord_a_BL_proto[i] = round(y_coord_a_BL_proto[i],3) 
    for i in range(len(y_coord_a_BL_proto)):
        x_coord_a_BR_proto[i] = round(x_coord_a_BR_proto[i],3)
        y_coord_a_BR_proto[i] = round(y_coord_a_BR_proto[i],3) 
    for i in range(len(x_coord_a_TL_proto)):
        x_coord_a_TL_proto[i] = round(x_coord_a_TL_proto[i],3)
        y_coord_a_TL_proto[i] = round(y_coord_a_TL_proto[i],3) 
    #for i in range(len(x_coord_a_TR_proto)):
       # x_coord_a_TR_proto[i] = round(x_coord_a_TR_proto[i],3)
        #y_coord_a_TR_proto[i] = round(y_coord_a_TR_proto[i],3) 
    for i in range(len(x_coord_a_iL_proto)):
        x_coord_a_iL_proto[i] = round(x_coord_a_iL_proto[i],3)
        y_coord_a_iL_proto[i] = round(y_coord_a_iL_proto[i],3) 
    #for i in range(len(x_coord_a_iR_proto)):
    #    x_coord_a_iR_proto[i] = round(x_coord_a_iR_proto[i],3)
    #    y_coord_a_iR_proto[i] = round(y_coord_a_iR_proto[i],3) 
    for i in range(len(x_coord_a_e_proto)):
        x_coord_a_e_proto[i] = round(x_coord_a_e_proto[i],3)
        y_coord_a_e_proto[i] = round(y_coord_a_e_proto[i],3) 
                
    # Modify top flange coordinates
    tf_proto = max(y_coord_tf_proto) - min(y_coord_tf_proto)
    x_coord_tf_new = x_coord_tf_proto
    y_coord_tf_new = []
    for i in range(len(y_coord_bf_proto)):
        if y_coord_tf_proto[i] == max(y_coord_tf_proto):
            y_coord_tf_new.append(y_coord_tf_proto[i] + (tf - tf_proto))
        else:
            y_coord_tf_new.append(y_coord_tf_proto[i])
    
    # Modify bottom flange coordinates
    x_coord_bf_new = x_coord_bf_proto
    y_bf_min = max(y_coord_tf_new) - H
    y_bf_max = max(y_coord_tf_new) - H + bf
    y_coord_bf_new = []
    for i in range(len(y_coord_bf_proto)):
        if y_coord_bf_proto[i] == min(y_coord_bf_proto):
            y_coord_bf_new.append(y_bf_min)
        else:
            y_coord_bf_new.append(y_bf_max)
    
    # Modify web  coordinates
    x_coord_w_new = x_coord_w_proto
    y_coord_w_new = []
    for i in range(len(y_coord_w_proto)):
        if y_coord_w_proto[i] == min(y_coord_w_proto):
            y_coord_w_new.append(max(y_coord_bf_new))
        else:
            y_coord_w_new.append(y_coord_w_proto[i])

    # Shift bottom angles
    x_coord_a_BL_new = x_coord_a_BL_proto
    x_coord_a_BR_new = x_coord_a_BR_proto
    delta_y_angle = min(y_coord_w_new) - min(y_coord_a_BL_proto)
    y_coord_a_BL_new = np.array(y_coord_a_BL_proto) + delta_y_angle
    y_coord_a_BR_new = np.array(y_coord_a_BR_proto) + delta_y_angle   
    # Shift extra edge  angles
    x_coord_a_e_new = x_coord_a_e_proto
    y_coord_a_e_new = np.array(y_coord_a_e_proto) + delta_y_angle
    
    # Round to the nearest 3rd digit (new section)
    for i in range(len(x_coord_tf_new)):
        x_coord_tf_new[i] = round(x_coord_tf_new[i],3)
        y_coord_tf_new[i] = round(y_coord_tf_new[i],3)
    for i in range(len(x_coord_bf_proto)):
        x_coord_bf_new[i] = round(x_coord_bf_new[i],3)
        y_coord_bf_new[i] = round(y_coord_bf_new[i],3)  
    for i in range(len(x_coord_w_new)):
        x_coord_w_new[i] = round(x_coord_w_new[i],3)
        y_coord_w_new[i] = round(y_coord_w_new[i],3)  
    for i in range(len(x_coord_a_BL_new)):
        x_coord_a_BL_new[i] = round(x_coord_a_BL_new[i],3)
        y_coord_a_BL_new[i] = round(y_coord_a_BL_new[i],3) 
    for i in range(len(y_coord_a_BL_new)):
        x_coord_a_BR_new[i] = round(x_coord_a_BR_new[i],3)
        y_coord_a_BR_new[i] = round(y_coord_a_BR_new[i],3)
    for i in range(len(y_coord_a_e_new)):
        x_coord_a_e_new[i] = round(x_coord_a_e_new[i],3)
        y_coord_a_e_new[i] = round(y_coord_a_e_new[i],3)
        
    # Create section
    SapModel.PropFrame.SetSDSection(sec_name,'Acier Puddlé',0,255)
    # Top flange
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'Top_Plates','Acier Puddlé','Default',len(x_coord_tf_new),tuple(x_coord_tf_new),
                                                 tuple(y_coord_tf_new),tuple(np.zeros(len(x_coord_tf_new))),65280,False)
    # Bottom flange
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'Bottom_Plates','Acier Puddlé','Default',len(x_coord_bf_new),tuple(x_coord_bf_new),
                                                 tuple(y_coord_bf_new),tuple(np.zeros(len(x_coord_bf_new))),65280,False)
    # Web 
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'Âme','Acier Puddlé','Default',len(x_coord_w_new),tuple(x_coord_w_new),
                                                 tuple(y_coord_w_new),tuple(np.zeros(len(x_coord_w_new))),65280,False)
    # Top angles
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L120.80.10_TL','Acier Puddlé','Default',len(x_coord_a_TL_proto),tuple(x_coord_a_TL_proto),
                                                 tuple(y_coord_a_TL_proto),tuple(np.zeros(len(x_coord_a_TL_proto))),65280,False)
    #SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L120.80.10_TR','Acier Puddlé','Default',len(x_coord_a_TR_proto),tuple(x_coord_a_TR_proto),
    #                                             tuple(y_coord_a_TR_proto),tuple(np.zeros(len(x_coord_a_TR_proto))),65280,False)
    # Bottom angles
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L120.80.10_BL','Acier Puddlé','Default',len(x_coord_a_BL_new),tuple(x_coord_a_BL_new),
                                                 tuple(y_coord_a_BL_new),tuple(np.zeros(len(x_coord_a_BL_new))),65280,False)
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L120.80.10_BR','Acier Puddlé','Default',len(x_coord_a_BR_new),tuple(x_coord_a_BR_new),
                                                 tuple(y_coord_a_BR_new),tuple(np.zeros(len(x_coord_a_BR_new))),65280,False)
    # Intermediate angles
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L70.70.9_L','Acier Puddlé','Default',len(x_coord_a_iL_proto),tuple(x_coord_a_iL_proto),
                                                 tuple(y_coord_a_iL_proto),tuple(np.zeros(len(x_coord_a_iL_proto))),65280,False)
    #SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L70.70.9_R','Acier Puddlé','Default',len(x_coord_a_iR_proto),tuple(x_coord_a_iR_proto),
    #                                             tuple(y_coord_a_iR_proto),tuple(np.zeros(len(x_coord_a_iR_proto))),65280,False)
    # Edge angle
    SapModel.PropFrame.SDShape.SetPolygon(sec_name,'L80.80.10','Acier Puddlé','Default',len(x_coord_a_e_new),tuple(x_coord_a_e_new),
                                                 tuple(y_coord_a_e_new),tuple(np.zeros(len(x_coord_a_e_new))),65280,False)
    return 

def sectionDim(SapModel,sec):
    """
    This function gets the dimensions of the main beam section
    Input: 
        SapModel: SAP Model object 
        sec: Deck beam section
    
    Output:
        h: Beam height
        b_tf: Top flange width
        t_tf: Top flange thickness
        t_w: Web thickness
        b_bf: Bottom flange width
        t_bf: Bottom flange thickness 
    """  
    
    SapModel.SetPresentUnits(9) #  N-mm unit system    
    # Get polygons the deck section
    polygons_sec = SapModel.PropFrame.GetSDSection(sec)[2]
    
    # Flange and web coordinates of the section
    # Top flange
    index_tf = polygons_sec.index('Top_Plates')
    top_flanges = SapModel.PropFrame.SDShape.GetPolygon(sec,SapModel.PropFrame.GetSDSection(sec)[2][index_tf])[3:5]
    x_coord_tf = top_flanges[0]
    y_coord_tf = top_flanges[1]
    # Bottom flange
    index_bf = polygons_sec.index('Bottom_Plates')
    bott_flanges = SapModel.PropFrame.SDShape.GetPolygon(sec,SapModel.PropFrame.GetSDSection(sec)[2][index_bf])[3:5]
    x_coord_bf = bott_flanges[0]
    y_coord_bf = bott_flanges[1]
    # Web
    index_w = polygons_sec.index('Âme')
    web = SapModel.PropFrame.SDShape.GetPolygon(sec,SapModel.PropFrame.GetSDSection(sec)[2][index_w])[3:5]
    x_coord_w = web[0]
    y_coord_w = web[1]
    
    # Get dimensions
    h = round(abs(max(y_coord_tf)-min(y_coord_bf)),1)
    b_tf = round(abs(max(x_coord_tf)-min(x_coord_tf)),1)
    t_tf = round(abs(max(y_coord_tf)-min(y_coord_tf)),1)
    t_w = round(abs(max(x_coord_w)-min(x_coord_w)),1)
    b_bf = round(abs(max(x_coord_bf)-min(x_coord_bf)),1)
    t_bf = round(abs(max(y_coord_bf)-min(y_coord_bf)),1)
    
    return h,b_tf,t_tf,t_w,b_bf,t_bf