# -*- coding: utf-8 -*-
"""
Created on Wed Aug  30 15:56:54 2023

@author: hammad.eljisr
"""

def isostaticPrestressLoadCaseSAP2000(SapModel,prestressed_group,support_points,support_section,support_extrusion,support_type,support_group,prestress):
    """
    This function creates a staged construction for the isolated prestressing of an object (e.g. beam). The output prestressing force consists of the isostatic force only.
    Input:
        - SapModel: SAP Model object
        - prestressed_group: The group corresponding to the object to be prestressed
        - support_points: Points at which the temporary supports are constructed
        - support_section: Frame section of the temporary supports (Axis 2 aligned along the object axis)
        - supports_extrusion: Direction in which the temporary suppors are extruded [x,y,z]
        - support type: 0 for pin/roller support, applicable in case the number of support points = 2 only, and supports are parallel to the axis of the beam. 
                        1 for fixed support, applicable for any number of support points, and supports are transverse to the axis of the beam .
        - supports_group: Group to which the temporary supports are added
        - prestress: Prestressing load pattern
    """
    
    # Add temporary supports for prestressing (frame sections)
    SapModel.SetPresentUnits(6) # kN-m unit system
    # Temporary supports orientation
    s_x = support_extrusion[0] 
    s_y = support_extrusion[1] 
    s_z = support_extrusion[2] 
    
    # Create temporary supports  group
    SapModel.GroupDef.SetGroup(support_group)
        
    if support_type == 0:
        # Support 1 (1 m)
        support_1 = SapModel.EditGeneral.ExtrudePointToFrameLinear(support_points[0],support_section,s_x,s_y,s_z,1)[0][0] # Frame object
        support_1_fp = SapModel.FrameObj.GetPoints(support_1)[1] # Fixed end point
        # Support 2 (1 m)
        support_2 = SapModel.EditGeneral.ExtrudePointToFrameLinear(support_points[1],support_section,s_x, s_y,s_z,1)[0][0] # Frame object
        support_2_fp = SapModel.FrameObj.GetPoints(support_2)[1] # Fixed end point
        
        # Align axis-2 with object axis
        SapModel.FrameObj.SetLocalAxesAdvanced(support_1, True, 12, 2, '', [0,0], support_points, [0,0,0])
        SapModel.FrameObj.SetLocalAxesAdvanced(support_2, True, 12, 2, '', [0,0], support_points, [0,0,0])
        
        # Assign frame releases to the supports (pin/roller)
        support_releases = [[0,0,0,0,0,1],[0,1,0,0,0,1]]
        SapModel.FrameObj.SetReleases(support_1,support_releases[0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0])
        SapModel.FrameObj.SetReleases(support_2,support_releases[1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0])
        
        # Add temporary supports to group
        SapModel.FrameObj.SetGroupAssign(support_1, support_group)
        SapModel.FrameObj.SetGroupAssign(support_2, support_group)
        
        # Assign fixed restraints to frame end points
        SapModel.PointObj.setRestraint(support_1_fp, [1,1,1,1,1,1])
        SapModel.PointObj.setRestraint(support_2_fp, [1,1,1,1,1,1])
        
        # Create prestressing stage load case
        # Create load case
        load_case_name = prestress + '_' + prestressed_group
        SapModel.LoadCases.StaticNonlinearStaged.SetCase(load_case_name)
        # Add stage
        SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions_2(load_case_name,1,[0],[True],[''],[''])
        # Operations
        operations = [1,1,1,3] # Add structure, load objects if new
        object_types = ['Group','Frame','Frame','Group'] # Type of the objets 
        object_names = [prestressed_group,support_1,support_2,prestressed_group] # Names of the objects
        object_age = [0,0,0,0] # Age of added structure
        load_type = ['','','','Load'] # Type of load
        load_name = ['','','',prestress] # Name of prestress load
        load_SF = [1,1,1,1]  # Load scale factor
        SapModel.LoadCases.StaticNonlinearStaged.SetStageData_2(load_case_name,1, len(operations), operations, object_types, object_names, object_age, load_type, load_name,load_SF)
     
    if support_type == 1:
        # Supports (1 m)
        supports_frames_group = prestress + '_' + prestressed_group + '_frames'
        SapModel.GroupDef.SetGroup(supports_frames_group)
        for j in range(len(support_points)):
            support_3 = SapModel.EditGeneral.ExtrudePointToFrameLinear(support_points[j],support_section,s_x,s_y,s_z,1)[0][0] # Frame object
            support_3_fp = SapModel.FrameObj.GetPoints(support_3)[1] # Fixed end point
        
            # Add temporary supports to group
            SapModel.FrameObj.SetGroupAssign(support_3, support_group)
       
            # Assign fixed restraints to frame end points
            SapModel.PointObj.setRestraint(support_3_fp, [1,1,1,1,1,1])
            
            # Assign frames to load case group
            SapModel.FrameObj.SetGroupAssign(support_3, supports_frames_group)
            
        # Create prestressing stage load case
        # Create load case
        load_case_name = prestress + '_' + prestressed_group
        SapModel.LoadCases.StaticNonlinearStaged.SetCase(load_case_name)
        # Add stage
        SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions_2(load_case_name,1,[0],[True],[''],[''])
        # Operations
        operations = [1,1,3] # Add structure, load objects if new
        object_types = ['Group','Group','Group'] # Type of the objets 
        object_names = [prestressed_group,supports_frames_group,prestressed_group] # Names of the objects
        object_age = [0,0,0] # Age of added structure
        load_type = ['','','Load'] # Type of load
        load_name = ['','',prestress] # Name of prestress load
        load_SF = [1,1,1]  # Load scale factor
        SapModel.LoadCases.StaticNonlinearStaged.SetStageData_2(load_case_name,1, len(operations), operations, object_types, object_names, object_age, load_type, load_name,load_SF)
            
            
    return load_case_name