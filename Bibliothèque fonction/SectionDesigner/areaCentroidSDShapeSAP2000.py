# -*- coding: utf-8 -*-
"""
Created on Tue Apr  22 15:56:54 2025

@author: hammad.eljisr
"""

from shapely import Polygon
from sectionproperties.analysis import Section
from sectionproperties.pre import Geometry
from interpSection import getSectionSlabPoints

def areaCentroidSDShapeSAP2000(SapModel,SDshape):
    """
    This function outputs the area and centroid of an SD shape in SAP2000. Openings are denoted as 'Open' material
    Input:
        - SapModel: SAP Model object
        - SDshape: Frame section (SD shape) property
    Output:
        - A_t: Area of the SD shape
        - y_CG: y coordinate of the centroid of the SD shape
    """
    
    # Get deck section
    S = SapModel.PropFrame.GetSDSection(SDshape)
    # Polygons
    P = list(S[2])
    # Polygon materials
    P_mat = []
    for i in range(len(P)):
        P_mat.append(SapModel.PropFrame.SDShape.GetPolygon(SDshape,P[i])[0])
        
    # Polygon coordinates
    P_coords = [[] for _ in range(len(P))]
    for i in range(len(P)):
        Coord_x = SapModel.PropFrame.SDShape.GetPolygon(SDshape,P[i])[3]
        Coord_y = SapModel.PropFrame.SDShape.GetPolygon(SDshape,P[i])[4]
        for x in range(len(Coord_x)):
            P_coords[i].append((Coord_x[x],Coord_y[x]))
    
    # Polygons
    polygons = []
    for i in range(len(P)):
        polygons.append(Polygon(P_coords[i]))
    
    # Polygon geometries
    polygon_geom = []
    for i in range(len(P)):
        if P_mat[i] != 'Open':
            polygon_geom.append(Geometry(geom=polygons[i]))
        else:
            polygon_geom.append(Geometry(geom=polygons[i]))
    
    # Get areas and centroid y of the polygon
    mesh_size = abs(max(Coord_y) - min(Coord_y))/10
    A = []
    y = []
    for i in range(len(P)):
        geom = polygon_geom[i]
        geom.create_mesh(mesh_sizes=[mesh_size])
        sec = Section(geometry=geom)
        sec.calculate_geometric_properties()
        if P_mat[i] == 'Open':
            A_p = sec.get_area()*-1
        else:
            A_p = sec.get_area()
        A.append(A_p)
        y.append(sec.get_c()[1])
    
    # Get centroid and area of SDshape
    A_t = 0
    y_CG = 0
    for i in range(len(P)): 
        A_t = A_t + A[i]
    for i in range(len(P)):     
        y_CG = y_CG + A[i]*y[i] 
    y_CG = y_CG/A_t
    
    # Centroid measured from center of top slab
    y_slab_center = (getSectionSlabPoints(SapModel,SDshape)[0][0][1] + getSectionSlabPoints(SapModel,SDshape)[0][1][1])/2
    y_CG = y_CG - y_slab_center
    
    return A_t,y_CG