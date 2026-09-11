"""
createLaneGroupsSAP2000.py
=============

Générateur de groupes AreaObj représentant des voies de circulation
("lanes"), construit dans le même esprit que selectLaneSAP2000.py (mêmes
utilitaires area_centroid / areas_of_group, mêmes conventions d'API).

Contrairement à selectLaneSAP2000 (sélection par alignement directionnel
autour d'une seed), ce module positionne une voie par sa largeur et sa
position transversale par rapport à l'axe du tablier ("centerline"), et
restreint chaque groupe résultat à une seule travée à la fois (en
s'appuyant sur les groupes de travée déjà créés, cf. assignSpanGroupsSAP2000).
"""

import numpy as np

from MeshingGeometry.getAreaCentroidsSAP2000 import getAreaCentroidsSAP2000
from MeshingGeometry.getTransverseOffsetsSAP2000 import getTransverseOffsetsSAP2000


def createLaneGroupsSAP2000(SapModel, span_groups, centerline_coord, lane_width,
                             left_edges, right_edges, lane_group_prefix="Voie",
                             position_names=None):
    """
    Crée, pour chaque travée et chaque position transversale demandée, un groupe
    AreaObj représentant une voie de circulation de largeur `lane_width`.

    La position transversale de la voie est définie par ses bords gauche et droit,
    exprimés en distance signée depuis l'axe du tablier ("centerline"), selon la
    même convention de signe que getOffsetPoints/getSlopeNormals du projet (offset
    positif vers le côté "extérieur"/droit de la tangente locale, négatif vers le
    côté "intérieur"/gauche). Pour chaque position, UN SEUL bord doit être fourni
    (l'autre vaut None) : le bord manquant est calculé à partir de `lane_width`, en
    convention "bord droit = bord gauche + lane_width".

    Un AreaObj est considéré comme appartenant à une voie si son centroïde,
    projeté transversalement sur l'axe du tablier (au segment le plus proche), est
    compris dans l'intervalle [bord gauche, bord droit] de cette voie.

    L'existence de chaque groupe (position x travée) est testée individuellement
    avant réassignation : si un groupe de ce nom exact contient déjà des AreaObj,
    il est conservé tel quel (non réassigné) et simplement inclus dans la valeur
    de retour. Les autres combinaisons position/travée dont le nom n'existe pas
    encore sont créées normalement, même si d'autres groupes du même préfixe
    existent déjà.

    Args:
        SapModel: objet SapModel de l'API SAP2000 (modèle actif).
        span_groups: liste des noms de groupes de travée (par ex. la valeur
            retournée par assignSpanGroupsSAP2000), un groupe de voie étant créé
            pour chaque travée de cette liste.
        centerline_coord: liste des points [(x1,y1),(x2,y2),...] (ou avec une 3e
            composante Z ignorée) de l'axe du tablier, dans l'ordre du tracé.
        lane_width: largeur de la voie [m].
        left_edges: liste des positions transversales (depuis centerline) du bord
            gauche de la voie, une valeur par position transversale de voie
            souhaitée. Mettre None pour les positions où c'est le bord droit qui
            est spécifié à la place.
        right_edges: liste des positions transversales du bord droit de la voie,
            même longueur que left_edges, avec None là où c'est left_edges qui est
            renseigné.
        lane_group_prefix: préfixe utilisé pour nommer les voies (par ex. "Voie"
            donne les groupes "Voie1_<travée>", "Voie2_<travée>", ...).
        position_names: si fourni, liste de labels (str) à utiliser à la place du
            numéro de position (1, 2, ...) dans le nom des groupes, même longueur
            que left_edges/right_edges. Par ex. ["G", "D"] avec lane_group_prefix
            "Voie1_" donne les groupes "Voie1_G_<travée>", "Voie1_D_<travée>", ...
            Si None (défaut), les positions sont numérotées 1, 2, 3, ...

    Returns:
        list[str]: liste des noms des groupes effectivement créés (les
        combinaisons voie/travée sans aucun AreaObj ne sont pas créées).

    Raises:
        ValueError: si left_edges et right_edges n'ont pas la même longueur, si
        position_names est fourni avec une longueur différente, ou si une position
        de voie ne spécifie pas exactement un des deux bords.
    """

    # ------------------------------------------------
    # utilitaires (mêmes conventions que selectLaneSAP2000)
    # ------------------------------------------------
    def areas_of_group(gname):
        n, types, names, ret = SapModel.GroupDef.GetAssignments(gname)
        return [name for t, name in zip(types, names) if t == 5]

    # ------------------------------------------------
    # validation et calcul des bords manquants
    # ------------------------------------------------
    if len(left_edges) != len(right_edges):
        raise ValueError("left_edges et right_edges doivent avoir la même longueur.")
    if position_names is not None and len(position_names) != len(left_edges):
        raise ValueError("position_names doit avoir la même longueur que left_edges/right_edges.")

    lane_bounds = []
    for i, (le, re) in enumerate(zip(left_edges, right_edges)):
        if (le is None) == (re is None):
            raise ValueError(
                f"Position de voie {i} : un seul bord (gauche OU droit) doit être spécifié, pas les deux ni aucun."
            )
        if le is None:
            le = re - lane_width
        else:
            re = le + lane_width
        lane_bounds.append((min(le, re), max(le, re)))

    # ------------------------------------------------
    # combinaisons position x travée restant à créer (les groupes déjà
    # existants et non vides sont conservés tels quels, sans recalcul)
    # ------------------------------------------------
    created_groups = []
    pending = []
    for lane_idx, (lo, hi) in enumerate(lane_bounds):
        pos_label = position_names[lane_idx] if position_names is not None else str(lane_idx + 1)
        lane_name = f"{lane_group_prefix}{pos_label}"
        for span_group in span_groups:
            group_name = f"{lane_name}_{span_group}"

            n_items_group, _, _, ret = SapModel.GroupDef.GetAssignments(group_name)
            if ret == 0 and n_items_group > 0:
                created_groups.append(group_name)
                continue

            pending.append((lo, hi, span_group, group_name))

    if not pending:
        return created_groups

    # Centroïde de chaque AreaObj récupéré en un seul appel API (cf.
    # getAreaCentroidsSAP2000), plutôt qu'un calcul par objet dont le coût en
    # appels COM devient prohibitif sur un tablier à plusieurs dizaines de
    # milliers d'AreaObj, a fortiori s'il était jusqu'ici répété pour chaque
    # position de voie.
    centroids = getAreaCentroidsSAP2000(SapModel, "")

    # Offset transversal de chaque AreaObj de chaque travée concernée par au
    # moins une combinaison restant à créer, calculé une seule fois (et non
    # une fois par position de voie) et de façon vectorisée (cf.
    # getTransverseOffsetsSAP2000) plutôt qu'une recherche du segment le plus
    # proche par AreaObj : sur un axe échantillonné sur plusieurs centaines de
    # points, ce calcul point par point devient le facteur limitant une fois
    # les appels API réduits au minimum ci-dessus.
    span_group_offsets = {}
    for span_group in {sg for _, _, sg, _ in pending}:
        areas = areas_of_group(span_group)
        if not areas:
            span_group_offsets[span_group] = []
            continue
        areas_xy = np.array([centroids[a] for a in areas])
        offsets = getTransverseOffsetsSAP2000(areas_xy, centerline_coord)
        span_group_offsets[span_group] = list(zip(areas, offsets))

    # ------------------------------------------------
    # création des groupes voie x travée
    # ------------------------------------------------
    for lo, hi, span_group, group_name in pending:
        group_created = False
        for area, offset in span_group_offsets[span_group]:
            if lo - 1e-9 <= offset <= hi + 1e-9:
                if not group_created:
                    SapModel.GroupDef.SetGroup(group_name)
                    group_created = True
                SapModel.AreaObj.SetGroupAssign(area, group_name)
        if group_created:
            created_groups.append(group_name)

    return created_groups
