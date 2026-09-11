# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:02:54 2023

@author: hammad.eljisr
"""

def createMeshSAP2000(SapModel,Point_labels,Points,Element_labels,Element_connectivity,mesh_type):
    """
    This function creates an area mesh in the SAP2000 model.
    Input:
        SapModel: SAP Model object
        Point_labels: List of all point labels
        Points: List of the [x,y,z] coordinates of each corresponding point label
        Element_labels: List of all element (area/solid) labels
        Element_connectivity: List corresponding to the joint connectivity of each element (area/solid)
        mesh_type = 0 for area (surface) mesh, 1 for solid (brick) mesh
    """

    # Define all points
    p = []
    for i in range(len(Point_labels)):
        p_temp = SapModel.PointObj.AddCartesian(Points[i][0], Points[i][1], Points[i][2])
        SapModel.PointObj.ChangeName(p_temp[0],Point_labels[i])
        p.append(p_temp)
    
    # Modify order of points for solid elements
    if mesh_type == 1:
        for i in range(len(Element_connectivity)):
            temp_1 = Element_connectivity[i][2]
            temp_2  = Element_connectivity[i][6]
            Element_connectivity[i][2] = Element_connectivity[i][3]
            Element_connectivity[i][6] = Element_connectivity[i][7]
            Element_connectivity[i][3] = temp_1
            Element_connectivity[i][7] = temp_2  
            
    # Define elements
    if mesh_type == 0:
        for i in range(len(Element_labels)):
            SapModel.AreaObj.AddByPoint(len(list(dict.fromkeys(Element_connectivity[i]))), list(dict.fromkeys(Element_connectivity[i])), Element_labels[i])
    else:
        for i in range(len(Element_labels)):
            SapModel.SolidObj.AddByPoint(Element_connectivity[i], Element_labels[i])
            
    return None

    

      