# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:29:13 2022

@author: hammad.eljisr
"""

def getFrameSectionLabelsSAP2000(SapModel,Frame_Property):
    """
    This function returns the frame section labels corresponding to a frame property.
    Input:
        - SapModel: SAP Model object
        - Frame_Property: Frame section property
    Output:
        - section_labels: frame section labels corresponding to the frame property
    """

    # All frame sections labels
    Frame_sections = SapModel.FrameObj.GetNameList()[1]
    # Get frame section labels corresponding to the frame property
    SapModel.SelectObj.ClearSelection()
    section_labels = []
    SapModel.SelectObj.PropertyFrame(Frame_Property)
    for i in range(len(Frame_sections)):
        if SapModel.FrameObj.GetSelected(Frame_sections[i])[0] == True:
            section_labels.append(Frame_sections[i])
   
    SapModel.SelectObj.ClearSelection()
    
    return section_labels
