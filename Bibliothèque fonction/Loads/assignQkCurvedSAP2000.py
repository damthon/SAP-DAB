# -*- coding: utf-8 -*-
"""
assignQkCurvedSAP2000.py
=========================

Variante de assignQkSAP2000 (modèle de charge 1, SIA 261) pour un tablier
courbe : l'empreinte des 4 pneus de l'essieu (espacement 1.2 m dans le sens
longitudinal, 2.0 m dans le sens transversal) est orientée selon la tangente
locale à l'axe du tablier au droit du point d'application O, et non selon les
axes globaux X/Y comme dans assignQkSAP2000. Cette dernière reste inchangée
(utilisée par d'autres projets) : le présent module s'ajoute à côté d'elle
pour les cas de tablier courbe.
"""

import numpy as np

from Selection.getGroupAreaObjSAP2000 import getGroupAreaObjSAP2000


def assignQkCurvedSAP2000(SapModel, O, r_inf, lane, l_pattern, value, tangent):
    """
    Crée les charges nodales des 4 pneus d'un essieu (modèle de charge 1, SIA 261)
    et les répartit sur les joints du maillage existant, en orientant l'empreinte
    de l'essieu selon la tangente locale de l'axe du tablier plutôt que selon les
    axes globaux X/Y (cf. assignQkSAP2000, dont ce module est une variante).

    Input:
        SapModel: SAP Model object
        O: Centre de l'essieu (point milieu entre les 4 pneus), en m [x, y, z]
        r_inf: Rayon d'influence en m, cf. docstring de assignQkSAP2000
        lane: Groupe de voie auquel les charges de pneu sont ajoutées
        l_pattern: Load pattern
        value: Charges par pneu [Vertical, Horizontal, Moment dû à l'horizontal]
            (kN, kN, kNm). La charge horizontale est appliquée selon la tangente
            locale (et non global X comme dans assignQkSAP2000) ; la charge
            verticale selon global Z.
        tangent: [dx, dy] direction (pas nécessairement unitaire) de la tangente à
            l'axe du tablier au droit de O, dans le plan global XY. L'espacement
            des pneus (1.2 m longitudinal, 2.0 m transversal) est appliqué selon ce
            repère local (tangent, normale) plutôt que selon global X/Y, pour que
            l'empreinte de l'essieu suive l'orientation réelle (courbe) du tablier
            en O.
    """

    # Set kN-m unit system
    SapModel.SetPresentUnits(6)

    tan_dir = np.array(tangent[0:2], dtype=float)
    tan_dir = tan_dir / np.linalg.norm(tan_dir)
    normal_dir = np.array([tan_dir[1], -tan_dir[0]])

    # Create tyres
    # Tyre centerpoints, dans le repère local (tangent, normale) au droit de O
    dx = [-0.6, -0.6, 0.6, 0.6]  # Delta longitudinal (tangent) pour chaque pneu
    dy = [-1, 1, 1, -1]  # Delta transversal (normale) pour chaque pneu

    # Tyre coordinates
    tyre_coord_x = [[], [], [], []]
    tyre_coord_y = [[], [], [], []]
    tyre_coord_z = [[], [], [], []]
    tyre_center = [None, None, None, None]
    for i in range(len(tyre_coord_x)):
        cx = O[0] + dx[i] * tan_dir[0] + dy[i] * normal_dir[0]
        cy = O[1] + dx[i] * tan_dir[1] + dy[i] * normal_dir[1]
        tyre_center[i] = (cx, cy)
        tyre_coord_x[i] = [cx - 0.4 / 2, cx - 0.4 / 2, cx + 0.4 / 2, cx + 0.4 / 2]
        tyre_coord_y[i] = [cy - 0.4 / 2, cy + 0.4 / 2, cy + 0.4 / 2, cy - 0.4 / 2]
        tyre_coord_z[i] = [O[2], O[2], O[2], O[2]]

    # Check lane joints that lie within the circle of influence
    lane_joints_loaded = [[], [], [], []]  # Loaded lane joints at each tyre
    lane_area_objects = getGroupAreaObjSAP2000(SapModel, lane)  # Lane area objects

    for i in range(len(lane_area_objects)):
        area_points = SapModel.AreaObj.GetPoints(lane_area_objects[i])[1]
        for j in range(len(area_points)):
            x_joint = SapModel.PointObj.GetCoordCartesian(area_points[j])[0]
            y_joint = SapModel.PointObj.GetCoordCartesian(area_points[j])[1]
            # Check if joint within circle of each tyre
            for k in range(4):  # 4 tyres
                if ((x_joint - tyre_center[k][0]) ** 2 + (y_joint - tyre_center[k][1]) ** 2) ** 0.5 <= r_inf:
                    lane_joints_loaded[k].append(area_points[j])

    for k in range(len(lane_joints_loaded)):
        lane_joints_loaded[k] = list(set(lane_joints_loaded[k]))
        if len(lane_joints_loaded[k]) == 0:
            print('Tyres for ' + l_pattern + ' outside lane!')

    for i in range(4):
        for j in range(len(lane_joints_loaded[i])):
            SapModel.PointObj.SetSelected(lane_joints_loaded[i][j], True, 0)

    # Load joints
    d = [[], [], [], []]  # Distance from each loaded joint to center of each tyre
    for i in range(4):  # Number of tyres
        for j in range(len(lane_joints_loaded[i])):  # Loaded joints
            x_ij = SapModel.PointObj.GetCoordCartesian(lane_joints_loaded[i][j])[0]
            y_ij = SapModel.PointObj.GetCoordCartesian(lane_joints_loaded[i][j])[1]
            d_ij = ((x_ij - tyre_center[i][0]) ** 2 + (y_ij - tyre_center[i][1]) ** 2) ** 0.5
            d[i].append(d_ij)

    # Ratio of axle load at each joint (inverse-distance weighting)
    w = [[], [], [], []]  # Weights
    r = [[], [], [], []]  # Ratio at each loaded joint
    for i in range(4):  # Number of tyres
        for j in range(len(d[i])):
            w[i].append(1 / (d[i][j] + 0.01))  # 0.01 to remove singularity
    for i in range(4):  # Number of tyres
        for j in range(len(d[i])):
            r[i].append(w[i][j] / sum(w[i]))

    # Assign loads : la composante horizontale (value[1]) et son moment (value[2])
    # sont projetés sur le repère local (tangent, normale) plutôt qu'appliqués
    # directement selon global X, pour rester cohérents avec l'orientation locale
    # de l'empreinte ci-dessus.
    for i in range(4):  # Number of tyres
        for j in range(len(lane_joints_loaded[i])):
            f1 = value[1] * r[i][j] * tan_dir[0]
            f2 = value[1] * r[i][j] * tan_dir[1]
            m1 = -value[2] * r[i][j] * normal_dir[0]
            m2 = -value[2] * r[i][j] * normal_dir[1]
            SapModel.PointObj.SetLoadForce(
                lane_joints_loaded[i][j], l_pattern,
                [f1, f2, -value[0] * r[i][j], m1, m2, 0], 1, 'Global', 0
            )

    return None
