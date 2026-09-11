import numpy as np


def getTransverseOffsetsSAP2000(points_xy, centerline_coord):
    """
    Calcule, pour un ensemble de points (ex. centroïdes d'AreaObj), l'offset
    transversal signé de chacun à l'axe centerline_coord (distance au segment
    de l'axe le plus proche, projetée sur la normale locale), selon la même
    convention de signe que le reste du projet (positif vers le côté
    "droit"/extérieur de la tangente locale).

    Version vectorisée (tous les points traités simultanément, un seul passage
    par segment de l'axe) d'un calcul auparavant fait point par point avec une
    recherche du segment le plus proche parcourant tout l'axe pour chaque point
    (coût O(n_points x n_segments) en boucles Python pures). Sur un tablier à
    plusieurs dizaines de milliers d'AreaObj et un axe échantillonné sur
    plusieurs centaines de points, ce calcul point par point devient le facteur
    limitant une fois les appels à l'API SAP2000 eux-mêmes réduits au minimum
    (cf. getAreaCentroidsSAP2000) : par exemple ~12 minutes pour 100'000 points
    sur un axe à 683 segments en boucle Python, contre quelques secondes en
    version vectorisée (écart numérique négligeable, de l'ordre de l'erreur
    d'arrondi flottant).

    Input:
        - points_xy: array-like (N, 2) des coordonnées XY des points
        - centerline_coord: liste des points de l'axe [(x,y),...] ou
          [(x,y,z),...] (une 3e composante Z est ignorée si présente), dans
          l'ordre du tracé
    Output:
        - offsets: array numpy (N,) des offsets transversaux signés, dans le
          même ordre que points_xy
    """
    pts = np.asarray(points_xy, dtype=float)
    cl = np.asarray(centerline_coord, dtype=float)[:, :2]

    a = cl[:-1]
    b = cl[1:]
    ab = b - a
    seg_len2 = np.einsum("ij,ij->i", ab, ab)

    best_dist = np.full(len(pts), np.inf)
    best_offset = np.zeros(len(pts))

    for i in np.nonzero(seg_len2 > 1e-12)[0]:
        ai, abi, l2 = a[i], ab[i], seg_len2[i]
        t = np.clip((pts - ai) @ abi / l2, 0.0, 1.0)
        proj = ai + t[:, None] * abi
        d = pts - proj
        dist = np.linalg.norm(d, axis=1)
        tangent = abi / np.sqrt(l2)
        normal = np.array([tangent[1], -tangent[0]])
        offset = d @ normal
        mask = dist < best_dist
        best_dist[mask] = dist[mask]
        best_offset[mask] = offset[mask]

    return best_offset
