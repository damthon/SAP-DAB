# -*- coding: utf-8 -*-
"""
Created on Mon Aug  28 15:56:54 2023

@author: hammad.eljisr
"""

from getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000
from getGroupPointObjSAP2000 import getGroupPointObjSAP2000
from Plane import Plane
import math
import numpy as np

# Problem at intersection of 2 faces, solution: Update local axis: vector from point to centroid of adjacent elements to define local axis 1, centroid of adjacent elements + 2 adjacent points to define plane

def getFlexuralComponentSAP2000(SapModel,area_group,interior_joints_group,Load_case_combo):
    """
    This function obtains the flexural component of the vertical forces in a selected cut of area (shell) elements.
    Input:
        SapModel: SAP Model object
        area_group: Group of the cut consisting of the area elements and joints along the cut
        interior_joints_group: Interior joints on the inside of the cut used to determine the orientation of the local 1-axis
    Output:
        F3_vectors: Vector of flexural forces at each joint
    """
    
    # Get cut joints
    cut_joints = getGroupPointObjSAP2000(SapModel,area_group)
    
    # Get interior joints
    interior_joints = getGroupPointObjSAP2000(SapModel,interior_joints_group)
    
    # Get closest interior joint to cut joint, to be used to define the local axis 1 of the cut joint
    closest_interior_joints = [[] for _ in range(len(cut_joints))]
    for i in range(len(cut_joints)):
        cut_joint_coord = SapModel.PointObj.GetCoordCartesian(cut_joints[i])[0:3]
        min_dist = 10^6
        for j in range(len(interior_joints)):
            int_joint_coord = SapModel.PointObj.GetCoordCartesian(interior_joints[j])[0:3]
            if math.dist(int_joint_coord,cut_joint_coord) < min_dist:
                min_dist = math.dist(int_joint_coord,cut_joint_coord)
                closest_joint = interior_joints[j]
        elems_cut = SapModel.PointObj.GetConnectivity(cut_joints[i])[2] # connecting area elements
        elems_closest = SapModel.PointObj.GetConnectivity(closest_joint)[2] 
        if any(e in elems_cut for e in elems_closest): # If joints have common connecting element
            closest_interior_joints[i] = closest_joint
        else:
            print('Error: joints ' + cut_joints[i] + ' and ' + closest_joint  + ' do not belong to the same element. Redefine interior joints')
    
    # Get the closest cut joint to another cut joint, to be used to define the plane to which axis 3 is perpendicular
    closest_cut_joints = [[] for _ in range(len(cut_joints))]
    for i in range(len(cut_joints)):
        cut_joint_coord = SapModel.PointObj.GetCoordCartesian(cut_joints[i])[0:3]
        min_dist = 10^6
        for j in range(len(cut_joints)):
            cut_joints_coord_2 = SapModel.PointObj.GetCoordCartesian(cut_joints[j])[0:3]
            if math.dist(cut_joints_coord_2,cut_joint_coord) < min_dist and cut_joints[i] != cut_joints[j]:
                min_dist = math.dist(cut_joints_coord_2,cut_joint_coord)
                closest_joint = cut_joints[j]
            closest_cut_joints[i] = closest_joint

            
    # Get vector perpendicular planes passing through the cut_joint and the 2 closest joint in the element
    v_perp = []
    for i in range(len(cut_joints)):
        point_1 = SapModel.PointObj.GetCoordCartesian(cut_joints[i])[0:3]
        point_2 = SapModel.PointObj.GetCoordCartesian(closest_cut_joints[i])[0:3]
        point_3 = SapModel.PointObj.GetCoordCartesian(closest_interior_joints[i])[0:3]
        v_p = np.array(Plane.get3PointsPlane(point_1,point_2,point_3)[1])
        # Orientt positive z
        if v_p[2] >= 0:
            v_perp.append(list(v_p))
        else:
            v_perp.append(list(v_p*-1))
            
    # Align joint local 1-axis and local 2-axis in direction of the 2 joints 
    for i in range(len(cut_joints)):
        SapModel.PointObj.SetLocalAxesAdvanced(cut_joints[i],True,2,'',[0,0],[cut_joints[i],closest_interior_joints[i]],[0,0,0],13,3,'Global',[0,0],[],v_perp[i],0)
    
    # Interactive database 
    ret = SapModel.Analyze.RunAnalysis()
    # Deselect results for all cases
    ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    # Select desired load case
    ret = SapModel.Results.Setup.SetCaseSelectedForOutput(Load_case_combo)
    if ret == 1: # Load combination instead of load case
        SapModel.Results.Setup.SetComboSelectedForOutput(Load_case_combo)
                
    # Joint forces
    joint_forces = SapModel.DatabaseTables.GetTableForDisplayArray('Element Joint Forces - Areas',[],area_group)
    index_Joint = joint_forces[2].index('Joint')
    index_F1 = joint_forces[2].index('F1')
    index_F2 = joint_forces[2].index('F2')
    index_F3 = joint_forces[2].index('F3')
    
    # Table data 
    T_data = np.array(list(joint_forces[4])) # List
    shape = (int(joint_forces[3])),len(joint_forces[2]) # Reshape rows,columns
    T_data = T_data.reshape(shape)
    
    Joints = []
    F1 = []
    F2 = []
    F3 = []
    
    for i in range(len(T_data)):
        Joints.append(T_data[i][index_Joint])
        f1 = float(T_data[i][index_F1])
        f2 = float(T_data[i][index_F2])
        f3 = float(T_data[i][index_F3])
        for j in range(i+1,len(T_data)):
            if T_data[j][2] == T_data[i][index_Joint]:
                f1 = f1 + float(T_data[j][index_F1])
                f2 = f2 + float(T_data[j][index_F2])
                f3 = f3 + float(T_data[j][index_F3])
        F1.append(f1)
        F2.append(f2)
        F3.append(f3)

    # Remove duplicates by creating a list of the index of the joint duplicates
    duplicates_index = []
    Joints_set = set(Joints)
    for item in Joints_set:
        dup = [i for i, x in enumerate(Joints) if x == item]
        dup.remove(min(dup))
        duplicates_index.append(dup)
    duplicates_index_flatten = sum(duplicates_index, [])
    
    # Sort duplicates index and delete duplicates
    for i in sorted(duplicates_index_flatten, reverse=True):
        del Joints[i] 
        del F1[i]
        del F2[i]
        del F3[i]
 
    # Remove joints/results not in the cut joints
    for i in reversed(range(len(Joints))):
        if Joints[i] not in cut_joints:
            del Joints[i]
            del F1[i]
            del F2[i]
            del F3[i]
    
    # Get flexural forces vectors at each joint
    F3_vectors = []
    for i in range(len(Joints)):
        F3_vectors.append(np.array(v_perp[i])*F3[i])
                                             
    return F3_vectors
