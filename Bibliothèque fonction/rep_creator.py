import os

# Dossier racine contenant vos scripts (celui que vous mettez dans le PYTHONPATH)
ROOT_DIR = r"Z:/02 Ressources/240 Bases de projet/Dimensionnements/Feuilles calcul/feuilles excel_Damien/SAP 2000/Scripts SAP"

# Dossiers à ignorer (pas de __init__.py à y créer)
EXCLUDE_DIRS = {".git", "__pycache__", "venv", ".venv", "env", "node_modules", ".idea", ".vscode"}

# Passez à False pour réellement créer les fichiers (True = juste un aperçu)
DRY_RUN = True

created = []
skipped = []

for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    # on retire les dossiers exclus de la suite du parcours
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]

    init_path = os.path.join(dirpath, "__init__.py")

    if "__init__.py" in filenames:
        skipped.append(init_path)
        continue

    # on ne crée un __init__.py que dans un dossier qui contient au moins
    # un fichier .py (sinon ce n'est probablement pas un package)
    has_py_file = any(f.endswith(".py") for f in filenames)
    if not has_py_file:
        continue

    created.append(init_path)
    if not DRY_RUN:
        with open(init_path, "w", encoding="utf-8") as f:
            pass  # fichier vide

print(f"{'[DRY RUN] ' if DRY_RUN else ''}__init__.py à créer : {len(created)}")
for p in created:
    print("  +", p)

print(f"\n__init__.py déjà présents (inchangés) : {len(skipped)}")