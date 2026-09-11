# -*- coding: utf-8 -*-
"""
Created on Thu May  28 15:56:54 2026

@author: hammad.eljisr
"""

import numpy as np
import math
from MeshingGeometry.getStations import getStations
from shapely.geometry import Polygon, Point
from collections import defaultdict
from MeshingGeometry.getOffsetPoints import getOffsetPoints, getSlopeNormals


def createSlabCLSAP2000(SapModel,centerline_coord,slab_width,slope,div_x,div_y,orientation,mesh_size,slab_group,accuracy):
    """
    This function creates the slab of a bridge steel deck with a given slope using shell elements from a centerline. Works well if curvature is smooth, no tight corners
    Input:
        - SapModel: SAP Model object
        - centerline_coord: List of centerline points coordinates of the deck [(x1,y1,z1),(x2,y2,z2)...]. Add points to ensure meshing at certain locations (e.g. piers)
        - slab_width: Width of the slab
        - slope: Slab slope in % (positive towards outer edge, that is positive offset)
        - div_x: Deck divisions in the longitudinal direction along centerline (e.g. location of stiffeners), arranged in increasing order
        - div_y: Deck divisions in the transverse direction along slab (e.g. location of longitudinal beams), arranged in increasing order
        - orientation: Element points orientation, 1 for counter-clockwise, -1 for clockwise
        - mesh_size: Slab mesh size, use large value to leave mesh unrefined
        - slab_group: Slab shell elements group name
        - accuracy: Number of decimal places for output stations (2 recommended for 10th digit m, -2 for 100s digit mm)
    Output:
        - slab_shell: Slab created shell elements
        - div_stations: Stations along centerline of the deck at the specified divisions (e.g. stiffeners)
        - all_stations: All stations along centerline of the deck
        - mesh_grid: List of mesh grid points in order of increasing stations, increasing transverse offsets
        - mesh_grid_y: List of mesh grid offset coordinates along inclined slope
    """
    
    # Stations tolerance 
    tol = 10**(-accuracy+1)
                     
    # Get stations along centerline  (in-plane)
    stations_cl = getStations(centerline_coord)
   
    # Round to decimal places
    stations_cl = [round(s,accuracy) for s in stations_cl] 
    div_x = [round(s,accuracy) for s in div_x] 
    
    ######################
    ###### DIVISIONS ###### 
    ####################### 
    # Add coordinates to centerline along divisions
    cl_array = np.array(centerline_coord)
    # Extract individual coordinate profiles
    x_cl = cl_array[:, 0]
    y_cl = cl_array[:, 1]
    z_cl = cl_array[:, 2]
    # Interpolate each axis independently at the new stations
    div_stations = np.sort(stations_cl + div_x) 
    # Include mesh divisions in the longitudinal direction
    mesh_div_diff = np.diff(div_stations)
    mesh_stations = []
    for m in range(len(mesh_div_diff)):
        if mesh_div_diff[m] > mesh_size:
            n_mesh_div = int(mesh_div_diff[m]/mesh_size)
            mesh_add = np.linspace(div_stations[m],div_stations[m+1],int(n_mesh_div)+2)
            mesh_stations.append(mesh_add)
    mesh_stations = list(set([float(val) for arr in mesh_stations for val in arr]))
    all_stations_o = np.sort(list(set(list(div_stations) + mesh_stations)))
    all_stations_o = [round(s,accuracy) for s in all_stations_o] 
    
    # Remove mesh stations spaced within the tolerance
    all_stations = [[] for _ in range(len(all_stations_o))]
    for i in range(len(all_stations_o)-1):
        if abs(all_stations_o[i+1]-all_stations_o[i]) < tol:   
            if all_stations_o[i] not in div_x:
                all_stations[i] = float("nan")
            if all_stations_o[i+1] not in div_x:
                all_stations[i+1] = float("nan")
    
    for i in range(len(all_stations)):
        try:
            math.isnan(all_stations[i]) == True         
        except:
            all_stations[i] = all_stations_o[i]
    all_stations = [x for x in all_stations if not (isinstance(x,float) and math.isnan(x))]
     
    interp_x = np.interp(all_stations, stations_cl,x_cl)
    interp_y = np.interp(all_stations, stations_cl,y_cl)
    interp_z = np.interp(all_stations, stations_cl,z_cl)
    interp_array = np.column_stack((interp_x, interp_y, interp_z))
    centerline_div_coord = [tuple(point) for point in interp_array] # Centerline coordinates with longitudinal divisions 
    
    # Mesh divisions (transversally)
    div_y_mesh = []
    unrefined_y = [-slab_width/2,0,slab_width/2] + div_y
    unrefined_y = np.sort(unrefined_y)
    unrefined_y_diff = np.diff(unrefined_y)
    for m in range(len(unrefined_y_diff)):
        if unrefined_y_diff[m] > mesh_size:
            n_mesh_div_y = int(unrefined_y_diff[m]/mesh_size)
            mesh_y = np.linspace(unrefined_y[m],unrefined_y[m+1],int(n_mesh_div_y)+1)[1:-1]
            div_y_mesh.append(mesh_y)
    div_y_mesh = list(set([float(val) for arr in div_y_mesh for val in arr]))
    
    ############################## 
    ###### MESH GRID POINTS ###### 
    ############################## 
    # Create centerline points
    centerline_points = []
    for i in range(len(centerline_div_coord)):
        pt = SapModel.PointObj.AddCartesian(centerline_div_coord[i][0],centerline_div_coord[i][1],centerline_div_coord[i][2])
        centerline_points.append(pt[0])
    
    # Add centerline_points to group
    SapModel.GroupDef.SetGroup("CL")
    for p in centerline_points:
        SapModel.PointObj.SetGroupAssign(p, "CL")
    
    # Get and create deck offset points
    s_normals = getSlopeNormals(centerline_div_coord,slope)
    # Edge outer and inner points
    outer_points_coord = getOffsetPoints(centerline_div_coord,slab_width/2,s_normals)
    outer_points = []
    for i in range(len(outer_points_coord)):
        pt = SapModel.PointObj.AddCartesian(outer_points_coord[i][0],outer_points_coord[i][1],outer_points_coord[i][2])
        outer_points.append(pt[0])
        
    inner_points_coord = getOffsetPoints(centerline_div_coord,-slab_width/2,s_normals)
    inner_points = []
    for i in range(len(inner_points_coord)):
        pt = SapModel.PointObj.AddCartesian(inner_points_coord[i][0],inner_points_coord[i][1],inner_points_coord[i][2]) 
        inner_points.append(pt[0])
    # Add points to group
    for d in range(len(outer_points)):
        SapModel.GroupDef.SetGroup('E-' + f"{slab_width/2:.2f}")
        SapModel.GroupDef.SetGroup('E-' + f"{-slab_width/2:.2f}")
        for p in outer_points:
            SapModel.PointObj.SetGroupAssign(p,'E-' + f"{slab_width/2:.2f}")
        for p in inner_points:
            SapModel.PointObj.SetGroupAssign(p,'E-' + f"{-slab_width/2:.2f}")
            
    # Create offset points at y divisions
    div_y_coord = [[] for _ in range(len(div_y))]
    div_y_points = [[] for _ in range(len(div_y))]
    for d in range(len(div_y_coord)):
        div_y_coord[d] = getOffsetPoints(centerline_div_coord,div_y[d],s_normals)
    for d in range(len(div_y_coord)):
        for i in range(len(div_y_coord[d])):
            pt = SapModel.PointObj.AddCartesian(div_y_coord[d][i][0],div_y_coord[d][i][1],div_y_coord[d][i][2])
            div_y_points[d].append(pt[0])
    # Add points to group
    for d in range(len(div_y_points)):
        SapModel.GroupDef.SetGroup('O-' + f"{div_y[d]:.2f}")
        for p in div_y_points[d]:
            SapModel.PointObj.SetGroupAssign(p,'O-' + f"{div_y[d]:.2f}")
    
    # Create offset points at mesh divisions
    div_y_mesh_coord = [[] for _ in range(len(div_y_mesh))]
    div_y_mesh_points = [[] for _ in range(len(div_y_mesh))]
    for d in range(len(div_y_mesh_coord)):
        div_y_mesh_coord[d] = getOffsetPoints(centerline_div_coord,div_y_mesh[d],s_normals) # Offset coordinates
    # Create points
    for d in range(len(div_y_mesh_coord)):
        for i in range(len(div_y_mesh_coord[d])):
            pt = SapModel.PointObj.AddCartesian(div_y_mesh_coord[d][i][0],div_y_mesh_coord[d][i][1],div_y_mesh_coord[d][i][2])
            div_y_mesh_points[d].append(pt[0])
               
    # Create shell elements div_y_mesh
    slab_shell = [] # Quad shell elements
    mesh_grid = [inner_points,centerline_points,outer_points] + div_y_points + div_y_mesh_points # Mesh grid points
    mesh_grid_y = [-slab_width/2,0,slab_width/2] + div_y + div_y_mesh
    I_mesh_y = np.argsort(mesh_grid_y)
    mesh_grid_y = np.array(mesh_grid_y)[I_mesh_y]
    mesh_grid = np.array(mesh_grid)[I_mesh_y]
    quad_points = getQuadMeshPoints(mesh_grid)
    # Sort counter-clockwise or clockwise
    quad_points_sorted = []
    for i in range(len(quad_points)):
        quad_points_sorted.append(sort3DpointsCCW(SapModel,quad_points[i])[::orientation])   
    for p in range(len(quad_points_sorted)):
        pts = quad_points_sorted[p]
        a_shell = SapModel.AreaObj.AddByPoint(4, pts, '')
        slab_shell.append(a_shell[1])
        
    # Add shell elements to group
    SapModel.GroupDef.SetGroup(slab_group)
    for s in slab_shell:
        SapModel.AreaObj.SetGroupAssign(s,slab_group)
        
    return slab_shell,list(div_stations),list(all_stations),list(mesh_grid),list(mesh_grid_y)


def createSlab2LSAP2000(SapModel,line_1_points,line_2_points,orientation,mesh_n_div,slab_group,accuracy):
    """
    This function creates the slab of a bridge steel deck between 2 sets of lines with equal number of points. Meshing can be modified in the transverse direction only. 
    Works well if curvature is smooth, no tight corners
    Input:
        - SapModel: SAP Model object
        - line_1_points: List of points of the first line ['p1a','p2a','p3a'...] arranged in order.
        - line_2_points: List of points of the second line ['p1b','p2b','p3b'...] arranged in order.
        - orientation: Element points orientation, 1 for counter-clockwise, -1 for clockwise
        - mesh_n_div: Slab number of mesh divisions in the transverse direction
        - slab_group: Slab shell elements group name
        - accuracy: Number of decimal places (1 recommended for 10th digit m, -2 for 100s digit mm)
    Output:
        - slab_shell: Slab created shell elements
        - mesh_grid: List of mesh grid points in order of increasing stations, increasing transverse offsets
    """
 
    # Mesh divisions (transversally)
    # Get coordinates  of intermediate points at mesh divisions
    x1, y1, z1 = [], [], [] # Line 1 coordinates
    x2, y2, z2 = [], [], [] # Line 2 coordinates
    for i in range(len(line_1_points)):
       x1.append(SapModel.PointObj.GetCoordCartesian(line_1_points[i])[0]) 
       y1.append(SapModel.PointObj.GetCoordCartesian(line_1_points[i])[1]) 
       z1.append(SapModel.PointObj.GetCoordCartesian(line_1_points[i])[2]) 
       x2.append(SapModel.PointObj.GetCoordCartesian(line_2_points[i])[0]) 
       y2.append(SapModel.PointObj.GetCoordCartesian(line_2_points[i])[1]) 
       z2.append(SapModel.PointObj.GetCoordCartesian(line_2_points[i])[2]) 
    # Intermediate coordinates
    x_int = np.linspace(x1,x2,num=mesh_n_div+1)[1:-1]
    y_int = np.linspace(y1,y2,num=mesh_n_div+1)[1:-1]
    z_int = np.linspace(z1,z2,num=mesh_n_div+1)[1:-1]
    
    # Create intermediate points
    intermediate_points = [[] for _ in range(len(x_int))]
    for i in range(len(x_int)):
        for j in range(len(x_int[i])):
            pt = SapModel.PointObj.AddCartesian(x_int[i][j],y_int[i][j],z_int[i][j])
            intermediate_points[i].append(pt[0])
        
    ############################## 
    ###### MESH GRID POINTS ###### 
    ##############################              
    # Create shell elements div_y_mesh
    slab_shell = [] # Quad shell elements
    mesh_grid = [list(line_1_points)] + intermediate_points + [list(line_2_points)] # Mesh grid points
    quad_points = getQuadMeshPoints(mesh_grid)
    # Sort counter-clockwise or clockwise
    quad_points_sorted = []
    for i in range(len(quad_points)):
        quad_points_sorted.append(sort3DpointsCCW(SapModel,quad_points[i])[::orientation])  
    for p in range(len(quad_points_sorted)):
        a_shell = SapModel.AreaObj.AddByPoint(4,quad_points_sorted[p])
        slab_shell.append(a_shell[1])
    # Add shell elements to group
    SapModel.GroupDef.SetGroup(slab_group)
    for s in slab_shell:
        SapModel.AreaObj.SetGroupAssign(s,slab_group)
        
    return slab_shell,list(mesh_grid)


def createWebSAP2000(SapModel,web_offset,int_points,web_depth,web_angle,div_z,orientation,mesh_size,web_group):
    """
    This function creates a web of a bridge steel deck using shell elements from a list of existing points. Works well if curvature is smooth, no tight corners
    RECOMMENDATION: Use after creating slab
    Input:
        - SapModel: SAP Model object
        - web_offset: Web offset from deck centerline
        - int_points: List of points at the slab-web intersection [(x1,y1,z1),(x2,y2,z2)...]. 
        - web_depth: Depth of the web (projected along vertical axis)
        - web_angle: Web angle measured clockwise from the vertical z-axis in degrees
        - div_z: Web divisions in the vertical direction, (e.g. location of stiffeners), arranged in increasing order (projected along vertical axis)
        - orientation: Element points orientation, 1 for counter-clockwise, -1 for clockwise
        - mesh_size: Web mesh size, use large value to leave mesh unrefined
        - web_group: Web shell elements group name
    Output:
        - web_shell: Web created shell elements
        - mesh_grid: List of mesh grid points in order
        - mesh_grid_z: List of mesh grid offset coordinates along inclined web plane
    """
    
    # Get depth and divisions projected along vertical axis
    web_depth = web_depth/math.cos(math.radians(web_angle))
    div_z = [d/math.cos(math.radians(web_angle)) for d in div_z]
    
    # Get intersection points coordinates
    int_coord = [[] for _ in range(len(int_points))]
    for i in range(len(int_points)):
        x_int = SapModel.PointObj.GetCoordCartesian(int_points[i])[0]
        y_int = SapModel.PointObj.GetCoordCartesian(int_points[i])[1]
        z_int = SapModel.PointObj.GetCoordCartesian(int_points[i])[2]
        int_coord[i] = (x_int,y_int,z_int)
        
    # Mesh divisions (vertically)
    div_z_mesh = []
    unrefined_z = [-web_depth,0] + div_z
    unrefined_z = np.sort(unrefined_z)
    unrefined_z_diff = np.diff(unrefined_z)
    for m in range(len(unrefined_z_diff)):
        if unrefined_z_diff[m] > mesh_size:
            n_mesh_div_z = math.ceil(round(unrefined_z_diff[m]/mesh_size,1))
            mesh_z = np.linspace(unrefined_z[m],unrefined_z[m+1],int(n_mesh_div_z)+1)[1:-1]
            div_z_mesh.append(mesh_z)
    div_z_mesh = list(set([float(val) for arr in div_z_mesh for val in arr]))
    
    ############################## 
    ###### MESH GRID POINTS ###### 
    ############################## 
    # Get and create web offset points
    # Get web normals
    nx = 0
    ny = 1
    nz = math.tan(math.radians(web_angle))
    normal = np.array([nx,ny,nz])
    web_normal = normal/np.linalg.norm(normal) 
    web_normals = np.tile(web_normal,(len(int_coord),1))
    
    # Web bottom points
    bott_points_coord = getOffsetPoints(int_coord,-web_depth,web_normals)
    bott_points = []
    for i in range(len(bott_points_coord)):
        pt = SapModel.PointObj.AddCartesian(bott_points_coord[i][0],bott_points_coord[i][1],bott_points_coord[i][2])
        bott_points.append(pt[0])
    # Add points to group
    SapModel.GroupDef.SetGroup('WB-' + f"{web_offset:.2f}")
    for p in bott_points:
        SapModel.PointObj.SetGroupAssign(p,'WB-' + f"{web_offset:.2f}")
    
    # Points at z divisions
    div_z_coord = [[] for _ in range(len(div_z))]
    div_z_points = [[] for _ in range(len(div_z))]
    for d in range(len(div_z_coord)):
        div_z_coord[d] = getOffsetPoints(int_coord,div_z[d],web_normals) # Offset coordinates
    # Create points
    for d in range(len(div_z_coord)):
        for i in range(len(div_z_coord[d])):
            pt = SapModel.PointObj.AddCartesian(div_z_coord[d][i][0],div_z_coord[d][i][1],div_z_coord[d][i][2])
            div_z_points[d].append(pt[0])
    # Add points to group
    for d in range(len(div_z_points)):
        SapModel.GroupDef.SetGroup('WD-' + f"{abs(div_z[d]):.2f}" + '_' + f"{web_offset:.2f}")
        for p in div_z_points[d]:
            SapModel.PointObj.SetGroupAssign(p,'WD-' + f"{abs(div_z[d]):.2f}" + '_' + f"{web_offset:.2f}")
    
    # Create offset points at mesh divisions
    div_z_mesh_coord = [[] for _ in range(len(div_z_mesh))]
    div_z_mesh_points = [[] for _ in range(len(div_z_mesh))]
    for d in range(len(div_z_mesh_coord)):
        div_z_mesh_coord[d] = getOffsetPoints(int_coord,div_z_mesh[d],web_normals) # Offset coordinates
    # Create points
    for d in range(len(div_z_mesh_coord)):
        for i in range(len(div_z_mesh_coord[d])):
            pt = SapModel.PointObj.AddCartesian(div_z_mesh_coord[d][i][0],div_z_mesh_coord[d][i][1],div_z_mesh_coord[d][i][2])
            div_z_mesh_points[d].append(pt[0])
               
    # Create shell elements div_z_mesh
    web_shell = [] # Quad shell elements
    mesh_grid = [bott_points,int_points] + div_z_points + div_z_mesh_points # Mesh grid points
    mesh_grid_z = [-web_depth,0] + div_z + div_z_mesh
    I_mesh_z = np.argsort(mesh_grid_z)
    mesh_grid_z = np.array(mesh_grid_z)[I_mesh_z]
    mesh_grid = np.array(mesh_grid)[I_mesh_z]
    quad_points = getQuadMeshPoints(mesh_grid)
    # Sort counter-clockwise or clockwise
    quad_points_sorted = []
    for i in range(len(quad_points)):
        quad_points_sorted.append(sort3DpointsCCW(SapModel,quad_points[i])[::orientation])  
    for p in range(len(quad_points_sorted)):
        a_shell = SapModel.AreaObj.AddByPoint(4,quad_points_sorted[p])
        web_shell.append(a_shell[1])
    # Add shell elements to group
    SapModel.GroupDef.SetGroup(web_group)
    for s in web_shell:
        SapModel.AreaObj.SetGroupAssign(s,web_group)
        
    return web_shell,list(mesh_grid),list(mesh_grid_z)


def createStiffenerSAP2000(SapModel,outline_points,orientation,stiff_group,accuracy):
    """
    This function creates the a quadrilateral stiffener from the defined outline points.
    Input:
        - SapModel: SAP Model object
        - outline_points: List of outline points of the stiffener e.g. [p1,p2,p3,p4,p5,p6...]. Minimum 4 points required
        - stiff_group: Stiffener shell elements group name
        - orientation: Element points orientation, 1 for counter-clockwise, -1 for clockwise
        - accuracy: Number of decimal places (5 recommended for 10th digit m, 2 for 100s digit mm to ensure points created points remain coplanar)
    Output:
        - stiff_shell: Stiffener created shell elements, (element points in counter-clockwise order)
        - div_stations: Stations along centerline of the deck at the specified divisions (e.g. stiffeners)
        - all_stations: All stations along centerline of the deck
        - mesh_grid: List of mesh grid points of the stiffener arranged in order
    """
    
    tolerance = 10**(-accuracy)
    
    # Get outline points coordinates
    outline_points_coord = []
    for i in range(len(outline_points)):
        x_pt = SapModel.PointObj.GetCoordCartesian(outline_points[i])[0]
        y_pt = SapModel.PointObj.GetCoordCartesian(outline_points[i])[1]
        z_pt = SapModel.PointObj.GetCoordCartesian(outline_points[i])[2]
        outline_points_coord.append((x_pt,y_pt,z_pt))
        
    pts = np.array(outline_points_coord, dtype=float)
    N = len(pts)
    if N < 4:
        raise ValueError("A quadrilateral polygon requires at least 3 outline points.")
    
    ############################## 
    ###### MESH COORDINATES ###### 
    ##############################     
    # Project to 2D to arrange the raw outline chronologically clockwise
    centroid = np.mean(pts, axis=0)
    shifted_pts = pts - centroid
    _, _, vh = np.linalg.svd(shifted_pts)
    
    normal, u_axis = vh[2], vh[0]
    v_axis = np.cross(normal,u_axis)
    
    pts_2d = np.array([(np.dot(p - centroid, u_axis),np.dot(p - centroid, v_axis)) for p in pts])
    cx_2d, cy_2d = np.mean(pts_2d[:,0]),np.mean(pts_2d[:,1])
    
    sorted_indices = sorted(range(len(pts_2d)),key=lambda i: -math.atan2(pts_2d[i, 1] - cy_2d,pts_2d[i, 0] - cx_2d))
    
    # Chronologically ordered 3D outline points
    ordered_pts = pts[sorted_indices]

    # Automatically detect the 4 true structural corners
    # Corners are identified by the sharpest turns (change in direction vector)
    directions = np.roll(ordered_pts,-1, axis=0) - ordered_pts
    directions /= np.linalg.norm(directions, axis=1, keepdims=True)
    dot_products = np.sum(directions*np.roll(directions, 1, axis=0), axis=1)
    
    # The 4 lowest dot products correspond to the 4 sharpest corners
    corner_indices = sorted(np.argsort(dot_products)[:4])
    
    # Extract the 4 sequential edge continuous paths
    edge0 = ordered_pts[corner_indices[0]:corner_indices[1]+1]
    edge1 = ordered_pts[corner_indices[1]:corner_indices[2]+1]
    edge2 = ordered_pts[corner_indices[2]:corner_indices[3]+1]
 
    # Remaining edge
    # Get the indices used by the first three edges
    used_indices = set(range(corner_indices[0], corner_indices[3]+1))
    # Isolate the indices left over in your ordered_pts list
    all_indices = set(range(len(ordered_pts)))
    remaining_indices = sorted(list(all_indices - used_indices))
    # Pull those leftover points out of ordered_pts
    remaining_pts = [ordered_pts[idx] for idx in remaining_indices]
    # Construct edge3: Start corner + remaining intermediate points + End corner
    if len(remaining_pts)>0:
        edge3 = np.vstack([[ordered_pts[corner_indices[0]]],remaining_pts,[ordered_pts[corner_indices[3]]]])
    else:
        edge3 = np.vstack([[ordered_pts[corner_indices[0]]],[ordered_pts[corner_indices[3]]]])
    
    # Define the 4 explicit true corner 3D anchor vectors
    c00 = ordered_pts[corner_indices[0]]  # Bottom-Left
    c10 = ordered_pts[corner_indices[1]]  # Bottom-Right
    c11 = ordered_pts[corner_indices[2]]  # Top-Right
    c01 = ordered_pts[corner_indices[3]]  # Top-Left

    # Clockwise sorting
    # Each edge sorts ascending from its starting corner to its destination corner
    edge0 = sorted(edge0, key=lambda p: np.linalg.norm(p - c00))  # c00 -> c10 (Left to Right)
    edge1 = sorted(edge1, key=lambda p: np.linalg.norm(p - c10))  # c10 -> c11 (Bottom to Top)
    edge2 = sorted(edge2, key=lambda p: np.linalg.norm(p - c11))  # c11 -> c01 (Right to Left)
    edge3 = sorted(edge3, key=lambda p: np.linalg.norm(p - c01))  # c01 -> c00 (Top to Bottom)

    # Grid dimensions
    num_u = max(len(edge0),len(edge2))
    num_v = max(len(edge1),len(edge3))

    # Parametric helper function to sample along an unevenly populated edge path
    def sample_edge_path(edge_pts,t):
        if len(edge_pts) == 1:
            return edge_pts[0]
        idx_float = t*(len(edge_pts) - 1)
        idx_low = int(np.floor(idx_float))
        idx_high = int(np.ceil(idx_float))
        weight = idx_float - idx_low
        return (1 - weight)*edge_pts[idx_low] + weight*edge_pts[idx_high]
    
    u_vals = np.linspace(0,1,num_u)
    v_vals = np.linspace(0,1,num_v)

   # Helper function to find if an exact original outline point matches our grid location
    def find_original_point_match(target_pt,original_points,tol=tolerance):
        for orig_pt in original_points:
            if np.linalg.norm(target_pt - orig_pt) < tol:
                return tuple(orig_pt)
        return None
    
    # Initialize your structured structural sub-lists
    mesh_grid_coords = []
    
    # Execute Coons Patch Linear Surface Blending
    # This matches opposite paths and creates smooth linear transitions across them
    for i, u in enumerate(u_vals):
        current_u_line = []
        for j, v in enumerate(v_vals):
            # Check for exact boundary alignments to lock them directly to original points
            is_boundary = (u == 0.0 or u == 1.0 or v == 0.0 or v == 1.0)
            
            # Determine the baseline blended point location
            p_u0 = sample_edge_path(edge0, u)       # Bottom boundary path
            p_u1 = sample_edge_path(edge2, 1 - u)   # Top boundary path (reversed)
            p_0v = sample_edge_path(edge3, 1 - v)   # Left boundary path (reversed)
            p_1v = sample_edge_path(edge1, v)       # Right boundary path

            line_u = (1 - v)*p_u0 + v*p_u1
            line_v = (1 - u)*p_0v + u*p_1v
            bilinear_corner = (1 - u)*(1 - v)*c00 + u*(1 - v)*c10 + u*v*c11 + (1 - u)*v*c01
            
            pt_3d = line_u + line_v - bilinear_corner
            
            # If the point sits on a boundary edge, cross-reference it against raw input
            matched_coord = None
            if is_boundary:
                matched_coord = find_original_point_match(pt_3d,pts)
            
                # Force interpolated points at the boundary it to be mathematically collinear between the true corners
                if matched_coord is None:
                    if v == 0.0:    # Bottom Edge (c00 -> c10)
                        collinear_pt = (1 - u)*c00 + u*c10
                    elif v == 1.0:  # Top Edge (c01 -> c11)
                        collinear_pt = (1 - u)*c01 + u*c11
                    elif u == 0.0:  # Left Edge (c00 -> c01)
                        collinear_pt = (1 - v)*c00 + v*c01
                    elif u == 1.0:  # Right Edge (c10 -> c11)
                        collinear_pt = (1 - v)*c10 + v*c11
                    
                    # Convert to float tuple without using round(), ensuring perfect lines
                    matched_coord = (round(float(collinear_pt[0]),accuracy),round(float(collinear_pt[1]),accuracy),round(float(collinear_pt[2]),accuracy))


            # Fallback to the rounded calculated coordinates if it is an internal point
            if matched_coord is None:
                matched_coord = (round(float(pt_3d[0]),accuracy),round(float(pt_3d[1]),accuracy),round(float(pt_3d[2]),accuracy))
            
            current_u_line.append(matched_coord)
    
        mesh_grid_coords.append(current_u_line)
        
    ############################## 
    ###### MESH GRID POINTS ###### 
    ############################## 
    mesh_grid = [[] for _ in range(len(mesh_grid_coords))]
    for u in range(len(mesh_grid_coords)):
        for v in range(len(mesh_grid_coords[u])):
            pt_mesh = SapModel.PointObj.AddCartesian(mesh_grid_coords[u][v][0],mesh_grid_coords[u][v][1],mesh_grid_coords[u][v][2])[0]
            mesh_grid[u].append(pt_mesh)
            
    # Create stiffener shell elements div_z_mesh
    stiff_shell = [] # Quad shell elements
    quad_points = getQuadMeshPoints(mesh_grid)
    # Sort counter-clockwise or clockwise
    quad_points_sorted = []
    for i in range(len(quad_points)):
        quad_points_sorted.append(sort3DpointsCCW(SapModel,quad_points[i])[::orientation])
        
    for p in range(len(quad_points_sorted)):
        pts = quad_points_sorted[p]
        a_shell = SapModel.AreaObj.AddByPoint(4, pts, '')
        stiff_shell.append(a_shell[1])

    # Add shell elements to group
    SapModel.GroupDef.SetGroup(stiff_group)
    for s in stiff_shell:
        SapModel.AreaObj.SetGroupAssign(s,stiff_group)
                           
    return stiff_shell,mesh_grid
     
   
def getQuadMeshPoints(grid):
    """ This function transforms vector into a unit vector 
    Input:
        - grid: List of lists of points corresponding to the mesh points. The points should be arranged in order from 1 side to the other e.g. [p1,p2,p3,p4]
          in both directions
    Output:
        - quad_points: List of quad element points
    """
    # Mesh dimensions
    # Total number of columns (U = 6)
    U = len(grid) 
    # Total number of rows (V = length of your path)
    V = len(grid[0]) 
    
    # Quad elements points indices
    quad_points = []

    # Loop through the rows
    for v in range(V - 1):
        # Loop through the columns 
        for u in range(U - 1):
            # Calculate the 1D mesh indices for the 4 corners of the quad
            p0 = grid[u][v]         # Bottom-Left
            p1 = grid[u + 1][v]     # Bottom-Right
            p2 = grid[u + 1][v + 1] # Top-Right
            p3 = grid[u][v + 1]     # Top-Left
            
            # Add quad element points
            quad_points.append([p0, p1, p2, p3])
     
    return quad_points


def sort3DpointsCCW(SapModel,points):
    """This function sorts a list of 3D points counter-clockwise relative to their centroid
    Input:
        - SapModel: SAP Model object
        - points: List of points e.g. [p1,p2,p3,p4...]
        
    Output:
        - points_sorted: List of sorted points 
    """
    
    # Get point coordinates
    points_coords =  []
    for p in points:
        x_temp = SapModel.PointObj.GetCoordCartesian(p)[0] 
        y_temp = SapModel.PointObj.GetCoordCartesian(p)[1] 
        z_temp = SapModel.PointObj.GetCoordCartesian(p)[2] 
        points_coords.append((x_temp,y_temp,z_temp))
   
    pts = np.array(points_coords)
    
    # Compute the centroid (average center point)
    centroid = np.mean(pts,axis=0)
    
    # Extract the local 2D coordinate basis vectors using SVD
    # vh contains the principal orthogonal directions of the dataset
    _, _, vh = np.linalg.svd(pts - centroid)
    u = vh[0,:]  # Local pseudo-X axis
    v = vh[1,:]  # Local pseudo-Y axis
    
    # Lock the basis direction automatically using the plane's true normal
    true_normal = vh[2, :]
    
    # Determine the closest global axis to use as a stable reference perspective
    if abs(true_normal[2]) > 0.5:
        ref = np.array([0.0, 0.0, 1.0])   # Horizontal slab/deck -> View from +Z
    elif abs(true_normal[0]) > 0.5:
        ref = np.array([1.0, 0.0, 0.0])   # Vertical wall on Y-Z plane -> View from +X
    else:
        ref = np.array([0.0, 1.0, 0.0])   # Vertical wall on X-Z plane -> View from +Y
        
    # Enforce right-handed coordinate system relative to the reference view
    if np.dot(np.cross(u,v),ref) > 0:
        v = -v  # Flips the system back to true Counter-Clockwise
     
    # Project each point onto the local 2D axes and calculate the angle
    angles = []
    for p in pts:
        r = p - centroid
        x_proj = np.dot(r,u)
        y_proj = np.dot(r,v)
        angles.append(math.atan2(y_proj,x_proj))
        
    # Sort original points by the calculated angles
    sorted_points = [p for _, p in sorted(zip(angles, points))]
    
    return sorted_points

