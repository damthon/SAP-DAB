import numpy as np

from MeshingGeometry.getAreaCentroidsSAP2000 import getAreaCentroidsSAP2000
from MeshingGeometry.getTransverseOffsetsSAP2000 import getTransverseOffsetsSAP2000


def assignTransverseGroupsSAP2000(SapModel, span_groups, centerline_coord, separators,
                                   group_prefix="Zone", position_names=None):
    """
    This function partitions, independently for each span ("travée") group, its
    area objects into transverse zones delimited by a list of transverse
    separator distances from the deck centerline. The (sorted) separator values
    directly define the zone edges: zone i is the interval
    [separators[i], separators[i+1]], so len(separators) values define
    len(separators) - 1 zones per travée (a bounded strip between each pair of
    consecutive separators). An area object is assigned to the zone in which its
    centroid's transverse offset (signed distance to the nearest centerline
    segment) falls, using the same sign convention as
    getOffsetPoints/getSlopeNormals of the project (positive offset towards the
    "outer"/right side of the local tangent). Area objects whose offset falls
    outside [min(separators), max(separators)] are not assigned to any zone.

    The existence of each zone/travée group is tested individually before
    (re)assignment: if a group of that exact name already contains area objects,
    it is left untouched (not reassigned) and simply included in the return
    value. Zone/travée combinations whose group name does not exist yet are
    created normally, even if other groups of the same prefix already exist.
    Input:
        - SapModel: SAP Model object
        - span_groups: List of span (travée) group names to process (e.g. the
          value returned by assignSpanGroupsSAP2000), one set of zone groups
          being created per travée of this list
        - centerline_coord: List of centerline points [(x1,y1),(x2,y2)...] (a 3rd
          Z component is ignored if present), in the order of the trace
        - separators: List of at least 2 transverse separator distances from
          centerline [m] delimiting the zone edges, not necessarily sorted
        - group_prefix: Prefix used to name the created zone groups (e.g. "Zone"
          gives "Zone1_<travée>", "Zone2_<travée>", ... ordered from the most
          negative offset zone to the most positive)
        - position_names: if given, list of labels (str) used instead of the zone
          number (1, 2, ...) in the group names, same length as
          len(separators) - 1 (the number of zones). If None (default), zones
          are numbered 1, 2, 3, ... from the most negative offset zone.
    Output:
        - zone_groups: List of the zone group names (created or already
          existing), ordered by travée (in the order of span_groups) then by
          increasing transverse offset. Only zone/travée combinations containing
          at least one area object are included.
    """

    def areas_of_group(gname):
        n, types, names, ret = SapModel.GroupDef.GetAssignments(gname)
        return [name for t, name in zip(types, names) if t == 5]

    sorted_separators = sorted(separators)
    n_zones = len(sorted_separators) - 1
    if n_zones < 1:
        raise ValueError("separators doit contenir au moins 2 valeurs (bornes) pour définir au moins une zone.")
    if position_names is not None and len(position_names) != n_zones:
        raise ValueError("position_names doit contenir len(separators) - 1 labels (un par zone).")

    def zone_label(z):
        return position_names[z] if position_names is not None else str(z + 1)

    zone_group_names = [
        f"{group_prefix}{zone_label(z)}_{span_group}"
        for span_group in span_groups
        for z in range(n_zones)
    ]
    created_groups = set()
    existing_status = {}

    def group_exists_nonempty(name):
        if name not in existing_status:
            n_items, _, _, ret = SapModel.GroupDef.GetAssignments(name)
            existing_status[name] = (ret == 0 and n_items > 0)
        return existing_status[name]

    # Si tous les groupes attendus existent déjà (et sont non vides), on évite le
    # parcours coûteux de tous les AreaObj (GetPoints/GetCoordCartesian pour chacun)
    if all(group_exists_nonempty(g) for g in zone_group_names):
        return zone_group_names

    # Centroïde de chaque AreaObj récupéré en un seul appel API (cf.
    # getAreaCentroidsSAP2000), plutôt qu'un calcul par objet dont le coût en
    # appels COM devient prohibitif sur un tablier à plusieurs dizaines de
    # milliers d'AreaObj.
    centroids = getAreaCentroidsSAP2000(SapModel, "")

    for span_group in span_groups:
        areas = areas_of_group(span_group)
        if not areas:
            continue

        # Offset transversal de tous les AreaObj de la travée calculé en un
        # seul passage vectorisé (cf. getTransverseOffsetsSAP2000), plutôt
        # qu'une recherche du segment le plus proche par AreaObj : sur un axe
        # échantillonné sur plusieurs centaines de points, ce calcul point par
        # point devient le facteur limitant une fois les appels API réduits
        # au minimum ci-dessus.
        areas_xy = np.array([centroids[a] for a in areas])
        offsets = getTransverseOffsetsSAP2000(areas_xy, centerline_coord)

        for area, offset in zip(areas, offsets):
            zone_idx = next(
                (z for z in range(n_zones)
                 if sorted_separators[z] - 1e-9 <= offset <= sorted_separators[z + 1] + 1e-9),
                None
            )
            if zone_idx is None:
                continue  # hors de [min(separators), max(separators)] : non assigné

            group_name = f"{group_prefix}{zone_label(zone_idx)}_{span_group}"

            # Groupe déjà existant (et non vide) : on le laisse tel quel
            if group_exists_nonempty(group_name):
                created_groups.add(group_name)
                continue

            if group_name not in created_groups:
                SapModel.GroupDef.SetGroup(group_name)
                created_groups.add(group_name)
            SapModel.AreaObj.SetGroupAssign(area, group_name)

    return [g for g in zone_group_names if g in created_groups]
