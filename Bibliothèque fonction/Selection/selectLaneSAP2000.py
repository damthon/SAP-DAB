"""
selectLaneSAP2000.py
=============

Outils pour sélectionner, dans un modèle SAP2000, les éléments de type
AreaObj (dalles/plaques) qui sont situés "dans le prolongement" d'un ou
plusieurs éléments de référence, selon une direction donnée.

Principe général utilisé par les trois fonctions :
  1. On calcule le centroïde (centre géométrique) de chaque AreaObj.
  2. On définit un vecteur direction unitaire à partir d'un angle (en degrés).
  3. Pour chaque AreaObj candidate, on regarde si le vecteur qui la relie à
     une AreaObj "seed" (de référence) est quasi-parallèle à la direction
     donnée (produit scalaire proche de 1, à une tolérance angulaire près).
  4. Si c'est le cas, l'AreaObj candidate est considérée comme "dans l'axe"
     de la seed, et donc sélectionnée / affectée au groupe résultat.

Cela permet par exemple de sélectionner automatiquement toutes les dalles
d'une voie de circulation ("lane") alignées avec une zone de départ donnée,
sans avoir à les cliquer une par une dans SAP2000.
"""

import math

import numpy as np


def selectLaneSAP2000(SapModel,
               group_global,
               group_seed,
               angle_deg,
               angle_tol_deg=0.1,
               assign_to_group=None):
    """
    Sélectionne les AreaObj du groupe `group_global` qui sont dans le
    prolongement directionnel d'au moins une AreaObj du groupe `group_seed`.

    La comparaison directionnelle est faite individuellement pour chaque
    AreaObj "seed" : une AreaObj candidate est retenue dès qu'elle est
    alignée avec AU MOINS une des seeds (pas besoin d'être alignée avec
    toutes).

    Args:
        SapModel: objet SapModel de l'API SAP2000 (modèle actif).
        group_global: nom du groupe contenant l'ensemble des AreaObj
            candidates (ex : toutes les dalles du tablier).
        group_seed: nom du groupe contenant les AreaObj de référence
            ("point de départ" de la direction recherchée).
        angle_deg: angle (en degrés) de la direction dans laquelle on
            cherche les AreaObj alignées, mesuré dans le plan XY.
        angle_tol_deg: tolérance angulaire (en degrés) autour de la
            direction `angle_deg` pour considérer une AreaObj comme
            "alignée". Plus la valeur est petite, plus le critère est
            strict.
        assign_to_group: si fourni, nom du groupe SAP2000 dans lequel les
            AreaObj sélectionnées seront affectées. Si None, les AreaObj
            sont simplement sélectionnées dans l'interface SAP2000 (comme
            si on les avait cliquées à la main).

    Returns:
        list[str]: liste des noms des AreaObj sélectionnées (candidates
        uniquement, les seeds ne sont pas incluses dans la valeur de
        retour, mais elles SONT ajoutées au groupe `assign_to_group`,
        voir note ci-dessous).

    Raises:
        ValueError: si `group_seed` ne contient aucune AreaObj.

    Note:
        Si `assign_to_group` vaut None, l'appel `SetGroupAssign(a, None)`
        effectué plus bas pour les AreaObj seed provoquera probablement une
        erreur côté API SAP2000 (un nom de groupe est attendu). Pensez à
        toujours fournir `assign_to_group` si vous voulez que les seeds
        soient aussi affectées à un groupe.
    """

    # ------------------------------------------------
    # utilitaires
    # ------------------------------------------------
    def area_centroid(area):
        """Calcule le centroïde (x, y, z) d'une AreaObj en moyennant les
        coordonnées de tous ses points (joints)."""
        n, pts, ret = SapModel.AreaObj.GetPoints(area)
        coords = []
        for p in pts:
            x, y, z = SapModel.PointObj.GetCoordCartesian(p)[0:3]
            coords.append([x, y, z])
        return np.mean(coords, axis=0)

    def areas_of_group(gname):
        """Retourne la liste des noms d'AreaObj (type=5 dans l'API SAP2000)
        appartenant au groupe `gname`."""
        n, types, names, ret = SapModel.GroupDef.GetAssignments(gname)
        return [name for t, name in zip(types, names) if t == 5]

    # ------------------------------------------------
    # récupérer les aires
    # ------------------------------------------------
    areas_global = areas_of_group(group_global)
    areas_seed = areas_of_group(group_seed)

    if not areas_seed:
        raise ValueError("Le groupe seed est vide")

    # ------------------------------------------------
    # centroïdes des seeds (calculés une seule fois, individuellement)
    # ------------------------------------------------
    seed_centroids = {
        a: area_centroid(a) for a in areas_seed
    }

    # ------------------------------------------------
    # vecteur direction global (dans le plan XY)
    # ------------------------------------------------
    alpha = math.radians(angle_deg)
    d = np.array([math.cos(alpha), math.sin(alpha)])
    d /= np.linalg.norm(d)  # normalisation (par sécurité, déjà unitaire)

    # Produit scalaire minimal (cosinus) pour qu'un vecteur soit considéré
    # comme "aligné" avec la direction d, compte tenu de la tolérance
    # angulaire. cos(angle_tol_deg) est proche de 1 pour une petite
    # tolérance : plus dot > cos_tol est strict, plus l'alignement doit
    # être précis.
    cos_tol = math.cos(math.radians(angle_tol_deg))

    selected = []

    # ------------------------------------------------
    # sélection directionnelle (seed par seed)
    # ------------------------------------------------
    for a_cand in areas_global:
        # On ignore les AreaObj qui sont elles-mêmes des seeds
        if a_cand in areas_seed:
            continue

        Cc = area_centroid(a_cand)

        # On compare la candidate à chaque seed individuellement : il
        # suffit qu'elle soit alignée avec UNE seule seed pour être retenue.
        for Cs in seed_centroids.values():
            # Vecteur (en 2D, XY) allant de la seed vers la candidate
            v = Cc[:2] - Cs[:2]
            norm_v = np.linalg.norm(v)

            # Si la candidate est quasiment au même endroit que la seed,
            # la direction n'a pas de sens : on ignore cette comparaison.
            if norm_v < 1e-6:
                continue

            v_unit = v / norm_v
            dot = np.dot(v_unit, d)  # cosinus de l'angle entre v et d

            # "devant" (même sens que d) ET aligné (dot proche de 1)
            if dot > cos_tol:
                selected.append(a_cand)
                break  # une seule seed alignée suffit, inutile de tester les autres

    # ------------------------------------------------
    # affectation au groupe résultat, ou simple sélection graphique
    # ------------------------------------------------
    if assign_to_group:
        # Crée (ou réutilise) le groupe cible, puis y affecte chaque
        # AreaObj candidate retenue.
        SapModel.GroupDef.SetGroup(assign_to_group)
        for a in selected:
            SapModel.AreaObj.SetGroupAssign(a, assign_to_group)
    else:
        # Pas de groupe cible : on se contente de sélectionner les AreaObj
        # dans le modèle SAP2000 (équivalent à une sélection manuelle),
        # après avoir d'abord tout désélectionné.
        SapModel.SelectObj.All(False)
        for a in selected:
            SapModel.AreaObj.SetSelected(a, True)

    # ✅ ajouter aussi les aires SEED au groupe résultat
    # (Attention : si assign_to_group est None, cet appel passera None comme
    # nom de groupe à l'API, ce qui provoquera probablement une erreur.)
    for a in areas_seed:
        SapModel.AreaObj.SetGroupAssign(a, assign_to_group)

    return selected


def selectLane_fromSelection(SapModel,
                             assign_to_group=None,
                             group_global='Tablier',
                             angle_deg=(90 - 24),
                             angle_tol_deg=0.1
                             ):
    """
    Variante de `selectLane` qui utilise comme "seeds" les AreaObj
    actuellement sélectionnées dans SAP2000 (plutôt qu'un groupe seed
    nommé) : pratique pour un usage interactif — on sélectionne d'abord
    quelques dalles à la souris dans SAP2000, puis on appelle cette
    fonction pour étendre la sélection dans une direction donnée.

    Les AreaObj initialement sélectionnées sont conservées dans le
    résultat final (contrairement à `selectLane`, où les seeds sont
    traitées à part).

    Args:
        SapModel: objet SapModel de l'API SAP2000 (modèle actif).
        assign_to_group: si fourni, nom du groupe SAP2000 dans lequel
            toutes les AreaObj retenues (seeds + candidates alignées)
            seront affectées et sélectionnées. Si None, les AreaObj sont
            simplement sélectionnées dans SAP2000.
        group_global: nom du groupe contenant l'ensemble des AreaObj
            candidates (par défaut : 'Tablier').
        angle_deg: angle (en degrés) de la direction recherchée dans le
            plan XY. Valeur par défaut : 90 - 24 = 66°.
        angle_tol_deg: tolérance angulaire (en degrés) autour de
            `angle_deg` pour considérer une AreaObj comme alignée.

    Returns:
        list[str]: liste des noms de toutes les AreaObj retenues (seeds
        sélectionnées à l'origine + candidates alignées trouvées).

    Raises:
        ValueError: si aucune AreaObj n'est actuellement sélectionnée
        dans le modèle (parmi celles du groupe `group_global`).
    """

    # ------------------------------------------------
    # utilitaires (identiques à ceux de selectLane)
    # ------------------------------------------------
    def area_centroid(area):
        """Calcule le centroïde (x, y, z) d'une AreaObj."""
        n, pts, ret = SapModel.AreaObj.GetPoints(area)
        coords = []
        for p in pts:
            x, y, z = SapModel.PointObj.GetCoordCartesian(p)[0:3]
            coords.append([x, y, z])
        return np.mean(coords, axis=0)

    def areas_of_group(gname):
        """Retourne la liste des noms d'AreaObj (type=5) du groupe `gname`."""
        n, types, names, ret = SapModel.GroupDef.GetAssignments(gname)
        return [name for t, name in zip(types, names) if t == 5]

    # ------------------------------------------------
    # récupérer les aires globales (toutes les candidates possibles)
    # ------------------------------------------------
    areas_global = areas_of_group(group_global)

    # ------------------------------------------------
    # récupérer les aires SEED depuis la sélection actuelle dans SAP2000
    # ------------------------------------------------
    selected_areas = [
        a for a in areas_global if SapModel.AreaObj.GetSelected(a)[0]
    ]

    if not selected_areas:
        raise ValueError("Aucune AreaObj sélectionnée dans le modèle")

    # ------------------------------------------------
    # centroïdes des seeds
    # ------------------------------------------------
    seed_centroids = {a: area_centroid(a) for a in selected_areas}

    # ------------------------------------------------
    # vecteur direction global (dans le plan XY)
    # ------------------------------------------------
    alpha = math.radians(angle_deg)
    d = np.array([math.cos(alpha), math.sin(alpha)])
    d /= np.linalg.norm(d)

    cos_tol = math.cos(math.radians(angle_tol_deg))

    selected = []

    # ------------------------------------------------
    # sélection directionnelle (identique au principe de selectLane)
    # ------------------------------------------------
    for a_cand in areas_global:
        if a_cand in selected_areas:
            continue

        Cc = area_centroid(a_cand)

        for Cs in seed_centroids.values():
            # Garde-fou : si le centroïde n'est pas un tableau exploitable
            # (cas normalement impossible avec area_centroid, mais gardé
            # par sécurité), on ignore cette comparaison.
            if isinstance(Cc, float):
                continue

            v = Cc[:2] - Cs[:2]
            norm_v = np.linalg.norm(v)

            if norm_v < 1e-6:
                continue

            v_unit = v / norm_v
            dot = np.dot(v_unit, d)

            if dot > cos_tol:
                selected.append(a_cand)
                break  # une seed alignée suffit

    # ------------------------------------------------
    # fusion des candidates trouvées et des seeds d'origine
    # ------------------------------------------------
    # set() élimine les doublons éventuels, puis on repasse en liste.
    all_final = list(set(selected + selected_areas))

    if assign_to_group:
        SapModel.GroupDef.SetGroup(assign_to_group)
        for a in all_final:
            SapModel.AreaObj.SetGroupAssign(a, assign_to_group)
            SapModel.AreaObj.SetSelected(a, True)
    else:
        SapModel.SelectObj.All(False)
        for a in all_final:
            SapModel.AreaObj.SetSelected(a, True)

    return all_final


def get_points_with_min_Y_in_area_group(SapModel, group_name, tol=1e-6):
    """
    Retourne la liste des noms de joints (PointObj) ayant la coordonnée Y
    minimale parmi tous les points de toutes les AreaObj appartenant à un
    groupe donné.

    Utile par exemple pour identifier automatiquement les joints situés sur
    le bord "amont" (Y minimal) d'une zone de tablier, sans les repérer
    manuellement.

    Parameters
    ----------
    SapModel : SapModel SAP2000
        Objet SapModel de l'API SAP2000 (modèle actif).
    group_name : str
        Nom du groupe d'AreaObj à analyser.
    tol : float
        Tolérance numérique sur la comparaison des coordonnées Y : tout
        point dont le Y est à moins de `tol` du minimum est inclus dans le
        résultat (permet de récupérer plusieurs points alignés sur un même
        bord, malgré de petites imprécisions numériques).

    Returns
    -------
    list[str]
        Liste des noms de joints ayant la coordonnée Y minimale (à `tol`
        près).

    Raises
    ------
    ValueError
        Si le groupe `group_name` ne contient aucune AreaObj.
    """

    # 1) Récupérer les AreaObj du groupe (type=5 = AreaObj dans l'API SAP2000)
    n, types, names, ret = SapModel.GroupDef.GetAssignments(group_name)
    area_names = [name for t, name in zip(types, names) if t == 5]

    if not area_names:
        raise ValueError(f"Aucune AreaObj dans le groupe '{group_name}'")

    # 2) Récupérer tous les points (joints) de ces AreaObj, avec leur Y.
    #    On utilise un dict pour éviter de traiter deux fois un même point
    #    partagé par plusieurs AreaObj.
    point_Y = {}  # point_name -> Y

    for area in area_names:
        n_pts, pts, ret = SapModel.AreaObj.GetPoints(area)
        for p in pts:
            if p not in point_Y:  # éviter les doublons
                x, y, z = SapModel.PointObj.GetCoordCartesian(p)[0:3]
                point_Y[p] = y

    # 3) Trouver la valeur Y minimale parmi tous les points collectés
    min_Y = min(point_Y.values())

    # 4) Sélectionner tous les points dont le Y est proche du minimum
    #    (à la tolérance `tol` près, pour absorber les imprécisions
    #    numériques entre points censés être alignés).
    min_Y_points = [
        p for p, y in point_Y.items() if abs(y - min_Y) <= tol
    ]

    return min_Y_points
