def createBeamsFromSlabSAP2000(SapModel, mesh_grid, mesh_grid_y, beam_offsets, beam_section, beam_group):
    """
    This function creates longitudinal beam frame elements connecting the existing
    points of one or several transverse rows of a slab mesh grid, as returned by
    createSlabCLSAP2000. The beams therefore share their points with the slab shell
    elements (guarantees connectivity), rather than being drawn on their own axis.
    RECOMMENDATION: Use after creating the slab, with the desired beam offsets
    already included in div_y at slab creation time.
    Input:
        - SapModel: SAP Model object
        - mesh_grid: List of lists of point names, one row per transverse offset,
          ordered by increasing station, as returned by createSlabCLSAP2000
        - mesh_grid_y: List of transverse offsets corresponding to each row of
          mesh_grid, as returned by createSlabCLSAP2000
        - beam_offsets: List of transverse offsets at which to create a beam
          (must match values already present in mesh_grid_y, e.g. from div_y)
        - beam_section: Frame section property name assigned to the beams
        - beam_group: Beam frame elements group name
    Output:
        - beam_frames: List of lists of created beam frame element names, one list
          per beam offset, in the same order as beam_offsets, each in station order
    """

    mesh_grid_y = list(mesh_grid_y)
    beam_frames = []

    for offset in beam_offsets:
        row_idx = min(range(len(mesh_grid_y)), key=lambda i: abs(mesh_grid_y[i] - offset))
        points_row = mesh_grid[row_idx]

        frames = []
        for p1, p2 in zip(points_row[:-1], points_row[1:]):
            name, ret = SapModel.FrameObj.AddByPoint(str(p1), str(p2), beam_section)
            frames.append(name)
        beam_frames.append(frames)

    # Add beam frame elements to group
    SapModel.GroupDef.SetGroup(beam_group)
    for frames in beam_frames:
        for f in frames:
            SapModel.FrameObj.SetGroupAssign(f, beam_group)

    return beam_frames
