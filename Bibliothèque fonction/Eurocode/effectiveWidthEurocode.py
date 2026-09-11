# -*- coding: utf-8 -*-
"""
Largeur efficace de table de compression (poutre en Té / poutre-caisson mixte
dalle+poutre principale) selon EN1992-1-1 §5.3.2.1, pour une poutre continue
sur plusieurs travées repérées par leurs piles d'appui.

Convention :
    - Les abscisses (s, pier_stations) sont des abscisses CURVILIGNES le long
      de l'axe du tablier (m), cohérentes avec centerline_arclength /
      project_arclength utilisés dans generate_loading.py de ce projet.
    - pier_stations : abscisses curvilignes des lignes d'appui (piles/culées),
      triées par ordre croissant. len(pier_stations) - 1 = nombre de travées.
    - b1, b2 : largeurs de table disponibles de part et d'autre de l'âme de
      la poutre (jusqu'à mi-distance de la poutre voisine, ou jusqu'au bord
      du tablier), en m. bw : largeur de l'âme (m).

Référence : EN1992-1-1 §5.3.2.1(1)-(3) et Figure 5.2 (l0 selon la position
le long d'une poutre continue). Le §5.3.2.1(2) autorise explicitement une
largeur efficace CONSTANTE sur toute la travée ("as a simplification, a
constant width may be used over the whole span") : c'est l'approche retenue
ici (2 paliers, "travee" et "appui", pas de transition linéaire type Fig 5.3).

Limites connues (à garder en tête, cf. note de méthode) :
    - Le classement travée d'about / travée courante est déduit uniquement
      de la position dans la liste pier_stations (première/dernière travée
      = "about"). Si une extrémité du tablier n'est PAS une travée de rive
      au sens EN1992-1-1 (continuité au-delà du modèle, appui-cadre, etc.),
      corriger end_span_indices en conséquence.
    - Le régime "appui" est appliqué sur une fenêtre SUPPORT_ZONE_FRACTION x
      (longueur de travée adjacente) de part et d'autre de chaque pile
      INTERMÉDIAIRE (pas aux culées d'about, qui ne sont pas des appuis
      continus au sens de l'EN1992-1-1 §5.3.2.1) ; à ajuster si les about
      sont en réalité encastrés/continus (portique, about intégral...).
"""

import bisect

# ---------------------------------------------------------------------------
# Paramètres modifiables par l'utilisateur
# ---------------------------------------------------------------------------

# Étendue de la "zone d'appui" de part et d'autre de chaque pile intermédiaire,
# en fraction de la travée adjacente (cf. EN1992-1-1 Fig 5.3 : la largeur
# efficace réelle transite entre valeur de travée et valeur d'appui sur une
# distance de l'ordre de 0.1 à 0.15 l ; ce module utilise un palier constant,
# pas une transition linéaire, cf. docstring ci-dessus).
SUPPORT_ZONE_FRACTION = 0.10   # <-- À ajuster

# Largeur efficace TOTALE (bw + beff,1 + beff,2) imposée manuellement sur
# appui, EN REMPLACEMENT du calcul EN1992-1-1 (l0 = 0.25*(l_gauche+l_droite)) :
# à renseigner si une valeur d'ingénieur (jugement, disposition constructive,
# continuité du ferraillage transversal...) doit prévaloir sur le calcul
# automatique pour une pile donnée. Clé : indice de la pile INTERMÉDIAIRE
# concernée (0-based dans pier_stations, la première/dernière pile de la
# liste = about, jamais une clé valide ici) ; valeur : beff totale (m).
USER_DEFINED_SUPPORT_WIDTH = {}   # <-- À ajuster, ex. {2: 2.40} pour la 3e pile

# Facteur multiplicatif appliqué à la largeur EN1992-1-1 calculée sur appui,
# UNIQUEMENT si la pile concernée n'a pas d'entrée dans
# USER_DEFINED_SUPPORT_WIDTH ci-dessus. 1.0 = pas de correction.
EFFECTIVE_WIDTH_SUPPORT_FACTOR = 1.0   # <-- À ajuster


def _span_index(s, pier_stations):
    """Indice k (0-based) de la travée contenant l'abscisse s, telle que
    pier_stations[k] <= s <= pier_stations[k+1]. Borne aux extrémités."""
    n_spans = len(pier_stations) - 1
    k = bisect.bisect_right(pier_stations, s) - 1
    return min(max(k, 0), n_spans - 1)


def classify_station(s, pier_stations, end_span_indices=None):
    """
    Classe l'abscisse s vis-à-vis d'EN1992-1-1 Fig 5.2 : zone ("travee" ou
    "appui"), portée effective l0 associée, et indice de la pile la plus
    proche si zone == "appui".

    Input:
        s : abscisse curviligne (m)
        pier_stations : abscisses curvilignes des lignes d'appui, triées
        end_span_indices : indices de travée (0-based) à traiter comme
            "travée de rive" (coefficient 0.85 au lieu de 0.7). Par défaut
            {0, n_spans-1} (première et dernière travée du tablier).

    Output:
        dict avec les clés :
            "zone"        : "travee" ou "appui"
            "span_index"  : indice de la travée contenant s
            "l0"          : portée effective (m), Fig 5.2
            "pier_index"  : indice de la pile la plus proche (si zone=="appui")
    """
    n_spans = len(pier_stations) - 1
    if n_spans < 1:
        raise ValueError("pier_stations doit contenir au moins 2 abscisses (1 travée).")
    if end_span_indices is None:
        end_span_indices = {0, n_spans - 1}

    k = _span_index(s, pier_stations)
    l_span = pier_stations[k + 1] - pier_stations[k]

    # Distance aux piles intermédiaires encadrant la travée k (une pile
    # d'about, k==0 côté gauche ou k==n_spans-1 côté droit, n'ouvre PAS de
    # zone d'appui : cf. limite documentée en tête de module).
    dist_to_pier_start = s - pier_stations[k]
    dist_to_pier_end = pier_stations[k + 1] - s
    pier_start_is_intermediate = k > 0
    pier_end_is_intermediate = k < n_spans - 1

    near_start = pier_start_is_intermediate and dist_to_pier_start <= SUPPORT_ZONE_FRACTION * l_span
    near_end = pier_end_is_intermediate and dist_to_pier_end <= SUPPORT_ZONE_FRACTION * l_span

    if near_start or near_end:
        pier_index = k if near_start else k + 1
        l_prev = pier_stations[k] - pier_stations[k - 1] if k > 0 else l_span
        l_next = pier_stations[k + 2] - pier_stations[k + 1] if k + 2 <= n_spans else l_span
        # l0 sur appui = 0.25*(l_gauche + l_droite), Fig 5.2 (travées encadrant
        # la pile pier_index) ; ici l_gauche/l_droite = les 2 travées qui se
        # rejoignent à cette pile, donc l_span et sa voisine directe.
        l_gauche = l_prev if near_start else l_span
        l_droite = l_span if near_start else l_next
        l0 = 0.25 * (l_gauche + l_droite)
        return {"zone": "appui", "span_index": k, "l0": l0, "pier_index": pier_index}

    coeff = 0.85 if k in end_span_indices else 0.7
    return {"zone": "travee", "span_index": k, "l0": coeff * l_span, "pier_index": None}


def effective_flange_width_side(bi, l0):
    """EN1992-1-1 §5.3.2.1(3), eq. 5.7a : beff,i = min(0.2*bi + 0.1*l0, 0.2*l0, bi)."""
    return min(0.2 * bi + 0.1 * l0, 0.2 * l0, bi)


def composite_effective_width(s, pier_stations, b1, b2, bw, end_span_indices=None):
    """
    Largeur efficace totale de la table de compression au droit de l'abscisse
    s, EN1992-1-1 §5.3.2.1.

    Input:
        s : abscisse curviligne de la section considérée (m)
        pier_stations : abscisses curvilignes des lignes d'appui (m), triées
        b1, b2 : largeurs de table disponibles de part et d'autre de l'âme
            (m), cf. docstring de module
        bw : largeur de l'âme de la poutre (m)
        end_span_indices : cf. classify_station

    Output:
        dict avec les clés :
            "beff"        : largeur efficace totale (m)
            "beff_1"      : contribution EN1992-1-1 côté 1 (m)
            "beff_2"      : contribution EN1992-1-1 côté 2 (m)
            "zone"        : "travee" ou "appui"
            "l0"          : portée effective utilisée (m)
            "overridden"  : True si beff vient de USER_DEFINED_SUPPORT_WIDTH
    """
    info = classify_station(s, pier_stations, end_span_indices)

    if info["zone"] == "appui" and info["pier_index"] in USER_DEFINED_SUPPORT_WIDTH:
        beff_user = USER_DEFINED_SUPPORT_WIDTH[info["pier_index"]]
        return {
            "beff": beff_user, "beff_1": None, "beff_2": None,
            "zone": info["zone"], "l0": info["l0"], "overridden": True,
        }

    beff_1 = effective_flange_width_side(b1, info["l0"])
    beff_2 = effective_flange_width_side(b2, info["l0"])
    beff = bw + beff_1 + beff_2

    if info["zone"] == "appui":
        beff *= EFFECTIVE_WIDTH_SUPPORT_FACTOR

    return {
        "beff": beff, "beff_1": beff_1, "beff_2": beff_2,
        "zone": info["zone"], "l0": info["l0"], "overridden": False,
    }
