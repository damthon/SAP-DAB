import math

def create_section_group_from_point(SapModel, point_master, tangent_vector, group_name,
                                    tol_long=1e-3):
    """
    Crée un groupe contenant tous les PointObj qui appartiennent
    à la même section transversale que 'point_master'.

    Paramètres
    ----------
    point_master : str
        Nom du joint SAP2000 servant de point de référence.
    tangent_vector : tuple(float,float,float)
        Vecteur tangent (Tx,Ty,Tz) de la poutre/pile au point.
    group_name : str
        Nom du groupe SAP2000 à créer/remplacer.
    tol_long : float
        Tolérance sur la projection longitudinale.
    """

    # --- A) Coordonnées du point maître ---
    x0, y0, z0, ret = SapModel.PointObj.GetCoordCartesian(point_master)
    if ret != 0:
        raise RuntimeError(f"Impossible de lire le point maître '{point_master}'")

    P0 = (x0, y0, z0)

    # --- B) Normaliser le vecteur tangent ---
    Tx, Ty, Tz = tangent_vector
    nT = math.sqrt(Tx*Tx + Ty*Ty + Tz*Tz)
    if nT < 1e-12:
        raise ValueError("Vecteur tangent nul")
    Tx, Ty, Tz = Tx/nT, Ty/nT, Tz/nT
    T = (Tx, Ty, Tz)

    # --- C) Récupérer TOUS les points du modèle ---
    n_pts, point_names,ret = SapModel.PointObj.GetNameList()
    if ret != 0:
        raise RuntimeError("Impossible de lire la liste des joints")

    # --- D) Fonction produit scalaire ---
    def dot(A, B):
        return A[0]*B[0] + A[1]*B[1] + A[2]*B[2]

    # --- E) Trouver les points appartenant à la même section ---
    same_section_points = []

    for p in point_names:
        x, y, z, ret2 = SapModel.PointObj.GetCoordCartesian(p)
        if ret2 != 0:
            continue
        if z<z0:
            continue
        v = (x - x0, y - y0, z - z0)

        s = dot(v, T)      # projection longitudinale
        if abs(s) <= tol_long:
            same_section_points.append(p)

    # --- F) (Re)créer un groupe propre ---
    SapModel.GroupDef.Delete(group_name)
    SapModel.GroupDef.SetGroup(group_name)

    # --- G) Y ajouter tous les points trouvés ---
    for p in same_section_points:
        SapModel.PointObj.SetGroupAssign(p, group_name, False)

    print(f"✔ Groupe '{group_name}' créé : {len(same_section_points)} joints trouvés.")
    return same_section_points