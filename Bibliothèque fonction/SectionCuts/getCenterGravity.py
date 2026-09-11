import numpy as np
import comtypes.client


def compute_cg_from_plane(
    SapModel,
    group_name,
    plane,
    sigma=0.5,
    use_weighting=True,
    tol=1e-6
):
    """
    Calcule le centre de gravité des AreaObj d'un groupe intersectant un plan.

    Paramètres
    ----------
    SapModel : objet SAP2000
    group_name : str
        Nom du groupe SAP contenant les AreaObj
    plane : list [A, B, C, D]
        Plan Ax + By + Cz + D = 0
    sigma : float
        Largeur de pondération (pour weighting gaussien)
    use_weighting : bool
        True = pondération distance (recommandé)
        False = pondération classique surfacique
    tol : float
        Tolérance intersection

    Retour
    ------
    CG_global : np.array([x, y, z])
    """

    [A,B,C,D] = plane.equation
    normal = np.array([A, B, C])
    normal = normal / np.linalg.norm(normal)

    # -----------------------------
    # Récupération des aires
    # -----------------------------
    NumberItems, ObjectType, ObjectName, ret = SapModel.GroupDef.GetAssignments(group_name)

    area_names = [
        ObjectName[i] for i in range(NumberItems)
        if ObjectType[i] == 5
    ]

    # -----------------------------
    # Accumulateurs
    # -----------------------------
    CG_total = np.array([0.0, 0.0, 0.0])
    W_total = 0.0

    # -----------------------------
    # Boucle sur les aires
    # -----------------------------
    for area in area_names:

        numPoints, pointNames, ret = SapModel.AreaObj.GetPoints(area)
        OffsetType, _, _, Offset, ret = SapModel.AreaObj.GetOffsets(area)

        # coordonnées brutes
        coords_raw = []
        for pt in pointNames:
            x, y, z, ret = SapModel.PointObj.GetCoordCartesian(pt)
            coords_raw.append([x, y, z])

        coords_raw = np.array(coords_raw)

        # normale de l'aire
        v1 = coords_raw[1] - coords_raw[0]
        v2 = coords_raw[2] - coords_raw[0]
        normal_area = np.cross(v1, v2)
        normal_area /= np.linalg.norm(normal_area)

        # appliquer offsets (Z local)
        coords = []
        for i in range(numPoints):
            zi = Offset[i] if OffsetType == 2 else 0.0
            pt = coords_raw[i] + zi * normal_area
            coords.append(pt)

        coords = np.array(coords)

        # -----------------------------
        # TEST INTERSECTION PLAN
        # -----------------------------
        distances = [A*P[0] + B*P[1] + C*P[2] + D for P in coords]

        if not (min(distances) <= tol and max(distances) >= -tol):
            continue

        # -----------------------------
        # CALCUL AIRE + CG
        # -----------------------------
        p0 = coords[0]
        A_area = 0.0
        CG = np.array([0.0, 0.0, 0.0])

        for i in range(1, numPoints - 1):
            v1 = coords[i] - p0
            v2 = coords[i+1] - p0

            area_tri = np.linalg.norm(np.cross(v1, v2)) / 2
            cg_tri = (p0 + coords[i] + coords[i+1]) / 3

            A_area += area_tri
            CG += cg_tri * area_tri

        if A_area == 0:
            continue

        CG = CG / A_area

        # -----------------------------
        # DISTANCE AU PLAN
        # -----------------------------
        d = (A*CG[0] + B*CG[1] + C*CG[2] + D) / np.linalg.norm([A, B, C])

        # -----------------------------
        # POIDS
        # -----------------------------
        if use_weighting:
            if sigma is None:
                sigma = 1.0
            w = np.exp(-(d**2) / (2 * sigma**2))
        else:
            w = 1.0

        # -----------------------------
        # ACCUMULATION
        # -----------------------------
        CG_total += CG * A_area * w
        W_total += A_area * w

    # -----------------------------
    # RESULTAT FINAL
    # -----------------------------

    xg,yg,zg = CG_total / W_total

    if W_total > 0:
        return xg,yg,zg
    else:
        return None