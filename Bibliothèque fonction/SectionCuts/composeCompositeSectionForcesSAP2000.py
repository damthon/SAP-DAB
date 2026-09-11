# -*- coding: utf-8 -*-
"""
Combine, en un point de référence commun (typiquement le centre de gravité
de la section composite dalle + poutre principale), les efforts issus :
    - d'un Section Cut "Design Slab" sur la dalle (cf. createSectionCutsSAP2000
      / bridgeDeckSectionCutsSAP2000 / getSectionCutForcesSAP2000, package
      SectionCuts) ;
    - d'un Frame Object représentant la poutre principale (résultats natifs
      SapModel.Results.FrameForce, cf. OutputDesign/frameSectionForces.py).

Pourquoi ne PAS réutiliser tel quel le transport par Delta_location de
getSectionCutForcesSAP2000.py :
    getSectionCutForcesSAP2000.SetResultLocation applique le décalage
    Delta_location=[d2,d3] directement aux coordonnées GLOBALES Y et Z
    (Y += d2, Z += d3), ce qui n'est rigoureusement exact QUE si l'axe local
    1 du Section Cut est aligné sur l'axe global X (auquel cas l'axe local 2
    coïncide avec Y global et l'axe local 3 avec Z global). Sur un tablier
    courbe ou biais, l'axe local 1 (tangente) n'est PAS aligné sur X global
    (cf. SC_angles calculé par createSectionCutsSAP2000/bridgeDeckSectionCuts
    SAP2000 précisément pour capturer cette rotation) : appliquer d2/d3
    directement à Y/Z global serait donc une erreur de transport pour ce
    projet (tablier courbe, cf. axe tablier.xlsx).

    Ce module transporte au contraire les efforts en repère GLOBAL, par un
    produit vectoriel classique, valable quelle que soit l'orientation du
    Section Cut ou du Frame Object :

        M_nouveau_point = M_ancien_point + F_global x (point_nouveau - point_ancien)

    (vérifié analytiquement en fin de fichier, cf. _self_check_transport).

Convention d'axes retenue pour le REPÈRE LOCAL DU TABLIER (utilisé pour
ré-exprimer le résultat final de façon lisible, indépendamment de la
numérotation d'axes locaux propre à SAP2000) :
    e_L : tangente à l'axe du tablier (longitudinal)
    e_T : transversale horizontale (perpendiculaire à e_L, dans le plan XY)
    e_V : verticale = (0,0,1) global

Axes locaux SAP2000 des deux objets (CORRIGÉ le 2026-08-25, cf. ci-dessous) :
    - Section Cut "Design Slab" (SetLocalAxesAngleDesign, angle = angle entre
      X global et l'axe local 1) : axe local 2 = VERTICAL (global Z), axe
      local 3 = TRANSVERSE horizontal.
    - Frame Object "poutre" (axe local 1 le long de l'élément) : convention
      SAP2000 par défaut pour un élément proche de l'horizontale -> axe
      local 2 tend vers la VERTICALE, axe local 3 est transverse horizontal.
      C'est donc la MÊME convention que le Section Cut ci-dessus, et non
      l'inverse comme ce module l'a supposé jusqu'au 2026-08-25. Cohérent
      avec l'usage constant du dépôt : OutputDesign/frameSectionForces.py et
      PostTraitement/get_Frame_Force.py utilisent tous deux M3 (indice 13 du
      tuple Results.FrameForce) comme moment de flexion "principal" des
      poutres longitudinales.
    Ce module ne se fie PAS à un numéro d'axe fixe : il reconstruit le
    repère global réel de chaque objet (matrice de transformation SAP2000
    pour le Frame, reconstruction géométrique pour le Section Cut) puis
    reprojette sur (e_L, e_T, e_V).

=============================================================================
CORRECTION DU 2026-08-25 - AXES LOCAUX 2 ET 3 DU SECTION CUT INTERVERTIS
=============================================================================
Jusqu'à cette date, section_cut_local_axes_global() supposait que l'axe local
3 d'un Section Cut "Design Slab" était VERTICAL et l'axe local 2 transversal.
Cette hypothèse, que ce docstring signalait lui-même comme "À VÉRIFIER
visuellement dans SAP2000 avant tout usage en production", est FAUSSE : c'est
l'inverse. Deux vérifications indépendantes :

  1. SAP2000 l'énonce lui-même, dans la boîte de dialogue de définition du
     Section Cut (Define > Section Cuts > Modify/Show, cadre "Section Cut
     Local Axes Orientation - Design", option "Slab") :

         "Slab: Local 2 axis is parallel to global Z.
          1 and 3 axes lie in global XY plane."

     C'est la source faisant autorité : l'axe 2 est vertical, les axes 1 et 3
     sont horizontaux. (Relevé sur le modèle du viaduc Plaine de l'Orbe,
     Section Cut "Composite_PG_0047.32", D. Balmer.)
  2. Modèle de validation à solution exacte - poutre continue 3 x 33.8 m,
     dalle 0.24 m collaborante, charge uniforme (cf. PostTraitement/
     validation_composite_beam.py, projet 9BV024 Viaduc Plaine de l'Orbe).
     Sur 37 sections de contrôle, le rapport |M2 / P| du Section Cut vaut
     0.661 m +/- 0.009 m, soit exactement le bras de levier TRANSVERSAL entre
     le point de report du cut et l'axe de la poutre (0.665 m) : M2 est donc
     le moment autour de la VERTICALE (flexion "en plan"), et non la flexion
     longitudinale. Physiquement, le traînage de cisaillement concentre la
     résultante de compression de la dalle au droit de la poutre. Contrôle
     croisé : la flexion longitudinale PROPRE de la dalle ne peut valoir, par
     la mécanique (E x I_dalle x courbure), que ~70 kNm dans ce modèle, alors
     que |M2| y atteint 4000 kNm.

Avec l'ancienne convention, le moment composite recombiné était faux de 74 %
(écart max) / 48 % (RMS) sur ce modèle de référence.

IMPACT : tout résultat produit par ce module avant le 2026-08-25 est à
recalculer (flexion longitudinale de la dalle et moment en plan intervertis).

SIGNE des efforts rapportés : il résulte de DEUX facteurs distincts, à ne pas
confondre.
  - La DIRECTION de l'axe local 1, donnée par "Angle from Global X to Local 1"
    dans la même boîte de dialogue. Elle est connue sans ambiguïté : c'est
    exactement l'angle passé à SetLocalAxesAngleDesign, donc
    e1 = (cos(angle), sin(angle), 0) sans correction à apporter.
  - Le CÔTÉ des éléments depuis lequel les résultats sont lus ("Results
    Reported Are On This Side of Elements : Right / Left" dans la boîte de
    dialogue ; SectCut.GetResultsSide renvoie 1 = Right, 2 = Left pour un
    Design Slab). Un Section Cut ne rapporte les efforts que d'un seul côté de
    la coupe : selon le côté retenu, le torseur rapporté est celui de l'action
    ou celui de la réaction, donc de signe opposé.

Le relevé graphique de la direction de l'axe 1 ne suffit donc PAS à fixer le
signe : c'est la combinaison des deux facteurs qui le détermine. C'est
pourquoi les paramètres axis1_sign / axis2_sign de
section_cut_local_axes_global ci-dessous captent le résultat NET des deux, et
se calibrent sur des contraintes d'équilibre plutôt que sur un relevé.

=============================================================================
CHANGELOG DU 2026-09-03 - SIGNE DE M_vertical_bending
=============================================================================
global_to_bridge_frame renvoyait  M_vertical_bending = + M_global . e_T , avec
e_T = e_V x e_L (transversale pointant vers la GAUCHE du sens de parcours).
Le moment de flexion principal ressortait donc avec le signe INVERSE de la
convention structurale usuelle : moment de travée (sagging) NÉGATIF, moment
sur appui (hogging) POSITIF. Vérifié sur le viaduc Plaine de l'Orbe, cas DEAD,
travée T3 : -6.3 MNm à mi-travée, +12.0 MNm sur appui ; et sur le modèle de
validation (detect_sign_convention -> sign_M = -1).

Depuis cette date :  M_vertical_bending = - M_global . e_T  (convention
"sagging positif", traction fibre inférieure > 0). Les cinq autres composantes
(P, V_transverse, V_vertical, T, M_transverse_bending) sont INCHANGÉES.

IMPACT : toute sortie M_vertical_bending / M_vert produite avant cette date
est à recalculer (changement de signe global de cette seule composante).
Aucun recalcul SAP2000 : la modification est en post-traitement pur. Le cache
composite_section_cuts_cache.json et les Section Cuts restent valables.
validation_composite_beam.py et plot_composite_beam_forces.py détectent le
facteur de signe automatiquement : ils restent valides, seul le facteur
rapporté change (sign_M : -1 -> +1).
"""

import numpy as np


# ---------------------------------------------------------------------------
# Repères locaux des deux objets, en coordonnées globales
# ---------------------------------------------------------------------------

def frame_local_axes_global(SapModel, frame_name):
    """
    Vecteurs unitaires des axes locaux 1,2,3 du Frame Object `frame_name`,
    exprimés en repère global, via SapModel.FrameObj.GetTransformationMatrix
    (matrice de 9 cosinus directeurs, [Global] = M @ [Local]).

    Un contrôle d'orthonormalité (R^T R = I, det = +1) est effectué ; si le
    premier remplissage (ligne par ligne) échoue, la transposée est essayée
    automatiquement avant d'abandonner - filet de sécurité pour un point de
    l'API (ordre de remplissage des 9 valeurs) qui n'est pas illustré par un
    exemple VBA exploitable dans la documentation disponible.

    Output: e1, e2, e3 (np.array de dimension 3 chacun)
    """
    value, ret = SapModel.FrameObj.GetTransformationMatrix(frame_name)
    if ret != 0:
        raise RuntimeError(f"GetTransformationMatrix a échoué pour '{frame_name}' (ret={ret}).")

    def _ortho_error(R):
        return np.max(np.abs(R.T @ R - np.eye(3)))

    R_row_major = np.array(value).reshape(3, 3)
    if _ortho_error(R_row_major) < 1e-6:
        R = R_row_major
    elif _ortho_error(R_row_major.T) < 1e-6:
        R = R_row_major.T
    else:
        raise RuntimeError(
            f"Matrice de transformation non orthonormale pour '{frame_name}' "
            f"(erreur={_ortho_error(R_row_major):.2e}) : vérifier l'ordre de "
            f"remplissage des 9 cosinus directeurs retournés par l'API."
        )
    return R[:, 0], R[:, 1], R[:, 2]


def section_cut_local_axes_global(sc_angle_deg, axis1_sign=1.0, axis2_sign=1.0):
    """
    Vecteurs unitaires des axes locaux 1,2,3 d'un Section Cut "Design Slab",
    reconstruits à partir de son angle SetLocalAxesAngleDesign (angle signé,
    en degrés, de l'axe global X vers l'axe local 1, dans le plan horizontal -
    cf. vg.signed_angle(X_vector, tangent, look=Z) utilisé par
    createSectionCutsSAP2000/bridgeDeckSectionCutsSAP2000).

    CONVENTION (corrigée le 2026-08-25, cf. docstring de module) : l'axe local
    2 est VERTICAL et l'axe local 3 est TRANSVERSE horizontal - soit la même
    convention qu'un Frame Object proche de l'horizontale.

    Input:
        sc_angle_deg : angle SetLocalAxesAngleDesign du Section Cut (deg)
        axis1_sign, axis2_sign : sens (+1.0 ou -1.0) des axes locaux 1 et 2,
            par rapport respectivement à la tangente du tablier et à la
            verticale ASCENDANTE.

            Pourquoi des paramètres, et pourquoi un relevé graphique ne suffit
            pas : la DIRECTION de l'axe 1 est certes connue (c'est l'angle
            passé à SetLocalAxesAngleDesign), mais un Section Cut ne rapporte
            les efforts que d'UN SEUL CÔTÉ de la coupe - "Results Reported Are
            On This Side of Elements : Right / Left", cf.
            SectCut.GetResultsSide (1 = Right, 2 = Left pour un Design Slab).
            Selon le côté retenu, le torseur rapporté est celui de l'action ou
            celui de la réaction, donc de signe opposé. Ces deux paramètres
            captent le résultat NET de la direction ET du côté.

            Comment les déterminer sans les deviner - deux contraintes
            physiques, toutes deux indépendantes du moment fléchissant (donc
            sans circularité si l'objectif est de calculer un moment) :
              - axis1_sign : équilibre de l'effort normal. En l'absence de
                charge horizontale et avec un seul appui bloqué
                longitudinalement, l'effort normal résultant de la section
                composite est nul, donc N_dalle = -N_poutre :
                    axis1_sign = -P_poutre / P_dalle   (doit valoir +/-1)
              - axis2_sign : cohérence de signe de l'effort tranchant
                vertical. Dalle et poutre appartenant à la même section, leurs
                efforts tranchants verticaux sont de même sens : axis2_sign
                est celui qui rend sign(V2_dalle) égal au signe de l'effort
                tranchant vertical de la poutre.
            Implémentation de référence : calibrate_section_cut_convention()
            dans PostTraitement/validation_composite_beam.py (projet 9BV024).

            Les valeurs par défaut (+1, +1) ne sont PAS un choix sûr : elles
            préservent seulement le comportement antérieur. Elles doivent être
            calibrées une fois pour un modèle et une façon de construire les
            quads donnés.

    Output: e1, e2, e3 (np.array de dimension 3 chacun), repère orthonormé DIRECT
    """
    theta = np.radians(sc_angle_deg)
    e1 = axis1_sign * np.array([np.cos(theta), np.sin(theta), 0.0])
    e2 = axis2_sign * np.array([0.0, 0.0, 1.0])
    # e1 x e2, et non e2 x e1 : les axes locaux 1,2,3 de SAP2000 forment
    # TOUJOURS un trièdre DIRECT. Un trièdre indirect donnerait une matrice de
    # passage de déterminant -1 (une réflexion, pas une rotation), qui inverse
    # silencieusement la composante transversale des efforts.
    e3 = np.cross(e1, e2)
    return e1, e2, e3


def bridge_local_frame(tangent_global):
    """
    Repère local du tablier (e_L, e_T, e_V) à une station donnée, à partir
    de la tangente (vecteur global, pas nécessairement unitaire) à l'axe du
    tablier en ce point. e_V = verticale globale fixe ; e_T complète un
    repère direct dans le plan horizontal.

    Accepte une tangente 2D (X,Y) OU 3D (X,Y,Z) : de nombreux projets (cf.
    convention CLAUDE.md - tracés fournis en colonnes X,Y uniquement, sans Z)
    calculent cette tangente à partir d'une polyligne purement horizontale.
    Une tangente 2D est complétée par une composante Z=0 (tablier supposé
    localement horizontal en plan) pour que e_L reste bien un vecteur 3D,
    cohérent avec e_T et e_V ci-dessous (sinon les torseurs global/local
    combinés plus loin dans ce module échouent avec un désaccord de forme
    3 vs 2, np.dot(F_global, e_L) notamment).
    """
    e_L = np.asarray(tangent_global, dtype=float)
    if e_L.shape[-1] == 2:
        e_L = np.append(e_L, 0.0)
    e_L = e_L / np.linalg.norm(e_L)
    e_V = np.array([0.0, 0.0, 1.0])
    e_T = np.cross(e_V, e_L)
    norm_T = np.linalg.norm(e_T)
    if norm_T < 1e-9:
        raise ValueError("Tangente verticale : repère transversal indéfini.")
    e_T = e_T / norm_T
    return e_L, e_T, e_V


# ---------------------------------------------------------------------------
# Transport rigoureux force + moment (repère global)
# ---------------------------------------------------------------------------

def local_to_global_force_moment(P, V2, V3, T, M2, M3, e1, e2, e3):
    """
    Convertit (P,V2,V3,T,M2,M3), exprimés dans le repère local (e1,e2,e3)
    d'un objet SAP2000, en un torseur (F_global, M_global) en repère global.

    Le SENS des axes joue bien un rôle, et pas seulement sur la composante
    concernée : (e1,e2,e3) doit former un trièdre DIRECT, comme le sont
    toujours les axes locaux 1,2,3 de SAP2000. Si le trièdre est indirect,
    R = [e1,e2,e3] a un déterminant de -1 : ce n'est plus une rotation mais
    une RÉFLEXION, qui inverse la composante transversale des efforts sans
    rien signaler. D'où le contrôle ci-dessous, qui couvre aussi bien les axes
    du Section Cut (section_cut_local_axes_global) que ceux du Frame Object
    (frame_local_axes_global).
    """
    F_local = np.array([P, V2, V3])
    M_local = np.array([T, M2, M3])
    R = np.column_stack([e1, e2, e3])   # [Global] = R @ [Local]

    if not np.allclose(R.T @ R, np.eye(3), atol=1e-9):
        raise ValueError(
            f"Repère local non orthonormé (erreur max "
            f"{np.max(np.abs(R.T @ R - np.eye(3))):.2e}) : e1, e2, e3 doivent "
            f"être unitaires et deux à deux perpendiculaires."
        )
    det = float(np.linalg.det(R))
    if not np.isclose(det, 1.0, atol=1e-9):
        raise ValueError(
            f"Repère local INDIRECT (det = {det:+.3f}, attendu +1) : les axes "
            f"locaux 1,2,3 de SAP2000 forment toujours un trièdre direct, donc "
            f"e3 = e1 x e2 (et non e2 x e1). Une matrice de déterminant -1 est "
            f"une réflexion : elle inverserait la composante transversale des "
            f"efforts sans le signaler."
        )

    return R @ F_local, R @ M_local


def transport_to_point(F_global, M_global_at_point, point_from, point_to):
    """
    Transporte le torseur (F_global, M_global_at_point), calculé au point
    `point_from`, au point `point_to` (tous deux en coordonnées globales).

        M_nouveau = M_ancien + F_global x (point_to - point_from)

    F_global est inchangé par un transport (une résultante de force ne
    dépend pas du point auquel on l'exprime, seul le moment en dépend).
    """
    r = np.asarray(point_to, dtype=float) - np.asarray(point_from, dtype=float)
    return F_global, np.asarray(M_global_at_point) + np.cross(F_global, r)


def global_to_bridge_frame(F_global, M_global, e_L, e_T, e_V):
    """Reprojette un torseur global sur le repère du tablier (e_L,e_T,e_V) et
    retourne un dict aux noms physiques explicites (cf. docstring de module,
    aucune référence à une numérotation d'axe locale 2/3)."""
    return {
        "P": float(np.dot(F_global, e_L)),
        "V_transverse": float(np.dot(F_global, e_T)),
        "V_vertical": float(np.dot(F_global, e_V)),
        "T": float(np.dot(M_global, e_L)),
        "M_transverse_bending": float(np.dot(M_global, e_V)),   # flexion "en plan"
        # Flexion principale de la poutre maîtresse, convention structurale
        # usuelle "sagging positif" : traction fibre INFÉRIEURE (moment de
        # travée) > 0 ; traction fibre SUPÉRIEURE (moment sur appui) < 0.
        # e_T = e_V x e_L pointe vers la GAUCHE du sens de parcours ; le
        # vecteur-moment d'une flexion sagging pointe vers la droite -> signe -.
        # Calibré sur DEAD / travée T3 du viaduc Plaine de l'Orbe et sur le
        # modèle de validation (cf. CHANGELOG 2026-09-03 de l'en-tête).
        "M_vertical_bending": -float(np.dot(M_global, e_T)),    # flexion principale (fibre sup/inf)
    }


# ---------------------------------------------------------------------------
# Composition dalle + poutre au centre de gravité composite
# ---------------------------------------------------------------------------

def composite_centroid_local(slab_area, slab_z, slab_y_offset,
                              beam_area, beam_z, modular_ratio=1.0):
    """
    Centre de gravité de la section composite (dalle + poutre), dans le plan
    transversal-vertical LOCAL (y' = transverse, z' = vertical) centré sur
    l'axe propre de la poutre (y'=0), avec la dalle homogénéisée par un
    coefficient d'équivalence modular_ratio = E_dalle / E_poutre (1.0 si
    même matériau : centre de gravité géométrique simple).

    Input:
        slab_area : aire de la bande de dalle de largeur efficace beff (m²)
        slab_z : cote (z') du plan moyen de la dalle, relative à l'axe de la
            poutre (m) - dans ce projet, z=0 en tête de tablier, dalle à
            z = -épaisseur_dalle/2 (cf. CLAUDE.md)
        slab_y_offset : décalage transversal du centre de la bande de dalle
            par rapport à l'axe de la poutre, (beff_2 - beff_1)/2 (m)
        beam_area, beam_z : aire et cote du centre de gravité PROPRE de la
            poutre (m², m) - à fournir explicitement (dépend du point
            d'insertion réel de la poutre, cf. FrameObj.SetInsertionPoint_1,
            non ré-interrogé automatiquement ici, cf. note de méthode)
        modular_ratio : E_dalle / E_poutre (défaut 1.0)

    Output: (y_c, z_c) - centre de gravité composite, mêmes coordonnées
        locales (transverse, vertical) que les entrées
    """
    a_slab_eq = slab_area * modular_ratio
    w_total = a_slab_eq + beam_area
    if w_total <= 0:
        raise ValueError("Aire composite nulle ou négative.")
    y_c = (a_slab_eq * slab_y_offset + beam_area * 0.0) / w_total
    z_c = (a_slab_eq * slab_z + beam_area * beam_z) / w_total
    return y_c, z_c


def combine_slab_beam_forces(
    slab_forces_local, slab_point_global, slab_angle_deg,
    beam_forces_local, beam_point_global, beam_frame_name, SapModel,
    target_point_global, tangent_global,
    slab_axis1_sign=1.0, slab_axis2_sign=1.0,
):
    """
    Combine, au point `target_point_global`, les efforts de la dalle (Section
    Cut Design Slab) et de la poutre (Frame Object), tous deux transportés en
    repère global puis sommés, et ré-exprimés dans le repère du tablier
    (e_L, e_T, e_V) à cette station.

    Input:
        slab_forces_local : (P,V2,V3,T,M2,M3) du Section Cut, REPÈRE LOCAL du
            cut (sortie de getSectionCutForcesSAP2000, une ligne = un
            output_type donné, cf. orchestrateur)
        slab_point_global : (X,Y,Z) global auquel slab_forces_local est
            rapporté (sortie X,Y,Z de getSectionCutForcesSAP2000)
        slab_angle_deg : angle SetLocalAxesAngleDesign du Section Cut (deg)
        beam_forces_local : (P,V2,V3,T,M2,M3) du Frame Object, REPÈRE LOCAL
            du frame (sortie SapModel.Results.FrameForce)
        beam_point_global : (X,Y,Z) global de la station du Frame Object à
            laquelle beam_forces_local est rapporté.
            ATTENTION : si la poutre est excentrée par FrameObj.
            SetInsertionPoint_1 (poutre dessinée sur les nœuds de la dalle puis
            décalée verticalement - cas courant d'un tablier à poutres),
            SAP2000 rapporte les efforts du FrameObj autour du CDG RÉEL de la
            section excentrée, PAS autour de la ligne dessinée. C'est donc la
            cote du CDG réel qu'il faut fournir ici : passer celle des nœuds
            dessinés introduit une erreur de transport égale au bras de levier
            de l'excentrement, ce qui annule quasiment le couple composite.
        beam_frame_name : nom du Frame Object (pour interroger sa matrice de
            transformation réelle, cf. frame_local_axes_global)
        SapModel : objet SAP2000
        target_point_global : (X,Y,Z) du point de report final (typiquement
            le centre de gravité composite, cf. composite_centroid_local +
            reconversion en coordonnées globales par l'appelant)
        tangent_global : tangente locale à l'axe du tablier à cette station
            (pour construire le repère (e_L,e_T,e_V) de sortie)
        slab_axis1_sign, slab_axis2_sign : sens des axes locaux 1 et 2 du
            Section Cut, transmis tels quels à section_cut_local_axes_global -
            voir son docstring pour la façon de les déterminer sans les
            deviner. Les valeurs par défaut (+1, +1) ne sont pas un choix sûr.

    Output: dict aux clés P, V_transverse, V_vertical, T,
        M_transverse_bending, M_vertical_bending (repère du tablier, cf.
        global_to_bridge_frame), plus F_global/M_global bruts pour traçabilité.
    """
    e1_sc, e2_sc, e3_sc = section_cut_local_axes_global(
        slab_angle_deg, slab_axis1_sign, slab_axis2_sign
    )
    F_slab, M_slab = local_to_global_force_moment(*slab_forces_local, e1_sc, e2_sc, e3_sc)
    F_slab, M_slab = transport_to_point(F_slab, M_slab, slab_point_global, target_point_global)

    e1_fr, e2_fr, e3_fr = frame_local_axes_global(SapModel, beam_frame_name)
    F_beam, M_beam = local_to_global_force_moment(*beam_forces_local, e1_fr, e2_fr, e3_fr)
    F_beam, M_beam = transport_to_point(F_beam, M_beam, beam_point_global, target_point_global)

    F_total = F_slab + F_beam
    M_total = M_slab + M_beam

    e_L, e_T, e_V = bridge_local_frame(tangent_global)
    result = global_to_bridge_frame(F_total, M_total, e_L, e_T, e_V)
    result["F_global"] = F_total
    result["M_global"] = M_total
    return result


# ---------------------------------------------------------------------------
# Auto-vérification de la formule de transport (exécutée à l'import)
# ---------------------------------------------------------------------------

def _self_check_transport():
    """Vérifie M_nouveau = M_ancien + F x (point_to - point_from) sur un cas
    simple analytique : force verticale F=(0,0,-P) appliquée en O=(0,0,0),
    aucun couple. Moment attendu en O'=(d,0,0) : (0,-d*P,0) (cf. note de
    méthode jointe à la réponse pour la dérivation)."""
    P, d = 100.0, 3.0
    F = np.array([0.0, 0.0, -P])
    M_O = np.array([0.0, 0.0, 0.0])
    _, M_Op = transport_to_point(F, M_O, [0, 0, 0], [d, 0, 0])
    expected = np.array([0.0, -d * P, 0.0])
    assert np.allclose(M_Op, expected), f"Transport incorrect : {M_Op} != {expected}"


def _self_check_section_cut_axes():
    """Vérifie la convention d'axes du Section Cut (corrigée le 2026-08-25) :
    axe 2 VERTICAL, axe 3 TRANSVERSE horizontal, et trièdre DIRECT quels que
    soient les sens demandés. Ces trois propriétés ayant chacune fait l'objet
    d'une erreur avérée, elles sont vérifiées à l'import."""
    for s1 in (1.0, -1.0):
        for s2 in (1.0, -1.0):
            for angle in (0.0, 37.0, -125.0):
                e1, e2, e3 = section_cut_local_axes_global(angle, s1, s2)
                assert np.isclose(abs(e2[2]), 1.0), f"axe 2 non vertical : {e2}"
                assert np.isclose(e3[2], 0.0, atol=1e-12), f"axe 3 non horizontal : {e3}"
                assert np.isclose(e1[2], 0.0, atol=1e-12), f"axe 1 non horizontal : {e1}"
                R = np.column_stack([e1, e2, e3])
                assert np.allclose(R.T @ R, np.eye(3), atol=1e-12), "trièdre non orthonormé"
                assert np.isclose(np.linalg.det(R), 1.0), (
                    f"trièdre INDIRECT (det={np.linalg.det(R):+.3f}) pour "
                    f"angle={angle}, signes=({s1:+.0f},{s2:+.0f}) : e3 doit valoir e1 x e2."
                )


_self_check_transport()
_self_check_section_cut_axes()
