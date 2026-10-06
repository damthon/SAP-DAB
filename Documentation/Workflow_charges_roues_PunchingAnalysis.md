# Workflow — charges de roue : PunchingAnalysis → JSON → SAP2000

> Plan d'implémentation (non exécuté). Rédigé après lecture de `Loads/` et `MeshingGeometry/`. Aucun fichier de code existant n'est modifié par ce plan : on ajoute des fonctions à côté.

## 1. Objectif
L'artefact `PunchingAnalysis/artifacts/perimetres_dalle_roulement.html` détermine les positions déterminantes des roues dans la coupe transversale. Ces positions sont exportées en JSON puis introduites comme charges de roue dans le modèle SAP2000 via des fonctions de cette bibliothèque.

## 2. Repère unique (artefact, JSON, modèle)
| Axe | Définition |
|---|---|
| x | tangente au tracé (abscisse curviligne, `getStations`) |
| y | horizontal, orthogonal à x, **positif à gauche** : `n = Z × t = (−t_y, t_x, 0)` |
| z | vertical ascendant |
| origine | axe de tracé, niveau supérieur de la dalle de roulement, centre de la section |

- Identique à la convention de `getOffsetPoints` / `createSlabCLSAP2000` (vérifié par exécution : tangente +X → offset +2 donne Y = +2).
- Pente transversale p [%] : positive si le dessus monte vers la gauche (y+), `z(y) = z_axe + p/100 · y` (vérifié : 5 % à 2 m → +0.10 m).
- y est **horizontal**. `createSlabCLSAP2000` mesure l'offset d le long de la surface inclinée : `y = d/√(1+s²)`, `d = y·√(1+s²)`, s = p/100 (0.12 % à 5 %).
- Placement global d'une roue : `P = C(s) + y·n(s) + z(y)·Z`, C(s) interpolé sur la polyligne de l'axe, tangente locale du segment (comme `getOffsetPoints`).

### ⚠ Incohérence de signe dans le dépôt
`getTransverseOffsetsSAP2000` renvoie un offset positif côté **droit** (point (10, −2) → +2) alors que `getOffsetPoints` est positif côté **gauche**, bien que la docstring de la première revendique « la même convention ». Ne pas utiliser `getTransverseOffsetsSAP2000` sans inverser le signe pour ce workflow. (À corriger ailleurs, hors périmètre.)

## 3. État des lieux de la bibliothèque
- `sap2000_connector.connect_to_sap2000()` : réutilisable tel quel.
- `Loads/assignQkSAP2000`, `assignQkCurvedSAP2000`, `assignMC3SAP2000` : pneus à géométrie fixe (essieu 1.2 × 2.0 m, empreinte 0.4 × 0.4), pas de position libre. Brique réutilisable : joints dans le rayon `r_inf` → pondération inverse de la distance (`w = 1/(d+0.01)`) → `PointObj.SetLoadForce(joint, pattern, [Fx,Fy,Fz,Mx,My,Mz], 1, 'Global', 0)`.
- `MeshingGeometry/createDeckSAP2000.py` ne contient **pas** de fonction `createDeckSAP2000` : il contient `createSlabCLSAP2000` (dalle depuis l'axe, retourne `slab_shell, div_stations, all_stations, mesh_grid, mesh_grid_y`), `createSlab2LSAP2000`, `createWebSAP2000`, `createStiffenerSAP2000`, `getQuadMeshPoints`, `sort3DpointsCCW`. Groupes de points créés : `CL`, `E-±w/2`, `O-<y>` (un par valeur de `div_y`).
- **Décision** : `div_y` reçoit uniquement les limites de largeur de voie (zones de charge répartie). Les y des roues n'y sont **pas** ajoutés : les charges de roue sont réparties sur les nœuds les plus proches.

## 4. Contrat JSON (produit par l'artefact, `format: punching-analysis/wheel-positions`, version 1)
- `frame` : description du repère ci-dessus. `units` : m, kN, %.
- `section` : `type`, `B_m`, `axis_from_left_edge_m`, `slope_pct` (convention y+), `slope_convention`.
- `wheel` : `contact_b_m`, `footprint_be_m` (empreinte carrée au niveau du béton), `axle_spacing_m`, `track_m`, `Q_d_note`.
- `positions[]` : `id`, `label`, `free`, `zone`, `determinant_for` (`punch`/`bend`/`shear`), `wheels.single_axle[]` et `wheels.tandem[]` (`{id, lane, Q_d_kN, y_m, x_rel_m}`), `groups[]` (`key`, `family`, `name`, `wheel_ids`, `determinant_for`).
- `Q_d_kN` : charge de calcul par roue (γ_Q·α_Q·Q_k/2), verticale vers le bas. `x_rel_m` : décalage longitudinal par rapport au centre de l'essieu/tandem (sens arbitraire, files symétriques). L'abscisse x (station) n'est **pas** dans le JSON : elle est fournie au script.

## 5. Étapes
1. **`MeshingGeometry/getWheelXYZSAP2000.py`** (calcul pur, sans API) : (centerline_coord, slope_pct, station, y) → XYZ global, en réutilisant `getStations`, `getOffsetPoints`, `getSlopeNormals` pour rester cohérent avec le tablier généré (conversion `d = y·√(1+s²)`).
2. **`Loads/assignWheelLoadsSAP2000.py`** : roues `[(x, y, z, Q, b_e)]` → joints du groupe de voie les plus proches (rayon ou empreinte b_e×b_e, au choix), pondération inverse de la distance, `SetLoadForce`, `ret` vérifié, `SetPresentUnits(6)`, copie locale de la logique (ne pas modifier `assignQkSAP2000`). Conventions du dépôt : un fichier = une fonction, camelCase + suffixe `SAP2000`, `SapModel` en premier argument, docstring anglaise `Input:/Output:`.
3. **Script d'orchestration** (script de calcul, hors fonctions de bibliothèque) : lit le JSON, choisit les positions/familles (déterminantes ou toutes), appelle 1 puis 2, crée les load patterns (vérifier la signature dans `Docs/SAP2000_API/API_Definitions_Load_Pattern.md`), déverrouille le modèle, coupe le rafraîchissement de vue. Mode `dry_run` (liste joints/forces, ΣF = ΣQ), validation explicite et rappel de sauvegarde avant écriture.
4. **Tests hors SAP** (mock de `SapModel`) : XYZ attendu = `getOffsetPoints(axe, d, getSlopeNormals(axe, p))` ; ΣF = ΣQ ; centre de gravité des forces = position de la roue ; tracé droit et courbe, p = 0 et p ≠ 0, y > 0 et y < 0.
5. **Validation sur modèle** (copie) : réaction totale = ΣQ ; comparaison des M/V transversaux SAP avec l'artefact (hypothèse d'éventail tan θ du modèle simplifié).
6. **Documentation** : mettre à jour `CLAUDE.md` (§3 arborescence, §11 chantiers ; corriger la mention « createDeckSAP2000 » → `createSlabCLSAP2000` dans le fichier `createDeckSAP2000.py`), compléter les `<À COMPLÉTER>` (version SAP2000, Python), README racine.

## 6. Points ouverts
- Q de calcul ou caractéristique côté SAP (les combinaisons γ sont-elles appliquées dans SAP ?) ; un load pattern par position ou un seul.
- Répartition : rayon `r_inf` (existant) ou empreinte b_e × b_e.
- Position longitudinale x : fournie par l'utilisateur (script) ou déduite (mi-travée / zone d'appui).
- Limites de largeur de voie à passer dans `div_y` : fournies par l'utilisateur.
