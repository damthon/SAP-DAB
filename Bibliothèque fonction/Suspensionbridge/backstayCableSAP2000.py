# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:04:08 2024

@author: hammad.eljisr
"""

def backstayCableSAP2000(SapModel,node_p,l_bs,bs_cable_section,T_bs):
    """
    This function creates the backstay cable for a pylon in a suspension bridge
    Input:
        SapModel: SAP model object
        node_p: Pylon node connecting the backstay
        l_bs: Backstay dimension [lx,ly,lz]
        bs_cable_section: Cable section
        T_bs: Tension in the backstay
        
    Output:
        bs_cable: Backstay cable
    """     

    # Get coordinates of the connecting points
    x_o = []
    y_o = []
    z_o = []
    x_o.append(SapModel.PointObj.GetCoordCartesian(node_p)[0])
    y_o.append(SapModel.PointObj.GetCoordCartesian(node_p)[1])
    z_o.append(SapModel.PointObj.GetCoordCartesian(node_p)[2])
    
    # Create backstay anchor point
    SapModel.SelectObj.ClearSelection()
    SapModel.PointObj.SetSelected(node_p,True)
    anchor_pt = SapModel.EditGeneral.ReplicateLinear(l_bs[0],l_bs[1],l_bs[2],1,1)[1][0]
    SapModel.PointObj.setRestraint(anchor_pt,[1,1,1,0,0,0],0) # Restrain anchor point
    
    # Construct cable
    bs_cable = SapModel.CableObj.AddByPoint(node_p,anchor_pt)[0]
    SapModel.CableObj.SetProperty(bs_cable,bs_cable_section) # Assign section
    SapModel.CableObj.SetCableData(bs_cable,3,1,0,0,T_bs) # Assign tension force
    
    return bs_cable