def createPilesSAP2000(SapModel, piles_coord, piles_height, z_top, pile_section, pile_group):
    """
    This function creates vertical pier frame elements (piles) from their plan position and height.
    Input:
        - SapModel: SAP Model object
        - piles_coord: List of pile plan coordinates [(x1,y1),(x2,y2)...], one per pile
        - piles_height: List of pile heights [m], in the same order as piles_coord
        - z_top: Elevation of the pile heads (top of piles), common to all piles
        - pile_section: Frame section property name assigned to the piles
        - pile_group: Pile frame elements group name
    Output:
        - pile_frames: List of created pile frame element names, in the same order as piles_coord
    """

    pile_frames = []
    for (x, y), h in zip(piles_coord, piles_height):
        z_bottom = z_top - h
        name, ret = SapModel.FrameObj.AddByCoord(x, y, z_top, x, y, z_bottom, "", pile_section)
        ret = SapModel.FrameObj.SetOutputStations(name, MyType = 2, MaxSegSize = h/8, MinSections = 9)
        pile_frames.append(name)

    # Add pile frame elements to group
    SapModel.GroupDef.SetGroup(pile_group)
    for f in pile_frames:
        SapModel.FrameObj.SetGroupAssign(f, pile_group)

    return pile_frames
