import numpy as np


def getAreaCentroidsSAP2000(SapModel, group_name=""):
    """
    Récupère en un seul appel API le centroïde XY (coordonnées globales) de
    chaque AreaObj de group_name, via la table "Connectivity - Area" de la
    Database Tables API (champs "Area", "CentroidX", "CentroidY", déjà
    calculés par SAP2000).

    Remplace un calcul objet par objet (AreaObj.GetPoints puis
    PointObj.GetCoordCartesian sur chaque point), qui nécessite ~5 appels API
    par AreaObj : sur un tablier de plusieurs dizaines de milliers d'AreaObj,
    ce calcul devient prohibitif (chaque appel API individuel implique un
    aller-retour COM), a fortiori s'il est répété (une fois par position de
    voie, une fois par zone transversale, etc.). La table "Connectivity -
    Area" renvoie tous les centroïdes en une seule fois, quel que soit le
    nombre d'AreaObj.

    Input:
        - SapModel: SAP Model object
        - group_name: Nom du groupe à interroger. "" (défaut) ou "All" pour
          tous les AreaObj du modèle.
    Output:
        - dict {area_name: np.array([x, y])}, un par AreaObj du groupe
    """
    _, _, _, n_records, table_data, ret = SapModel.DatabaseTables.GetTableForDisplayArray(
        "Connectivity - Area", ["Area", "CentroidX", "CentroidY"], group_name
    )
    centroids = {}
    for i in range(n_records):
        name, cx, cy = table_data[3 * i:3 * i + 3]
        centroids[name] = np.array([float(cx), float(cy)])
    return centroids
