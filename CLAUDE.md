# CLAUDE.md — Dépôt SAP-DAB

> Contexte permanent du dépôt `damthon/SAP-DAB`. À lire en entier avant toute
> modification de code.

---

## 1. Nature du dépôt

Bibliothèque Python d'automatisation de **SAP2000** via la **CSI OAPI**, orientée
**ouvrages d'art** : ponts haubanés, ponts suspendus, tabliers mixtes,
précontrainte, analyse vibratoire, vérifications de dimensionnement.

Environ **24 000 lignes réparties sur ~190 fichiers**. Ce n'est **pas un package
installable** : c'est une collection de modules à un seul niveau, posée sur un
chemin partagé et ajoutée au `PYTHONPATH`.

**Origine du code — point important :** 118 fichiers portent
`@author: hammad.eljisr`, un seul `@author: damien.balmer`. C'est donc une
bibliothèque **héritée**, largement non écrite par l'utilisateur courant. En
conséquence :

- Ne jamais présumer que l'utilisateur connaît le détail d'une fonction
  existante ; proposer de la lire avant de s'appuyer dessus.
- Ne **jamais** réécrire, renommer ou « moderniser » du code existant sans
  demande explicite : d'autres scripts en dépendent, hors dépôt.
- Les corrections doivent être **locales et minimales**.

**Interlocuteur :** ingénieur en structure, sait programmer. Pas de
vulgarisation, ni côté génie civil ni côté Python. Réponses directes et
techniques. Le français est la langue d'échange.

---

## 2. Environnement

| Élément | Valeur |
|---|---|
| Pont COM | `comtypes` (jamais `win32com`) |
| Interface | `SAP2000v1.Helper` → `comtypes.gen.SAP2000v1.cHelper` |
| Version SAP2000 | `<À COMPLÉTER>` |
| Python | `<À COMPLÉTER — 64 bits obligatoire>` |

**Dépendances tierces réellement utilisées :** `numpy`, `scipy`, `matplotlib`,
`pandas`, `comtypes`, `shapely`, `tabulate`, `vg`, `sectionproperties`,
`alphashape`.

### Connexion

Point d'entrée unique : `sap2000_connector.connect_to_sap2000()` →
`(sap_object, sap_model)`.

Cette fonction **s'attache à une instance de SAP2000 déjà ouverte**
(`helper.GetObject`) — elle n'en lance pas et ne crée pas de modèle. **Tout
script agit donc sur un modèle réel ouvert à l'écran.** Ne jamais proposer
d'exécuter un script d'écriture sans validation explicite, et rappeler la
sauvegarde préalable quand la modification est massive ou irréversible
(`deleteFloatingPointsSAP2000`, `scaleGroupSAP2000`,
`disconnectMeshPointsSAP2000`, `offsetPointsMoveSAP2000`…).

Aucun test d'intégration ne peut tourner en CI : SAP2000 doit être installé et
licencié localement.

---

## 3. Arborescence

Racine de la bibliothèque : `Bibliothèque fonction/`
*(le nom contient un accent et une espace — toujours citer ce chemin entre
guillemets en shell, et préférer `pathlib` en Python).*

```
Bibliothèque fonction/
├── sap2000_connector.py          # attache COM — point d'entrée unique
├── rep_creator.py                # utilitaire : génère les __init__.py manquants
├── Docs/SAP2000_API/             # documentation OAPI (voir §4)
│
├── MeshingGeometry/              # stations, offsets, maillage, createDeckSAP2000
├── FrameShellsCablesPoints/      # manipulation d'objets, axes locaux, contraintes
├── Selection/                    # sélection par groupe, voies de circulation
├── Loads/                        # Qk, MC3, vent, précontrainte isostatique
├── Prestressing/                 # profils de câbles, tendons, pertes
├── SectionCuts/                  # coupes, efforts, sections mixtes
├── SectionDesigner/              # interpolation de sections
├── OutputDesign/                 # vérifications (fib 2020, SIA 262, sections en I)
│   ├── Built-up I-section Design/
│   ├── Shell Design/
│   └── fib 2020 Shear Level II/
├── Cable-stayedbridge/           # haubans : fonctions + scripts Cable_Design_C*
├── Suspensionbridge/             # câble porteur, câbles latéraux, backstay
├── Simplesuspensionbridge/       # caténaire
├── Vibrationanalysis/            # SETRA, AISC, amortisseurs accordés (TMD)
└── Eurocode/                     # largeur efficace
```

### Fonctions ≠ scripts

Deux natures de fichiers cohabitent, à ne pas confondre :

- **Fonctions de bibliothèque** — un fichier = une fonction, réutilisable.
- **Scripts de calcul** — code au niveau module, chemins et paramètres en dur,
  propres à un ouvrage. Typiquement `Cable-stayedbridge/Cable_Design_C*.py`
  (10 variantes quasi identiques de 500–700 lignes, une par cas de hauban),
  `OutputDesign/Preliminary_Design.py`, `OutputDesign/Tablier_metallique.py`.

Ne jamais importer un script depuis une fonction. Ne jamais tenter de
factoriser les `Cable_Design_C*` sans demande explicite : leurs divergences sont
probablement intentionnelles.

---

## 4. Documentation OAPI locale

`Bibliothèque fonction/Docs/SAP2000_API/` — documentation CSI officielle
convertie du `.chm` en ~50 fichiers Markdown catégorisés.
Index d'entrée : **`_README_INDEX.md`**.

Repères : `API_Object_Model_*` par type d'objet (Frame, Area, Cable, Point,
Link, Tendon, Solid), `API_Definitions_*` par catégorie de définition
(Section_Cuts, Load_Pattern, Constraints, Properties…), `API_Analysis_Results`,
`API_Analyze`, `Database_Tables`, `Example_Code`, `Getting_Started`,
`API_Bridge_Advanced`.

> **Règle absolue : ne jamais inventer une signature OAPI.** Avant d'écrire un
> appel qui n'existe pas déjà dans le dépôt, ouvrir le fichier de doc
> correspondant et vérifier l'ordre exact des arguments et la composition du
> tuple de retour. En cas de doute résiduel, le dire — ne pas deviner.
>
> Vérifier aussi `API_Obsolete_Functions.md` et `API_Breaking_Changes_*` :
> une partie du code hérité utilise des appels dépréciés.

---

## 5. Conventions du dépôt

Elles sont implicites mais cohérentes. Du code nouveau doit s'y conformer.

### Nommage
- **Un fichier = une fonction, et le nom du fichier est le nom de la fonction.**
- `camelCase`, suffixe **`SAP2000`** si — et seulement si — la fonction touche à
  l'API (`getGroupFrameObjSAP2000`, `createDeckSAP2000`). Sans suffixe pour le
  calcul pur (`getStations`, `circleThreepoints`, `effectiveWidthEurocode`).
- Préfixes usuels : `get` / `set` / `create` / `assign` / `orient` / `delete` /
  `plot` / `interp`.

### En-tête et docstring
Modèle en vigueur, à reproduire :

```python
# -*- coding: utf-8 -*-
"""
Created on <date>

@author: <auteur>
"""

def maFonctionSAP2000(SapModel, arg1, arg2):
    """
    This function <ce qu'elle fait>
    Input:
        SapModel: SAP Model object
        arg1: <description, avec l'unité>
    Output:
        result: <description, avec l'unité>
    """
```

Docstrings **en anglais**, style `Input:` / `Output:` (pas NumPy, pas Google).
`SapModel` est **toujours le premier argument** des fonctions API. Aucune
connexion implicite par variable globale.

### Imports internes — fragile, à connaître
Deux styles coexistent :

```python
from getGroupPointObjSAP2000 import getGroupPointObjSAP2000   # plat (majoritaire)
from MeshingGeometry.getStations import getStations           # qualifié
```

Il n'y a **aucune manipulation de `sys.path`** dans le code. Le `PYTHONPATH`
doit donc contenir **à la fois la racine de la bibliothèque et chacun de ses
sous-dossiers**. `rep_creator.py` sème des `__init__.py` vides pour rendre les
dossiers importables — ils sont tous vides et n'exportent rien.

Conséquence : **ne pas convertir les imports plats en imports relatifs**, cela
casserait les scripts existants hors dépôt.

---

## 6. Règles OAPI critiques

### 6.1 Paramètres de sortie
En Python, les paramètres `ByRef` de l'API sont renvoyés **dans le tuple de
retour**, jamais passés en argument.

```python
# CORRECT
name, ret = SapModel.AreaObj.AddByPoint(4, pts, prop_name)
name, ret = SapModel.PointObj.AddCartesian(x, y, z)
```

Même piège sur tous les `Get*` : `SapModel.FrameObj.GetNameList()[1]`,
`GetCoordCartesian(pt)[0:3]`, etc. Vérifier l'indexation dans la doc.

### 6.2 Codes de retour
Le dernier élément du tuple est `ret` ; `0` = succès. Le code hérité l'ignore
très souvent. **Dans tout code neuf, le vérifier** :

```python
if ret != 0:
    raise RuntimeError(f"OAPI ret={ret} — <contexte>")
```

### 6.3 Noms d'objets
SAP2000 attribue les noms lui-même. Toujours récupérer le nom renvoyé et le
stocker. Ne jamais supposer une numérotation séquentielle ni reconstruire un nom
à partir d'un index.

### 6.4 Unités — état global du modèle
Convention maison : **appeler `SetPresentUnits` en tête de chaque fonction qui
écrit ou lit une grandeur dimensionnée**, sans jamais se fier à l'état laissé par
la fonction précédente.

| Code | Système | Usage dans le dépôt |
|---|---|---|
| `6` | kN-m-C | **défaut dominant** — charges, coupes, précontrainte |
| `9` | N-mm-C | sections (`interpSection`) |
| `10` | N-m-C | ponctuel (TMD) |

Les unités des arguments et des retours sont documentées dans les docstrings et
**ne suivent pas toutes le même système** (des fonctions attendent des mm alors
que le modèle est en kN-m). Lire la docstring avant d'enchaîner deux fonctions.

### 6.5 Verrouillage et performance
- Déverrouiller avant modification : `SapModel.SetModelIsLocked(False)`.
- Couper le rafraîchissement de vue pendant les constructions en masse, le
  rétablir une seule fois à la fin. Sur les maillages de tablier, le refresh par
  élément domine le temps d'exécution.
- Privilégier les affectations par **groupe** (`ItemType`) aux boucles
  élément par élément.

---

## 7. Conventions de modélisation

Choix établis. Les respecter par défaut ; signaler tout écart.

### Poutres principales (`FrameObj`)
- Axe tracé à **`z = 0`**, section positionnée en dessous par point cardinal **8**
  (haut-centre) via `SetInsertionPoint_1`.
- Avec `StiffTransform = True`, SAP2000 insère une liaison rigide vers le point
  d'insertion : `FrameForce` et `FrameJointForce` tiennent **déjà** compte de
  l'excentrement. **Aucune transformation manuelle** en post-traitement.

### Tablier (`AreaObj`)
Rééchantillonnage curviligne à pas configurable, grille transversale, éléments
quadrangulaires. Voir `MeshingGeometry/createDeckSAP2000.py` (657 lignes — la
fonction centrale de génération de tablier) et `getStations`,
`getOffsetPoints`, `getTransverseOffsetsSAP2000`.

### Appuis
Nœuds de pieux projetés perpendiculairement sur l'axe de chaque poutre, filtrés
par seuil de proximité (`max_pier_dist`) via `scipy.spatial.cKDTree`.

### Connexion pile / tablier
1. **Body / Rigid Body Constraint** côté tablier pour l'excentrement en plan.
2. **Link** avec raideurs réelles de néoprène et raideurs de rotation nulles.
3. Pas de relâchements en tête de pile : la gestion des DDL passe par le Link.
4. **Toujours** aligner explicitement les axes locaux du Link
   (`SetLocalAxesAdvanced`) — un Link non vertical génère sinon des efforts
   couplés parasites.

> Limite connue et acceptée : les Links ne modélisent pas le couplage V-M sur
> leur longueur (contrairement aux Frames). Acceptable tant que la hauteur
> d'appareil d'appui reste faible devant la hauteur de pile.

---

## 8. Extraction des résultats

| Besoin | Voie |
|---|---|
| Efforts internes le long d'un élément | `Results.FrameForce` |
| Efforts transmis aux appuis (repère local) | `Results.FrameJointForce` |
| Résultante mixte dalle + poutre, station par station | Section Cut → `Results.SectionCutAnalysis` |

### Section Cuts — module `SectionCuts/`
Fonctions existantes : `createSectionCutsSAP2000`,
`createSectionCutsWithResultPointSAP2000`, `bridgeDeckSectionCutsSAP2000`,
`getSectionCutForcesSAP2000`, `composeCompositeSectionForcesSAP2000` (491 l.),
`getCenterGravity`, `Plane.py`.

Règles :
- **`SetByQuad` est préféré** pour l'automatisation station par station (plan de
  coupe explicite filtré par groupe). `SetByGroup` repose sur l'équilibre en
  corps libre à la frontière du groupe.
- `MyType = 1` (Analysis), lecture via `Results.SectionCutAnalysis`.
- Aligner les **axes locaux de chaque coupe sur le vecteur tangent** du tracé,
  sinon les moments n'ont pas de sens physique.
- Les **Links sont exclus** de l'équilibre des Section Cuts : prudence près des
  appuis.

### Coût d'analyse
La factorisation de la matrice de rigidité (LU/Cholesky) a lieu **une seule
fois**, quel que soit le nombre de cas de charge ; les cas supplémentaires ne
coûtent qu'une descente/remontée. **Les patterns de charge par travée sont donc
peu coûteux** — ne pas chercher à les réduire pour des raisons de performance.

---

## 9. Pièges connus du dépôt

### 9.1 Doublons divergents
Certains fichiers existent en plusieurs exemplaires. **Cinq d'entre eux ont
divergé** — les copies ne sont pas interchangeables :

| Fichier | Emplacements divergents |
|---|---|
| `variableAreaSectionGroupSAP2000.py` | `SectionCuts/` ≠ `FrameShellsCablesPoints/` |
| `fib2020_V_Level_II.py` | `OutputDesign/` ≠ `OutputDesign/fib 2020 Shear Level II/` |
| `interpSection.py` | `SectionDesigner/` ≠ `OutputDesign/Built-up I-section Design/` |
| `flexuralBucklingSIA296_3.py` | `OutputDesign/` ≠ `OutputDesign/Built-up I-section Design/` |
| `getCableAxialForces.py` | `Cable-stayedbridge/` ≠ `Suspensionbridge/` |

Copies strictement identiques (moins risquées, mais à corriger de front en cas
de bug) : `getGroupPointObjSAP2000` (×3), `isostaticPrestressLoadCaseSAP2000`
(×3), `getGroupAreaObjSAP2000`, `getGroupFrameObjSAP2000`,
`getGroupCableObjSAP2000`, `getOffsetPoints`, `circleThreepoints`,
`getCircularCurve`, `deleteFloatingPointsSAP2000`,
`jointBodyConstraintsGroupSAP2000`.

**Avec des imports plats, c'est l'ordre du `PYTHONPATH` qui décide de la version
chargée.** Devant un comportement inexpliqué sur une de ces fonctions,
c'est la première hypothèse à tester. Toujours indiquer le chemin complet de la
version visée quand on en parle.

### 9.2 Fichiers non versionnables à la racine
`Algorithm_cables.pptx`, `Redaelli FLC.xlsx` sont mêlés au code.
`Algorithm_cables.pptx` est de plus dupliqué dans `Cable-stayedbridge/`.

### 9.3 `rep_creator.py`
Chemin absolu en dur vers un lecteur réseau (`Z:/…`) et `DRY_RUN = True`.
Ce n'est pas une fonction de bibliothèque mais un utilitaire ponctuel.

---

## 10. À ne pas faire

- Inventer ou supposer une signature OAPI sans la vérifier dans
  `Docs/SAP2000_API/`.
- Passer un paramètre de sortie en argument positionnel (§6.1).
- Appliquer une transformation d'excentrement manuelle sur des résultats obtenus
  avec `StiffTransform = True`.
- Exécuter un script d'écriture sur le modèle ouvert sans validation explicite.
- Convertir les imports plats en imports relatifs / package.
- Renommer, refactorer ou reformater du code hérité non concerné par la demande.
- Factoriser les scripts `Cable_Design_C*` de sa propre initiative.
- Proposer une refonte d'architecture quand une correction ciblée suffit.

---

## 11. Chantiers en cours

- Génération automatique des Section Cuts par station à partir des vecteurs
  tangent/normal déjà calculés en amont.
- Patterns de charge par travée pour l'analyse enveloppe de poutre continue.
- À évaluer : outils Bridge / Vehicle Live Load intégrés de SAP2000
  (`API_Bridge_Advanced.md`, `API_Definitions_Bridge_Objects.md`) comme
  alternative à la discrétisation manuelle des patterns.

---

**Entretien de ce fichier :** toute découverte sur un comportement non documenté
de l'OAPI, ou toute décision de modélisation durable, est consignée ici plutôt
que dans un commentaire de code isolé. Les champs `<À COMPLÉTER>` restent à
renseigner.
