import comtypes.client


def connect_to_sap2000():
    """Attache le script à une instance de SAP2000 déjà ouverte sur le poste.

    Returns
    -------
    tuple(cOAPI, cSapModel)
        L'objet SapObject (SapObject.SapModel donne accès à toute l'API) et
        le SapModel actif, prêts à être utilisés directement.

    Raises
    ------
    RuntimeError
        Si aucune instance de SAP2000 en cours d'exécution n'a pu être trouvée.
    """
    helper = comtypes.client.CreateObject('SAP2000v1.Helper')
    helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)

    try:
        sap_object = helper.GetObject("CSI.SAP2000.API.SapObject")
    except (OSError, comtypes.COMError) as exc:
        raise RuntimeError(
            "Aucune instance de SAP2000 en cours d'exécution n'a été trouvée. "
            "Ouvrez SAP2000 avec le modèle voulu avant de lancer ce script."
        ) from exc

    sap_model = sap_object.SapModel

    return sap_object, sap_model
