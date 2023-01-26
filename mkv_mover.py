import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Initialiser la fenêtre de sélection de fichier
root = tk.Tk()
root.withdraw()

# Demander à l'utilisateur de sélectionner le dossier racine
root_path = filedialog.askdirectory(title = "Sélectionnez le dossier racine")

# Demander à l'utilisateur de sélectionner le dossier cible
target_path = filedialog.askdirectory(title = "Sélectionnez le dossier cible")

# Pour compter le nombre de fichiers mkv
count = 0

# Pour chaque fichier dans le dossier racine et ses sous-dossiers
for subdir, dirs, files in os.walk(root_path):
    for file in files:
        # Si le fichier a l'extension .mkv
        if file.endswith(".mkv"):
            count += 1

# Pour compter le nombre de fichier déplacés
            moved_count = 0
            # Pour chaque fichier dans le dossier racine et ses sous-dossiers
            for subdir, dirs, files in os.walk(root_path):
                for file in files:
                    # Si le fichier a l'extension .mkv
                    if file.endswith(".mkv"):
                        # Construire le chemin complet du fichier
                        file_path = os.path.join(subdir, file)
                        # Déplacer le fichier vers le dossier cible
                        shutil.move(file_path, target_path)
                        moved_count += 1
                        print(f"{moved_count}/{count} fichiers .mkv déplacés")

print("Tous les fichiers .mkv ont été déplacés vers " + target_path)
