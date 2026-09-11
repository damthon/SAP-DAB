# -*- coding: utf-8 -*-
"""
Created on Tue May 02 11:30:16 2023

@author: hammad.eljisr
"""

import os

def importAnsysMesh(file_directory,input_file_name,mesh_type):
    """
    This function reads the .dat Ansys input file and imports the mesh.
    It is applicable for area (surface) and solid (brick) meshes with linear
    elements only.
    Input:
        R_directory = Directory of folder with the displacement files
        input_file_name = Name of the Ansys .dat input file
        mesh_type = 0 for area (surface) mesh, 1 for solid (brick) mesh
    Output (in order):
        nodes = List of all node numbers
        nodes_coord = List of the [x,y,z] coordinates of the corresponding node number
        elements = List of all elements (area elements) numbers
        elements_connect = List corresponding to the nodal connectivity of each element. 
        Duplicates of nodes in case of triangular (area) elements or tetrahedral (solid) elements are not removed
    """
    
    # List .txt files in directory
    os.chdir(file_directory)  # Go to directory with the input file
    
    r = open(input_file_name, 'r')
    content_list = r.readlines()
    
    """ Get all nodal coordinates """
    # Start, end locations
    start_line_nodes = len(content_list)
    for  i in range(len(content_list)):
        if content_list[i].find('Nodes for the whole assembly') !=-1: 
            start_line_nodes = i + 3 # Get starting line of all nodes
        if i > start_line_nodes and content_list[i] == '-1\n':
            end_line_nodes = i - 1 #♠ Get end line of all nodes
            break
       
    # Get nodes
    nodes = []
    nodes_coord = []
    content_list[35].split()  
    for i in range(start_line_nodes,end_line_nodes+1):
        node_temp = content_list[i].split()[0]
        node_x_coord_temp = float(content_list[i].split()[1])
        node_y_coord_temp = float(content_list[i].split()[2])
        node_z_coord_temp = float(content_list[i].split()[3])
        nodes.append(node_temp)
        nodes_coord.append([node_x_coord_temp,node_y_coord_temp,node_z_coord_temp])
    
    """ Get all elements/connectivity """ 
    # Get linear element type
    if mesh_type == 0:
        Element_type = '181'
    else:
        Element_type = '185'
    # Start locations
    start_line_elements = []   
    for  i in range(len(content_list)):
        if content_list[i].find(','+ Element_type) !=-1: 
            j = i
            while 1:
                j = j + 1
                if(content_list[j][0]) == '(':
                   start_line_elements.append(j+1)
                   break
    # End locations
    end_line_elements = []
    for i in start_line_elements:
        j = i
        while 1:
            j = j + 1
            if content_list[j] == '-1\n':
                end_line_elements.append(j-1)
                break
            
    # Get elements/connectivity
    elements = []
    elements_connect = []     
    for i in range(len(start_line_elements)):
        for j in range(start_line_elements[i],end_line_elements[i]+1):
            ele_temp = content_list[j].split()[10]
            ele_conn_1 = content_list[j].split()[11]
            ele_conn_2 = content_list[j].split()[12]
            ele_conn_3 = content_list[j].split()[13]
            ele_conn_4 = content_list[j].split()[14]
            if mesh_type == 1:
                ele_conn_5 = content_list[j].split()[15]
                ele_conn_6 = content_list[j].split()[16]
                ele_conn_7 = content_list[j].split()[17]
                ele_conn_8 = content_list[j].split()[18]
            elements.append(ele_temp)
            if mesh_type == 0:
                elements_connect.append([ele_conn_1,ele_conn_2,ele_conn_3,ele_conn_4])
            else:
                elements_connect.append([ele_conn_1,ele_conn_2,ele_conn_3,ele_conn_4,ele_conn_5,ele_conn_6,ele_conn_7,ele_conn_8])
   
    return nodes,nodes_coord,elements,elements_connect


