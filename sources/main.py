import subprocess
import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Menu Principal - Convertisseurs")
root.geometry("1200x600")

# Fonction pour ouvrir les différentes interfaces
def ouvrir_convertisseur_enzo():
    subprocess.Popen(["python", "sources/convertisseurs/ConvertisseurEnzo.py"])

def ouvrir_convertisseur_nolan():
    subprocess.Popen(["python", "sources/convertisseurs/ConvertisseurNolan.py"])

def ouvrir_convertisseur_erwan():
    subprocess.Popen(["python", "sources/convertisseurs/ConvertisseurErwan.py"])

# Ajouter les boutons pour ouvrir chaque convertisseur
tk.Label(root, text="Choisissez un convertisseur :", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Convertisseur Enzo", command=ouvrir_convertisseur_enzo, width=30, height=2).pack(pady=5)
tk.Button(root, text="Convertisseur Nolan", command=ouvrir_convertisseur_nolan, width=30, height=2).pack(pady=5)
tk.Button(root, text="Convertisseur Erwan", command=ouvrir_convertisseur_erwan, width=30, height=2).pack(pady=5)

# Lancer la boucle Tkinter
root.mainloop()
