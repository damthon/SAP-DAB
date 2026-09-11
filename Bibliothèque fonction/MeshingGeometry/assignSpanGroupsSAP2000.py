import numpy as np

from MeshingGeometry.getAreaCentroidsSAP2000 import getAreaCentroidsSAP2000


def assignSpanGroupsSAP2000(SapModel, deck_group, piles_coord, span_group_prefix="Travee"):
    """
    This function assigns the area objects of a deck (slab) group to span ("travée")
    groups, the spans being delimited in plan by the pier lines formed by consecutive
    pairs of piles. Each pier line is the straight line passing through its 2 piles'
    plan coordinates, extended across the whole width of the deck; it does not need
    to be perpendicular to the bridge centerline. An area object is assigned to the
    span located between the pier line immediately behind it and the pier line
    immediately ahead of it (based on its centroid position), following the pile
    numbering order (piles are numbered consecutively from the start to the end of
    the bridge). Two additional groups are created for the deck areas located before
    the first pier line and after the last one, if any (e.g. end spans reaching to
    an abutment not included in piles_coord).
    Input:
        - SapModel: SAP Model object
        - deck_group: Name of the group containing all the deck area objects
        - piles_coord: List of pile plan coordinates [(x1,y1),(x2,y2)...], one per
          pile, ordered consecutively from the start to the end of the bridge and
          organized in consecutive pairs (2 piles per pier line, e.g. piles 1-2 =
          pier line 1, piles 3-4 = pier line 2, etc.)
        - span_group_prefix: Prefix used to name the created span groups
    Output:
        - span_groups: List of the created span group names, ordered from start to
          end of the bridge. Only groups that actually contain at least one area
          object are created (e.g. the "before first pier line" / "after last pier
          line" groups are omitted if the deck does not extend past the outer piers)
    """

    if len(piles_coord) % 2 != 0:
        raise ValueError("piles_coord doit contenir un nombre pair de piles (une paire par ligne d'appui).")

    pier_lines = [piles_coord[i:i + 2] for i in range(0, len(piles_coord), 2)]
    n_piers = len(pier_lines)

    # Point et normale de chaque ligne d'appui (droite passant par la paire de piles
    # de cette ligne), orientés dans le sens de la numérotation des piles (du début
    # vers la fin de l'ouvrage)
    mids = [np.mean(np.array(pier, dtype=float), axis=0) for pier in pier_lines]
    boundaries = []
    for i, (p1, p2) in enumerate(pier_lines):
        p1 = np.array(p1, dtype=float)
        p2 = np.array(p2, dtype=float)
        line_dir = p2 - p1
        line_dir = line_dir / np.linalg.norm(line_dir)
        normal = np.array([-line_dir[1], line_dir[0]])

        if i < n_piers - 1:
            forward_ref = mids[i + 1] - mids[i]
        elif n_piers > 1:
            forward_ref = mids[i] - mids[i - 1]
        else:
            forward_ref = normal  # ligne d'appui unique : orientation arbitraire

        if np.dot(normal, forward_ref) < 0:
            normal = -normal

        boundaries.append((p1, normal))

    # Récupère les area objects du groupe du tablier (ObjectType 5 = Area object)
    n_items, obj_types, obj_names, ret = SapModel.GroupDef.GetAssignments(deck_group)
    area_names = [obj_names[i] for i in range(n_items) if obj_types[i] == 5]

    # Centroïde de chaque AreaObj récupéré en un seul appel API (cf.
    # getAreaCentroidsSAP2000), plutôt qu'un calcul par objet (AreaObj.GetPoints
    # + PointObj.GetCoordCartesian) dont le coût en appels COM devient
    # prohibitif sur un tablier à plusieurs dizaines de milliers d'AreaObj.
    centroids = getAreaCentroidsSAP2000(SapModel, deck_group)

    span_groups = [f"{span_group_prefix}_{k}" for k in range(n_piers + 1)]
    created_groups = set()

    for area_name in area_names:
        centroid = centroids[area_name]

        signed = [np.dot(centroid - p1, normal) for p1, normal in boundaries]

        if signed[0] < 0:
            span_idx = 0
        elif signed[-1] >= 0:
            span_idx = n_piers
        else:
            span_idx = next(
                (k + 1 for k in range(n_piers - 1) if signed[k] >= 0 and signed[k + 1] < 0),
                n_piers
            )

        group_name = span_groups[span_idx]
        if group_name not in created_groups:
            SapModel.GroupDef.SetGroup(group_name)
            created_groups.add(group_name)
        SapModel.AreaObj.SetGroupAssign(area_name, group_name)

    return [g for g in span_groups if g in created_groups]
